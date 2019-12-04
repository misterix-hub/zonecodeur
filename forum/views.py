from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from forum.functions.functions import handle_uploaded_file

def index(request):
    return render(request, 'forum/index.phtml')

def connexion(request):
    return render(request, 'forum/connexion.phtml')

def inscription(request):
    return render(request, 'forum/inscription.phtml')

def inscriptionAction(request):
    return render(request, 'forum/inscriptionSuccess.phtml')

def motDePasseOublie(request):
    return render(request, 'forum/motDePasseOublie.phtml')

def poserQuestion(request):
    return render(request, 'forum/poserQuestion.phtml')

def publication(request):
    return render(request, 'forum/publication/index.phtml')

def documentation(request):
    return render(request, 'forum/documentation/index.phtml')

def cours(request):
    return render(request, 'forum/cours/index.phtml')

def membre(request):
    return render(request, 'forum/membre/index.phtml')

def aPropos(request):
    return render(request, 'forum/aPropos.phtml')

def contacts(request):
    return render(request, 'forum/contacts.phtml')

def equipe(request):
    return render(request, 'forum/equipe.phtml')

def detailsCours(request):
    return render(request, 'forum/cours/details.phtml')

def detailsVideos(request):
    return render(request, 'forum/cours/video.phtml')

def profilMembre(request):
    return render(request, 'forum/users/profil.phtml')

def avatar(request):
    return render(request, 'forum/users/avatar.phtml')

def setAvatar(request):
    if request.method == 'POST' and request.FILES['image']:  
        handle_uploaded_file(request.FILES['image'])
        return render(request, 'forum/inscriptionSuccess.phtml')
