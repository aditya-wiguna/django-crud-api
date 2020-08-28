from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['name'] == "":
            raise serializers.ValidationError("name is required")
        return data
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