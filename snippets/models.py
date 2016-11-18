from django.db import models

# Create your models here.

# Create your models here.
class Snippets(models.Model):
    desc = models.TextField()
    snippets = models.TextField()
    syntax_type =models.CharField(max_length=50, default=None, blank=True)

