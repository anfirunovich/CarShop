from django.core.validators import RegexValidator


phone_number_validator = RegexValidator(
    regex=r"^\+375 \((29|44|33)\) [0-9]{3}-[0-9]{2}-[0-9]{2}$",
)
