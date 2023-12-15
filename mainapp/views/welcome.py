from django.views.generic import TemplateView


class WelcomeToSpeedPyView(TemplateView):
    template_name = "mainapp/welcome.html"
