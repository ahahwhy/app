from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request) -> HttpResponse:
    context = {"title": "Home", "content": "Строим экономику будущего - вместе"}

    return render(request, "main/index.html", context)


def start(request) -> HttpResponse:
    context = {"title": "Home", "content": "Строим экономику будущего - вместе"}
    return render(request, "main/start.html", context)


def discover(request) -> HttpResponse:
    context = {"title": "Home", "content": "Строим экономику будущего - вместе"}
    return render(request, "main/discover.html", context)


def about(request) -> HttpResponse:
    context = {"title": "Home", "content": "Строим экономику будущего - вместе"}
    return render(request, "main/about.html", context)


def project(request) -> HttpResponse:
    return HttpResponse("Project page")
