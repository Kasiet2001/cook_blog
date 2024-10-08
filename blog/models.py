from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipe(self):
        return self.recipe.all()

    def get_comments(self):
        return self.comment.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

