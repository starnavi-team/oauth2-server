from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/user_update.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('main')

    def get_object(self, queryset=None):
        return self.request.user
