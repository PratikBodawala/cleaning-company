from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers

from api.models import Cleaner, Appointment, Customer

# Serializers define the API representation.
from api.utils import return_slug


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class CleanerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        first = validated_data.get('user', {}).get('first_name', '')
        last = validated_data.get('user', {}).get('last_name', '')
        return Cleaner.objects.create(city=validated_data.get('city'),
                                      user=User.objects.create(first_name=first,
                                                               last_name=last,
                                                               username=return_slug(first, last)
                                                               ))

    class Meta:
        model = Cleaner
        fields = ('id', 'city', 'user',)


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    def create(self, validated_data):
        customer = validated_data.get('customer', {})
        first = customer.get('user', {}).get('first_name', '')
        last = customer.get('user', {}).get('last_name', '')
        customer_obj = Customer.objects.filter(
            phone=customer.get('phone')
        ).first()
        if customer_obj:
            return Appointment(cleaner=validated_data.get('cleaner'),
                               start_datetime=validated_data.get('start_datetime'),
                               end_datetime=validated_data.get('end_datetime'),
                               customer=customer_obj)
        else:
            return Appointment(cleaner=validated_data.get('cleaner'),
                               start_datetime=validated_data.get('start_datetime'),
                               end_datetime=validated_data.get('end_datetime'),
                               customer=Customer.objects.create(
                                   phone=customer.get('phone'),
                                   city=customer.get('city'),
                                   user=User.objects.create(first_name=first,
                                                            last_name=last,
                                                            username=return_slug(first, last))))

    class Meta:
        model = Appointment
        fields = '__all__'
