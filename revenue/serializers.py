from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = ("id", "name", "date", "revenue")


class RevenueListSerializer(RevenueSerializer):
    class Meta(RevenueSerializer.Meta):
        fields = RevenueSerializer.Meta.fields + ("spend",)
