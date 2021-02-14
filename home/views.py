from django.shortcuts import render
from django.views.generic import TemplateView,View


class HomePageTemplateView(View):
    

    def get(self, request):

        template_name="index_page.html" 

        context = dict()

        return render(request, template_name, context)
