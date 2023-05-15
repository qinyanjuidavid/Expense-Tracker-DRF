from django.contrib import admin

from modules.expense.models import Expense, ExpenseType


@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    search_fields = (" expense_type",)
    list_display = ("expense_type", "created_at", "updated_at")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ("expense",)
    list_display = (
        "expense",
        "get_expense_type",
        "amount",
        "paid_to",
        "created_at",
        "updated_at",
    )

    def get_expense_type(self, obj):
        return obj.expense_type.expense_type

    get_expense_type.short_description = "Expense Type"
    get_expense_type.admin_order_field = "expense_type__expense_type"
