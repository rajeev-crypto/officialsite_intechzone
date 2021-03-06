from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name + "-" +  self.email

class Career(models.Model):
    name = models.CharField(max_length=200, help_text="")
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Careers"

    def __str__(self):
        return self.name + "-" +  self.email