from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Publication(models.Model):
    titre = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=128)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    localisation = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.localisation})"

    def get_absolute_url(self):
        return reverse("publication", kwargs={"slug": self.slug})