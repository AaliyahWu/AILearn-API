from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import openai
import configparser

from api.models import Chat # 資料表名稱
from django.utils import timezone

openai_api_key = 'XXXXXX'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        # model = "gpt-4",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    answer = response.choices[0].message.content.strip()
    return answer

# def generate_image(request):
#     config = configparser.ConfigParser()
#     config.read('apikey.ini')
#     api_key = config['API_KEYS']['api_key']
#     url = "https://api.openai.com/v1/images/generations"
#
#     headers = {
#         "Authorization": f"Bearer {api_key}"
#     }
#
#     data = {
#         'model': 'dall-e-3',
#         "prompt": "students are in the class, Flat Style",
#         "n": 1,
#         "size": "1024x1024"
#     }
#
#     response = requests.post(url, headers=headers, json=data)
#
#     if response.status_code == 200:
#         image_url = response.json()["data"][0]
#         return JsonResponse({"image_url": image_url})
#     else:
#         return JsonResponse({"error": response.json()["error"]["message"]}, status=500)


# Create your views here.
@api_view(['POST'])
def chatbot(request):
    # chats = Chat.objects.filter(user=request.user.id)


    message = request.POST.get('message')
    response = ask_openai(message)

    chat = Chat(user_id='1', message=message, response=response, created_at=timezone.now())
    chat.save()

    chats = Chat.objects.all(user_id='1')
    chat = chats.latest()

    return Response({
        'success': True,
        'data':
            {
                'no': chat.pk,
                'user_id': chat.user,
                'message': chat.message,
                'response': chat.response,
                'created_at': chat.created_at,
            }
    })

        # return JsonResponse({'message': message, 'response': response})
