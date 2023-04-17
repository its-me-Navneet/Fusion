from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from applications.income_expenditure.models import *
from django.contrib.auth.models import User
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation

class ExpenditureTypeApi(APIView):

    def get(self, request):
        ExpenditureType_obj = ExpenditureType.objects.all();
        serialized_obj = ExpenditureTypeSerializer(ExpenditureType_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})

    def post(self, request):
        data = request.data
        
        # mess = data['mess']
        # _type = data['type']
        # desc = data['desc']
        _expenditure_type =  data['expenditure_type'] 
        # username = get_object_or_404(User,username=request.user.username)
        # idd = ExtraInfo.objects.get(user=username)
        # student = Student.objects.get(id=idd.id)
        obj = ExpenditureType(
            # student_id = student,
            # mess =mess,
            # feedback_type=_type
            # description=desc
             expenditure_type= _expenditure_type
        )
        obj.save()
        return Response({'status':200})