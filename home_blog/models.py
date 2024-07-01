from django.db import models


class Art(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='art/covers/%Y/%m/%d/')
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title