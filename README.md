THIS NEEDS REFACTORING

# Facial Recognition Server

## Overview
The Facial Recognition Server allows users to authenticate via OpenCV's facial ID library and alerts admins upon login via email.

## Project Status
This project is in need of refactoring.

## To-Do List
- Migrate to MongoDB
- Host on AWS
- Implement JWT tokens for authentication after face recognition
- Create an endpoint that fetches something fun (e.g., Goggins' quotes LOL)

## Getting Started
### Running Locally
1. **Install Python 3 and Django.**
2. **Clone the repository.**
3. **Create an `images` directory under the root directory and populate it with clear profile photos (you can first call the POST request and then use those images).**
4. **Create a `.env` file that consists of the SMTP information for email notifications:**

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=...
SMTP_USERNAME=example@gmail.com
SMTP_PASSWORD=examplepassword

*Note: To create an `SMTP_PASSWORD`, go to your Gmail account, navigate to Security, enable 2-Step Verification, and generate an App password.*
