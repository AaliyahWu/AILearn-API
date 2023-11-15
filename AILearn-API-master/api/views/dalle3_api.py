import requests
from django.http import JsonResponse
import openai
def generate_image(request):
    api_key = "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"
    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        'model':'dall-e-3',
        "prompt": "students are in the class, Flat Style",
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        image_url = response.json()["data"][0]
        return JsonResponse({"image_url": image_url})
    else:
        return JsonResponse({"error": "API request failed"}, status=500)
