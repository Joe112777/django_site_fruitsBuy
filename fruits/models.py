from django.db import models

class Fruits(models.Model):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=100)
   
    def __unicode__(self):
        return self.title
    
   

class Order(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField('e-mail',blank=True)
    fruits=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    pay=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name    
    
    class Meta:
        ordering=['name']   
