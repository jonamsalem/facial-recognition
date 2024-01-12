THIS NEEDS REFACTORING

TODO: migrate to mongoDB, host on aws. 
Implement JWT tokens for authentication after face recognized. 
Create endpoint that fetches something fun (goggin's quotes LOL)

Facial-recognition server allows users to autneticate via openCV's facial ID library and alerts admins upon login via email.
To run locally:
1. Install python3 and Django
2. Clone the repository
3. Create an images directory under the root directory and populate with clear profile photos
4. Create an .env file that consists of the SMTP information (email notification- see below).
