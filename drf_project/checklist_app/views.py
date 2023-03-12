from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response  import Response 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from checklist_app.models import CheckList,CheckListItem
from checklist_app.serializers import CheckListSerializer,CheckListItemSerializer
# Create your views here.

@api_view()
def test_api(request):
    return Response({'name': 'Charu'})


class TestAPIView(APIView):
    def get(self,request,format=None):
        return Response({'name': 'Charu from Class_v'})


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    def get(self,request, format=None):
        data= CheckList.objects.all()
        serializer = CheckListSerializer(data,many=True)
        print(serializer.data)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def post(self, request, format=None):
        serializer = CheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data= serializer.data
            return Response(serializer_data, status= status.HTTP_201_CREATED)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
        # print(request.data)
        # serialized_data= None
        # return Response(serializer_data, status= status.HTTP_201_CREATED)

class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self,pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data= serializer.data
        return Response(serialized_data)

    def put(self, request, pk, format=None):
        check_item = self.get_object(pk)
        serializer = self.serializer_class(check_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status= status.HTTP_201_CREATED)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data= serializer.data
            return Response(serialized_data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class CheckListItemAPIView(APIView):
    serializer_class = CheckListItemSerializer

    def get_object(self,pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data= serializer.data
        return Response(serialized_data)

    def put(self, request, pk, format=None):
        check= self.get_object(pk)
        serializer = self.serializer_class(check, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status= status.HTTP_201_CREATED)
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

