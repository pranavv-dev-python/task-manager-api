from rest_framework import serializers
from django.contrib.auth import get_user_model

USER = get_user_model()
class AccountSerializers(serializers.ModelSerializer):
    password = serializers.CharField( write_only = True )

    class Meta:
        model = USER
        fields = ["username" , "password" , "email"]

    def create(self , validated_data  ):
        user = USER.objects.create_user(
            username = validated_data["username"],
            password = validated_data["password"] ,
            email = validated_data.get("email" , "")
        )
        return user

