from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Products
from django.db.models.functions import Now
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


@shared_task()
def deactivate_product():

    tim = Products.objects.filter(created_at__lte=Now() - timedelta(minutes=1))

    for product in tim:

        time_difference = timezone.now() - product.created_at

        if time_difference >= timedelta(minutes=1):
            product.is_active = False
            product.save()
            
            token_generator = PasswordResetTokenGenerator()
            uid = urlsafe_base64_encode(force_bytes(product.id))
            token = token_generator.make_token(product.user_id)

            domain = settings.DOMAIN_NAME  
            reactivation_url = f"http://{domain}/reactivate/{uid}/{token}/"


            send_mail(
                "Product Deactivation",
                f'Your product "{product.name}" has been deactivated. You can reactivate it by clicking the following link: {reactivation_url}',
                "from@example.com",
                [product.user_id.email],
                fail_silently=False,
            )

    return " Ugurla deaktiv edildi "
