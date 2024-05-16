from django.shortcuts import render

from vacancy_app.models import Vacancy


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_app/vacancy_list.html', {'vacancies': vacancies})
