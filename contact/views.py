from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render

from .decorators import unauthenticated_user
from .forms import ContactForm
from .models import contact


# Create your views here.

def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@unauthenticated_user
def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'login.html',)


@login_required(login_url='login')
def index(request):
    contacts = contact.objects.filter(author_id=request.user.id)
    context = {'contacts': contacts}

    return render(request,'index.html',context)


@login_required(login_url='login')
def addContact(request):
    form = ContactForm()
    context = {'form': form}
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.author = request.user
            instance.save()
            return redirect('/index')

    return render(request, 'new-contact.html',context)


@login_required(login_url='login')
def profile(request,pk):
    contacts= contact.objects.get(id=pk)
    context = {'contacts': contacts}

    return render(request,'contact-profile.html', context)


@login_required(login_url='login')
def edit (request,pk):
    contacts = contact.objects.get(id=pk)
    form = ContactForm(instance=contacts)
    context = {'contacts': contacts,'form':form}
    if request.method=='POST':
        form = ContactForm(request.POST, instance=contacts)
        if form.is_valid():
            instance = form.save()
            instance.author = request.user
            instance.save()
            return redirect('/index')
    return render(request,'edit.html',context)


@login_required(login_url='login')
def logoutt(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='login')
def delete(request,pk):
    contacts = contact.objects.get(id=pk)
    context={'contacts':contacts}
    if request.method=='POST':
        contacts.delete()
        return redirect('/index')

    return render(request,'delete.html',context)



def home(request):
    return render(request,'home.html')