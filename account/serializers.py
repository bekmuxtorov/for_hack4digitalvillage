from rest_framework import serializers
from .models import Account


class AccountRegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Account
        fields = [
            'phone_number', 'full_name', 'farm_name', 'password', 'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

        def create(self, validate_date):
            phone_number = validate_date.get('phone_number')
            full_name = validate_date.get('full_name')
            farm_name = validate_date.get('farm_name')
            password = validate_date.get('password')
            password2 = validate_date.get('password2')

            if password == password2:
                user = Account(
                    phone_number=phone_number,
                    full_name=full_name,
                    farm_name=farm_name
                )
                user.set_password(password)
                user.save()
                return user
            else:
                raise serializers.ValidationError({
                    'error': 'Both passwords do not match'
                })
