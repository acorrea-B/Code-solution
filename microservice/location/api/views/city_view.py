from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from location.serializers import CitySerializer
from location.serializers import UpdateCitySerializer

from location.models import City


class CityView(generics.ListAPIView):
    def get_object(self, id):
        """
        Helper method to get the object with given id
        """
        try:
            return City.objects.get(id=id)
        except City.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=CitySerializer,
        responses={
            status.HTTP_201_CREATED: CitySerializer(),
            status.HTTP_400_BAD_REQUEST: CitySerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer_context = {
            "request": request,
        }

        serializer = CitySerializer(data=request.data, context = serializer_context)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(
           serializer.data,
            status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=UpdateCitySerializer,
        responses={
            status.HTTP_202_ACCEPTED: UpdateCitySerializer(),
            status.HTTP_400_BAD_REQUEST: UpdateCitySerializer,
        },
    )
    def put(self, request, *args, **kwargs):

        serializer_context = {
            "request": request,
        }
        city = self.get_object(request.data.get("id"))

        if not city:
            return Response(
                {"message": "City does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdateCitySerializer(
            city, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data,
            status.HTTP_202_ACCEPTED,
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="City id",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "state_id",
                openapi.IN_QUERY,
                description="State id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            status.HTTP_200_OK: CitySerializer(many=True),
            status.HTTP_400_BAD_REQUEST: CitySerializer,
        },
    )
    def get(self, request):
        serializer_context = {
            "request": request,
        }

        if request.query_params.get("id"):
            city = self.get_object(request.query_params.get("id"))

            if not city:
                return Response(
                    {"message": "City does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                CitySerializer(
                    city,
                    context=serializer_context,
                ).data
            )
        
        if request.query_params.get("state_id"):
            return Response(
                CitySerializer(
                    City.objects.filter(state_id=request.query_params.get("state_id")),
                    many=True,
                    context=serializer_context,
                ).data
            )

        return Response(
            CitySerializer(
                City.objects.all().order_by("id"),
                many=True,
                context=serializer_context,
            ).data
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="City id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={status.HTTP_200_OK: "message", status.HTTP_400_BAD_REQUEST: "message"},
    )
    def delete(self, request):
        if request.query_params.get("id"):
            City = self.get_object(request.query_params.get("id"))

            if not City:
                return Response(
                    {"message": "City does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            City.delete()
            return Response({"message": "City deleted"}, status.HTTP_200_OK)
