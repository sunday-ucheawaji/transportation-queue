from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    password = serializers.CharField(max_length=30, min_length=4, write_only=True, style={
                                     "input_type": "password"})
    confirm_password = serializers.CharField(max_length=30, min_length=4, write_only=True, style={
        "input_type": "password"})

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        keys = list(dict(validated_data).keys())
        keys.remove("confirm_password")
        user_dict = {key: validated_data.get(key) for key in keys}
        user = CustomUser.objects.create_user(**user_dict)
        user.set_password(user_dict["password"])
        user.save()
        return user

