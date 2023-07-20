from django.shortcuts import render
from rest_framework.response import Response
from .models import APITable
from .serializers import APITableSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_func(request):
    data = APITable.objects.all()
    serializer = APITableSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_func(request):
    serializer = APITableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_func(request, id):
    
    try:
        apiTable = APITable.objects.get(id=id)
    except APITable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = APITableSerializer(apiTable, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)