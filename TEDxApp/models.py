from django.db import models

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)

EDUCATION_CHOICES = (
    ('high_school', 'high_school'),
    ('university', 'university'),
    ('bachelors', 'bachelors'),
    ('masters', 'masters'),
    ('doctorate', 'doctorate'),
    ('other', 'other'),
)

COUNTRY_CHOICES = (
    ('saudi', 'saudi'),
    ('kuwait', 'kuwait'),
    ('egypt', 'egypt'),
    ('other', 'other'),
)

# Create your models here.
class Attendee(models.Model):
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
    )
    age = models.IntegerField(default=18)
    education = models.CharField(
        max_length=50,
        choices=EDUCATION_CHOICES,
    )
    country = models.CharField(
        max_length=50,
        choices=COUNTRY_CHOICES,
    )
    phone = models.IntegerField()
    email = models.EmailField(blank=False)

    # Tracks if attendee confirmed registration using their email
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Seat(models.Model):
    order = models.AutoField(primary_key=True)
    assigned_to = models.OneToOneField(
        Attendee,
        on_delete=models.SET_NULL,
        null=True
    )
    seat_number = models.CharField(max_length=5)
    
    def __str__(self):
        return self.seat_number