from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from location.serializers import StateSerializer
from location.serializers import UpdateStateSerializer

from location.models import State


class StateView(generics.ListAPIView):
    def get_object(self, id):
        """
        Helper method to get the object with given id
        """
        try:
            return State.objects.get(id=id)
        except State.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=StateSerializer,
        responses={
            status.HTTP_201_CREATED: StateSerializer(),
            status.HTTP_400_BAD_REQUEST: StateSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        serializer_context = {
            "request": request,
        }

        serializer = StateSerializer(data=request.data, context = serializer_context)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(
           serializer.data,
            status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        request_body=UpdateStateSerializer,
        responses={
            status.HTTP_202_ACCEPTED: UpdateStateSerializer(),
            status.HTTP_400_BAD_REQUEST: UpdateStateSerializer,
        },
    )
    def put(self, request, *args, **kwargs):

        serializer_context = {
            "request": request,
        }
        State = self.get_object(request.data.get("id"))

        if not State:
            return Response(
                {"message": "State does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdateStateSerializer(
            State, data=request.data, partial=True
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
                description="State id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            status.HTTP_200_OK: StateSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: StateSerializer,
        },
    )
    def get(self, request):
        serializer_context = {
            "request": request,
        }

        if request.query_params.get("id"):
            state = self.get_object(request.query_params.get("id"))

            if not state:
                return Response(
                    {"message": "State does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                StateSerializer(
                    state,
                    context=serializer_context,
                ).data
            )

        return Response(
            StateSerializer(
                State.objects.all().order_by("id"),
                many=True,
                context=serializer_context,
            ).data
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="State id",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={status.HTTP_200_OK: "message", status.HTTP_400_BAD_REQUEST: "message"},
    )
    def delete(self, request):
        if request.query_params.get("id"):
            state = self.get_object(request.query_params.get("id"))

            if not state:
                return Response(
                    {"message": "State does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            state.delete()
            return Response({"message": "State deleted"}, status.HTTP_200_OK)
