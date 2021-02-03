import uuid  
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from decouple import config
# from core_api.models import Address
from django.utils import timezone
from rest_api.models import Student

company_name = config('COMPANY-NAME')
company_email = config('COMPANY-EMAIL')
company_address = config('COMPANY-Address')



def generate_txnid():
    return 'txn' + str(uuid.uuid4())

def send_mail_to_student(request,user,amount,order_id):
    now = timezone.now()
    student = Student.objects.filter(user=user).first()
    context = {
            'transaction_id': order_id,
            'Sender_Name': company_name,
            'Sender_Address': company_address,
            'student_name':student.name,
            'grand_total':amount,
          }
    message = get_template('Order-Confirmation.html').render(context)
    msg = EmailMessage(
        'Your Sardarji Communication order',
        message,
        f'{company_email}',
        [f'{student.email}'],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")