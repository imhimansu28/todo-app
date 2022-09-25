import datetime as dt

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class TodoListItem(models.Model):
    user = models.ForeignKey(
        User, related_name='todo', on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=dt.datetime.today())
    end_date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content

    def get_absolute_url(self):
        return reverse("task_complete", kwargs={"pk": self.pk})
