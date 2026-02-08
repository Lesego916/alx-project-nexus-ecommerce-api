from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        "status": "OK",
        "message": "E-commerce API is running"
    })
