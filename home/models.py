from django.db import models

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=200)
    descreption = models.TextField(max_length=5000)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    #author = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)