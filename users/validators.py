import re
from django.core.exceptions import ValidationError

def validate_password(field):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    if not 8 <= len(field) <= 16:
        print('The password must contain from 8 to 16 symbols.')
        raise ValidationError('The password must contain from 8 to 16 symbols.')
    if not bool(re.match(pattern, field)):
        print('The password must contain only digits and Latin letters.')
        raise ValidationError('The password must contain only digits and Latin letters.')