from functools import partial
import queue
from rest.models import *
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest.serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin


import rest_framework
# Create your views here.

# for renter home page
def home(request):
    return HttpResponse("Hello world")


# start rest_framework 
class GetPostAPI(GeneratorExit,ListModelMixin, CreateModelMixin):
    queryset = Stud.objects.all()
    serializers_class = StudSerializer

    def get(self, request, *args,**kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)

class RUDAPI(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Stud.objects.all()
    serializer_class = Stud

    def retrive(self, request, pk = None, *args,**kwargs):
        return self.retrive(request, *args, **kwargs)

    def update(self,request, pk = None, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request,pk = None, *args, **kwargs):
        return self.delete(request,*args, **kwargs)



# start concrete view from here------------------------------------------------------
# concrete view extend the GenetricView and ModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView



# start class from here
class StudList(ListAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

class StudCreate(CreateAPIView):
    queryset = Stud.objects.all()
    serializer_class  = StudSerializer
    

class StudRetrive(RetrieveAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

class StudUpdate(UpdateAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


class StudDestroy(DestroyAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# mixed List&CreateAPI View which don't required pk-----------------------------------------
from rest_framework.generics import ListCreateAPIView

class StudListCreate(ListCreateAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

#mixed RetriveUpdateDestroyAPIView which required pk------------------------------------
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class StudRUD(RetrieveUpdateDestroyAPIView):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# api using class method----------------------------------------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudAPI(APIView):
    def get(self, request, pk = None, format = None):
        # id = pk
        # if id is not None:
        #     stu = Stud.objects.get(id = id)
        #     serializer = StudSerializer(stu)
        #     return Response(serializer.data)

        # stu = Stud.objects.all()
        # serializer = StudSerializer(stu)
        # return Response(serializer.data)
        try:
            id = pk
            stu = Stud.objects.get(id = id)

        except :
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = StudSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,format = None):
        data = request.data
        serializer = StudSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# viewset start from here---------------------------------------------------------
# Note every views models is same here 
from rest_framework import viewsets

class StudViewSet(viewsets.ViewSet):
    # list() is for get all records
    # retrive() = for get single records
    # create = for create insert record
    # update = update data fully
    # partial_update = update data partially
    # distory = delete data

    def list(self,request):
        stu = Stud.objects.all()
        serializers = StudSerializer(stu, many = True)
        data = serializers.data
        return Response(data, status= status.HTTP_200_OK)

    def retrive(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu)
        return Response(serializers.data, status = status.HTTP_200_OK)

    def create(self,request):
        serializers = StudSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Updated'}, status = status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        serializers = StudSerializer(stu,data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Updated'}, status = status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        stu = Stud.objects.get(id = id)
        stu.delete()
        return Response({'msg':'Delet'}, status= status.HTTP_508_LOOP_DETECTED)

# model viewset start from here-------------------------------------------------
# modelViewSet Viewset inside nai hunxa
class StudModelVievSet(viewsets.ModelViewSet):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer


# modelviewset Getonly Get and retrive 
# which helps to get users only
#  list and retrive data not update delete

class StudReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer







