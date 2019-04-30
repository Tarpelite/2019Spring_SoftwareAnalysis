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
    balance = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)

    def is_expert(self):
        return self.Type == 'E'

    def is_admin(self):
        return self.Type == 'A'

    def __str__(self):
        return self.username
    


class Resource(models.Model):

    TYPE_CHOICES = (
        ("P1", "Paper"),
        ("P2", "Patent"),
        ("P3", "Project"),
    )

    resource_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    authors = models.TextField(blank=True)  # split by ','
    intro = models.TextField(blank=True)
    url = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    Type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    publisher = models.CharField(max_length=255, blank=True)
    publish_date = models.CharField(max_length=255, blank=True)
    citation_numbers = models.IntegerField(default=0, blank=True)
    agency = models.CharField(max_length=255, blank=True)
    patent_number = models.TextField(blank=True)
    patent_applicant_number = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):

    SEX_TYPE = (
        ('M', 'man'),
        ('W', 'woman')
    )

    author_ID = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=1, choices=SEX_TYPE, default = 'M')
    name = models.CharField(max_length=255, unique=True)
    institute = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)
    bind = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True, blank=True)
    citation_times = models.IntegerField(default=0, blank=True)
    article_numbers = models.IntegerField(default=0, blank=True)
    h_index = models.IntegerField(default=0, blank=True)
    g_index = models.IntegerField(default=0, blank=True)
    avator = models.ImageField(upload_to="author_avator", blank=True)

    def __str__(self):
        return self.name


class U2E_apply_form(models.Model):

    form_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_created=True)
    approve_time = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default=" ")
    institute = models.CharField(max_length=255, blank=True)
    domain = models.CharField(max_length=255, blank=True)

    def __str__(self):
        user_obj = User.objects.get(user_ID=self.user_ID)
        user_name = user_obj.username
        return user_name + " " + str(self.created_time) + " " + str(self.approved)


class starForm(models.Model):

    form_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_ID = models.ForeignKey(Resource, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_created=True)
    class Meta:
        unique_together=("user_ID", "resource_ID")
    def __str__(self):

         # user = User.objectes.get(user_ID=self.user_ID)
         # resource = Resource.objects.get(resource_ID = self.resource_ID)
         # return user.username+":" + resource.title
         return "{0}-{1}".format(self.user_ID.username, self.resource_ID.title)


class Transaction(models.Model):

    t_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_ID = models.ForeignKey(Resource, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):

        return "{0}-{1}".format(self.user_ID.username, self.resource_ID.title)


class A2R(models.Model):

    form_ID = models.AutoField(primary_key=True)
    author_ID = models.ForeignKey(Author, on_delete=models.CASCADE)
    resource_ID = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):

        return "{0}-{1}".format(self.author_ID.name, self.resource_ID.title)
    class Meta:
        unique_together=("author_ID", "resource_ID")



class ItemCart(models.Model):

    r_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_ID = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):

        return "{0}-{1}".format(self.user_ID.username, self.resource_ID.title)


class publish_item_application_form(models.Model):

    TYPE_CHOICES = (
        ("P1", "Paper"),
        ("P2", "Patent"),
        ("P3", "Project"),
    )

    f_ID = models.AutoField(primary_key=True)
    author_ID = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    authors = models.TextField(blank=True)  # split by ','
    intro = models.TextField(blank=True)
    url = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    Type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    passed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "{0}-{1}".format(self.author_ID.name, self.title)

























