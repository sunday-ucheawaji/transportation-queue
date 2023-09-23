from rest_framework import serializers
from .models import CustomUser
from customer import signals

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    password = serializers.CharField(max_length=30, min_length=4, write_only=True, style={
                                     "input_type": "password"})
    confirm_password = serializers.CharField(max_length=30, min_length=4, write_only=True, style={
        "input_type": "password"})

    pickup_location = serializers.CharField(max_length=255,  write_only=True,)
    drop_off_location = serializers.CharField(max_length=255,   write_only=True,)


    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def validate_pickup_location(self, value):
        # Your custom validation logic here
        return value
    
    def validate_drop_off_location(self, value):
        # Your custom validation logic here
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        keys = list(dict(validated_data).keys())
        pickup_location= dict(validated_data)['pickup_location']
        drop_off_location= dict(validated_data)['drop_off_location']

        keys.remove("pickup_location")
        keys.remove("drop_off_location")
        keys.remove("confirm_password")

        user_dict = {key: validated_data.get(key) for key in keys}
        user = CustomUser.objects.create_user(**user_dict)
        user.set_password(user_dict["password"])
        user.save()
        customer_name = f"{user.first_name} {user.last_name}"

        signals.custom_user_signal.send(
                sender=request, 
                user=user, 
                customer_name=customer_name, 
                pickup_location=pickup_location, 
                drop_off_location=drop_off_location 
            )
        return user

