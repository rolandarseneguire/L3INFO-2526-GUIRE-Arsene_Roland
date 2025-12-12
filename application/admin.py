
from django.contrib import admin
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "Titre1", "Titre2",
        "Titre3", "Titre4",
        "Titre5", "Titre6",
        "image1", "image2", "image3",
        "video",
        "bouton",
    )


    # Champs de recherche
    search_fields = (
        "Titre1", "Titre2",
        "Titre3", "Titre4",
        "Titre5", "Titre6",
    )

    # Filtres latéraux
    list_filter = ("Titre1", "Titre3", "Titre5")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Slider 1", {
            "fields": ("image1", "Titre1", "Titre2"),
            "description": "Première diapositive du slider"
        }),
        ("Slider 2", {
            "fields": ("image2", "Titre3", "Titre4"),
            "description": "Deuxième diapositive du slider"
        }),
        ("Slider 3", {
            "fields": ("image3", "video", "Titre5", "Titre6"),
            "description": "Troisième diapositive avec vidéo"
        }),
        ("Bouton", {
            "fields": ("bouton",),
            "description": "Image du bouton associé au slider"
        }),
    )
    # Ordre par défaut
    ordering = ("id",)

@admin.register(Aboutaccueil)
class AboutaccueilAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre1",
        "sousTitre2",
        "nom_person",
        "role",
        "info1",
        "info2",
        "info3",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre1",
        "sousTitre2",
        "nom_person",
        "role",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre1",
        "sousTitre2",
        "nom_person",
        "role",
        "info1",
        "info2",
        "info3",
    )

    # Filtres latéraux
    list_filter = ("role", "sousTitre1", "sousTitre2")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("image1", "titre", "sousTitre1", "sousTitre2", "description", "nom_person", "role"),
            "description": "Informations principales de la section About"
        }),
        ("Informations supplémentaires 1", {
            "fields": ("icon1", "info1", "contenu1"),
            "description": "Bloc supplémentaire avec icône et contenu"
        }),
        ("Informations supplémentaires 2", {
            "fields": ("icon2", "info2", "contenu2"),
            "description": "Bloc supplémentaire avec icône et contenu"
        }),
        ("Informations supplémentaires 3", {
            "fields": ("icon3", "info3", "contenu3"),
            "description": "Bloc supplémentaire avec icône et contenu"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)

from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre1",
        "sousTitre2",
        "motivation",
        "nom1", "nom2", "nom3", "nom4", "nom5", "nom6",
        "bouton",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre1",
        "sousTitre2",
        "motivation",
        "bouton",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre1",
        "sousTitre2",
        "motivation",
        "nom1", "nom2", "nom3", "nom4", "nom5", "nom6",
    )

    # Filtres latéraux
    list_filter = ("sousTitre1", "sousTitre2")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("titre", "sousTitre1", "sousTitre2", "motivation"),
            "description": "Informations générales de la section Services"
        }),
        ("Service 1", {
            "fields": ("nom1", "description1", "image1"),
            "description": "Premier service"
        }),
        ("Service 2", {
            "fields": ("nom2", "description2", "image2"),
            "description": "Deuxième service"
        }),
        ("Service 3", {
            "fields": ("nom3", "description3", "image3"),
            "description": "Troisième service"
        }),
        ("Service 4", {
            "fields": ("nom4", "description4", "image4"),
            "description": "Quatrième service"
        }),
        ("Service 5", {
            "fields": ("nom5", "description5", "image5"),
            "description": "Cinquième service"
        }),
        ("Service 6", {
            "fields": ("nom6", "description6", "image6"),
            "description": "Sixième service"
        }),
        ("Bouton", {
            "fields": ("bouton",),
            "description": "Texte du bouton associé à la section Services"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)

from django.contrib import admin
from .models import Feature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre1",
        "sousTitre2",
        "titre1",
        "titre2",
        "titre3",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre1",
        "sousTitre2",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre1",
        "sousTitre2",
        "titre1",
        "titre2",
        "titre3",
        "description",
        "description1",
        "description2",
        "description3",
    )

    # Filtres latéraux
    list_filter = ("sousTitre1", "sousTitre2")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("image", "titre", "sousTitre1", "sousTitre2", "description"),
            "description": "Informations principales de la section Feature"
        }),
        ("Bloc 1", {
            "fields": ("titre1", "description1"),
            "description": "Premier bloc détaillé"
        }),
        ("Bloc 2", {
            "fields": ("titre2", "description2"),
            "description": "Deuxième bloc détaillé"
        }),
        ("Bloc 3", {
            "fields": ("titre3", "description3"),
            "description": "Troisième bloc détaillé"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)



from django.contrib import admin
from .models import Parallax

@admin.register(Parallax)
class ParallaxAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "message",
        "numero",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
        "message",
        "numero",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre",
        "description",
        "message",
        "numero",
    )

    # Filtres latéraux
    list_filter = ("sousTitre", "numero")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "sousTitre", "description"),
            "description": "Texte principal affiché dans la section Parallax"
        }),
        ("Contact / Message", {
            "fields": ("message", "numero"),
            "description": "Message et numéro associés à la section"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "motivation",
        "categorie1",
        "categorie2",
        "categorie3",
        "categorie4",
        "categorie5",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
        "motivation",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre",
        "motivation",
        "categorie1",
        "categorie2",
        "categorie3",
        "categorie4",
        "categorie5",
    )

    # Filtres latéraux
    list_filter = ("categorie1", "categorie2", "categorie3", "categorie4", "categorie5")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "sousTitre", "motivation", "categorie1", "categorie2", "categorie3", "categorie4", "categorie5"),
            "description": "Titres, sous-titres et catégories du portfolio"
        }),
        ("Aire plane (Catégorie 3)", {
            "fields": ("aireplane1", "aireplane2", "aireplane3", "aireplane4"),
            "description": "Images pour la catégorie Aire plane"
        }),
        ("Maritime (Catégorie 4)", {
            "fields": ("maritime1", "maritime2", "maritime3", "maritime4"),
            "description": "Images pour la catégorie Maritime"
        }),
        ("Road & Truck (Catégorie 2)", {
            "fields": ("roadtruck1", "roadtruck2", "roadtruck3", "roadtruck4"),
            "description": "Images pour la catégorie Road & Truck"
        }),
        ("Vidéos (Catégorie 5)", {
            "fields": ("video1", "video2", "video3", "video4"),
            "description": "Vidéos associées au portfolio"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "motivation",
        "prenom1", "role1",
        "prenom2", "role2",
        "prenom3", "role3",
        "prenom4", "role4",
        "prenom5", "role5",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
        "motivation",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre",
        "motivation",
        "prenom1", "role1",
        "prenom2", "role2",
        "prenom3", "role3",
        "prenom4", "role4",
        "prenom5", "role5",
    )

    # Filtres latéraux
    list_filter = ("role1", "role2", "role3", "role4", "role5")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("titre", "sousTitre", "motivation"),
            "description": "Informations générales de la section Team"
        }),
        ("Membre 1", {
            "fields": ("photo1", "prenom1", "role1"),
            "description": "Premier membre de l’équipe"
        }),
        ("Membre 2", {
            "fields": ("photo2", "prenom2", "role2"),
            "description": "Deuxième membre de l’équipe"
        }),
        ("Membre 3", {
            "fields": ("photo3", "prenom3", "role3"),
            "description": "Troisième membre de l’équipe"
        }),
        ("Membre 4", {
            "fields": ("photo4", "prenom4", "role4"),
            "description": "Quatrième membre de l’équipe"
        }),
        ("Membre 5", {
            "fields": ("photo5", "prenom5", "role5"),
            "description": "Cinquième membre de l’équipe"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


from django.contrib import admin
from .models import Pricing

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "motivation",
        "par",
        "utilisateur",
        "temps",
        "discution",
        "bouton",
        "niveau1", "prix1", "nombre_projet1", "espace1", "securite",
        "niveau2", "prix2", "nombre_projet2", "espace2",
        "niveau3", "prix3", "nombre_projet3", "espace3",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
        "motivation",
        "bouton",
    )

    # Champs de recherche
    search_fields = (
        "titre",
        "sousTitre",
        "motivation",
        "par",
        "avantage",
        "utilisateur",
        "temps",
        "discution",
        "niveau1", "prix1", "nombre_projet1", "espace1", "securite",
        "niveau2", "prix2", "nombre_projet2", "espace2",
    )

    # Filtres latéraux
    list_filter = ("niveau1", "niveau2", "utilisateur")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "sousTitre", "motivation", "par", "avantage", "utilisateur", "temps", "discution", "bouton"),
            "description": "Texte principal et informations générales de la section Pricing"
        }),
        ("Niveau 1", {
            "fields": ("niveau1", "prix1", "nombre_projet1", "espace1", "securite"),
            "description": "Détails du premier niveau de prix"
        }),
        ("Niveau 2", {
            "fields": ("niveau2", "prix2", "nombre_projet2", "espace2"),
            "description": "Détails du deuxième niveau de prix"
        }),
        ("Niveau 2", {
            "fields": ("niveau3", "prix3", "nombre_projet3", "espace3"),
            "description": "Détails du deuxième niveau de prix"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


from django.contrib import admin
from .models import Blogaccueil

@admin.register(Blogaccueil)
class BlogaccueilAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "motivation",
        "vers",
        "nom1", "auteur1", "date1", "nombre_commentaire1", "nombre_vue1",
        "nom2", "auteur2", "date2", "nombre_commentaire2", "nombre_vue2",
        "nom3", "auteur3", "date3", "nombre_commentaire3", "nombre_vue3",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
        "motivation",
        "vers",
    )

    # Champs de recherche
    search_fields = (
        "titre", "sousTitre", "motivation", "vers",
        "nom1", "auteur1", "nom2", "auteur2", "nom3", "auteur3",
    )

    # Filtres latéraux
    list_filter = ("auteur1", "auteur2", "auteur3", "date1", "date2", "date3")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("titre", "sousTitre", "motivation", "vers"),
            "description": "Informations générales de la section Blogaccueil"
        }),
        ("Blog 1", {
            "fields": ("image1", "nom1", "contenu1", "auteur1", "nombre_commentaire1", "nombre_vue1"),
            "description": "Premier article du blog"
        }),
        ("Blog 2", {
            "fields": ("image2", "nom2", "contenu2", "auteur2", "nombre_commentaire2", "nombre_vue2"),
            "description": "Deuxième article du blog"
        }),
        ("Blog 3", {
            "fields": ("image3", "nom3", "contenu3", "auteur3", "nombre_commentaire3", "nombre_vue3"),
            "description": "Troisième article du blog"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "client1", "provenance1",
        "client2", "provenance2",
        "client3", "provenance3",
    )

    # Champs éditables directement dans la liste
    list_editable = (
        "sousTitre",
    )

    # Champs de recherche
    search_fields = (
        "titre", "sousTitre",
        "client1", "provenance1", "temoignage1",
        "client2", "provenance2", "temoignage2",
        "client3", "provenance3", "temoignage3",
    )

    # Filtres latéraux
    list_filter = ("provenance1", "provenance2", "provenance3")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Section principale", {
            "fields": ("titre", "sousTitre","image"),
            "description": "Informations générales de la section Témoignages"
        }),
        ("Témoignage 1", {
            "fields": ("image1", "client1", "provenance1", "temoignage1"),
            "description": "Premier témoignage client"
        }),
        ("Témoignage 2", {
            "fields": ("image2", "client2", "provenance2", "temoignage2"),
            "description": "Deuxième témoignage client"
        }),
        ("Témoignage 3", {
            "fields": ("image3", "client3", "provenance3", "temoignage3"),
            "description": "Troisième témoignage client"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


# Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id",
        "titre",
        "sousTitre",
        "photo1", "photo2", "photo3", "photo4",
        "photo5", "photo6", "photo7", "photo8",
    )

    # Champs éditables directement dans la liste
    list_editable = ("sousTitre",)

    # Champs de recherche
    search_fields = ("titre", "sousTitre")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "sousTitre"),
            "description": "Titre et sous-titre de la section Client"
        }),
        ("Photos", {
            "fields": ("photo1", "photo2", "photo3", "photo4", "photo5", "photo6", "photo7", "photo8"),
            "description": "Photos des différents clients"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


# Video
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("id", "video")
    # Champs de recherche
    search_fields = ("video",)

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Vidéo", {
            "fields": ("video",),
            "description": "Fichier vidéo associé"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)


from django.contrib import admin
from .models import Join

@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("id", "titre", "sousTitre", "motivation", "bouton")

    # Champs éditables directement dans la liste
    list_editable = ("sousTitre", "motivation", "bouton")

    # Champs de recherche
    search_fields = ("titre", "sousTitre", "motivation", "bouton")

    # Filtres latéraux
    list_filter = ("sousTitre", "bouton")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "sousTitre", "motivation", "bouton"),
            "description": "Section Join avec titre, sous-titre, motivation et bouton"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)

