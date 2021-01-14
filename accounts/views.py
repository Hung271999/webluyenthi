from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


class LoginClass(View):
    def get(self,request):
        form=LoginForm()
        a=RegisterForm()
        return render(request,'accounts/login_register.html',{'form':form,'a':a})

    def post(self,request):
        taikhoan=request.POST['username']
        matkhau=request.POST['password']
        user = authenticate(username=taikhoan, password=matkhau)
        if user is None:
            return HttpResponse('Error')
        login(request,user)
        return redirect('/')


class register(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'accounts/login_register.html',{'form':form})

    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        if user is None:
            return redirect('/')
        return redirect('login')
def logoutt(request):
    try:
        logout(request)
    except:
        pass
    return redirect('/')

class changepassword(View):
    def get(self,request):
        return render(request,'accounts/changepassword.html')

    def post(self,request):
        usernames=request.POST['username']
        passwords=request.POST['password']
        newpassword=request.POST['newpassword']
        email=request.POST['email']
        user = authenticate(username=usernames, password=passwords)
        if newpassword == passwords:
            messages.warning(request, 'Mật khậu mới không được trùng mật khẩu cũ !')
            return redirect('changepassword')
        if user is None:
            messages.warning(request, 'Lỗi vui lòng nhập đúng tài khoản hoặc mật khẩu !')
            return redirect('changepassword')
        else:
            user.set_password(newpassword)
            user.email=email
            messages.warning(request, 'Thành công !')
            user.save()
            login(request,user)
            return redirect('changepassword')
