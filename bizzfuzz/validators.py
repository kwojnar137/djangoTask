from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

def date_max(birth_date):
    
    if birth_date > date.today():
        raise ValidationError('Invalid date. Date from a future.')
    else:
        return birth_date