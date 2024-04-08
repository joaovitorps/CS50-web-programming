from . import views
from django.test import TestCase
from django.urls import reverse
from datetime import datetime

# Create your tests here.


class ChristmasTest(TestCase):
    def test_is_christmas_function_should_return_false_when_not_christmas(self):
        today = datetime.now()
        function = views.is_christmas(today)

        self.assertIs(function["is_christmas"], False)

    def test_is_christmas_function_should_return_true_when_is_christmas(self):
        christmas_day = datetime.strptime("25 12", "%d %m")
        function = views.is_christmas(christmas_day)

        self.assertIs(function["is_christmas"], True)

    def test_should_return_status_code_200(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
