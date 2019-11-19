from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
def todo_create(request):

    serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        serializer.save()

        return JsonResponse(serializer.data)

    return HttpResponse(status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
def todo_detail(request, todo_id):

    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)

        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)

        return HttpResponse(status=400)
    elif request.method == 'DELETE':
        todo.delete()
        
        return HttpResponse(status=204)
