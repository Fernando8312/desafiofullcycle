from django.db import models
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=150, verbose_name="Título", null=False)
    content=models.TextField(verbose_name="Conteúdo", null=True)
    created_at=models.DateTimeField(verbose_name="Data de Publicação", null=True) 
    tags=models.ManyToManyField("Tags", verbose_name="Tags")
    

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    name=models.CharField(max_length=50, verbose_name="Tags")


    def __str__(self):
        return self.name


    
