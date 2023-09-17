from django.db import models

# Create your models her
class Liabrary(models.Model):
    Section=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.Section
    
class Books(models.Model):
    Section=models.ForeignKey(Liabrary,on_delete=models.CASCADE)
    Book_name=models.CharField(max_length=100,primary_key=True)
    Auther=models.CharField(max_length=100)

    def __str__(self):
        return self.Book_name