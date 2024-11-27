from rest_framework import serializers

from api.models import Order,OrderItem

class OrderSerializer(serializers.ModelSerializer):

    items=serializers.SerializerMethodField(method_name="total_items",read_only=True )

    class Meta:

        model=Order

        fields="__all__"

        read_only_fields=[
            "id",
            "status",
            "total",
            "waiter",
            "created_date",
            "updated_date",
            "is_active",
        ]


    def total_items(self,obj):

        qs=OrderItem.objects.filter(order_object=obj)

        serializer_instance=OrderItemSerializer(qs,many=True)

        return serializer_instance.data    

class OrderItemSerializer(serializers.ModelSerializer):

    item_total=serializers.SerializerMethodField(method_name="get_item_total",read_only=True)

    class Meta:

        model=OrderItem

        fields="__all__"

        read_only_fields=[
            "id","owner","created_date","updated_date","order_object","is_active"
        ]


    def get_item_total(self, obj):

        return obj.qty*obj.price

