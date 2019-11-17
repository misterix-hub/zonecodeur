from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="forum"),
    url('login', views.connexion, name="connexion"),
    url('register', views.inscription, name="inscription"),
    url('processings/reg', views.inscriptionAction, name="inscriptionAction"),
    url('resets/password', views.motDePasseOublie, name="motDePasseOublie"),
    url('ask', views.poserQuestion, name="poserQuestion"),

    url('news', views.publication, name="publications"),
    url('docs', views.documentation, name="documentations"),
    url('courses', views.cours, name="cours"),
    url('members', views.membre, name="membres"),

    url('about', views.aPropos, name="aPropos"),
    url('contats', views.contacts, name="contacts"),
    url('team', views.equipe, name="equipe"),
    url('crs/1/details', views.detailsCours, name="detailsCours"),
    url('tutos/1/video', views.detailsVideos, name="detailsVideos"),
    url('users/2/profile', views.profilMembre, name="profilMembre"),
    url('avatar', views.avatar, name="avatar"),
]
