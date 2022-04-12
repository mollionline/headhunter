from django.views.generic import ListView, DetailView, RedirectView, DeleteView


class VacancyListView(ListView):
    pass


class VacancyDetailsView(DetailView):
    pass


class VacancyCreateView(RedirectView):
    pass


class VacancyDeleteView(DeleteView):
    pass
