# -*- coding: utf-8 -*-
from django.db import models

'''''
class Groups(models.Model):
    class Meta:
        db_table = 'roles'

    roles_users = models.CharField(max_length=100)

    def __str__(self):
        return self.roles_users


class Users(models.Model):
    class Meta:
        db_table = 'users'
        ordering = ["second_name", "first_name"]

    second_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    login = models.EmailField()
    password = models.CharField(max_length=128, help_text=_("Use'[algo]$[salt]$[hexdigest]'"))
    users_roles = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.second_name
'''''