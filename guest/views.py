from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from guest.models import Event, Guest
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index2.html")

#登录操作
def login_action(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"error": "username or password null!"})

        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)#验证登录
            response = HttpResponseRedirect('/event_manage/')
            request.session['username'] = username #将seeeion信息写到服务器
            return response
        else:
            return render(request, "index2.html", {"error": "username or password error!"})

#登录之后的页面
# @login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('username', '')
    return render(request, "event_manage.html", {"user": username, "events": event_list})

@login_required
def logout(request):
    response = HttpResponseRedirect('/index/')
    del request.session['username']
    return response

def sreach_name(request):
    username = request.session.get('username', '')
    search_name = request.GET.get("name", "")
    # aa = search_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# @login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})



