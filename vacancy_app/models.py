from django.db import models

from service_app.models import MasterSpeciality


class Vacancy(models.Model):
    speciality = models.ForeignKey(MasterSpeciality, on_delete=models.CASCADE)
    experience_in_years = models.IntegerField("Required experience in years", default=0)

    def __str__(self):
        return f"{self.speciality.name} - {self.experience_in_years} years of experience"
