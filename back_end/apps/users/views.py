from django.shortcuts import render
from apps.users.models import User, Profile
from apps.users.serializer import UserSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = ([AllowAny])
  serializer_class = RegisterSerializer
  #@api_view(['GET'])
  #def getRoutes(request):
  #  routes = [
  #    '/api/token/',
  #    '/api/register/',
  #    '/api/token/refresh/'
  #  ]
  #  pass #return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
  if request.method == 'GET':
    response = f"Hey {request.user.username}, You are seeing a GET response!"
    return Response({'response': response}, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    text = request.POST.get('text')
    response = f"Hey {request.user.username}, You are seeing a POST response! You sent: {text}"
    return Response({'response': response}, status=status.HTTP_200_OK)
  return Response({}, status=status.HTTP_400_BAD_REQUEST)