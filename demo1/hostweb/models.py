from django.db import models


# Create your models here.

class User(models.Model):
    TYPE_CHOICES = (
        ('U', 'User'),
        ('E', 'Expert'),
        ('A', 'Admin'),
    )
    user_ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    passwd = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255, default="")
    Type = models.CharField(max_length=1, choices=TYPE_CHOICES)# 0 for normal user, 1 for expert, 2 for admin
    introduction = models.TextField(blank=True)
    institute = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    avatar_url = models.CharField(max_length=255, blank=True)

    def is_expert(self):
        return self.Type == 'E'

    def is_admin(self):
        return self.Type == 'A'

    def __str__(self):
        return self.username



















