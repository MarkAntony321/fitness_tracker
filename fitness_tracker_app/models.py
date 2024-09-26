from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MembershipCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membership_card')
    card_number = models.CharField(max_length=10, unique=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user}: {self.card_number}"


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    workout_type = models.CharField(max_length=50, choices=[
        ('cardio', 'Cardio'),
        ('strength', 'Strength')
    ])
    date = models.DateField()
    duration = models.PositiveIntegerField()
    meals = models.ManyToManyField('Meal', related_name='workout_meal')

    def __str__(self):
        return f"{self.user}: {self.workout_type}"


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.workout}: {self.name}"


class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name}"
