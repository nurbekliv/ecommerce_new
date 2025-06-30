from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
import requests
from drf_yasg.utils import swagger_auto_schema

TELEGRAM_BOT_TOKEN = '8050469487:AAF-QtW10XJvYfWfTTZ99QsDagVIWMD4BdA'
TELEGRAM_CHAT_ID = '1727172054'

class SendMessageView(APIView):

    @swagger_auto_schema(request_body=MessageSerializer)
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message
            }
            response = requests.post(url, data=payload)
            return Response({'status': 'sent', 'telegram_response': response.json()})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
