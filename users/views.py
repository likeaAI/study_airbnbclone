from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializers

# Create your views here.


class Me(APIView) : 
     def get(self, request) :  
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)


    
     def put(self, request) : 
         user = request.user 
         serializers = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial = True        
         )

         if serializers.is_valid() : 
             user = serializers.save()
             serializer = serializers.PrivateUserSerializer(user)
             return Response(serializer.data)

         else : 
             return Response(serializers.errors)