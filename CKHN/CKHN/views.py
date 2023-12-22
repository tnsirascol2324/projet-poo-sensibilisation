from django.shortcuts import render

def homepage_render(request):
    page= render(request,"homepage.html") 
    return page

def randompage_render(request):
    import random                               #on peut import dans une fonction
    nb= random.randint(1,100)
    context={"nombre_aleatoire":nb}
    page = render (request,"random.html",context)#les context sont des dico pous associer les valeur 
    return page

def annuairepage_render(request):
    contact=["jean",'arthur',"zebi"]
    context={"contact_list":contact} #les balise et les pages entre guillemets
    page= render (request,"annuaire.html",context)
    return page

def accesspage_render(request):
    context ={"access":False} 
    page= render (request,"acces.html",context) #quand le context a une valeur ne pas l'oublier sinon pas d'affichage
    return page

def biopage_render(request,username):
    print("hello",username)
    context={"nom":username}
    page=render(request,"bio.html",context)
    return page

def mdppage_render(request):
    if request.method =="GET":
        page=render(request,"mdp.html") #penser au guillemet de la page por render
        return page 
    if request.method=="POST":
        #recuperation du post
        mp= request.POST["mdp_input"]
        if mp=="yep":
            from django.http import HttpResponse
            return HttpResponse("nice")
        else:
            page=render(request,"mdp.html")
            return page

