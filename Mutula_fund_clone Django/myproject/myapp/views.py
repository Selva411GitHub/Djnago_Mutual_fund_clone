from django.shortcuts import render,redirect
from myapp.models import User
from django.contrib import messages
import requests
# Create your views here.

    
URL =  'https://api.mfapi.in/mf/'


def home(request):
    key = User.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        fundcode = request.POST['fundcode']
        unitheld = request.POST['unitsheld']
        invested_amount = request.POST['investedamount']
        response = requests.get(URL+fundcode)
        data = response.json()
        
        fundhousename = data['meta']['fund_house']
        date = data['data'][0]['date']
        nav = float(data['data'][0]['nav'])
        currentvalue = float(nav) * float(invested_amount)
        growth = float(currentvalue) - float(unitheld)
        

        new = User()
        new.name = name
        new.fund_house = fundhousename
        new.fund_number = fundcode
        new.unit_held = unitheld
        new.invested = invested_amount
        new.unit_held = unitheld
        new.currentvalue = currentvalue
        new.nav = nav
        new.growth = growth
        new.save()  
        messages.success(request,'newuser added succesfully')
        return redirect('home')
    return render(request, 'home.html',{'data':key})



def update(request,id):
    id_user = User.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        fundcode = request.POST['fundcode']
        unitheld = request.POST['unitsheld']
        invested_amount = request.POST['investedamount']
        response = requests.get(URL+fundcode)
        data = response.json()
        
        fundhousename = data['meta']['fund_house']
        date = data['data'][0]['date']
        nav = float(data['data'][0]['nav'])
        currentvalue = float(nav) * float(invested_amount)
        growth = float(currentvalue) - float(unitheld)

        id_user.name = name
        id_user.fund_house = fundhousename
        id_user.fund_number = fundcode
        id_user.unit_held = unitheld
        id_user.invested = invested_amount
        id_user.unit_held = unitheld
        id_user.currentvalue = currentvalue
        id_user.nav = nav
        id_user.growth = growth
        id_user.save()  
        messages.success(request,'user edited succesfully')
        return redirect('home')
    return render(request,'edit.html',{'data':id_user})


def delete(request,id):
    id_data = User.objects.get(id=id)
    id_data.delete()
    messages.success(request,'user deleted succesfully')
    return redirect('home')