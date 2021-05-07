from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib import auth

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BaseAuthentication
from rest_framework.authtoken.models import Token

from .models import Profile

    
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        user = User(username=email)
        user.set_password(password)
        profile = Profile(user=user, first_name=first_name,last_name=last_name,phone_number=phone_number,address=address)
        user.save()
        profile.save()
        # refresh = RefreshToken.for_user(user)
        token = Token.objects.create(user=user)
        return redirect('userlogin')
    return render(request,'register.html')

class Testting(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        return  Response({'get':'chaking is authenticate it is login ','user':request.user.username})

class AuthView(APIView):
    
    def post(self , request):
        email = request.data['email']
        password = request.data['password']
        user = auth.authenticate(username=email, password=password)
        if user:
            token, iscreated = Token.objects.get_or_create(user=user)
            return Response(
            {
                "status":"success you are login successfully" ,
                'user_id' :user.id , 
                'token' : token.key,
                'user' : user.username,

                # 'refresh': str(refresh),
                # 'access': str(refresh.access_token)
            })
        else:
            return Response({'error':'username or password invalid'})    
        # refresh = RefreshToken.for_user(user)

def userlogin(request):
    return render(request,'login.html')


def profile(request,username):
    user = User.objects.get(username= username)
    param = {
        'user' : user
    }
    return render(request,'profile.html',param)