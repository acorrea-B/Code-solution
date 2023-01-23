import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from location.models import Country


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

        self.assertEqual(result.get("id"), 1)
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
