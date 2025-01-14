from django.db import models

class Client(models.Model):
    client_id=models.AutoField(primary_key=True)
    Firstname=models.CharField(max_length=255, blank=True, null=True)
    Lastname=models.CharField(max_length=15, blank=True, null=True)
    Email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    CreateAt=models.DateTimeField()
    updateAt=models.DateTimeField()
    adresse=models.TextField()
    def __str__(self):
        return f"Client #{self.client_id}-{self.Firstname}-{self.Lastname}"
