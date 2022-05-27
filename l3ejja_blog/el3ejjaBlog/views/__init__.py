# -*- coding: utf-8 -*-
"""
Definitions of all views of the application.
"""
from django.shortcuts import render

from .home import *


# %% INDEX
def index(request):
    return render(request, 'el3ejjaBlog/index.html')