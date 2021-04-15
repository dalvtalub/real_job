# from django.db import models
# from django.contrib.auth.models import User
#
#
# class MyToken(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     mytoken = models.CharField('Token', max_length=40)
#
#     def __str__(self):
#         return f'{self.user} {self.mytoken}'
#
#     class Meta:
#         verbose_name = 'MyToken'
#         verbose_name_plural = 'MyTokens'
