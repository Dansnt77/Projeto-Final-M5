from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import AccountSerializer


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
