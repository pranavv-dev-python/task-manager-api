from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated 
from .serializers  import AccountSerializers
from rest_framework.views import APIView
from rest_framework.response import Response 


class RegisterAcoounts(generics.CreateAPIView):
    permission_classes = []
    serializer_class = AccountSerializers

class ProfileView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self , request ):
        return Response({
            "email": request.user.email ,
            "username" : request.user.username ,
        })

