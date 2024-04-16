from celery import shared_task
import time
from datetime import timedelta
from django.core.mail import send_mail
from catalog.models import Order
from django.conf import settings


@shared_task
def some_task():
    time.sleep(5)
    return 'qwerty'


@shared_task
def some_schedule_task():
    return 'DAROVA'


@shared_task
def check_orders_and_send_mails():
    orders = Order.objects.filter(payment_status='Paid')

    for order in orders:
        if not order.is_notif_sent:
            send_mail(
                'Заказ из магазина',
                f'Ваш заказ {order.id} оплачен и уже в пути',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.user.email],
            )

            order.is_notif_sent = True
            order.save()
