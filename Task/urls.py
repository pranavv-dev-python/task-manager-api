from django.urls import path 
from .views import ListViewTask , UpdateDeleteRevive


urlpatterns = [
    path("create_view/" , ListViewTask.as_view() , name = "create") ,
    path("perform_task/<int:pk>/" , UpdateDeleteRevive.as_view() , name = "perform_task") ,
]