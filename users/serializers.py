from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Create a new user instance
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        # Hash the user's password
        user.set_password(validated_data["password"])

        # Save the user instance
        user.save()

        return user
