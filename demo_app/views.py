from django.shortcuts import render,redirect
from .models import profile
from .forms import add_form
# Create your views here.
def home(request):
    profile_data=profile.objects.all()
    return render(request,'home.html',{'data':profile_data})

def add_people(request):
    if request.method=='POST':
        form=add_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('add_people')
    form=add_form()
    return render(request,'register.html',{'form':form})

def delete(request,pk):
    data=profile.objects.get(pk=pk)
    data.delete()
    return redirect('home')