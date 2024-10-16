from django.urls import path
from .views import index, soumettre_panne, confirmation, signup_view, login_view, a_propos  # Ajoutez a_propos ici

urlpatterns = [
    path('', index, name='index'),  # Page d'accueil
    path('pannes/soumettre/', soumettre_panne, name='soumettre_panne'),  # Vue pour soumettre une panne
    path('pannes/confirmation/', confirmation, name='confirmation'),  # Vue de confirmation
    path('signup/', signup_view, name='signup'),  # Vue d'inscription
    path('login/', login_view, name='login'),  # Vue de connexion
    path('a-propos/', a_propos, name='a_propos'),  # Vue À propos
]
