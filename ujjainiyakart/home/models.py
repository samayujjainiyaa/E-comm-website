from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=30)
    product_details=models.CharField(max_length=30)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    imges=models.ImageField(upload_to='myimages')
    # quantity = models.IntegerField()
    def __str__(self) -> str:
        return self.pname+' '+self.product_details
    
class Cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.item.pname

