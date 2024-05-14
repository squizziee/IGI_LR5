from django.db import models


class FAQ(models.Model):
    question = models.TextField("Question")
    answer = models.TextField("Answer")
    date = models.DateField("Date of answer")

    def __str__(self):
        return self.question
