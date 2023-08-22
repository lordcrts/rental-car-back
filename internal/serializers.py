# -*- encoding: utf-8 -*-

# Django
from django.contrib.auth.models import User
from django.conf import settings
from internal.models import Brand, Car, Specification, State
from rest_flex_fields import FlexFieldsModelSerializer
# Django Rest
from rest_framework import serializers, exceptions

class UserSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active')
        read_only_fields = (
            'last_login',
            'date_joined',
            'is_active',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'format': settings.DATETIME_FORMAT},
            'date_joined': {'format': settings.DATETIME_FORMAT},
            'first_name': {'required': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        uu = User.objects.filter(username__iexact=self.data["username"]).first()
        if uu != " " and uu is not None:
            raise exceptions.ParseError(detail='Username already exist')
        else:
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        for attr, value in validated_data.items():
            if attr == 'password':
                setattr(instance, attr, value)

        instance.save()

        return instance
    
class StateSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class BrandSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        expandable_fields = {
            'state': (StateSerializer),
        }



class SpecificationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Specification
        # fields = '__all__'
        exclude = ('car',)
        expandable_fields = {
            'state': (StateSerializer),
            'car': (Specification),
        }

class CarSerializer(FlexFieldsModelSerializer):
    specification = SpecificationSerializer()
    class Meta:
        model = Car
        # fields = '__all__'
        include= ('specification',)
        exclude= ('user',)
        expandable_fields = {
            'state': (StateSerializer),
            'brand': (BrandSerializer),
        }

    def create(self, validated_data):
        """
           Funcion crear automaticanmente el campo name_folder
        """
        specification_data = validated_data.pop('specification')
        instance = Car.objects.create(user_id= self.context['request'].user.id, **validated_data)
        Specification.objects.create(
            car=instance,
            maker=specification_data['maker'],
            identification_number=specification_data['identification_number'],
            height=specification_data['height'],
            widht=specification_data['widht'],
            longitude=specification_data['longitude'],
            km=specification_data['km']
        )
        instance.save()

        return instance