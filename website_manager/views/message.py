from rest_framework.response import Response
from rest_framework.views import APIView
from website_manager.utils import error_decorator
from ..models import Message

class ReceiveMessage(APIView):
    @error_decorator
    def post(self, request):
        nameMessage = request.data.get('nameMessage')
        emailMessage = request.data.get('emailMessage')
        messageMessage = request.data.get('messageMessage')
        
        message = Message(nameMessage=nameMessage, emailMessage=emailMessage, messageMessage=messageMessage)
        message.save()

        return Response(
            {'response':'Data saved!'}
        )
