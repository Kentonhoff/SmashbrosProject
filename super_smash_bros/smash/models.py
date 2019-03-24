from django.db import models

class Franchise(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Fighter(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class First_game(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=150)
    year = models.PositiveIntegerField(null=True)
    number_of_smash_appearances = models.PositiveIntegerField(null=True)
    franchise = models.ForeignKey('franchise', on_delete=models.CASCADE)
    fighter = models.ForeignKey('fighter', on_delete=models.CASCADE)
    gender = models.ForeignKey('gender', on_delete=models.CASCADE)
    first_game = models.ForeignKey('first_game', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
