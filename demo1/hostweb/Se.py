from rest_framework import serializers
from hostweb.models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_ID', 'username', 'passwd', 'mail', 'telephone', 'Type', 'introduction', 'institute', 'domain', 'avatar_url', 'balance', 'name')

    '''
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    passwd = serializers.CharField()
    mail = serializers.CharField(required=False, allow_blank=True)
    telephone = serializers.CharField(required=False, allow_blank=True)
    introduction = serializers.CharField(required=False, allow_blank=True)
    institute = serializers.CharField(required=False, allow_blank=True)
    domain = serializers.CharField(required=False, allow_blank=True)
    avatar_url = serializers.CharField(required=False, allow_blank=True)
    balance = serializers.IntegerField(default=0, required=False)
    name = serializers.CharField(required=False, allow_blank=True)
    '''
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validate_data):

        instance.username = validate_data.get('username', instance.username)
        instance.passwd = validate_data.get('passwd', instance.passwd)
        instance.mail = validate_data.get('mail', instance.passwd)
        instance.telephone = validate_data.get('telephone', instance.telephone)
        instance.introduction = validate_data.get('introduction', instance.introduction)
        instance.institute = validate_data.get('institute', instance.institute)
        instance.domain = validate_data.get('domain', instance.domain)
        instance.avatar_url = validate_data.get('avatar_url', instance.avatar_url)
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('resource_ID', 'title', 'authors', 'intro', 'url', 'price', 'Type')

    def create(self, validated_data):
        return Resource.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.intro = validated_data.get('intro', instance.intro)
        instance.url = validated_data.get('url', instance.url)
        instance.price = validated_data.get('price', instance.price)
        instance.Type = validated_data.get('Type', instance.Type)
        instance.save()
        return instance


class starFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = starForm
        fields = '__all__'

    def create(self, validated_data):
        return starForm.objects.create(**validated_data)






