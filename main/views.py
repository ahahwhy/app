from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request) -> HttpResponse:
    context = {"title": "Home", "content": "Строим экономику будущего - вместе"}

    return render(request, "main/index.html", context)


def account(request) -> HttpResponse:
    return HttpResponse("Account page")


def authorization(request) -> HttpResponse:
    return HttpResponse("Authorization page")


def registration(request) -> HttpResponse:
    return HttpResponse("Registration page")


def project(request) -> HttpResponse:
    return HttpResponse("Project page")
