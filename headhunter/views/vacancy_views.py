from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, View

from headhunter.forms.vacancy_forms import VacancyForm
from headhunter.models import Vacancy, Resume, CATEGORIES
from headhunter.helpers import FormView as CustomFormView
from accounts.models import Profile


class VacancyListView(ListView):
    template_name = 'vacancy/vacancy_list.html'
    model = Vacancy
    ordering = ('-updated_at',)
    context_object_name = 'vacancies'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['resumes'] = Resume.objects.all().order_by('-updated_at')
        return super().get_context_data(**kwargs)


class VacancyDetailsView(DetailView):
    context_object_name = 'vacancy'
    template_name = 'vacancy/vacancy_details.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        resumes = Resume.objects.filter(user_id=self.request.user.pk)
        kwargs['resumes'] = resumes
        return super().get_context_data(**kwargs, form=VacancyForm())


class VacancyCreateView(LoginRequiredMixin, CustomFormView):
    template_name = 'vacancy/vacancy_create.html'
    form_class = VacancyForm
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        form = VacancyForm()
        categories = CATEGORIES
        return render(request, self.template_name,
                      context={'form': form,
                               'categories': categories})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        categories = CATEGORIES
        if form.is_valid():
            vacancy = form.save(commit=False)
            user = request.user
            vacancy.author = user
            vacancy.save()
            return redirect('/')
        return render(request, self.template_name,
                      context={
                          'form': form,
                          'categories': categories
                      })


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancy/vacancy_update.html'
    form_class = VacancyForm
    model = Vacancy

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        return super(VacancyUpdateView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('vacancy_details', kwargs={'pk': self.get_object().pk})


class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'vacancy/vacancy_delete.html'
    model = Vacancy
    confirm_deletion = False
    context_object_name = 'vacancy'

    def get_success_url(self):
        return reverse('vacancy_list')


class CompanyListView(ListView):
    template_name = 'vacancy/company_list.html'
    model = Profile
    ordering = ('user',)
    context_object_name = 'profiles'
    paginate_by = 6


class CompanyProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'vacancy/company.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        kwargs['vacancies'] = Vacancy.objects.all().order_by('-updated_at')
        kwargs['resumes'] = Resume.objects.all().order_by('-updated_at')
        return super().get_context_data(**kwargs)


class SearchResultsListView(ListView):
    model = Vacancy
    template_name = 'vacancy/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Vacancy.objects.filter(
            Q(position__istartswith=query)
        ).order_by('-updated_at')
        return object_list


class SearchCategoryListView(ListView):
    model = Vacancy
    template_name = 'vacancy/search_results.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        query = self.request.GET.get('search_cat')
        object_list = Vacancy.objects.filter(
            Q(category__icontains=query)
        ).order_by('-updated_at')
        return object_list


class SearchMoneyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/search_results.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        query = self.request.GET.get('search_val')
        object_list = Vacancy.objects.filter(
            Q(salary__istartswith=query)
        ).order_by('-updated_at')
        return object_list
