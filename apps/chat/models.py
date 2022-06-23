""" apps/course/models.py """
from django.db import models


class ChatGroupList(models.Model):

    admin_name = models.CharField(max_length=100)
    member_name = models.CharField(max_length=100)
    

class OnetoOneMessage(models.Model):

    e_id = models.IntegerField()
    e_name = models.CharField(max_length=100)
    e_message = models.TextField(max_length = 500, null = True)
    e_image = models.ImageField(null = True, upload_to = 'document/')
    # e_docs    = models.FileField(null = True, upload_to = 'document/')
    e_time = models.TimeField(auto_now=True)
    e_groupid = models.IntegerField()
