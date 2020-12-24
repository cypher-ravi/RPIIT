from  rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from datetime import datetime
from decouple import config

# api_key = 'A5740DB2B7C1FE79CA9A2FDC8491B2C6'
api_key = config('api_key')

@api_view(['GET'])
def index(request,slug):
    if key == api_key:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message = 'Server is live current time is'
        return Response(data=message +' '+date, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)