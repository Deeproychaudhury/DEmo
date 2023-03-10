from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=70,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="noimage")
    description=models.CharField(max_length=500)
    pub_date=models.DateField()

    def __str__(self):
       return self.product_name

