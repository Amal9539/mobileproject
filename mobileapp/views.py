from django.shortcuts import render
from django.http import HttpResponse
from mobileapp import views
from mobileapp import models
from .models import User
from .models import Login
import pywhatkit
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from datetime import datetime
import pywhatkit as kit
import os
import time

def login_get(request):
    return render(request, 'login.html')
def home_get(request):
        return render(request, 'Home.html')


def login_post(request):
    if request.method == 'POST':
        UserName = request.POST.get('textfield')
        Password = request.POST.get('textfield2')

        # check if user exists
        a = Login.objects.filter(Username=UserName, Password=Password)

        if a.exists():
            l = a.first()
            request.session['lid'] = l.id
            return HttpResponse('''<script>alert("Login Successful");window.location='/mobileproject/home_get/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid Username or Password");window.location='/mobileproject/login_get/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid Request Method");window.location='/mobileproject/login_get/'</script>''')


def user_get(request):
    return render(request, 'user.html')  # your HTML file name

def user_post(request):
    if request.method == 'POST':
        phonemodel = request.POST.get('phonemodel')
        imeino = request.POST.get('imeino')
        password = request.POST.get('password')
        complaint = request.POST.get('complaint')
        customer_name = request.POST.get('customer_name')
        phone_number = request.POST.get('phone_number')

        # Save data to the model
        User.objects.create(
            phonemodel=phonemodel,
            imeino=imeino,
            password=password,
            complaint=complaint,
            customer_name=customer_name,
            phone_number=phone_number
        )

        return HttpResponse(
            '''<script>alert("Details saved successfully!");window.location='/mobileproject/user_view/'</script>'''
        )

def user_view(request):
    data = User.objects.all()
    return render(request, 'userview.html', {'data': data})

def user_view_post(request):
       
       return render(request, "/template/userview.html")

#  👇 Set your shop's WhatsApp number here (must be logged into WhatsApp Web)
SHOP_WHATSAPP_NUMBER = "+919562612834"  # replace with your own WhatsApp number

def user_action(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        action_type = request.POST.get('action_type')
        bill_amount = request.POST.get('bill_amount', None)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse("<script>alert('User not found');window.location='/mobileproject/user_view/'</script>")

        # Get customer's WhatsApp number from database
        customer_number = str(user.phone_number).strip()
        if not customer_number.startswith("+"):
            customer_number = "+91" + customer_number  # default to India code

        # Prepare message content
        if action_type == "completed":
            message = (
                f"Hello {user.customer_name},\n"
                f"Your device ({user.phonemodel}) repair is completed.\n"
                f"Bill Amount: ₹{bill_amount}\n\n"
                f"Thank you!\n- {SHOP_WHATSAPP_NUMBER} (Service Center)"
            )
            image_path = os.path.abspath("static/completed.jpg")
        else:
            message = (
                f"Hello {user.customer_name},\n"
                f"We are sorry to inform you that we couldn't repair your device ({user.phonemodel}).\n\n"
                f"- {SHOP_WHATSAPP_NUMBER} (Service Center)"
            )
            image_path = os.path.abspath("static/return.jpg")
            if not os.path.exists(image_path):
                return HttpResponse("<script>alert('Image file not found. Please check the path.');window.location='/mobileproject/user_view/'</script>")


        try:
            # Send message instantly using WhatsApp Web (logged in with SHOP_WHATSAPP_NUMBER)
            import time
            pywhatkit.sendwhatmsg_instantly(phone_no=customer_number, message=message, wait_time=10, tab_close=False)
            time.sleep(8)  # allow extra time for message to load and send


            return HttpResponse("<script>alert('WhatsApp message sent successfully!');window.location='/mobileproject/user_view/'</script>")

        except Exception as e:
            return HttpResponse(f"<script>alert('Error sending WhatsApp message: {e}');window.location='/mobileproject/user_view/'</script>")

    return redirect('/mobileproject/user_view/')