from django.db import models
from django.utils.translation import gettext as _


class TrackingModel(models.Model):
    """
    Abstract base model for tracking creation and modification timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExpenseType(TrackingModel):
    """
    Represents a type of expense that can be incurred.
    Inherits from TrackingModel to track creation and modification timestamps.
    """    
    expense_type = models.CharField(_("expense type"), max_length=260, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)

    def __str__(self):
        return self.expense_type

    class Meta:
        verbose_name_plural = "Expense types"
        ordering = ("-id",)


class Expense(TrackingModel):
    """
    Represents an individual expense.
    Inherits from TrackingModel to track creation and modification timestamps.
    """
    expense = models.CharField(_("expense"), max_length=156)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.FloatField(_("amount"), default=0.00)
    paid_to = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.expense} - {self.expense_type} - {self.amount} - {self.paid_to}"

    class Meta:
        verbose_name_plural = "Expenses"
        ordering = ("-id",)
