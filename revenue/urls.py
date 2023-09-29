from django.urls import path

from revenue.views import revenue_summary, RevenueListView

urlpatterns = [
    path("revenues/", RevenueListView.as_view(), name="revenue-list"),
    path("summary/", revenue_summary, name="revenue-summary"),
]

app_name = "revenue"
