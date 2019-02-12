
from django.shortcuts import render
from rest_framework.views import APIView
from .models import profile
from .serializers import profileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


#@api_view(['GET','POST'])
#def profilelist(request): #list profile or create a new one
 #   if request.method == 'GET':
  #      profiles = profile.objects.all()
   #     serializer = profileSerializer(profiles, many= True)
    #    return Response(serializer.data)
    
    #elif request.method == 'POST':
     #   serializer= profileSerializer(data=request.DATA)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
       # else:
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class profilelist(APIView):
    
    def get(self, request): #return all profile info
        profiles = profile.objects.all()
         
        serializer = profileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self,request): #save profile info
        print('hi')
        serializer= profileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)