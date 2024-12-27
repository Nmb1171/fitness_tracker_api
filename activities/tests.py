from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Activity
# Create your tests here.



class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_login_and_token_generation(self):
        # Attempt to log in and generate a token
        response = self.client.post("/api/token/", {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)  # Ensure access token is returned

    def test_invalid_login(self):
        # Attempt to log in with incorrect credentials
        response = self.client.post("/api/token/", {"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)  # Ensure error message is returned




class ActivityCRUDTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        response = self.client.post("/api/token/", {"username": "testuser", "password": "password123"})
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.activity = Activity.objects.create(
            user=self.user, type="running", duration=30, calories=200, date="2024-01-01"
        )

    def test_create_activity(self):
        data = {
            "type": "cycling",
            "duration": 45,
            "calories": 300,
            "date": "2024-01-02"
        }
        response = self.client.post("/api/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_activity(self):
        response = self.client.get(f"/api/activities/{self.activity.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_activity(self):
        updated_data = {"type": "cycling", "duration": 60, "calories": 400, "date": "2024-01-03"}
        response = self.client.put(f"/api/activities/{self.activity.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_activity(self):
        response = self.client.delete(f"/api/activities/{self.activity.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ActivityValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        response = self.client.post("/api/token/", {"username": "testuser", "password": "password123"})
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_missing_required_fields(self):
        data = {"type": "running"}  # Missing required fields
        response = self.client.post("/api/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ActivityPermissionTests(APITestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")

        # Log in as user1 and create an activity
        response = self.client.post("/api/token/", {"username": "user1", "password": "password123"})
        self.user1_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user1_token}")
        self.activity = Activity.objects.create(
            user=self.user1, type="running", duration=30, calories=200, date="2024-01-01"
        )

    def test_user_cannot_access_others_activity(self):
        # Log in as user2
        response = self.client.post("/api/token/", {"username": "user2", "password": "password123"})
        self.user2_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user2_token}")

        # Attempt to retrieve user1's activity
        response = self.client.get(f"/api/activities/{self.activity.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Should return 404