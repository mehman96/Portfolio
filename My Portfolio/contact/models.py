from django.db import models





class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    message = models.TextField()
   

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name 