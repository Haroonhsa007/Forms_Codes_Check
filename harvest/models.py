from django.db import models


class Person(models.Model):

    id = models.CharField(max_length=100, primary_key=True)

    men = 'M'
    women = 'W'
    sex_choices = [
        (men, 'Men'),
        (women, 'Women'),
    ]
    sex = models.CharField(
        max_length=2,
        choices=sex_choices,
        null=True
    )

    age = models.PositiveSmallIntegerField(null=True)
