from django.http import JsonResponse
from .models import Greeting

def hello(request):
    """API endpoint returning a greeting message from the database."""
    # Fetch the first Greeting object (if exists)
    greeting = Greeting.objects.first()
    if greeting:
        message = greeting.message
    else:
        message = "Hello from the database!"
        # If no greeting in DB, optionally create one (commented out):
        # greeting = Greeting.objects.create(message=message)
    return JsonResponse({"message": message})
