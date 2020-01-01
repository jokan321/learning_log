from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.


from django.contrib.auth import logout

def logout_view(request):
    '''ユーザログアウト'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''ユーザ新規登録'''
    if request.method!='POST':
        #空のフォームを表示する
        form = UserCreationForm()
    else:
        #入力完了フォームを処理する
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #ユーザーに自動登録させ、リダイレクトする
            authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)