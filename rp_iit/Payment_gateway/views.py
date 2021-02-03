from django.conf import settings
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render,reverse
from django.views.decorators.csrf import csrf_exempt
import requests
from authentication.models import User
# Import Payu from Paywix
import json
from rest_api.models import Student, Trip
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_txnid


# -------------------------------------------PAYTM------------------------------------------------


from .PayTm import CheckSum
from .models import *
import random
from .utils import send_mail_to_student
MKEY = 'CoFOS0%M%hUCPkcl'
MID = 'CEGtTI62617142353568'

def payment(request):
    return render(request, 'payment-form.html',{'plan_id':0})

@api_view(['GET', 'POST'])
def purchase(request, user_id, amount, trip_id):
    
    user = User.objects.filter(id=user_id).first()
    if user != None:
        student = Student.objects.filter(user = user).first()
        if student != None:
            trip = Trip.objects.filter(id = trip_id).first()
            if trip != None:
                if trip.charges == amount:
                    if RegisteredTrip.objects.filter(trip = trip).filter(user = user).exists():
                        return Response({'already_registered':True})
                    order_id = random.randint(0,99999)
                    obj = RegisteredTrip(user = user, trip = trip, order_id = order_id)
                    obj.save()
                    detail_dict = {
                        "MID": MID,
                        "TXN_AMOUNT":amount,
                        "CUST_ID":student.email,
                        "CHANNEL_ID": "WEB",
                        "WEBSITE": "WEBSTAGING",
                        "INDUSTRY_TYPE_ID": "Retail",
                        "ORDER_ID": str(order_id),
                        "CALLBACK_URL": f'http://127.0.0.1:8000/payment/paytm_request_handler',
                    }
                    param_dict = detail_dict
                    # CheckSum.generateSignature 
                    param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(detail_dict, MKEY)
                    return render(request, 'redirect.html', {'detail_dict': param_dict})
                else:
                    return Response({"amount_valid":False})
            else:
                return Response({"trip_exists":False})
        else:
            return Response({"students":False})
    else:
        return Response({"user_exists":False})


@csrf_exempt
@api_view(['POST'])
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        # another if to handle if user load refresh
        is_order_exist = OrderPayment.objects.filter(order_id=form["ORDERID"]).exists()
        if is_order_exist == False:
            # FOR ALL VALUES
            for i in form.keys():
                response_dict[i] = form[i]
                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]
            verify = CheckSum.verifySignature(response_dict, MKEY, response_check_sum)
            # response_dict["STATUS"] = "PENDING"

            if(verify and response_dict["STATUS"] != "TXN_FAILURE") or (verify and response_dict["STATUS"] == "PENDING"):
                order_payment = OrderPayment()
                # id = models.AutoField(primary_key = True)
                order = RegisteredTrip.objects.get(order_id=response_dict["ORDERID"])

                order_payment.order_summary = order
                # paytm responses
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                # Txn Success
                order_payment.response_message = response_dict["RESPMSG"]
                order_payment.bank_name = response_dict["BANKNAME"] # WALLET
                # PPI
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]
                # MID = models.CharField(max_length=8) # VdMxPH61970223458566
                order_payment.response_code = response_dict["RESPCODE"]  # 01
                # 20200905111212800110168406201874634
                order_payment.txn_id = response_dict["TXNID"]
                # 2400.00
                order_payment.txn_amount = response_dict["TXNAMOUNT"]
                order_payment.order_id = response_dict["ORDERID"]  # 6556
                order_payment.status = response_dict["STATUS"]  # TXN_SUCCESS
                # 63209779
                order_payment.bank_txn_id = response_dict["BANKTXNID"]
                # 2020-09-05 18:51:59.0
                order_payment.txn_date = response_dict["TXNDATE"]
                # order_payment.refund_amount =  #  0.00
                order_payment.save()
                order_id=response_dict["ORDERID"]
                send_mail_to_student(request, order.user, response_dict["TXNAMOUNT"], response_dict["ORDERID"])
                return render(request, 'success.html')
            else:
                failed_payment = FailedPayment() 
                failed_payment.txn_date = response_dict["TXNDATE"]
                failed_payment.response_message = response_dict["RESPMSG"]
                failed_payment.response_code = response_dict["RESPCODE"]
                failed_payment.bank_txn_id = response_dict["BANKTXNID"]
                failed_payment.txn_id = response_dict["TXNID"]
                failed_payment.txn_amount = response_dict["TXNAMOUNT"]
                failed_payment.order_id = response_dict["ORDERID"] 
                failed_payment.status = response_dict["STATUS"]
                failed_payment.Payment_mode = response_dict["PAYMENTMODE"]
                failed_payment.gateway_name = response_dict["GATEWAYNAME"]
                failed_payment.currency = response_dict["CURRENCY"]
                failed_payment.save()

#                 Order.objects.filter(
#                     order_id=response_dict["ORDERID"]).delete()
                return render(request, 'Failure.html')
        else:
            return HttpResponse('Already Placed Order, check your order by your OrderId ')
    return HttpResponse('Invalid Request')

@api_view(['POST'])
def order_status(request):
    try:
        if request.method =='POST':
            slug = request.data['order-id']
            print("----------",slug)
            if RegisteredTrip.objects.filter(order_id = slug).exists():
                paytmParams = dict()
                
                paytmParams["MID"] = MID
                paytmParams["ORDERID"] = slug
                
                checksum = CheckSum.generateSignature(paytmParams, MKEY)
                paytmParams["CHECKSUMHASH"] = checksum
                post_data = json.dumps(paytmParams)

                # for Staging
                url = "https://securegw-stage.paytm.in/order/status"

                # for Production
                # url = "https://securegw.paytm.in/order/status"

                response = requests.post(url, data=post_data, headers={
                                            "Content-type": "application/json"}).json()
                
                if response["STATUS"] == "TXN_SUCCESS":
                    obj = OrderPayment.objects.get(order_id=slug)
                    obj.status = response["STATUS"]
                    obj.response_code = response["RESPCODE"]
                    obj.response_message = response["RESPMSG"]
                    obj.txn_date = response["TXNDATE"]
                    obj.bank_name = response["BANKNAME"]
                    obj.save()
                    return Response({'detail':"order success fully placed"})
                elif response["STATUS"] == "TXN_FAILURE":
                    return Response({'detail':"Booking Failed"})
                else:
                    return Response({'detail':"order is still in pending state"})
            return Response({'detail':"Invalid Request"})
        return Response({'detail':'form.html'})
    except :
        return Response({'detail':'An unexpected error occured'})

