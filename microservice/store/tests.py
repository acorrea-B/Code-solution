import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from store.models import Store


class CreateStore(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.request_data = {"name": "Kodak", "code": "Ko"}
        self.wrong_request = {"code": "Tk"}
        self.wrong_request_data = {"name": "Kodak", "code": "Kodak"}

    def test_fail_creation_wrong_request(self):
        response = self.api.post(
            "/api/v1/store/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("name")[0], "This field is required.")

    def test_fail_creation_wrong_data_request(self):
        response = self.api.post(
            "/api/v1/store/",
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
            "/api/v1/store/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)

        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))


class UpdateStore(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.Store = Store.objects.create(name="China", code="Ch")
        self.request_data = {"id": self.Store.id, "name": "China", "code": "Ch"}
        self.wrong_request = {"code": "Tk"}
        self.wrong_request_data = {
            "id": self.Store.id,
            "name": "China",
            "code": "China",
        }

    def test_fail_update_wrong_request(self):
        response = self.api.put(
            "/api/v1/store/",
            data=self.wrong_request,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Store does not exists")

    def test_fail_update_wrong_data_request(self):
        response = self.api.put(
            "/api/v1/store/",
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
            "/api/v1/store/",
            data=self.request_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.Store.id)
        self.assertEqual(result.get("name"), self.request_data.get("name"))
        self.assertEqual(result.get("code"), self.request_data.get("code"))


class DeleteStore(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.store = Store.objects.create(name="Kodak", code="Ko")

    def test_fail_delete_does_not_exist(self):
        response = self.api.delete(
            "/api/v1/store/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Store does not exists")

    def test_success_delete(self):
        response = self.api.delete(
            f"/api/v1/store/?id={self.store.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Store deleted")


class GetStore(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.store = Store.objects.create(name="Kodak", code="Ko")

    def test_fail_get_does_not_exist(self):
        response = self.api.get(
            "/api/v1/store/?id=1000",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.content)

        self.assertEqual(result.get("message"), "Store does not exists")

    def test_success_get(self):
        response = self.api.get(
            f"/api/v1/store/?id={self.store.id}",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(result.get("id"), self.store.id)
        self.assertEqual(result.get("name"), self.store.name)
        self.assertEqual(result.get("code"), self.store.code)


class ListStore(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.stores = [
            {"name": "Colombia", "code": "CO"},
            {"name": "China", "code": "CH"},
            {"name": "Paraguay", "code": "PR"},
        ]

        self.list_store = [
            Store.objects.create(name=store["name"], code=store["code"])
            for store in self.stores
        ]

    def test_success_list(self):
        response = self.api.get(
            "/api/v1/store/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)

        self.assertEqual(len(result), len(self.stores))
