from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "home.html"


class MailView(TemplateView):
    template_name = "mail.html"


