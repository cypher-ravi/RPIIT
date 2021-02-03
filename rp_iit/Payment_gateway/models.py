from django.db import models
from authentication.models import User
from rest_api.models import Trip
# Create your models here.
# {'return_data': {'isConsentPayment': 
# '0', 'mihpayid': '9084144640',
#  'mode': 'CC',
#  'status': 'success',
#  'unmappedstatus': 'captured',
#  'key': 'ZQGI2x56',
#  'txnid': 'txna6784692-f102-4820-920d-68559264ac46',
#  'amount': '9451.00', 
# 'addedon': '2021-02-02 16:19:15', 
# 'productinfo': 'Susan',
#  'firstname': 'Alexander',
#  'lastname': '', 'address1':
#  '', 'address2': '1266 Laurie Fords Suite 714br /New Jason 
#  HI 
# 01847', 'city': '',
#  'state': '', 
# 'country': 'test', 
# 'zipcode': '  
#  ', 'email': 'janicephelps@hotmail.com',
# 'phone': '99376444162', 
# 'udf1': '', 
# 'udf2': '',
#  'udf3': '',
#  'udf4': '',
#  'udf5': '',
#  'udf6': '',
#  'udf7': '',
#  'udf8': '',
#  'udf9': '',
#  'udf10': ''
# , 'hash': 'b456b9722739191a7207696533d5488358d47f5eba704c94eb5cb7c656f3f84c23d48f809598e0307c94b5375cdd4e029f095ef92285eaff8d9259a376ce595e', 
# 'field1': '127913664928',
#  'field2': '369825',
#  'field3': '833002059068314',
# 'field4': 'eG9qMVlDSnI3VE9tekJadGpwR1U=',
# 'field5': '05', 
# 'field6': '',
#  'field7': 'AUTHPOSITIVE', 'field8': '', 'field9': '', 'giftCardIssued': 'true', 'PG_TYPE': 'HDFCPG', 'encryptedPaymentId': '7ACD0801EC47B3C8D52F3E6B18151A7B', 'bank_ref_num': '833002059068314', 'bankcode': 'VISA', 'error': 'E000', 'error_Message': 'No Error', 'name_on_card': 'Test', 'cardnum': '401200XXXXXX1112', 'cardhash': 'This field is no longer supported in postback params.', 'amount_split': '{"PAYU":"9451.00"}', 'payuMoneyId': '250768997', 'discount': '0.00', 'net_amount_debit': '9451'}, 'hash_string': 'VTsYoY3kBp|success|||||||||||janicephelps@hotmail.com|Alexander|Susan|9451.00|txna6784692-f102-4820-920d-68559264ac46|ZQGI2x56', 'generated_hash': 'b456b9722739191a7207696533d5488358d47f5eba704c94eb5cb7c656f3f84c23d48f809598e0307c94b5375cdd4e029f095ef92285eaff8d9259a376ce595e', 'recived_hash': 'b456b9722739191a7207696533d5488358d47f5eba704c94eb5cb7c656f3f84c23d48f809598e0307c94b5375cdd4e029f095ef92285eaff8d9259a376ce595e', 'hash_verified': True}


# class PaymentDetail(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status=	models.CharField(max_length=9)#Transaction Status. (Described in detail in the Transaction Status section)	success;
#     firstname= models.CharField(max_length=25)
#     amount=	models.FloatField(editable = False)
#     txnid=	models.CharField(max_length=25)#Transaction Id passed by the merchant	0nf725;
#     hash=	models.TextField()
#     productinfo	= models.CharField(max_length=25)
#     mobile=	models.CharField(max_length=25)
#     email=	models.CharField(max_length=25)
#     payuMoneyId=models.CharField(max_length=25)
#     payment_mode=	models.CharField(max_length=25)

# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_id = models.IntegerField(null=False)
#     email_id = models.CharField(max_length=45)
#     name = models.CharField(max_length=20)
#     phone = models.CharField(max_length=14,blank=True,null=True)
#     address = models.CharField(max_length=111)
#     state = models.CharField(max_length=111, choices=VALID_STATE_CHOICES)
#     city = models.CharField(max_length=111)
#     order_date =  models.DateTimeField(auto_now_add=True)
#     zip_code = models.CharField(max_length=8)
#     amount = models.IntegerField(null=False)
#     plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
#     discount = models.IntegerField(default=0,null=True,blank=True)
#     role = models.CharField(max_length=100,blank=True, null=True)
#     order_completed = models.BooleanField()

#     def __str__(self):
#         return self.phone


class RegisteredTrip(models.Model):
    order_id = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='RegisteredTrip')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.order_id)


class OrderPayment(models.Model):
    id = models.AutoField(primary_key = True)
    order_summary = models.ForeignKey(RegisteredTrip, on_delete = models.CASCADE)
    # paytm responses 
    currency = models.CharField(max_length=8) # INR
    gateway_name = models.CharField(max_length=25) # WALLET
    response_message = models.TextField() # Txn Success
    bank_name = models.CharField(max_length=25) # WALLET
    Payment_mode = models.CharField(max_length=25)# PPI
    # MID = models.CharField(max_length=8) # VdMxPH61970223458566
    response_code = models.CharField(max_length=3) # 01
    txn_id = models.TextField() #  20200905111212800110168406201874634
    txn_amount = models.CharField(max_length=9) #  2400.00
    order_id = models.IntegerField() #  6556
    status = models.CharField(max_length=12) # TXN_SUCCESS
    bank_txn_id = models.CharField(max_length=12) #  63209779
    txn_date = models.CharField(max_length=23) #  2020-09-05 18:51:59.0
    refund_amount = models.IntegerField(default=0.00) #  0.00
    # test = models.CharField(max_length=23)
    
    def __str__(self):
        return str(self.order_id)

class FailedPayment(models.Model):
    txn_date = models.CharField(max_length=23) #  2020-09-05 18:51:59.0
    response_message = models.TextField() # Txn Success
    response_code = models.CharField(max_length=3) # 01
    txn_id = models.TextField() #  20200905111212800110168406201874634
    txn_amount = models.CharField(max_length=9) #  2400.00
    order_id = models.IntegerField() #  6556
    status = models.CharField(max_length=12) # TXN_SUCCESS
    bank_txn_id = models.CharField(max_length=12) #  63209779
    Payment_mode = models.CharField(max_length=25)# PPI
    gateway_name = models.CharField(max_length=25) # WALLET
    currency = models.CharField(max_length=8) # INR
    def __str__(self):
        return str(self.order_id)

