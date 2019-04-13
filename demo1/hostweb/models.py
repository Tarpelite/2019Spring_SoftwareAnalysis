from django.db import models


# Create your models here.

class user(models.Model):

    Id= models.CharField(max_length=255)
    nickname = models.CharField(max_length = 255)
    phone = models.CharField(max_length=255)
    balance = models.FloatField()
    avator = models.ImageField()
    stat = models.IntegerField()

    def __str__(self):
        return self.nickname



class expert(user):

    introduction = models.CharField(max_length=255)
    consitution = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    background_img = models.CharField(max_length=255)
    citation_times = models.IntegerField()
    article_numbers = models.IntegerField()
    h_index = models.IntegerField()
    g_index = models.IntegerField()


class expert_applicant_form(models.Model):

    Id = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    content = models.TextField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    state = models.IntegerField()
    user_name = models.CharField(max_length=255)
    expert_name = models.CharField(max_length=255)

class resource(models.Model):

    Id = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    Type = models.IntegerField()
    check_state = models.IntegerField() # 0: cheking 1:unchecked 2:pass
    leader_id = models.CharField(max_length=255)
    introduction = models.TextField()
    price = models.FloatField()
    is_user_visible = models.BooleanField()
    is_expert_visible  = models.BooleanField()
    create_at = models.DateTimeField()
    file_path = models.FilePathField()
    authors = models.TextField()

class patent(resource):

    application_number = models.TextField()
    publication_number = models.TextField()
    application_date = models.DateField()
    publication_date = models.DateField()
    address = models.TextField()
    inventor = models.TextField()
    agency = models.TextField()
    agent = models.TextField()
    patent_class = models.TextField()

class paper(resource):

    source = models.TextField()
    classification = models.TextField()
    keywords = models.TextField()

class project(resource):

    institution = models.TextField()
    keywords = models.TextField()
    subject_classification = models.TextField()
    category = models.TextField()
    level = models.IntegerField()
    duration = models.TextField()
    evaluation_form = models.TextField()
    store_at = models.DateField()

class resource_transaction_form(models.Model):

    Id = models.CharField(max_length=255)
    price = models.FloatField()
    Type = models.IntegerField()
    started_time = models.DateTimeField()
    ended_time = models.DateTimeField()
    seller_id = models.CharField(max_length=255)
    buyer_id = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)
    state = models.IntegerField()

class resource_comment(models.Model):

    Id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    score = models.FloatField()
    user_id = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)
    state = models.IntegerField()

class admin_user(models.Model):
    Id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    state = models.IntegerField()
















