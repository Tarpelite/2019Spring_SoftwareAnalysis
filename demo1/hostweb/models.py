from django.db import models

# Create your models here.

class user(models.Model):

    id_  = models.uuidField(unique=True)
    nickname = models.CharField(max_length = 255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    balance = models.FloatField()
    password = models.CharField()
    avator = models.ImageField()
    stat = models.IntegerField()

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['c_time']
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class expert(user):

    introduction = models.CharField(max_length=255)
    phone = models.CharField()
    consitution = models.CharField()
    major = models.CharField()
    background_img = models.CharField()
    citation_times = models.IntegerField()
    article_numbers = models.IntegerField()


class expert_applicant_form(models.Model):

    id_ = models.uuidField(unique=True)
    created_at = models.DateField()



