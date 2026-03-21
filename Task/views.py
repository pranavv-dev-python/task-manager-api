from .serializers import TaskSerializers 
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated 
from .models import Tasks

# Create your views here.

class ListViewTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializers

    def perform_create(self , serializer):
        serializer.save(user= self.request.user )
    
    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)

class UpdateDeleteRevive(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializers 

    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)

