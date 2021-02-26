from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from User.models import Profile, Login


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    user_name = serializers.CharField(required=True)

    class Meta:
        model = Login
        fields = [
            'email',
            'password',
            'identifier',
            'user_name'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    login = CreateUserSerializer(many=False)

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'identifier',
            'login'
        ]

    def create(self, validated_data):
        login_data = validated_data.pop('login')
        login_data['password'] = make_password(login_data['password'])
        login_instance = Login.objects.create(**login_data)
        profile_instance = self.Meta.model.objects.create(login=login_instance, **validated_data)
        return profile_instance


class ProfileDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = [
            'full_name',
            'identifier',
        ]