# Assuming the main function is in a file called "realtime_facial_recognition.py"
from django.http import JsonResponse
from realtime_facial_recognition import main  

def facial_recognition_view(request):
    if request.method == 'GET':
        # Call the main function to start real-time facial recognition
        results = main()

        # Construct the JSON response based on the result
        response_data = {
            "results": results
        }

        # Return the JSON response
        return JsonResponse(response_data)
    else:
        # Handle unsupported request methods (e.g., POST, PUT, etc.)
        return JsonResponse({"error": "Unsupported request method"}, status=405)
