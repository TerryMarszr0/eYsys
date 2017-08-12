#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import redirect,HttpResponse,render
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf


@login_required()
def index(request):

    return render(request,'navi/index.html')