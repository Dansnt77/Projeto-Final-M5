from .models import Account
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )

    def create(self, validated_data) -> Account:
        return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = ["id", "username", "email", "password", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
