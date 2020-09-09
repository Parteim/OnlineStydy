from django.shortcuts import render, redirect
from django.http import HttpResponse

import json


def index(request):
    data = {
        'title': 'Home'
    }

    return render(request, 'index.html', data)
