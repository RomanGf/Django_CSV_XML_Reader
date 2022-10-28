from django.db import models


class File(models.Model):
    file_name_csv = models.FileField(upload_to='files')
    file_name_xml = models.FileField(upload_to='files')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'file id: {self.id}'