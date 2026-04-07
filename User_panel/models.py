from django.db import models

# Create your models here.
class Contact_Data(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'Contact_Data'