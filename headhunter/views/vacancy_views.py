from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, RedirectView, DeleteView, CreateView

from headhunter.forms.vacancy_forms import VacancyForm
from headhunter.models import Vacancy
from headhunter.helpers import FormView as CustomFormView


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


class VacancyCreateView(LoginRequiredMixin, CustomFormView):
    template_name = 'vacancy/vacancy_create.html'
    form_class = VacancyForm
    redirect_url = ''

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.save()
            return redirect('vacancy_list')
        return render(request, self.template_name,
                      context={
                          'form': form
                      }
                      )


class VacancyUpdateView(RedirectView):
    pass


class VacancyDeleteView(DeleteView):
    pass
