from core.models import User,Product,Link,Order
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','password','is_ambassador','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = Link
        fields = '__all__'
