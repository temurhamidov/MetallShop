from django.db import models
from django.utils.text import slugify

# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Category(BaseModel):
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Type(BaseModel):
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "Image is not defined"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    size = models.IntegerField(null=True)
    manfacturer = models.CharField(max_length=100, null=True)
    theory = models.IntegerField(null=True)
    unit = models.CharField(max_length=20, null=True)
    price_cash = models.IntegerField(null=True)
    price_cashless = models.IntegerField(null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
