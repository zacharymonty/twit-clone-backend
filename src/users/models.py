# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, default="Bio goes here")
    image = models.ImageField(default='media/profile_pictures/default.png', upload_to='profile_pictures')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'

    @property
    def followers(self):
        return FollowAndBlock.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return FollowAndBlock.objects.filter(user=self.user).count()

    @property
    def blocked(self):
        return FollowAndBlock.objects.filter(block_user=self.user)

    # @property
    # def favorites(self):
    #     return

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FollowAndBlock(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    block_user = models.ForeignKey(User, related_name='block_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


# class Favorite(models.Model):
#     user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
#     block_user = models.ForeignKey(User, related_name='block_user', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)