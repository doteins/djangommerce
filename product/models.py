from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)

  # Meta classes to display info about category in admin panel
  class Meta:
    ordering = ("name",)
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name

class Item(models.Model):
  AVAILABLE = "AV"
  SOLD = "SO"
  RESERVED = "RE"

  STATUS_CHOICES = [
    (AVAILABLE, "Available"),
    (SOLD, "Sold"),
    (RESERVED, "Reserved")
  ]

  category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=False, null=False)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='items', blank=True, null=True)
  status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AVAILABLE)
  created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True, null=False)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name