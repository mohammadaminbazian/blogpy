from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from _datetime import datetime

# validator
def validate_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported  file extension.' + valid_extensions)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user_avatar/", null=False, blank=False, validators=[validate_file_extention])  # mandatory
    description = models.CharField(max_length=512, null=False, blank=False)  # mandatory

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)# mandatory
    cover = models.FileField(upload_to="files/article_cover/", null=False, blank=False, validators=[validate_file_extention])  # mandatory
    contact = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ManyToManyField(UserProfile)
    promote = models.BooleanField(default=False)

    """ def __str__(self):
        return self.title """

class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)# mandatory
    cover = models.FileField(upload_to="files/category_cover/", null=False, blank=False, validators=[validate_file_extention])  # mandatory

    def __str__(self):
        return self.title #self.cover.url

