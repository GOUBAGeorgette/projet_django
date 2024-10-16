from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import PanneForm, SignupForm  # Assurez-vous que ces formulaires sont bien importés


# Vue pour soumettre une panne
def soumettre_panne(request):
    if request.method == 'POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # Redirigez vers la vue de confirmation
    else:
        form = PanneForm()

    return render(request, 'soumission_pannes/soumettre.html', {'form': form})  # Utilisez le chemin correct

# Vue pour la confirmation
def confirmation(request):
    return render(request, 'soumission_pannes/confirmation.html')  # Page de confirmation

# Page d'accueil
def index(request):
    return render(request, 'soumission_pannes/index.html')  # Page d'accueil (si elle existe)

# Vue pour l'inscription
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Création de l'utilisateur
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirection vers la page de connexion
    else:
        form = SignupForm()

    return render(request, 'soumission_pannes/signup.html', {'form': form})

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirection vers la page d'accueil après connexion
        else:
            # Affichez un message d'erreur si les identifiants sont incorrects
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'soumission_pannes/login.html', {'error_message': error_message})
    return render(request, 'soumission_pannes/login.html')  # Afficher le formulaire de connexion

# Vue pour la page "À Propos"
def a_propos(request):
    return render(request, 'soumission_pannes/a_propos.html')  # Assurez-vous que ce template existe
