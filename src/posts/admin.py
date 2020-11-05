# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user.email', 'user.username', 'bio')


admin.site.register(Post)
