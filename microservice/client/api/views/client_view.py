from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from microservice.client.api.views.serializers import ClientSerializer
from microservice.client.api.views.serializers import UpdateClientSerializer

from client.models import Client


class ClientView(generics.ListAPIView):
    def get_object(self, id):
        """
        Helper method to get the object with given id
        """
        try:
            return Client.objects.get(id=id)
        except Client.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=ClientSerializer,
        responses={
            status.HTTP_201_CREATED: ClientSerializer(),
            status.HTTP_400_BAD_REQUEST: ClientSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer_context = {
            "request": request,
        }

        serializer = ClientSerializer(data=request.data, context=serializer_context)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=UpdateClientSerializer,
        responses={
            status.HTTP_202_ACCEPTED: UpdateClientSerializer(),
            status.HTTP_400_BAD_REQUEST: UpdateClientSerializer,
        },
    )
    def put(self, request, *args, **kwargs):

        serializer_context = {
            "request": request,
        }
        client = self.get_object(request.data.get("id"))

        if not client:
            return Response(
                {"message": "Client does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdateClientSerializer(client, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            serializer.data,
            status.HTTP_202_ACCEPTED,
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Client id",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "store_id",
                openapi.IN_QUERY,
                description="Store id",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "state_id",
                openapi.IN_QUERY,
                description="State id",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={
            status.HTTP_200_OK: ClientSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: ClientSerializer,
        },
    )
    def get(self, request):
        serializer_context = {
            "request": request,
        }

        if request.query_params.get("id"):
            client = self.get_object(request.query_params.get("id"))

            if not client:
                return Response(
                    {"message": "Client does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                ClientSerializer(
                    client,
                    context=serializer_context,
                ).data
            )

        if request.query_params.get("store_id"):
            return Response(
                ClientSerializer(
                    Client.objects.filter(store_id=request.query_params.get("store_id")),
                    many=True,
                    context=serializer_context,
                ).data
            )
        
        if request.query_params.get("state_id"):
            return Response(
                ClientSerializer(
                    Client.objects.filter(state_id=request.query_params.get("state_id")),
                    many=True,
                    context=serializer_context,
                ).data
            )

        return Response(
            ClientSerializer(
                Client.objects.all().order_by("id"),
                many=True,
                context=serializer_context,
            ).data
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Client id",
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
            client = self.get_object(request.query_params.get("id"))

            if not client:
                return Response(
                    {"message": "Client does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            client.delete()
            return Response({"message": "Client deleted"}, status.HTTP_200_OK)
