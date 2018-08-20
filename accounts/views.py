from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView


class SignUp(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignUp, self).form_valid(form)
