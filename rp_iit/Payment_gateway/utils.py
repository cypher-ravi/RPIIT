import uuid  
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from decouple import config
# from core_api.models import Address
# from django.utils import timezone


# company_name = config('COMPANY-NAME')
# company_email = config('COMPANY-EMAIL')
# company_address = config('COMPANY-Address')
# delivery_charges = config('DELIVERY-CHARGES')


def generate_txnid():
    return 'txn' + str(uuid.uuid4())

# def send_mail_to_customer_order(request,user,order_items,transaction_id):
    now = timezone.now()
    total = order_items.get_total() + float(delivery_charges)
    address = Address.objects.filter(user=user).order_by('-created_at').first()

    context = {
            'transaction_id': transaction_id,
            'Sender_Name': company_name,
            'Sender_Address': company_address,
            'customer_name': user.phone,
            'customer_address': address.street_address + ' ' + address.apartment_address+ ' ' + address.zip_code,
            'subtotal':order_items.get_total(),
            'delivery_charges':delivery_charges,
            'grand_total':total,
          }
    message = get_template('Order-Confirmation.html').render(context)
    msg = EmailMessage(
        'Your Sardarji Communication order',
        message,
        f'{company_email}',
        [f'{address.email}'],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")