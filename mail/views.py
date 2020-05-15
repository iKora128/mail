from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MailModel


class BaseView(TemplateView):
    template_name = "home.html"


class MailView(LoginRequiredMixin, ListView):
    model = MailModel
    template_name = "mail.html"
    context_object_name = "mails_list"

    def get_queryset(self):
        mails = MailModel.objects.filter(send_to_id=self.request.user.id)
        return mails


class DetailView(LoginRequiredMixin, DetailView):
    template_name = "detail.html"
    model = MailModel
    context_object_name = 'content'


class LikeView(LoginRequiredMixin, CreateView):
    model = MailModel
    template_name = "mail.html"

