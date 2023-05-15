from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, serializers, status, viewsets
from django.db.models import Q
from django.shortcuts import get_object_or_404

from modules.expense.serializers import ExpenseTypeSerializer, ExpenseSerializer
from modules.expense.models import Expense, ExpenseType


class ExpenseTypeViewSet(ModelViewSet):
    """
    A viewset for managing expense types.
    This viewset allows retrieving, creating, updating, and deleting expense types.
    """

    serializer_class = ExpenseTypeSerializer
    permission_classes = (AllowAny,)
    queryset = ExpenseType.objects.all()
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Overrided the delete method
        Delete an expense type.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Expense type deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class ExpenseViewSet(ModelViewSet):
    """
    A viewset for managing expenses.
    This viewset allows retrieving, creating, updating, and deleting expense.
    """

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Expense was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
