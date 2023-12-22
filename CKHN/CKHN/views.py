from django.shortcuts import render
def accueil_render(request):
    page=render(request,"homepage.html") 
    return page
