from django.contrib.sites.shortcuts import get_current_site
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

from django.template.loader import render_to_string

from customer.models import Customer
from root.settings import BASE_DIR
import json


@receiver(pre_delete, sender=Customer)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'customer/deleted_customers/', f'customer_{instance.id}.json')

    customer_data = {
        'id': instance.id,
        'full_name': instance.full_name,
        'email': instance.email,
        'phone_number': instance.phone_number,
        'address': instance.address,
        'joined' : instance.joined.isoformat(),

    }

    with open(file_path, mode='w') as file_json:
        json.dump(customer_data, file_json, indent=4)

    print(f'{instance.full_name} is deleted')

    # current_site = get_current_site(request)
    #
    # subject = "Verify Email"
    # message = render_to_string('email/verify_email_message.html', {
    #     'request': request,
    #     'user': user,
    #     'domain': current_site.domain,
    #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #     'token': account_activation_token.make_token(user),
    # })
    # email = EmailMessage(subject, message, to=[email])
    # email.content_subtype = 'html'
    #
    # email.send()

    # This did not work because of request


