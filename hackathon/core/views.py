from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework  import status
from .serializers import RequestSenderSerializer
import subprocess #noqa
def index(request):
    return HttpResponse("Hello world")


class StringFieldView(APIView):
    def post(self,request:HttpRequest, *args, **kwargs):
        serializer = RequestSenderSerializer(data=request.data)
        if serializer.is_valid():
            response = [self.process_generate(request.input)]
            return Response({"response": response})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def process_generate(self,request,input):
        response = self.process
    
    