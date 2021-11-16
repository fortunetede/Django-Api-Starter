# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Sum
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils import timezone
import requests
import json
from django.core.mail import EmailMessage
import time
from decimal import Decimal
from django.http import HttpResponse
from django.db.models import Count
from django.template.loader import render_to_string
import os
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import urllib.request
from rest_framework.authtoken.models import Token
import hashlib

from apps.users.models import APPUser

def home(request):
    return render(request, 'index.html')

