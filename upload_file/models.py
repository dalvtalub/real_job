from django.db import models


class Csv(models.Model):
    file_name = models.FileField(upload_to='upload_file')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.file_name}'
