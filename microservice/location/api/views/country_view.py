from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from location.api.serializers import CountrySerializer
from location.api.serializers import UpdateCountry

from location.models import Country


class CountryView(generics.ListAPIView):
    def get_object(self, id):
        """
        Helper method to get the object with given id
        """
        try:
            return Country.objects.get(id=id)
        except Country.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=CountrySerializer,
        responses={
            status.HTTP_201_CREATED: CountrySerializer(),
            status.HTTP_400_BAD_REQUEST: CountrySerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer_context = {
            "request": request,
        }

        serializer = CountrySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            CountrySerializer(serializer.data, context=serializer_context).data,
            status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=UpdateCountry,
        responses={
            status.HTTP_202_ACCEPTED: CountrySerializer(),
            status.HTTP_400_BAD_REQUEST: UpdateCountry,
        },
    )
    def put(self, request, *args, **kwargs):

        serializer_context = {
            "request": request,
        }
        country = self.get_object(request.data.get("id"))

        if not country:
            return Response(
                {"message": "Country does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdateCountry(country, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            CountrySerializer(serializer.data, context=serializer_context).data,
            status.HTTP_202_ACCEPTED,
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Country id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            status.HTTP_200_OK: CountrySerializer(many=True),
            status.HTTP_400_BAD_REQUEST: CountrySerializer,
        },
    )
    def get(self, request):
        serializer_context = {
            "request": request,
        }

        if request.query_params.get("id"):
            country = self.get_object(request.query_params.get("id"))

            if not country:
                return Response(
                    {"message": "Country does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                CountrySerializer(
                    country,
                    context=serializer_context,
                ).data
            )

        return Response(
            CountrySerializer(
                Country.objects.all().order_by("id"),
                many=True,
                context=serializer_context,
            ).data
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Country id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            status.HTTP_200_OK: "message",
            status.HTTP_400_BAD_REQUEST: "message",
        },
    )
    def delete(self, request):
        if request.query_params.get("id"):
            country = self.get_object(request.query_params.get("id"))

            if not country:
                return Response(
                    {"message": "Country does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            country.delete()
            return Response({"message": "Country deleted"}, status.HTTP_200_OK)
