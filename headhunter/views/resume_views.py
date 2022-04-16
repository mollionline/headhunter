from django.shortcuts import redirect, render, reverse
from django.views.generic import CreateView, DetailView

from headhunter.forms.resume_forms import ResumeForm
from headhunter.models import Resume, CATEGORIES


class ResumeCreateView(CreateView):
    template_name = 'resume/create_resume.html'
    form_class = ResumeForm
    model = Resume
    object = None

    def get_success_url(self):
        return reverse('detail_resume', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['categories'] = CATEGORIES
        return super().get_context_data(**kwargs)


class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume/detail_resume.html'
    context_object_name = 'resume'
