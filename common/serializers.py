
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','password','is_ambassador','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }

        def create(self,validated_data):
            """
            harsh user passsword
            """
            password= validated_data.pop('password',None)
            instance=self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


