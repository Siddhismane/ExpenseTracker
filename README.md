# Expense Tracker App

A simple Django web app to track personal expenses.
You can add, view, edit, and delete expenses. The app also includes a dashboard with charts and an analysis table to help understand your spending better.

**Features**

Add expenses with amount, category, description, and date

View all expenses in a clean table

Edit or delete any entry

**Dashboard with:**

Monthly total

Pie chart of expenses by category

Analysis table with percentages

**Prerequisites**

Make sure you have these installed before running the project:

# Install Python (>= 3.9 recommended)
python --version

# Install pip (Python package manager)
pip --version

# Install virtual environment (optional but recommended)
pip install virtualenv

Setup Instructions
# 1. Clone the repository
git clone https://github.com/Siddhismane/ExpenseTracker.git
cd ExpenseTracker

# 2. Create and activate virtual environment
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Mac/Linux:
source myenv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver


Then open http://127.0.0.1:8000/ in your browser.

Tech Stack

Python + Django (backend)

SQLite (database)

Matplotlib (charts)

Bootstrap (frontend styling)