from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("id", "page", "titre", "nom")

    # Champs éditables directement dans la liste
    list_editable = ("titre", "nom")

    # Champs de recherche
    search_fields = ("page", "titre", "nom")

    # Filtres latéraux
    list_filter = ("page",)

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations du Banner", {
            "fields": ("page", "titre", "nom"),
            "description": "Définir le titre et le sous-titre du banner pour une page spécifique"
        }),
    )

    # Ordre par défaut
    ordering = ("id",)



from django.contrib import admin
from .models import Servicedetail

@admin.register(Servicedetail)
class ServicedetailAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "id", "nomservice", "numero",
        "service1", "service2", "service3",
        "service4", "service5", "service6"
    )

    # Champs éditables directement dans la liste
    list_editable = ("nomservice", "numero")

    # Champs de recherche
    search_fields = (
        "nomservice", "numero",
        "service1", "service2", "service3",
        "service4", "service5", "service6"
    )

    # Filtres latéraux
    list_filter = ("nomservice",)

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations générales", {
            "fields": ("nomservice", "numero", "conseilImage")
        }),
        ("Services", {
            "fields": ("service1", "service2", "service3", "service4", "service5", "service6")
        }),
        ("Bloc 1", {
            "fields": ("sousTitr1", "description1", "Image", "explication")
        }),
        ("Bloc 2", {
            "fields": ("sousTitr2", "description2", "block1", "contenu1", "block2", "contenu2", "block3", "contenu3")
        }),
        ("Bloc 3", {
            "fields": ("sousTitr3", "descript1", "descript2")
        }),
        ("Lignes", {
            "fields": (
                "ligne1", "ligne2", "ligne3", "ligne4", "ligne5",
                "sousligne1", "sousligne2", "sousligne3", "ligne6"
            )
        }),
    )

    # Ordre par défaut
    ordering = ("id",)








