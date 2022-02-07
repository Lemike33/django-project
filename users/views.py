from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, LinkForm
from django.contrib.auth.decorators import login_required
from .models import Link
from django.views.generic import ListView, CreateView


def open_to_main_page(request):
    """ Переход на главную страницу сайта """
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'users/start.html',
    context = {'num_visits':num_visits},
    )


def open_to_registration_page(request):
    """ Переход на страницу регистрации и создание регистрации на сайте """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required()
def open_to_profile_page(request):
    """ Переход на страницу профайла и изменение данных зарегистрированного пользователя"""
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)


class CreateLinkView(CreateView):
    """ класс для создания веб-сервиса по добавлению сокращаемых ссылок """
    model = Link
    template_name = 'users/links.html'

    fields = ['longLink', 'shortLink']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CreateLinkView, self).get_context_data(**kwargs)
        links = Link.objects.filter(user=self.request.user)
        ctx['links'] = links
        return ctx

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
