from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from store.serializers import StoreSerializer
from store.serializers import UpdateStoreSerializer

from store.models import Store


class StoreView(generics.ListAPIView):
    def get_object(self, id):
        """
        Helper method to get the object with given id
        """
        try:
            return Store.objects.get(id=id)
        except Store.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=StoreSerializer,
        responses={
            status.HTTP_201_CREATED: StoreSerializer(),
            status.HTTP_400_BAD_REQUEST: StoreSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer_context = {
            "request": request,
        }

        serializer = StoreSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            StoreSerializer(serializer.data, context=serializer_context).data,
            status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=UpdateStoreSerializer,
        responses={
            status.HTTP_202_ACCEPTED: StoreSerializer(),
            status.HTTP_400_BAD_REQUEST: UpdateStoreSerializer,
        },
    )
    def put(self, request, *args, **kwargs):

        serializer_context = {
            "request": request,
        }
        country = self.get_object(request.data.get("id"))

        if not country:
            return Response(
                {"message": "Store does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdateStoreSerializer(country, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            StoreSerializer(serializer.data, context=serializer_context).data,
            status.HTTP_202_ACCEPTED,
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Id of store",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            status.HTTP_200_OK: StoreSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: StoreSerializer,
        },
    )
    def get(self, request):
        serializer_context = {
            "request": request,
        }

        if request.query_params.get("id"):
            store = self.get_object(request.query_params.get("id"))

            if not store:
                return Response(
                    {"message": "Store does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                StoreSerializer(
                    store,
                    context=serializer_context,
                ).data
            )

        return Response(
            StoreSerializer(
                Store.objects.all().order_by("id"),
                many=True,
                context=serializer_context,
            ).data
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="Store id",
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
            store = self.get_object(request.query_params.get("id"))

            if not store:
                return Response(
                    {"message": "Store does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            store.delete()
            return Response({"message": "Store deleted"}, status.HTTP_200_OK)
