from .views import TaskSummary , Task_Per_Month ,  Task_Month
from django.urls import path

urlpatterns = [
    
    path("TaskSummary/" , TaskSummary.as_view() , name = "TaskSummary" ) , 
    path("Task_Month/" , Task_Month.as_view() , name = "Task_Month" ) , 
    path("Task_Per_Month/" , Task_Per_Month.as_view() , name = "Task_Per_Month" ) , 

]