from django.shortcuts import render
from .models import Course

def index(request):
    couses = Course.objects.all()
    template_name = 'cursos/index.html'
    context = {
        'courses': couses
    }
    return render(request, template_name, context)


def details(request, pk ):
    print('pkzera', pk)
    course = Course.objects.get(pk=pk)
    context = {'courses': course}
    template_name = 'cursos/details.html'
    return render(request, template_name, context)