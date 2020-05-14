from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from bot.helper.helper import *
from bot.helper.Chat import Chat
import os



@api_view(['GET'])
def hello_world(request):
    if request.method == 'GET':
        name = request.query_params.get('name')
        response = 'Hello, {}'.format(name)
        return Response(response)

@api_view(['POST'])
def detect_intent_texts(request):
    session_id = generateSessionId()
    texts = request.data.get('texts')

    chat = Chat(session_id)
    response = chat.detect_intent_text(texts)
    return Response(response)
   

    

