from django.urls import path

from spend.views import spend_summary, SpendListView

urlpatterns = [
    path("spends/", SpendListView.as_view(), name="spend-list"),
    path("summary/", spend_summary, name="spend-summary"),
]

app_name = "spend"
