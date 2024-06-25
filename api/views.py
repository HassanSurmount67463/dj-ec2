from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request):
        # return HttpResponse("Hello, world. You're at the polls home page.")
        return render(request, "html/home.html")
        # return render(request, "html/home.html")
