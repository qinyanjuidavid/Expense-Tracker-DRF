from modules.expense.models import Expense, ExpenseType
from rest_framework import serializers


class ExpenseTypeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the ExpenseType model.
    """
    class Meta:
        model = ExpenseType
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Expense model.
    """
    class Meta:
    
        model = Expense  
        fields = "__all__"
