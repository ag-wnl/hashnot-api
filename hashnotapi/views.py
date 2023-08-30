from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requetsted")
    friends = [
        'test1',
        'test2',
        'test3'
    ]
    return JsonResponse(friends, safe = False)