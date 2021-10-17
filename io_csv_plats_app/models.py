from django.db import models
from django.utils.translation import activate

# Create your models here.

class CSVs(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.file_name}"

    # delete when file not exist on database.
    def delete(self, *args, **kwargs):
        self.file_name.delete()
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'CSVs'
        verbose_name = "CSV"
