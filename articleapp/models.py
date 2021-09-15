from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    # auto_now_add로 해야함!!!
    created_at = models.DateField(auto_now_add=True, null=True)
    # created_at = models.DateField(auto_created=True, null=True)
    # 위에꺼는 잘못된거임!!
# Create your models here.
