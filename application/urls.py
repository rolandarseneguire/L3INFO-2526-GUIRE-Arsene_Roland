from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
   path("services/", views.services, name="services"),
   path("services-detail/", views.services_detail, name="services_detail"),
   path("gallery/", views.gallery, name="gallery"),
    path("team/", views.team, name="team"),
    path("pricing/", views.pricing, name="pricing"),

    # route principale vers la page d'accueil
]

# Gestion des fichiers médias (images, vidéos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
