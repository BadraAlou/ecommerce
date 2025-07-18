from django.shortcuts import render

# Create your views here.
def home(request):
    """Vue pour la page d'accueil de la boutique"""
    return render(request, 'boutique/home.html', {
        'title': 'Accueil Boutique'
    })
