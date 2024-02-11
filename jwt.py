import jwt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the JWT secret key from environment variables
jwt_key = os.getenv('JWT_KEY')
print(jwt_key)
jwt_token = jwt.encode({}, jwt_key, algorithm='HS256')