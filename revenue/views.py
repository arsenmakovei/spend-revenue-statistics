from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .models import RevenueStatistic
from .serializers import RevenueListSerializer


class RevenueListView(generics.ListAPIView):
    """Retrieve a list of all revenue statistics with associated spend statistics."""

    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueListSerializer


@api_view(["GET"])
def revenue_summary(request):
    """Retrieve a list of revenue statistics by date and name with aggregated data."""
    queryset = RevenueStatistic.objects.values("name", "date").annotate(
        revenue_sum=Sum("revenue"),
        spend_sum=Sum("spend__spend"),
        impressions_sum=Sum("spend__impressions"),
        clicks_sum=Sum("spend__clicks"),
        conversion_sum=Sum("spend__conversion"),
    )

    return Response(queryset)
