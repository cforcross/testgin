from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,OrderItem,Order,Link,Product
# Register your models here.

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Link)
admin.site.register(Product)

class SuperAdmin(UserAdmin):
    ordering =['-id']

admin.site.register(User,SuperAdmin)