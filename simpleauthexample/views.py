from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def loginview(request):
    c = {}
    c.update(csrf(request))
    context = {'request': request}
    return render(request, 'login.html', context)

def auth_and_login(request, onsuccess="/simpleauthexample/", onfail="/simpleauthexample/login/"):
    user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)  

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    if not user_exists(post.get('email')): 
        user = create_user(username=post['email'], email=post.get('email'), password=post.get('password'))
    	return auth_and_login(request)
    else:
    	return auth_and_login(request)
    	#return redirect("/simpleauthexample/login/")

@login_required(login_url='/simpleauthexample/login/')
def secured(request):
    context = {'request': request}
    return render(request, 'secure.html', context)
    #return render_to_response("secure.html")

def logout_view(request):
    logout(request)
    return redirect('/simpleauthexample/login/')
    
