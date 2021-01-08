from django.db import models

# Create your models here.
# 出版商
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# 作者信息
class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name

# 书
class Book(models.Model):
    title = models.CharField(max_length=100, help_text="书名")
    authors = models.ManyToManyField(Author, verbose_name="作者", help_text="作者")
    publisher = models.ForeignKey(Publisher, verbose_name="出版社", help_text="出版社", on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

