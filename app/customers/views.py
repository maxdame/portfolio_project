from django.shortcuts import render
from django.core import serializers
from customers.models import Customer


def index(request):
    return serializers.serialize('json', Customer.objects.all())
