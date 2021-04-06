from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default=' ',null=True,blank=True)
    Image=models.ImageField(upload_to='products/')

    class Meta:
        db_table="Product_Info"

    @staticmethod
    def get_all_products():
        return Product.objects.all()

