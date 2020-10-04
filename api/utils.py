from django.contrib.auth.models import User
from django.utils.text import slugify


def return_slug(firstname: str, lastname: str):
    # get a slug of the firstname and last name.
    # it will normalize the string and add dashes for spaces
    # i.e. 'HaRrY POTTer' -> 'harry-potter'
    u_username = slugify(f'{firstname.lower()} {lastname.lower()}')

    # count the number of users that start with the username
    count = User.objects.filter(username__startswith=u_username).count()
    if count == 0:
        return u_username
    else:
        return f'{u_username}-{count}'
