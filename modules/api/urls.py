from rest_framework.routers import SimpleRouter
from modules.expense.views import ExpenseTypeViewSet, ExpenseViewSet


app_name = "api"  # Specify the name of the Django app (API in this case)


routes = SimpleRouter() 

# ExpenseType CRUD routes
routes.register("expense-type", ExpenseTypeViewSet, basename="expenseType")


# Expenses CRUD routes
routes.register("expense", ExpenseViewSet, basename="expense")


urlpatterns = [
    *routes.urls,  # Include the URLs generated by the router in the urlpatterns
]