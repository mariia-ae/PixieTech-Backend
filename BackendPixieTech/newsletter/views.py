import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NewsletterSubscriber

@csrf_exempt
def newsletter_subscribe(request):
    if request.method !="POST":
        return JsonResponse(
            {"error": "Only POST allowed"},
            status=405
        )
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )
    email = data.get("email")

    if not email:
        return JsonResponse(
            {"error": "Email is required"},
            status=400
        )
    subscriber = NewsletterSubscriber.objects.create(email=email)

    return JsonResponse(
        {"status": "ok", "id": subscriber.id},
        status=201
    )



# Create your views here.
