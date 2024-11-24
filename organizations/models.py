from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    is_main = models.BooleanField(default=False)  # Identifies the main organization

    def __str__(self):
        return self.name

#User Model
class CustomUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Editor', 'Editor'), ('Viewer', 'Viewer')])

    def __str__(self):
        return self.username

#Role Model
class Role(models.Model):
    name = models.CharField(max_length=50)  # Admin, Editor, Viewer

    def __str__(self):
        return self.name