from django.utils.text import slugify
from random import choice
import string

def CreateRandomString(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def CreateUniqueSlug(instance, NewSlug=None):
    if NewSlug is not None:
        slug = newSlug
    else:
        slug = slugify(instance.title)

    InstClass = instance.__class__
    SameExists = InstClass.objects.filter(slug=slug).exists()
    if SameExists:
        NewSlug = "{slug}-{random}".format(
            slug=slug,
            random=CreateRandomString()
        )
        return CreateUniqueSlug(instance, NewSlug=NewSlug)
    return slug