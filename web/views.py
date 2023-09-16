from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class StudentView(APIView):
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        result=Students.objects.all()
        serializers=StudentSerializer(result, many=True)
        return Response({'status':'success','students':serializers.data}, status=200)
    
    def delete(self, request, id=None):
        result=get_object_or_404(Students,id=id)
        result.delete()
        return Response({"status": "success","data":"Record Deleted"})
    