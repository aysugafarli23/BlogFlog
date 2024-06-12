from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, verbose_name="Yazıçı", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Başlıq")
    content = models.TextField(verbose_name=("Məzmun"), blank=True, null=True,)
    created_date = models.DateField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    image = RichTextUploadingField( verbose_name="Şəkil",blank=True, null=True,)
    price = models.IntegerField(verbose_name="Qiyməti" )
    
    def __str__(self):
        return f"{self.author.username.capitalize()}______{self.title}_______{self.price}"