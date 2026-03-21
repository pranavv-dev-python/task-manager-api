from django.db import models
from django.conf import settings
# Create your models here.


class Tasks(models.Model):
    status_report = [

        ("Completed" , "completed ") ,
        ("pending" , "Pending ") ,
        ("On_going" , "on_going ") 

    ]

    priority_status = [
        ("Low" , "low") ,
        ("Medium" , "medium") ,
        ("High" , "high")
    ]

    id = models.AutoField(primary_key=True)
    user  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="Task" )
    title = models.CharField(max_length=100) 
    description = models.TextField()
    status = models.CharField(max_length= 50 , choices=status_report , default= "pending")
    priority = models.CharField(max_length=40 , choices=priority_status) 
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    


