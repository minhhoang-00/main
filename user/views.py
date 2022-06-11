from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import getAllUser, setUser
from user.models import user
# Create your views here.

class GetAllUser(APIView):
    
    def get(self, request):
        mydata = user.objects.all()
        data = getAllUser(mydata, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = setUser(data=request.data)
        if not mydata.is_valid():
            return Response('Dữ Liệu Lỗi', status=status.HTTP_400_BAD_REQUEST)
        email = mydata.data['email']
        password = mydata.data['password']
        fullname = mydata.data['fullname']
        phonenumber = mydata.data['phonenumber']
        if user.objects.filter(email=email).exists():
            return Response('Dữ Liệu Đã Tồn Tại', status=status.HTTP_303_SEE_OTHER)
        else: 
            user.objects.create(email=email, password=password, fullname=fullname, phonenumber=phonenumber)
            return Response('Tạo Dữ Liệu Thành Công', status=status.HTTP_200_OK)
        
    