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
    openid = models.CharField(max_length=64, unique=True)
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

    def __str__(self):
        return self.nickName

    # # 修改昵称和个人介绍
    # def change_info(self, nickname, info):
    #     try:
    #         self.nickname = nickname
    #         self.info = info
    #         self.save()
    #         return True
    #     except IntegrityError as e:
    #         return False

    class Meta(AbstractUser.Meta):
        # swappable = 'AUTH_USER_MODEL'
        verbose_name = '用户'
        verbose_name_plural = verbose_name