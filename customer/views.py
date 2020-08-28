from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    #Get Data
    if request.method == 'GET':
        customer = Customer.objects.all()

        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse({
            "success": bool(1),
            "message": "Data Found",
            "data": customer_serializer.data
        }, safe=False)

    #Store Data
    elif request.method == 'POST':
        if request.name == "":
            return JsonResponse({
                "success": bool(0),
                "message": "name is required",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)

        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()

            return JsonResponse({
                "success": bool(1),
                "message": "Data Successfuly Insert",
                "data": customer_serializer.data
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            "success": bool(0),
            "message": customer_serializer.errors,
            "data": []
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def show(request, pk):
    # find tutorial by pk (id)
    try:
        customer = Customer.objects.get(pk=pk)

        #Get Single Data
        if request.method == 'GET':
            customer_serializer = CustomerSerializer(customer)
            return JsonResponse({
                "success": bool(1),
                "message": "Data Found",
                "data": customer_serializer.data
            })
        # Update Data
        elif request.method == 'PUT':
            customer_data = JSONParser().parse(request)
            customer_serializer = CustomerSerializer(customer, data=customer_data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return JsonResponse({
                    "success": bool(1),
                    "message": "Data Successfully Update",
                    "data": customer_serializer.data
                })
            return JsonResponse({
                "success": bool(0),
                "message": customer_serializer.errors,
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        # Delete Data
        elif request.method == 'DELETE':
            customer.delete()
            return JsonResponse({
                "success": bool(1),
                "message": "Customer was deleted successfully!",
                "data": []
            }, status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
        return JsonResponse({
            "success": bool(0),
            "message": "Customer does not exist!",
            "data": []
        }, status=status.HTTP_204_NO_CONTENT)
