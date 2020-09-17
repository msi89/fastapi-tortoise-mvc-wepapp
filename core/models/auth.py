from tortoise import models, fields
from core.middlewares.security import hash_password


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=60, default=None, null=True)
    username = fields.CharField(max_length=25, unique=True)
    email = fields.CharField(max_length=256, unique=True)
    password = fields.CharField(max_length=1000)
    is_admin = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    avatar = fields.CharField(max_length=256, default=None, null=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    async def save(self, *args, **kwargs) -> None:
        self.password = hash_password(self.password)
        await super().save(*args, **kwargs)

    class PydanticMeta:
        exclude = ['password']
