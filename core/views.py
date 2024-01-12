
from django.http import JsonResponse
from realtime_facial_recognition import main  
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def facial_recognition_view(request):
    if request.method == 'GET':
        results = main(request.method)
        if results[0] == False:
            # If the first result is False, return 400 Bad Request
            response = {
                "result": "No match found"
            }
            return JsonResponse(response, status=400)

        # If the first result is not False, return the actual results
        response = {
            "result": results[1]
        }
        return JsonResponse(response)
    if request.method == 'POST':
        # Call the main function to start real-time facial recognition
        results = main(request.method)

        # Construct the JSON response based on the result
        response_data = {
            "results": results
        }
        if results[0] == False:
            response = {
                "result": "No face detected"
            }
            return JsonResponse(response, status=400)
        response = {
            "result": results[1]
        }
        return JsonResponse(response)
    else:
        # Handle unsupported request methods (e.g., POST, PUT, etc.)
        return JsonResponse({"error": "Unsupported request method"}, status=400)
