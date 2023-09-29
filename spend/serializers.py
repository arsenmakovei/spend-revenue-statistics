from rest_framework import serializers

from revenue.serializers import RevenueSerializer
from spend.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ("id", "name", "date", "spend", "impressions", "clicks", "conversion")


class SpendListSerializer(SpendSerializer):
    revenues = RevenueSerializer(many=True, read_only=True)

    class Meta(SpendSerializer.Meta):
        fields = SpendSerializer.Meta.fields + ("revenues",)
