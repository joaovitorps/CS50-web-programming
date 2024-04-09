from django.urls import reverse
from django.test import TestCase


# Create your tests here.
class TasksTest(TestCase):
    def test_should_return_status_code_200(self):
        url = reverse("tasks:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
