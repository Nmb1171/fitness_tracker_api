Authentication Setup for Fitness Tracker API
Overview
The Fitness Tracker API uses JWT-based authentication to secure endpoints. Users need to obtain a JWT access token by providing valid credentials and include the token in the Authorization header when accessing protected endpoints.
This document explains:
How to set up and test JWT authentication.
How to use the tokens to interact with the API.

Authentication Setup
The authentication system is implemented using the djangorestframework-simplejwt package.
1. Installation
Ensure that djangorestframework-simplejwt is installed. Add it to your requirements.txt:
plaintext
djangorestframework-simplejwt==5.2.2

If not installed, run:
bash
pip install djangorestframework-simplejwt



2. Configuration in Django
In settings.py, add the following configurations:
python
# Add Simple JWT to REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Import Simple JWT settings
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


3. JWT Token Endpoints
The following endpoints are set up for authentication:
Endpoint
Method
Description
/api/token/
POST
Obtain an access token and a refresh token.
/api/token/refresh/
POST
Refresh the access token using a refresh token.




How to Test Authentication Using Postman
Step 1: Obtain JWT Token
To get an access token and refresh token:
Endpoint: POST /api/token/
Request Headers:
Content-Type: application/json
Request Body:
json
{
    "username": "your-username",
    "password": "your-password"
}


Response: If the credentials are correct, you will receive:
json
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}









Step 2: Use the Access Token
To access protected endpoints:
Include the token in the Authorization header:
makefile
Key: Authorization
Value: Bearer <your-access-token>

Example Request:
Method: GET
URL: /api/activities/
Headers:
makefile
Authorization: Bearer <your-access-token>

Expected Response:
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




Step 3: Refresh the Access Token
When the access token expires, you can use the refresh token to obtain a new one.
Endpoint: POST /api/token/refresh/
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


Summary of Testing Steps
Obtain Token:
Send a POST request to /api/token/ with your credentials.
Access Protected Endpoints:
Add the Authorization header: Bearer <your-access-token>.
Refresh Token:
Send a POST request to /api/token/refresh/ with the refresh token.




Troubleshooting
Error
Cause
Solution
401 Unauthorized
Invalid or missing token in the header.
Ensure the token is correct and in Bearer format.
Token is invalid or expired
Access token has expired.
Use the refresh token to obtain a new access token.
Authentication credentials not provided
Missing Authorization header.
Include the Authorization header with your token.


Conclusion
This document explains how to test JWT-based authentication in the Fitness Tracker API. Always include the access token in the Authorization header when accessing protected endpoints.

