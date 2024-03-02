<<<<<<< HEAD
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
=======
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
>>>>>>> ae60163fc39d5cb5f4cd146166a880552bf3f717
