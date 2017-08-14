#! /usr/bin/env python
# -*- coding: utf-8 -*-
# update by guohongze@126.com
from django.shortcuts import render, HttpResponseRedirect, RequestContext,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import LoginUserForm, EditUserForm, ChangePasswordForm
from django.contrib.auth import get_user_model
from django.core import serializers
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
import json
from .forms import AddUserForm
from django.core.urlresolvers import reverse
from .permission import permission_verify
from django.views.decorators.csrf import ensure_csrf_cookie



def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET' and request.GET.__contains__('next'):
        next_page = request.GET['next']
    else:
        next_page = '/'
    if next_page == "/accounts/logout/":
        next_page = '/'
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm(request)
    kwargs = {
        'request': request,
        'form':  form,
        'next': next_page,
    }
    return render(request, 'accounts/login.html', kwargs)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def user_list(request):
    all_user = get_user_model().objects.all()
    kwargs = {
        'all_user':  all_user,
    }
    return render(request, 'accounts/user_list.html', kwargs)


@login_required
def userdel(request):
    id=request.GET.get('id')
    if id:
        get_user_model().objects.filter(id=id).delete()
        return HttpResponseRedirect('/accounts/userlist/')


def userupdate_msg(request):

    id = request.GET.get('id')
    spec_user = get_user_model().objects.filter(id=id)
    spec_user = [ obj.as_dict() for obj in spec_user ]
    kwargs = {
        'spec_user': spec_user,
        'code':0,
    }
    return HttpResponse(json.dumps(kwargs), content_type="application/json")

def update_sure(request):
    if request.POST:
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        role = request.POST.get('role')
        remark = request.POST.get('remark')
        id = request.POST.get('id')
        password = request.POST.get('changpwd')
        updateuser = get_user_model().objects.filter(id=id)

        updateuser.update(username=username)
        updateuser.update(nickname=nickname)
        updateuser.update(email=email)
        uobj = UserInfo.objects.get(username__exact=username)
        uobj.set_password(password)
        updateuser.update(remark=remark)
        if request.POST.get('have_publish'):
            updateuser.update(have_publish="1")
        else:
            updateuser.update(have_publish="0")
        if request.POST.get('have_review'):
            updateuser.update(have_review="1")
        else:
            updateuser.update(have_review="0")
        if request.POST.get('have_test'):
            updateuser.update(have_test="1")
        else:
            updateuser.update(have_test="0")
        if request.POST.get('status'):
            updateuser.update(is_active=True)
        else:
            updateuser.update(is_active = False)
        for item in updateuser:
            item.save()

        kwargs = {
            'code': 0,
        }
        return HttpResponse(json.dumps(kwargs), content_type="application/json")


def add_user(request):
    if request.POST:
        username =request.POST.get('username')
        nickname = request.POST.get('nickname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if request.POST.get('status'):
            get_user_model().objects.create_user(username=username, is_active=True, nickname=nickname, email=email,
                                                 password=password)
        else:
            get_user_model().objects.create_user(username=username, is_active=False, nickname=nickname, email=email,
                                                 password=password)


        kwargs = {
            'code': 0,
        }
        return HttpResponse(json.dumps(kwargs), content_type="application/json")


def updatepwd_sure(request):
    if request.POST:
        password= request.POST.get("updatepwd")
        username=request.POST.get("username")
        ids = request.POST.get('id')
        uobj = get_user_model().objects.get(id=ids)
        uobj.set_password(password)
        uobj.save()
        kwargs = {
            'code': 0,
        }
        return HttpResponse(json.dumps(kwargs), content_type="application/json")