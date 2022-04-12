from django.views.generic import ListView, DetailView, RedirectView, DeleteView

from headhunter.forms.vacancy_forms import VacancyForm
from headhunter.models import Vacancy


class VacancyListView(ListView):
    pass


class VacancyDetailsView(DetailView):
    context_object_name = 'vacancy'
    template_name = 'vacancy/vacancy_details.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, form=VacancyForm())


class VacancyCreateView(RedirectView):
    pass


class VacancyDeleteView(DeleteView):
    pass
