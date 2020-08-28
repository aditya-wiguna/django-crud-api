from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',
                  'name',
                  'marital_status',
                  'identity_number',
                  'address',
                  'parent_name',
                  'is_active'
                  )