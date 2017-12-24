from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Views
def index(request, template_name='index.html'):
    data = {}
    data['user'] = 'hello'
    return render(request, template_name, data)
