import django.dispatch

user_password_update = django.dispatch.Signal(providing_args=['instance'])
