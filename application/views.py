from django.shortcuts import render

from django.shortcuts import render
from .models import *

from django.shortcuts import render, get_object_or_404



def index(request):
    context = {
        "slider": Slider.objects.first(),
        "aboutaccueil": Aboutaccueil.objects.first(),
        "service": Service.objects.first(),
        "feature": Feature.objects.first(),
        "parallax": Parallax.objects.first(),
        "portfolio": Portfolio.objects.first(),
        "team": Team.objects.first(),
        "pricing": Pricing.objects.first(),
        "blog": Blogaccueil.objects.first(),
        "testimonial": Testimonial.objects.first(),
        "client": Client.objects.first(),
        "video": Video.objects.first(),
        "join": Join.objects.first(),
    }
    return render(request, "application/index.html", context)

def about(request):
    # Récupération des données dynamiques
    banner = get_object_or_404(Banner, page="about")   # Banner spécifique à la page About
    about_section = Aboutaccueil.objects.first()      # Section About
    team_section = Team.objects.first()                # Section Team
    testimonial_section = Testimonial.objects.first()  # Témoignages
    client_section = Client.objects.first()            # Clients

    context = {
        "banner": banner,
        "aboutaccueil": about_section,
        "team": team_section,
        "testimonial": testimonial_section,
        "client": client_section,
    }
    return render(request, "application/about-us.html", context)




def services(request):
    # Récupération des données dynamiques
    banner = get_object_or_404(Banner, page="services")   # Banner spécifique à la page Services
    about_section = Aboutaccueil.objects.first()          # Section About
    service_section = Service.objects.first()             # Section Services
    feature_section = Feature.objects.first()             # Section Feature
    testimonial_section = Testimonial.objects.first()     # Témoignages
    client_section = Client.objects.first()               # Clients

    context = {
        "banner": banner,
        "aboutaccueil": about_section,
        "service": service_section,
        "feature": feature_section,
        "testimonial": testimonial_section,
        "client": client_section,
    }
    return render(request, "application/our-services.html", context)



def services_detail(request):
    # Banner spécifique à la page Services Detail
    banner = get_object_or_404(Banner, page="services-detail")

    # Détail du service par son id
    service_detail =Servicedetail.objects.first()

    # Bloc "Join" (appel à l’action, newsletter, etc.)
    join = Join.objects.first()  # ou get_object_or_404(Join, pk=1) si tu gères une entrée unique

    context = {
        "banner": banner,
        "servicedetail": service_detail,
        "join": join,
    }
    return render(request, "application/services-detail.html", context)



def gallery(request):
    # Banner spécifique à la page Gallery
    banner = get_object_or_404(Banner, page="gallery")

    # Section Portfolio (galerie des projets)
    portfolio_items = Portfolio.objects.first()

    # Section Aboutaccueil (utilisée dans about_X.html)
    about_section = Aboutaccueil.objects.first()

    # Témoignages
    testimonial_section = Testimonial.objects.first()

    context = {
        "banner": banner,
        "portfolio": portfolio_items,
        "aboutaccueil": about_section,
        "testimonial": testimonial_section,
    }
    return render(request, "application/gallery.html", context)



def team(request):
    # Banner spécifique à la page Team
    banner = get_object_or_404(Banner, page="team")

    # Section Team (liste des membres)
    team_members = Team.objects.first()

    # Témoignages
    testimonials = Testimonial.objects.first()

    context = {
        "banner": banner,
        "team": team_members,
        "testimonial": testimonials,
    }
    return render(request, "application/team.html", context)



def pricing(request):
    # Banner spécifique à la page Pricing
    banner = get_object_or_404(Banner, page="pricing")

    # Section Pricing (plans tarifaires)
    pricing_items = Pricing.objects.first()

    # Témoignages
    testimonials = Testimonial.objects.first()

    context = {
        "banner": banner,
        "pricing": pricing_items,
        "testimonial": testimonials,
    }
    return render(request, "application/pricing.html", context)






