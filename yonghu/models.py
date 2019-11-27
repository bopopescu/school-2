# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
import uuid
import random
from django.db.utils import IntegrityError


class User(AbstractUser):
    """
    用户类
    """
    # username = models.CharField(unique=False, null=True)
    openid = models.CharField(max_length=64, primary_key=True)
    nickName = models.CharField(max_length=64, verbose_name='昵称', null=True)
    GENDER = (
        (0, '未知'),
        (1, '男性'),
        (2, '女性')
    )
    gender = models.IntegerField(choices=GENDER, verbose_name='性别', default=0)
    country = models.CharField(max_length=16, verbose_name='国家', default='')
    province = models.CharField(max_length=32, verbose_name='省份', default='')
    city = models.CharField(max_length=16, verbose_name='城市', default='')
    avatarUrl = models.URLField(default='',null=True,blank=True, verbose_name='头像地址')
    is_auth = models.BooleanField(default=False, verbose_name='是否认证')

    def change_info(self, nickName):
        try:
            self.nickName = nickName
            self.save()
            return True
        except Exception:
            return False

    def __str__(self):
        return self.nickName

    class Meta(AbstractUser.Meta):
        # swappable = 'AUTH_USER_MODEL'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class UscInfo(models.Model):
    UserName = models.CharField(max_length=16, verbose_name='校园网用户名', unique=True, null=True)
    Password = models.CharField(max_length=32, verbose_name='校园网密码', null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, verbose_name='所关联用户', related_name='usc')

    class Meta:
        verbose_name = '南华大学教务在线用户信息'
        verbose_name_plural = verbose_name