from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Register(models.Model):
    gtype=(
        ('Erkak','Erkak'),('Ayol','Ayol')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    gender=models.CharField(choices=gtype,max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.user.first_name +' '+ self.user.last_name


class Category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/categoryImg',blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
class Advertisement(models.Model):
    STATUS=(
        ('Aktiv','Aktiv'),('Yakunlandi','Yakunlandi')
    )
    PERMISSION_STATUS=(
        ('Ha','Ha'),('Yoq','Yoq')
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=RichTextField()
    phone=models.CharField(max_length=100)
    address=models.TextField()
    condition=models.CharField(choices=STATUS,max_length=50,default='Aktiv')
    permission=models.CharField(choices=PERMISSION_STATUS,max_length=50,default='Yoq')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Employer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title = RichTextField()
    about=RichTextField()
    experience=models.CharField(max_length=50)
    salary=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    address=RichTextField()

    def __str__(self):
        return self.user.first_name
