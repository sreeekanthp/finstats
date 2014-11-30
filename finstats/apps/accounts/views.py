from django.views.generic import TemplateView, RedirectView

class TestView(TemplateView):
    template_name = "index1.html"
