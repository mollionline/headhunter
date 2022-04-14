from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

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


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancy/vacancy_update.html'
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        return reverse('vacancy_details', kwargs={'pk': self.get_object().pk})


class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'vacancy/vacancy_delete.html'
    model = Vacancy
    confirm_deletion = False
    context_object_name = 'vacancy'

    def get_success_url(self):
        return reverse('vacancy_list')
