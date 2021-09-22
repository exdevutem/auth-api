import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Role(models.Model):
    name = models.CharField(unique=True, max_length=50)


class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    email = models.EmailField()
    emoji = models.CharField(max_length=50)
    img_profile = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    role = models.ForeignKey(Role, to_field="id", on_delete=models.DO_NOTHING)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email", "emoji", "name", "nickname", "role"]

    def __str__(self):
        return f"{self.emoji}: {self.nickname}"
