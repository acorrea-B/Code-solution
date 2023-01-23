import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from location.models import Country
from location.models import State
from location.models import City


class CreateCountry(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.request_data = {"name": "China", "code": "Ch"}
        self.wrong_request = {"code": "Tk"}
        self.wrong_request_data = {"name": "China", "code": "China"}

    def test_fail_creation_wrong_request(self):
        response = self.api.post(
            "/api/v1/location/country/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("name")[0], "This field is required.")

    def test_fail_creation_wrong_data_request(self):
        response = self.api.post(
            "/api/v1/location/country/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 2 characters."
        )

    def test_success_creation(self):
        response = self.api.post(
            "/api/v1/location/country/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)

        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))


class UpdateCountry(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")
        self.request_data = {"id": self.country.id, "name": "China", "code": "Ch"}
        self.wrong_request = {"code": "Tk"}
        self.wrong_request_data = {
            "id": self.country.id,
            "name": "China",
            "code": "China",
        }

    def test_fail_update_wrong_request(self):
        response = self.api.put(
            "/api/v1/location/country/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Country does not exists")

    def test_fail_update_wrong_data_request(self):
        response = self.api.put(
            "/api/v1/location/country/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 2 characters."
        )

    def test_success_update(self):
        response = self.api.put(
            "/api/v1/location/country/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.country.id)
        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))


class DeleteCountry(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")

    def test_fail_delete_does_not_exist(self):
        response = self.api.delete(
            "/api/v1/location/country/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Country does not exists")

    def test_success_delete(self):
        response = self.api.delete(
            f"/api/v1/location/country/?id={self.country.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Country deleted")


class GetCountry(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")

    def test_fail_get_does_not_exist(self):
        response = self.api.get(
            "/api/v1/location/country/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Country does not exists")

    def test_success_get(self):
        response = self.api.get(
            f"/api/v1/location/country/?id={self.country.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.country.id)
        self.assertEqual(result.get("name"), self.country.name)
        self.assertEqual(result.get("code"), self.country.code)


class ListCountry(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.countrys = [
            {"name": "Colombia", "code": "CO"},
            {"name": "China", "code": "CH"},
            {"name": "Paraguay", "code": "PR"},
        ]

        self.list_country = [
            Country.objects.create(name=country["name"], code=country["code"])
            for country in self.countrys
        ]

    def test_success_list(self):
        response = self.api.get(
            f"/api/v1/location/country/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), len(self.countrys))


class CreateState(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.request_data = {
            "name": "Idiana",
            "code": "Indi",
            "country": self.country.id,
        }
        self.wrong_request = {"name": "Florida", "country": 100}
        self.wrong_request_data = {"name": "Florida", "code": "Florida"}

    def test_fail_creation_wrong_request(self):
        response = self.api.post(
            "/api/v1/location/country/state/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("code")[0], "This field is required.")

    def test_fail_creation_wrong_data_request(self):
        response = self.api.post(
            "/api/v1/location/country/state/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 4 characters."
        )

    def test_success_creation(self):
        response = self.api.post(
            "/api/v1/location/country/state/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)

        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(result.get("country"), self.country.id)


class UpdateState(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.first_country = Country.objects.create(name="China", code="Ch")
        self.second_country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Ohiooo", code="Ohto", country=self.first_country
        )
        self.request_data = {
            "id": self.state.id,
            "name": "Ohio",
            "code": "Ohio",
            "country": self.second_country.id,
        }
        self.wrong_request = {"country": 100}
        self.wrong_request_data = {
            "id": self.state.id,
            "name": "Toronto",
            "code": "Toron",
        }

    def test_fail_update_wrong_request(self):
        response = self.api.put(
            "/api/v1/location/country/state/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "State does not exists")

    def test_fail_update_wrong_data_request(self):
        response = self.api.put(
            "/api/v1/location/country/state/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 4 characters."
        )

    def test_success_update(self):
        response = self.api.put(
            "/api/v1/location/country/state/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.state.id)
        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(result.get("country"), self.second_country.id)


class DeleteState(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")
        self.state = State.objects.create(
            name="Ohiooo", code="Ohto", country=self.country
        )

    def test_fail_delete_does_not_exist(self):
        response = self.api.delete(
            "/api/v1/location/country/state/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "State does not exists")

    def test_success_delete(self):
        response = self.api.delete(
            f"/api/v1/location/country/state/?id={self.state.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "State deleted")


class GetState(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")
        self.state = State.objects.create(
            name="Ohiooo", code="Ohto", country=self.country
        )

    def test_fail_get_does_not_exist(self):
        response = self.api.get(
            "/api/v1/location/country/state/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "State does not exists")

    def test_success_get(self):
        response = self.api.get(
            f"/api/v1/location/country/state/?id={self.state.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.state.id)
        self.assertEqual(result.get("name"), self.state.name)
        self.assertEqual(result.get("code"), self.state.code)
        self.assertEqual(result.get("country"), self.country.id)


class CreateCity(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Idiana", code="Indi", country=self.country
        )
        self.request_data = {
            "name": "Gary",
            "code": "Gary",
            "state": self.state.id,
        }
        self.wrong_request = {"name": "Cary", "country": 100}
        self.wrong_request_data = {"name": "Gary", "code": "Gary capital"}

    def test_fail_creation_wrong_request(self):
        response = self.api.post(
            "/api/v1/location/country/state/city/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("code")[0], "This field is required.")

    def test_fail_creation_wrong_data_request(self):
        response = self.api.post(
            "/api/v1/location/country/state/city/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 8 characters."
        )

    def test_success_creation(self):
        response = self.api.post(
            "/api/v1/location/country/state/city/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)

        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(result.get("state"), self.state.id)


class UpdateCity(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="USA", code="US")
        self.state = State.objects.create(
            name="Ohiooo", code="Ohto", country=self.country
        )
        self.second_state = State.objects.create(
            name="Ohio", code="Ohio", country=self.country
        )
        self.city = City.objects.create(name="Garyss", code="GA", state=self.state)
        self.request_data = {
            "id": self.city.id,
            "name": "Gary",
            "code": "Gary",
            "state": self.second_state.id,
        }
        self.wrong_request = {"state": 100}
        self.wrong_request_data = {
            "id": self.city.id,
            "name": "Indiana",
            "code": "Inianan capital",
        }

    def test_fail_update_wrong_request(self):
        response = self.api.put(
            "/api/v1/location/country/state/city/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "City does not exists")

    def test_fail_update_wrong_data_request(self):
        response = self.api.put(
            "/api/v1/location/country/state/city/",
            data=self.wrong_request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        result = json.loads(response.content)

        self.assertEqual(
            result.get("code")[0], "Ensure this field has no more than 8 characters."
        )

    def test_success_update(self):
        response = self.api.put(
            "/api/v1/location/country/state/city/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.city.id)
        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))
        self.assertEqual(result.get("state"), self.second_state.id)


class DeleteCity(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")
        self.state = State.objects.create(
            name="Ohiooo", code="Ohto", country=self.country
        )
        self.city = City.objects.create(name="Garyss", code="GA", state=self.state)

    def test_fail_delete_does_not_exist(self):
        response = self.api.delete(
            "/api/v1/location/country/state/city/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "City does not exists")

    def test_success_delete(self):
        response = self.api.delete(
            f"/api/v1/location/country/state/city/?id={self.city.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "City deleted")


class ListCity(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.country = Country.objects.create(name="China", code="Ch")
        self.state1 = State.objects.create(
            name="Ohio", code="ohio", country=self.country
        )
        self.state2 = State.objects.create(
            name="Texas", code="Tex", country=self.country
        )
        self.citys = [
            {"name": "Houston", "code": "Hous", "state": self.state2},
            {"name": "China", "code": "CH", "state": self.state1},
            {"name": "Paraguay", "code": "PR", "state": self.state2},
        ]

        self.List_city = [
            City.objects.create(
                name=city["name"], code=city["code"], state=city["state"]
            )
            for city in self.citys
        ]

    def test_success_list_all_citys(self):
        response = self.api.get(
            f"/api/v1/location/country/state/city/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), len(self.citys))

    def test_success_list_all_citys_of_state(self):
        response = self.api.get(
            f"/api/v1/location/country/state/city/?state_id={self.state2.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), 2)
