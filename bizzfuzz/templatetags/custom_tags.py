from django import template
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth import get_user_model
register = template.Library()



@register.filter
def eligible(user_id):
    userModel = get_user_model()
    userInstance = get_object_or_404(userModel, pk=user_id)

    now_year = timezone.now().year
    now_month = timezone.now().month
    now_day = timezone.now().day

    try:
        user_year = userInstance.birth_date.year 
        user_month = userInstance.birth_date.month
        user_day = userInstance.birth_date.day  

        userYearsOld = now_year - user_year
        monthCheck = now_month - user_month
        dayCheck = now_day - user_day
        dayCheckState = False

        if userYearsOld > 13:
            return 'Allowed'
        elif userYearsOld == 13 and monthCheck > 0:
            return 'Allowed'  
        elif userYearsOld == 13 and monthCheck == 0 and dayCheck >= 0:
            return 'Allowed'
        else:
            return 'Blocked' 
    except:
        return 'No Birth Day ;('


@register.filter
def bizzfuzz(random_number):
    if random_number % 3 == 0 and random_number % 5 == 0:
        return 'BizzFuzz'
    elif random_number % 3 == 0:
        return 'Bizz'
    elif random_number % 5 == 0:
        return 'Fuzz'
    else:
        return random_number