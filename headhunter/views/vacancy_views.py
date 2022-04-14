from django.views.generic import ListView, DetailView, RedirectView, DeleteView

from headhunter.forms.vacancy_forms import VacancyForm
from headhunter.models import Vacancy


class VacancyListView(ListView):
    template_name = 'vacancy/vacancy_list.html'
    model = Vacancy
    ordering = ('-updated_at',)
    context_object_name = 'vacancies'
    paginate_by = 6


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
