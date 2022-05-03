from django.db import models


class Person(models.Model):

    id = models.CharField(max_length=100, primary_key=True)

    man = 'M'
    woman = 'W'
    sex_choices = [
        (man, 'Man'),
        (woman, 'Woman'),
    ]
    sex = models.CharField(
        max_length=2,
        choices=sex_choices,
        null=True
    )

    age = models.PositiveSmallIntegerField(null=True)
