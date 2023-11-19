# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



# 使用者資訊
from django.db.models import Model

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user'

class Chat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'chatT'

