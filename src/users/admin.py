# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, FollowAndBlock


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user.email', 'user.username', 'bio')


admin.site.register(Profile)
