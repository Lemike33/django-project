from django.views.generic import ListView, DetailView, CreateView
from .models import Job


class WorkPageList(ListView):
    """ Вызов страницы со списком рабочих мест и их сортировкой по полю id """
    model = Job
    template_name = 'users/about.html'
    context_object_name = 'jobs'
    ordering = ['-id']  # sort for -id
    paginate_by = 1  # create paginate

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(WorkPageList, self).get_context_data(**kwargs)
        ctx['title'] = 'мое резюме'
        return ctx




