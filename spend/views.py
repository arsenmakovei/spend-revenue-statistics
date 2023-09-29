from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .models import SpendStatistic
from .serializers import SpendListSerializer


class SpendListView(generics.ListAPIView):
    """Retrieve a list of all spend statistics with associated revenue statistics."""

    queryset = SpendStatistic.objects.prefetch_related("revenues")
    serializer_class = SpendListSerializer


@api_view(["GET"])
def spend_summary(request):
    """Retrieve a list of spend statistics by date and name with aggregated data."""
    queryset = SpendStatistic.objects.values("name", "date").annotate(
        spend_sum=Sum("spend"),
        impressions_sum=Sum("impressions"),
        clicks_sum=Sum("clicks"),
        conversion_sum=Sum("conversion"),
        revenue_sum=Sum("revenues__revenue"),
    )

    return Response(queryset)
