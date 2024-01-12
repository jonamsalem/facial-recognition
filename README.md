
# Facial Recognition Server

## Overview
 Facial Recognition software that allows users to authenticate via OpenCV's facial ID library and alerts admins upon login via email.

## To-Do List
- Migrate to MongoDB rather than store images in directory
- Host on AWS
- Implement JWT tokens for authentication after face recognition
- Create an endpoint that fetches something fun (e.g., Goggins' quotes LOL)

## Getting Started
### Running Locally
1. **Install Python 3 and Django.**
2. **Clone the repository.**
3. **Create an `images` directory under the root directory and populate it with clear profile photos (you can first call the POST request and then use those images).**
4. **Populate the `.env` file to consist of the SMTP information for email notifications:**

**SMTP_SERVER**: smtp.gmail.com  
**SMTP_PORT**: ...  
**SMTP_USERNAME**: example@gmail.com  
**SMTP_PASSWORD**: examplepassword

*Note: To create an `SMTP_PASSWORD`, go to your Gmail account, navigate to Security, enable 2-Step Verification, and generate an App password.*

5. **Run the Django server and call the endpoints:**
   ```bash
   python manage.py runserver
    curl http://localhost:8000/api/start-facial-recognition/
    curl -X POST http://localhost:8000/api/start-facial-recognition/
