from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Saikat'})


def send_email(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Saikat'}
        )
        message.send(['john@buy.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Saikat'})
