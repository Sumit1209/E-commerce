from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=15)
    discription=models.TextField()
    
    def __str__(self):
        return self.email
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date = models.DateField()
    image1=models.ImageField(upload_to='shop/images',default="")
    image2=models.ImageField(upload_to='shop/images',default="")
    image3=models.ImageField(upload_to='shop/images',default="")
    image4=models.ImageField(upload_to='shop/images',default="")
    image5=models.ImageField(upload_to='shop/images',default="")
    image6=models.ImageField(upload_to='shop/images',default="")


    def __str__(self):
        return self.product_name
class Logo(models.Model):
    logo=models.ImageField(upload_to='shop/images',default="")


