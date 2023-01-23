import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from location.models import Country
from location.models import State
from location.models import City

from store.models import Store

from client.models import Client


class CreateClient(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Idiana", code="Indi", country=self.country
        )
        self.city = City.objects.create(name="Gary", code="Gary", state=self.state)
        self.store = Store.objects.create(
            name="Reebok",
            code="Re",
        )
        self.request_data = {
            "name": "Antonio",
            "surname": "Pototsi",
            "country": self.country.id,
            "state": self.state.id,
            "city": self.city.id,
            "favorite_store": self.store.id,
        }
        self.wrong_request = {"name": "Cary", "surname": "potosi"}
        self.wrong_request_data = {
            "name": "Antonio",
            "surname": "Pototsi",
            "country": 900,
            "state": self.state.id,
            "city": self.city.id,
            "favorite_store": self.store.id,
        }

    def test_fail_creation_wrong_request(self):
        response = self.api.post(
            "/api/v1/client/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("country")[0], "This field is required.")
        self.assertEqual(result.get("state")[0], "This field is required.")
        self.assertEqual(result.get("favorite_store")[0], "This field is required.")

    def test_fail_creation_wrong_data_request(self):
        response = self.api.post(
            "/api/v1/client/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("country")[0], 'Invalid pk "900" - object does not exist.'
        )

    def test_success_creation(self):
        response = self.api.post(
            "/api/v1/client/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)

        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(result.get("state"), self.state.id)


class UpdateClient(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Idiana", code="Indi", country=self.country
        )
        self.city = City.objects.create(name="Gary", code="Gary", state=self.state)
        self.store = Store.objects.create(
            name="Reebok",
            code="Re",
        )
        self.store2 = Store.objects.create(
            name="Nike",
            code="Ni",
        )
        self.client = Client.objects.create(
            name="Antonio",
            surname="Pototsi",
            country=self.country,
            city=self.city,
            state=self.state,
            favorite_store=self.store,
        )
        self.request_data = {
            "id": self.client.id,
            "name": "Antonio jose",
            "surname": "Potosi",
            "favorite_store": self.store2.id,
        }
        self.wrong_request = {"state": 100}
        self.wrong_request_data = {"id": self.client.id, "favorite_store": 100}

    def test_fail_update_wrong_request(self):
        response = self.api.put(
            "/api/v1/client/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Client does not exists")

    def test_fail_update_wrong_data_request(self):
        response = self.api.put(
            "/api/v1/client/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("favorite_store")[0], 'Invalid pk "100" - object does not exist.'
        )

    def test_success_update(self):
        response = self.api.put(
            "/api/v1/client/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.client.id)
        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(
            result.get("favorite_store"), self.request_data.get("favorite_store")
        )
        self.assertEqual(result.get("state"), self.state.id)


class DeleteClient(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Idiana", code="Indi", country=self.country
        )
        self.city = City.objects.create(name="Gary", code="Gary", state=self.state)
        self.store = Store.objects.create(
            name="Reebok",
            code="Re",
        )
        self.store2 = Store.objects.create(
            name="Nike",
            code="Ni",
        )
        self.client = Client.objects.create(
            name="Antonio",
            surname="Pototsi",
            country=self.country,
            city=self.city,
            state=self.state,
            favorite_store=self.store,
        )

    def test_fail_delete_does_not_exist(self):
        response = self.api.delete(
            "/api/v1/client/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Client does not exists")

    def test_success_delete(self):
        response = self.api.delete(
            f"/api/v1/client/?id={self.client.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Client deleted")


class ListClient(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Idiana", code="Indi", country=self.country
        )
        self.city = City.objects.create(name="Gary", code="Gary", state=self.state)
        self.store = Store.objects.create(
            name="Reebok",
            code="Re",
        )
        self.store2 = Store.objects.create(
            name="Nike",
            code="Ni",
        )
        self.clients = [
            {
                "name": "Camilo",
                "surname": "Velazco",
                "country": self.country,
                "state": self.state,
                "city": self.city,
                "favorite_store": self.store,
            },
            {
                "name": "Antonia",
                "surname": "Torres",
                "country": self.country,
                "state": self.state,
                "city": self.city,
                "favorite_store": self.store2,
            },
            {
                "name": "Patrica",
                "surname": "Pillimue",
                "country": self.country,
                "state": self.state,
                "city": self.city,
                "favorite_store": self.store,
            },
        ]

        self.list_client = [
            Client.objects.create(
                name=client["name"],
                surname=client["surname"],
                country=client["country"],
                state=client["state"],
                city=client["city"],
                favorite_store=client["favorite_store"],
            )
            for client in self.clients
        ]

    def test_success_list_all_clients(self):
        response = self.api.get(
            "/api/v1/client/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), len(self.clients))

    def test_success_list_all_clients_of_state(self):
        response = self.api.get(
            f"/api/v1/client/?state_id={self.state.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), 3)

    def test_success_list_all_clients_of_store(self):
        response = self.api.get(
            f"/api/v1/client/?store_id={self.store.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), 2)
