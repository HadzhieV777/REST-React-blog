from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    CATEGORY_NAME_MAX_LEN = 100

    name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LEN,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    # custom manager to show only the posts with status='published'
    # no need to filter the data in our views
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    DEFAULT_CATEGORY = 1
    TITLE_MAX_LEN = 250
    SLUG_MAX_LEN = 250

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        default=DEFAULT_CATEGORY,
    )
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    excerpt = models.TextField(
        null=True,
    )
    content = models.TextField()
    slug = models.SlugField(
        max_length=SLUG_MAX_LEN,
        unique_for_date='published',
    )
    published = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    status = models.CharField(
        max_length=10,
        choices=options,
        default='published',
    )
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
