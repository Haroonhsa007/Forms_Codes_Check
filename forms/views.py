from django.http import HttpResponse


def home(request):
    return HttpResponse("Hola mundo. Estás en la página de inicio")


def about(request):
    return HttpResponse("Hola, esta es la página sobre la información de los investigadores.")
