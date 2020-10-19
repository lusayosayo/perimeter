from django.http import JsonResponse

def hello(request):
    response = {
        'message': 'hey',
    }

    return JsonResponse(
        response,
        safe=False,
    )