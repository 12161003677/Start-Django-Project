from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=60)
    qtd_students = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=8)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone_1 = models.CharField(max_length=14, null=True)
    phone_2 = models.CharField(max_length=14, null=True)
    photo = models.ImageField(upload_to='image', null=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    bill = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name

class TypeProd(models.Model):
    type = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Types of Product'
        verbose_name = 'Type of Product'

    def __str__(self):
        return self.type

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ForeignKey("TypeProd", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='image', null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class Purchase(models.Model):
    date = models.DateField(auto_now_add=False,blank=True, null=True)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    qtd_prod = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return self.product.name