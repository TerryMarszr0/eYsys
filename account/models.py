# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.url)


class RoleList(models.Model):
    name = models.CharField(max_length=64)
    # permission = models.ManyToManyField(PermissionList, null=True, blank=True)
    permission = models.ManyToManyField(PermissionList, blank=True)

    def __unicode__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self,email,nickname,is_active,username,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nickname=nickname,
            is_active=is_active
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
            username=username,
            password=password,
        )

        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserInfo(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    role = models.ForeignKey(RoleList, null=True, blank=True)
    ftp_path = models.CharField(max_length=32,null=True)
    remark = models.CharField(max_length=32,null=True)
    have_publish = models.BooleanField(default=False)
    have_review = models.BooleanField(default=False)
    have_test = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    def as_dict(self):
        return {
            "id": self.id,
            "username":self.username,
            "email":self.email,
            "is_active":self.is_active,
            "is_superuser":self.is_superuser,
            "nickname":self.nickname,
            "role":self.role,
            "have_publish":self.have_publish,
            "have_review":self.have_review,
            "have_test":self.have_test,
            "remark":self.remark,




        }


