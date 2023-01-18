from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=200,default="https://zabas.com/wp-content/uploads/2017/01/food-placeholder.png")

    def __str__(self):
        return self.item_name
    