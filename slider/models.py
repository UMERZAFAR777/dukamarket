from django.db import models

# Create your models here.
class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('NEW ARRIVAL','NEW ARRIVAL'),
    )
    name = models.CharField(max_length=100)
    discount_deal = models.CharField(max_length=100,choices = DISCOUNT_DEAL )
    sale = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    img = models.ImageField(upload_to='media/slider',null=True,default=None)
    link = models.CharField (max_length= 200)

    def __str__(self):
        return self.name







