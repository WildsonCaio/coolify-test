from django.db import models


class User(models.Model):    
    name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, default=0)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.age} {self.email}"

    class Meta:
        verbose_name_plural = "Users"

