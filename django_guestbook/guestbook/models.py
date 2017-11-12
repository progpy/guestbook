from django.db import models
from django.db.models import fields


class Message(models.Model):
    created_at = fields.DateTimeField("Дата и время создания сообщения", auto_now=True)
    name = fields.CharField("Имя", max_length=255)
    text = fields.TextField("Текст сообщения")
