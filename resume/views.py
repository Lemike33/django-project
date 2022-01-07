from django.views.generic import ListView, DetailView, CreateView
from .models import Job


class WorkPage(ListView):
    model = Job
    template_name = 'users/about.html'
    context_object_name = 'jobs'
    ordering = ['-id']  # sort for -id
    paginate_by = 1  # create paginate

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(WorkPage, self).get_context_data(**kwargs)
        ctx['title'] = 'мое резюме'
        return ctx




