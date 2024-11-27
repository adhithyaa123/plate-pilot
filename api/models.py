from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

class Order(BaseModel):

    phone=models.CharField(max_length=15)

    table=models.CharField(max_length=15)

    status=models.BooleanField(default=False)

    total=models.PositiveIntegerField(null=True)

    waiter=models.ForeignKey(User,on_delete=models.CASCADE)

class OrderItem(BaseModel):

    item=models.CharField(max_length=200)

    qty=models.PositiveIntegerField(default=1)

    price=models.PositiveIntegerField()

    order_object=models.ForeignKey(Order,on_delete=models.CASCADE)

