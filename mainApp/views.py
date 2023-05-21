from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.core.mail import send_mail
from mainApp.models import Buyer,mashalachicken,tavadhosa,registerresturantNewModels2
from TomatoProj.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
from django.conf import settings
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.conf import settings
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def index(request):
	return render(request,'index.html')
def LogoutPage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")
def loginPage(Request):
    if (Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin")
            else:
                
                subject = 'LogedIn | FoodOpia'
                message = f'Hi {user.username}, You are Now Successfully Loged In to our WEBSITE FoodOpia'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )

                return redirect("/")
            
        else:
        	return HttpResponse("Error")
   
    return render(Request, "login.html")
# Create your views here.
def registerResturant(Request):

    if (Request.method == "POST"):
        da = registerresturantNewModels2()

        da.restaurantName = Request.POST.get("restaurantName") 
        da.ownerName = Request.POST.get("ownerName")
        da.GSTNumber = Request.POST.get("GSTNumber")
        da.FSSAINumber = Request.POST.get("FSSAINumber")
        da.Address = Request.POST.get("Address")
        da.PhoneNo = Request.POST.get("PhoneNo")
        da.UserName = Request.POST.get("UserName")
        da.Email = Request.POST.get("Email")
        da.save()
        # return HttpResponse("Done")
    return render(Request,'registerResturant.html')
def successRegistration(Request):
    return render(Request, "successRegistration.html")
def signupPage(Request):
    if (Request.method == "POST"):
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        if (p == cp):
            b = Buyer()
            b.name = Request.POST.get("name")
            b.username = Request.POST.get("username")
            b.phone = Request.POST.get("phone")
            b.email = Request.POST.get("email")
            user = User(username=b.username, email=b.email)
            if (user):
                user.set_password(p)
                user.save()
                b.save()
                subject = 'Registered | FoodOpia'
                message = f'Hi {user.username}, You are Now Successfully Registed to our WEBSITE FoodOpia'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [b.email, ]
                send_mail( subject, message, email_from, recipient_list )

                return redirect("/login/")
            else:
                messages.error(Request, "Username Already Taken!!!!!!")
        else:
            messages.error(
                Request, "Password And Confirm Password Doesn't Matched!!!")
    return render(Request, "signup.html")
def resturantNearMe(Request):
    return render (Request,"resturantNearMe.html")
def AboutUs(request):
    return render(request,'AboutUs.html')
def order(request):
    return render(request,"order.html")
def Payment(request):
    
    return render(request,"Payment.html")
def detail(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'detail.html', context=context)
    # data = mashalachicken.objects.all()
    # client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))

    # paymentOrder = client.order.create( {'amount' : "500",'currency':"INR",'payment_capture' : 1})
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # print(paymentOrder)
    # return render(request,"detail.html",{"data":data},context=paymentOrder)
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
            
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    # else:
    #    # if other than POST request is made.
    #     return HttpResponse("if other than POST request is made")
def detail2(request):
    data = tavadhosa.objects.all()
    return render(request,"detail2.html",{"data":data})
def cod(request):
    return render(request,"cod.html")
def location(request):
    return render(request,"location.html")
def Privacy(request):
    return render(request,"Privacy.html")
def feedback(request):
    return render (request,'feedback.html')
def paymentlink(request):
    return render (request,'paymentlink.html')

def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")