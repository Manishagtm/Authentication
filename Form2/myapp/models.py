from django.db import models


# Create your models here.
# Create your models here.

class tbl_Login(models.Model):
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')

    #  pdf = models.FileField(upload_to="information/pdfs/")
    # pictures = models.ImageField(null=True, blank=True, upload_to="information/images/")

    def __str__(self):
        return self.email


