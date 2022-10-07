from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    text = models.TextField(max_length=100,null=True)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.email