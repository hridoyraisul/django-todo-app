from django.http import JsonResponse


class ResponseUtil:
    
    def apiResponse(message = '', data = None, statusCode = 200):
        generated_response = {
            'success': 200 <= statusCode < 300,
            'status_code': statusCode,
            'message': message,
            'data': data
        }
        return JsonResponse(generated_response, status=statusCode)