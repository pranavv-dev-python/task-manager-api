from accounts.models import USER
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
from django.db.models import Count 
from django.db.models.functions import TruncMonth
from Task.models import Tasks



class TaskSummary(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        tasks = Tasks.objects.filter(user = request.user )
        summary = tasks.values("status").annotate(total = Count("status"))
        return Response(summary)


class Task_Per_Month(APIView):

    permission_classes = [IsAuthenticated]

    def get(self , request):

        tasks = Tasks.objects.filter(user = request.user)
        summary = tasks.annotate(month = TruncMonth("created_at")).values("month").annotate(Total =Count("title"))
        return Response(summary)



class Task_Month(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request ):
        task = Tasks.objects.filter(user = request.user , priority = "High")
        summary = task.filter(status = "completed").annotate(month = TruncMonth("created_at")).values("month").annotate(total = Count("id"))
        return Response(summary)

