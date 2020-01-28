from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


def validate_image(image):
    return None


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=60, blank=True, null=True)
    view = models.PositiveIntegerField(default=0)
    date = models.DateField(default=datetime.now)
    slug = models.SlugField(blank=True, null=True, max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    present_address = models.CharField(max_length=300, blank=True, null=True)
    permanent_address = models.CharField(max_length=300, blank=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    college = models.CharField(max_length=200, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    relation = models.CharField(max_length=200, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    session = models.CharField(max_length=20, blank=True, null=True)
    blood = models.CharField(max_length=9, blank=True, null=True)
    father = models.CharField(max_length=100, blank=True, null=True)
    mother = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    fb = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='profile_pics',
                            blank=True, default="default.png")
    alumni = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.img)
        # set self.image to new_image
        self.img = new_image
        # save
        super().save(*args, **kwargs)


class About(models.Model):
    about = models.TextField(null=True, blank=True)
