from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import getAllUser, Login, register
from user.models import user
# Create your views here.


class GetAllUser(APIView):

    def get(self, request):
        mydata = user.objects.all()
        data = getAllUser(mydata, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

    def post(self, request):
        mydata = Login(data=request.data)
        if not mydata.is_valid():
            return Response('Dữ Liệu Lỗi', status=status.HTTP_400_BAD_REQUEST)
        email = mydata.data['email']
        matkhau = mydata.data['matkhau']
        if user.objects.filter(email=email).exists():
            return Response('Đăng Nhập Thành Công', status=status.HTTP_200_OK)
        else:
            return Response('Tài Khoản Không Tồn Tại', status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):

    def post(self, request):
        mydata = register(data=request.data)
        if not mydata.is_valid():
            return Response('Dữ Liệu Lỗi', status=status.HTTP_400_BAD_REQUEST)
        email = mydata.data['email']
        matkhau = mydata.data['matkhau']
        bienso = mydata.data['bienso']
        loaixe = mydata.data['loaixe']
        if user.objects.filter(email=email).exists():
            return Response('Tài Khoản Đã Tồn Tại', status=status.HTTP_400_BAD_REQUEST)
        else:
            cs = user.objects.create(email=email, matkhau=matkhau, bienso=bienso, loaixe=loaixe)
            return Response('Đăng Ký Thành Công', status=status.HTTP_200_OK)
