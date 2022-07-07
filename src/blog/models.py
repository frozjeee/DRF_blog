from django.db import models
from django.conf import settings
from django.utils import timezone
from tryDjangoREST.utils import CreateUniqueSlug
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _
# Create your model s here.

def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):


    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1) 
    title = models.CharField(max_length=250)
    image  = models.ImageField(_('Image'), upload_to=upload_to, default='media/default.jpg')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', blank=True, null=True)
    published = models.DateTimeField(default=timezone.now, blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()
    post_objects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title   

# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = CreateUniqueSlug(instance, NewSlug=instance.slug)
    
# pre_save.connect(slug_generator, sender=Post)