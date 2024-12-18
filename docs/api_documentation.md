Fitness Tracker API Documentation
Overview
The Fitness Tracker API allows users to manage their fitness activities. Users can log, update, delete, and view their activities while ensuring their data is secure through JWT-based authentication.
This documentation provides a clear explanation of the API’s functionality, including endpoints, request parameters, and responses.

Authentication
The API uses JWT-based authentication provided by djangorestframework-simplejwt. Users must obtain an access token and include it in the Authorization header to access protected endpoints.
1. Obtain Token
URL: /api/token/
Method: POST
Description: Authenticate the user and receive access and refresh tokens.
Request Body:
json
{
    "username": "your-username",
    "password": "your-password"
}
Response:
json
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}


2. Refresh Token
URL: /api/token/refresh/
Method: POST
Description: Obtain a new access token using the refresh token.
Request Body:
json
{
    "refresh": "your-refresh-token"
}

Response:
json
{
    "access": "new-access-token"
}


Endpoints
1. List All Activities
URL: /api/activities/
Method: GET
Description: Retrieve a list of all activities for the authenticated user.
Request Headers:
Authorization: Bearer <your-access-token>



Response:
json
[
    {
        "id": 1,
        "type": "running",
        "duration": 30,
        "calories": 300,
        "date": "2024-12-16",
        "notes": "Morning jog"
    }
]


2. Create a New Activity
URL: /api/activities/
Method: POST
Description: Create a new activity for the authenticated user.
Request Headers:
Authorization: Bearer <your-access-token>
Content-Type: application/json

Request Body:
json
{
    "type": "cycling",
    "duration": 45,
    "calories": 350,
    "date": "2024-12-16",
    "notes": "Evening cycling session"
}


Response:
json
{
    "id": 2,
    "type": "cycling",
    "duration": 45,
    "calories": 350,
    "date": "2024-12-16",
    "notes": "Evening cycling session"
}


3. Retrieve a Specific Activity
URL: /api/activities/<id>/
Method: GET
Description: Retrieve details of a specific activity.
Request Headers:
Authorization: Bearer <your-access-token>

Example Response:
json
{
    "id": 1,
    "type": "running",
    "duration": 30,
    "calories": 300,
    "date": "2024-12-16",
    "notes": "Morning jog"
}




4. Update a Specific Activity
URL: /api/activities/<id>/
Method: PUT
Description: Update an existing activity.
Request Headers:
Authorization: Bearer <your-access-token>
Content-Type: application/json

Request Body:
json
{
    "type": "walking",
    "duration": 60,
    "calories": 200,
    "date": "2024-12-17",
    "notes": "Afternoon walk"
}

Response:
json
{
    "id": 1,
    "type": "walking",
    "duration": 60,
    "calories": 200,
    "date": "2024-12-17",
    "notes": "Afternoon walk"
}




5. Delete a Specific Activity
URL: /api/activities/<id>/
Method: DELETE
Description: Delete an activity.
Request Headers:
Authorization: Bearer <your-access-token>

Response:
json
{
    "detail": "Activity deleted successfully."
}


Testing the API in Postman
Authentication:
Send a POST request to /api/token/ with the username and password to obtain your tokens.
Add the access token to the Authorization header:
makefile
Key: Authorization
Value: Bearer <your-access-token>


Test Each Endpoint:
Use GET, POST, PUT, and DELETE methods to interact with the endpoints listed above.
Add the required headers (Authorization and Content-Type where necessary).
Ensure you’re passing valid JSON data in the request body for POST and PUT requests.

Conclusion
This documentation outlines the key features and endpoints of the Fitness Tracker API. It includes detailed instructions for authentication, as well as request and response examples for each endpoint.

