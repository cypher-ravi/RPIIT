from django.conf import settings
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render,reverse
from django.views.decorators.csrf import csrf_exempt

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
                    payu_checkout(request,student,amount,trip)
                    # redirect('Payment_gateway:payu_checkout',args=(student),kwargs=amount)
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
def payu_checkout(request,student,amount,trip):
    if request.method == 'GET':
        # The dictionary data  should be contains following details
        data = { 'amount': amount, 
            'firstname': student.name, 
            'email': student.email,
            'phone': student.user.phone, 
            'lastname': 'test', 
            'address2': student.address, 
            'state': 'test', 'country': 'test', 
            'zipcode': 'tes', 'udf1': '', 
            'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
        }

        # No Transactio ID's, Create new with paywix, it's not mandatory
        # Create your own
        # Create transaction Id with payu and verify with table it's not existed
        txnid = '123'
        data.update({"txnid": txnid})
        payu_data = payu.transaction(**data)
        return render(request, 'checkout.html', {"posted": payu_data})
    



# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)


@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)



