from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
# Create your models here.


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["title", "author"],
                name="unique_by_author"),
        ]

    def __str__(self):
        return f'{self.title} by {self.author}'


READING_STATUS_CHOICES = (
    ("WtR", "Want to Read"),
    ("RG", "Reading"),
    ("RD", "Read"),
)


class ReadingStatus(models.Model):
    reading_state = models.CharField(
        max_length=20, choices=READING_STATUS_CHOICES, default='WtR')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reading_state}'
