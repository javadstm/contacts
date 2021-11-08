from django.shortcuts import render
from django.shortcuts import redirect
from contact.models import contact


# Create your views here.
def index(request):
    contacts = contact.objects.all()
    return render(request, 'index.html', {'contacts':contacts})


def addContact(request):
    if request.method == 'POST':
        new_contact = contact(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            address=request.POST['address'],

        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new-contact.html')


def profile(request, pk):
    contacts = contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contacts})


def edit(request, pk):
    updatedContact = contact.objects.get(id=pk)
    if request.method == 'POST':
        updatedContact.first_name = request.POST['first_name']
        updatedContact.last_name = request.POST['last_name']
        updatedContact.phone_number = request.POST['phone_number']
        updatedContact.email = request.POST['email']
        updatedContact.address = request.POST['address']
        updatedContact.save()
        return redirect('/profile/'+ str(updatedContact.id))
    return render(request, 'edit.html', {'contact':updatedContact})


def delete(request, pk):
    deleted = contact.objects.get(id=pk)

    if request.method == 'POST':
        deleted.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact':deleted})

