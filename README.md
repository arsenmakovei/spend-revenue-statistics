# Spend Revenue Statistics 

An efficient Django project for tracking and analyzing spending and revenue statistics, 
offering API endpoints to retrieve aggregated data by date and category

## Installation
Python3 must be already installed

1. Clone project and create virtual environment
```shell
git clone https://github.com/arsenmakovei/spend-revenue-statistics.git
cd spend_revenue_statistics
python -m venv venv
Windows: venv\Scripts\activate
Linux, Unix: source venv/bin/activate
pip install -r requirements.txt
```

2. Make migrations and run server
```shell
python manage.py migrate
python manage.py runserver
```

3. Also you can create admin user using `python manage.py createsuperuser` and visit admin panel `/admin/`
4. You can load test data using `python manage.py loaddata spend_revenue_db_data.json`
5. Visit `/api/spend/summary`, `/api/revenue/summary/` to see aggregated data by date and category for spend, revenue statistics
6. Visit `api/doc/swagger/` to see and use Swagger documentation for all endpoints.