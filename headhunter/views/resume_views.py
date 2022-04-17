from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from headhunter.forms.resume_forms import ResumeForm, ResumeUpdateForm, ExperienceUpdateForm, EducationUpdateForm
from headhunter.models import Resume, CATEGORIES, Experiences, Educations


class ResumeCreateView(CreateView):
    template_name = 'resume/create_resume.html'
    form_class = ResumeForm
    model = Resume
    object = None

    def get_success_url(self):
        return reverse('detail_resume', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        return super().get_context_data(**kwargs)


class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume/detail_resume.html'
    context_object_name = 'resume'


class ResumeDeleteView(DeleteView):
    template_name = 'resume/detail_resume.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        return self.delete(request=request)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class ResumeUpdateView(UpdateView):
    template_name = 'resume/update_resume.html'
    form_class = ResumeUpdateForm
    model = Resume
    extra_context = {'categories': CATEGORIES}

    def get_success_url(self):
        return reverse('detail_resume', kwargs={'pk': self.get_object().pk})


class ExperienceUpdateView(UpdateView):
    template_name = 'resume/experience_update.html'
    form_class = ExperienceUpdateForm
    model = Experiences

    def get_success_url(self):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        return reverse('detail_resume', kwargs={'pk': resume.pk})

    def get_context_data(self, **kwargs):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        kwargs['resume'] = resume
        return super().get_context_data(**kwargs)


class ExperienceDeleteView(DeleteView):
    template_name = 'resume/detail_resume.html'
    model = Experiences

    def get(self, request, *args, **kwargs):
        return self.delete(request=request)

    def get_success_url(self):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        return reverse('detail_resume', kwargs={'pk': resume.pk})


class EducationUpdateView(UpdateView):
    template_name = 'resume/education_update.html'
    form_class = EducationUpdateForm
    model = Educations

    def get_success_url(self):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        return reverse('detail_resume', kwargs={'pk': resume.pk})

    def get_context_data(self, **kwargs):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        kwargs['resume'] = resume
        return super().get_context_data(**kwargs)


class EducationDeleteView(DeleteView):
    template_name = 'resume/detail_resume.html'
    model = Educations

    def get(self, request, *args, **kwargs):
        return self.delete(request=request)

    def get_success_url(self):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume'))
        return reverse('detail_resume', kwargs={'pk': resume.pk})


class ExperienceCreateView(CreateView):
    template_name = 'resume/create_experience.html'
    form_class = ExperienceUpdateForm
    model = Experiences

    def get_context_data(self, **kwargs):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        kwargs['resume'] = resume
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        if form.is_valid():
            experience = Experiences.objects.create(
                name_company=form.cleaned_data.get('name_company'),
                position=form.cleaned_data.get('position'),
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date'),
                responsibilities=form.cleaned_data.get('responsibilities')
            )
            resume.work_experience.add(experience)
            url = (reverse('detail_resume', kwargs={'pk': resume.pk}))
            return HttpResponseRedirect(url)
        return render(request, self.template_name, context={'form': form})


class EducationCreateView(CreateView):
    template_name = 'resume/create_education.html'
    form_class = EducationUpdateForm
    model = Educations

    def get_context_data(self, **kwargs):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        kwargs['resume'] = resume
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        if form.is_valid():
            education = Educations.objects.create(
                institution_name=form.cleaned_data.get('institution_name'),
                speciality=form.cleaned_data.get('speciality'),
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date')
            )
            resume.education.add(education)
            url = (reverse('detail_resume', kwargs={'pk': resume.pk}))
            return HttpResponseRedirect(url)
        return render(request, self.template_name, context={'form': form})
