from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response  import Response 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from checklist_app.models import CheckList,CheckListItem
from checklist_app.serializers import CheckListSerializer
# Create your views here.

@api_view()
def test_api(request):
    return Response({'name': 'Charu'})


class TestAPIView(APIView):
    def get(self,request,format=None):
        return Response({'name': 'Charu from Class_v'})


class CheckListAPIView(APIView):
    def get(self,request, format=None):
        data= CheckList.objects.all()
        serializer = CheckListSerializer(data,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)


