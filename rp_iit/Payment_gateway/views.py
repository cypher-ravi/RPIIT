from django.conf import settings
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render,reverse
from django.views.decorators.csrf import csrf_exempt
import requests
from authentication.models import User
# Import Payu from Paywix
from paywix.payu import Payu
from rest_api.models import Student, Trip
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_txnid

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

# Create Payu Object for making transaction
# The given arguments are mandatory
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)

@api_view(['GET'])
def verify_user_and_amount(request,user_id,amount,trip_id):
    user = User.objects.filter(id=user_id).first()
    if user != None:
        student = Student.objects.filter(user = user).first()
        if student != None:
            trip = Trip.objects.filter(id = trip_id).first()
            if trip != None:
                if trip.charges == amount:
                    info_data = {
                        'amount':amount,
                        'email':student.email,
                        'phone':student.user.phone,
                        'name':student.name,
                        'address':student.address,
                        'trip':trip.name
                    }
                    # url = 'http://127.0.0.1:8000/payment/payu/'# use for local server
                    url = 'http://rpiit.herokuapp.com/payment/payu/'# use for local server
                    response = requests.post(url,data=info_data)
                    return HttpResponse(response)
                else:
                    return Response({"detail":'trip amount not valid'})
            else:
                return Response({"detail":'trip not exists'})
        else:
            return Response({"detail":'student profile not exists'})
    else:
        return Response({"detail":'user not exists'})

# Payu checkout page
@csrf_exempt
def payu_checkout(request,**kwargs):
    if request.method == 'POST':
        data = { 'amount': request.POST.get('amount'), 
            'firstname': request.POST.get('name'), 
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'), 
            'lastname': 'test', 
            'address2': request.POST.get('address'), 
            'productinfo': request.POST.get('trip'),
            'state': 'test', 'country': 'test', 
            'zipcode': 'tes', 'udf1': '', 
            'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
        }

        # No Transactio ID's, Create new with paywix, it's not mandatory
        # Create your own
        # Create transaction Id with payu and verify with table it's not existed
        txnid = generate_txnid() 
        data.update({"txnid": txnid})
        payu_data = payu.transaction(**data)
        return render(request, 'checkout.html', {"posted": payu_data})
    



# Payu success return page
# @csrf_exempt
# def payu_success(request):
#     data = {k: v[0] for k, v in dict(request.POST).items()}
#     response = payu.verify_transaction(data)
#     print('--------------------------',response)

#     return render(request, 'success.html')


# @csrf_exempt
# def payu_failure(request):
#     data = {k: v[0] for k, v in dict(request.POST).items()}
#     response = payu.verify_transaction(data)
#     print(response)
#     # {'return_data': {}, 'hash_string': 'VTsYoY3kBp|None|||||||||||None|None|None|None|None|None', 'generated_hash': '9691a87e776456870ac3565a24f1eedbdf50e703e030645806d7afd075acd45d9798ef6355f9345f7957ca321273d15267a78b9a2f879014cf339db2fbb3a72e', 'recived_hash': None, 'hash_verified': False}
#     return render(request, 'failure.html')



from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# from django.core.context_processors import csrf
from django.template.context_processors import csrf


def Home(request):
	MERCHANT_KEY = ""
	key=""
	SALT = ""
	PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment"
	action = ''
	posted={}
	# Merchant Key and Salt provided y the PayU.
	for i in request.POST:
		posted[i]=request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid']=txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key']=key
	hash_string=''
	hashVarsSeq=hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string+=str(posted[i])
		except Exception:
			hash_string+=''
		hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	action =PAYU_BASE_URL
	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
		return render(request, 'current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://test.payu.in/_payment" })
	else:
		return render(request, 'current_datetime.html',{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." })

@csrf_protect
@csrf_exempt
def payu_success(request):
    c = {}
    c.update(csrf(request))
    status=request.POST["status"]
    firstname=request.POST["firstname"]
    amount=request.POST["amount"]
    txnid=request.POST["txnid"]
    posted_hash=request.POST["hash"]
    key=request.POST["key"]
    productinfo=request.POST["productinfo"]
    email=request.POST["email"]
    salt="GQs7yium"
    try:
        additionalCharges=request.POST["additionalCharges"]
        retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
    if(hashh !=posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ",txnid)
        print("We have received a payment of Rs. ", amount ,". Your order will soon be shipped.")
    return render(request, 'sucess.html',{"txnid":txnid,"status":status,"amount":amount})


@csrf_protect
@csrf_exempt
def payu_failure(request):
    c = {}
    c.update(csrf(request))
    status=request.POST["status"]
    firstname=request.POST["firstname"]
    amount=request.POST["amount"]
    txnid=request.POST["txnid"]
    posted_hash=request.POST["hash"]
    key=request.POST["key"]
    productinfo=request.POST["productinfo"]
    email=request.POST["email"]
    salt=""
    try:
        additionalCharges=request.POST["additionalCharges"]
        retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
    if(hashh !=posted_hash):
        print("Invalid Transaction. Please try again")
    else:
        print("Thank You. Your order status is ", status)
        print("Your Transaction ID for this transaction is ",txnid)
        print("We have received a payment of Rs. ", amount ,". Your order will soon be shipped.")
    return render(request, "Failure.html",{'request':request,'c':c})

	



