from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from revenue.models import RevenueStatistic
from .models import SpendStatistic


class SummaryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        for i in range(2):
            spend = SpendStatistic.objects.create(
                name="Test Spend 1",
                date="2023-09-29",
                spend=50 * (i + 1),
                impressions=100 * (i + 1),
                clicks=50 * (i + 1),
                conversion=5 * (i + 1),
            )

            RevenueStatistic.objects.create(
                name="Test Revenue 1",
                date="2023-09-29",
                revenue=100 * (i + 1),
                spend=spend,
            )

        for i in range(2):
            spend = SpendStatistic.objects.create(
                name=f"Test Spend {i + 1}",
                date=f"2023-09-{30 - i}",
                spend=50 * (i + 3),
                impressions=100 * (i + 3),
                clicks=50 * (i + 3),
                conversion=5 * (i + 3),
            )

            RevenueStatistic.objects.create(
                name=f"Test Revenue {i + 1}",
                date=f"2023-09-{30 - i}",
                revenue=100 * (i + 3),
                spend=spend,
            )

    def test_spend_summary(self):
        url = reverse("spend:spend-summary")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["spend_sum"], 150)
        self.assertEqual(response.data[1]["spend_sum"], 150)
        self.assertEqual(response.data[2]["spend_sum"], 200)
        self.assertEqual(response.data[0]["revenue_sum"], 300)
        self.assertEqual(response.data[1]["revenue_sum"], 300)
        self.assertEqual(response.data[2]["revenue_sum"], 400)

    def test_revenue_summary(self):
        url = reverse("revenue:revenue-summary")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["revenue_sum"], 300)
        self.assertEqual(response.data[1]["revenue_sum"], 300)
        self.assertEqual(response.data[2]["revenue_sum"], 400)
        self.assertEqual(response.data[0]["spend_sum"], 150)
        self.assertEqual(response.data[1]["spend_sum"], 150)
        self.assertEqual(response.data[2]["spend_sum"], 200)
