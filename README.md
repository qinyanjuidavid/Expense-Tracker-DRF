# Expense-Tracker-DRF
### Project Setup
  - Clone the project using the command `git clone https://github.com/qinyanjuidavid/Tabibu-Health-Care-API.git`
  - Change to the project directory using the command `cd expenseTracker`
  - Ensure you have Python 3.8 and above installed
  - Install virtualenv using the command `pip install virtualenv`
  - Create a new virtual environment for the project using the command `python -m venv venv`
  - Activate the virtual environment using the command `.\venv\Scripts\activate`
  - Install the project's dependencies using the command `pip install -r requirements.txt`
  - Collect the project's static files using the command `python manage.py collectstatic`
  - Create database migrations using the command `python manage.py makemigrations`
  - Apply the migrations to the database using the command `python manage.py migrate`
  - Create a superuser account using the command `python manage.py createsuperuser`
  - Run the project using the command `python manage.py runserver 8000`
  - Check the project endpoints at [http://127.0.0.1:8000](http://127.0.0.1:8000/)
### Overview
> On my models i had an Abstract base model for tracking creation and modification timestamps.
  - `created_at` 
  - `updated_at`
> The second model was the ExpenseType which represents a type of expense that can be incurred. Inherits from TrackingModel to track creation and modification timestamps.
  - `expense_type`
  - `description`
> The last model was the Expense model which represents an individual expense. It also inherits from TrackingModel to track creation and modification timestamps. 
  - `expense` The name or description of the expense.
  - `expense_type` The type of expense associated with this expense (related to ExpenseType model).
  - `amount` The amount of the expense.
  - `paid_to` The person or organization to which the expense was paid to

> I had all the CRUD operations for both Expense and ExpenseType, Below are the images to the Swagger UI;
#### Expense Type
![ExpenseType](https://github.com/qinyanjuidavid/Expense-Tracker-DRF/assets/49823575/1f73d0a7-7a00-47b0-85c8-9468ee3012fd)
#### Expense
![Expense](https://github.com/qinyanjuidavid/Expense-Tracker-DRF/assets/49823575/cf768cd7-13c2-483c-a5a5-da06fff29ad8)
