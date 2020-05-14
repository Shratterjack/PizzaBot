from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from bot.helper.helper import *
from bot.helper.Chat import Chat


GOOGLE_AUTHENTICATION_FILE_NAME = 'credential_key.json'
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path


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
   

    

