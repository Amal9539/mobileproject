from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Login
import pywhatkit
import os
import time

def login_get(request):
    return render(request, 'login.html')

def home_get(request):
    return render(request, 'Home.html')

def login_post(request):
    if request.method == 'POST':
        username = request.POST.get('textfield')
        password = request.POST.get('textfield2')

        user = Login.objects.filter(Username=username, Password=password)
        if user.exists():
            request.session['lid'] = user.first().id
            return HttpResponse("<script>alert('Login Successful');window.location='/mobileproject/home_get/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid Login');window.location='/mobileproject/login_get/'</script>")

def user_get(request):
    return render(request, 'user.html')

def user_post(request):
    if request.method == 'POST':
        User.objects.create(
            phonemodel=request.POST.get('phonemodel'),
            imeino=request.POST.get('imeino'),
            password=request.POST.get('password'),
            complaint=request.POST.get('complaint'),
            customer_name=request.POST.get('customer_name'),
            phone_number=request.POST.get('phone_number'),
            actual_price=request.POST.get('actual_price') or None,
            status="Pending"
        )

        return HttpResponse("<script>alert('Saved Successfully');window.location='/mobileproject/user_view/'</script>")

def user_view(request):
    data = User.objects.all().order_by('id')
    return render(request, 'userview.html', {'data': data})

SHOP_WHATSAPP_NUMBER = "+919562612834"

def user_action(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        action_type = request.POST.get('action_type')
        bill_amount = request.POST.get('bill_amount')

        user = User.objects.get(id=user_id)

        customer_number = str(user.phone_number)
        if not customer_number.startswith("+"):
            customer_number = "+91" + customer_number

        if action_type == "completed":
            user.actual_price = bill_amount
            user.status = "Completed"
            user.save()

            message = (
                f"Hello {user.customer_name},\n"
                f"Your {user.phonemodel} repair is completed.\n"
                f"Bill Amount: ₹{bill_amount}\n\n"
                f"Thank you!"
            )
        else:
            user.status = "Returned"
            user.save()

            message = (
                f"Hello {user.customer_name},\n"
                f"Your {user.phonemodel} could not be repaired.\n\n"
                f"Sorry for inconvenience."
            )

        pywhatkit.sendwhatmsg_instantly(customer_number, message, wait_time=10)
        time.sleep(5)

        return redirect('/mobileproject/user_view/')
