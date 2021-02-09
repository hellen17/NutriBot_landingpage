from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
   return render(request, 'index.html')

def chatroom(request):
   return render(request, 'chatroom.html')

def login(request):
   return render(request, 'login.html')

def register(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Account created for {username}!')
         return redirect('chatroom')
   else:
      form = UserCreationForm()   
   form = UserCreationForm()
   return render(request, 'register.html', {'form':form})  


