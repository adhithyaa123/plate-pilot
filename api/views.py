from django.shortcuts import render

from api.serializers import OrderSerializer,OrderItemSerializer

from api.models import Order

from rest_framework.generics import ListAPIView,CreateAPIView

from rest_framework import permissions,authentication
# Create your views here.

class OrderListCreateView(ListAPIView,CreateAPIView):

    serializer_class=OrderSerializer

    queryset=Order.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        serializer.save(waiter=self.request.user)


class OrderItemCreateView(CreateAPIView):

    serializer_class=OrderItemSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        order_obj=Order.objects.get(id=id)

        data=serializer.validated_data

        order_obj.total=data.get("price")*data.get("qty")

        order_obj.save()


        serializer.save(order_object=order_obj)    



 