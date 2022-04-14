from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    link=models.CharField(max_length=128,blank=True, null=True)
    heading=models.CharField(max_length=128, blank=True,)
    desc=models.CharField(max_length=128, blank=True, null=True)

    class Meta: 
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
     
    
    def __str__(self):
        return self.heading