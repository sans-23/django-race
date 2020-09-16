from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Feedback
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class FeedbackCreate(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['feedback']
    success_url = reverse_lazy('quiz:quiz_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
