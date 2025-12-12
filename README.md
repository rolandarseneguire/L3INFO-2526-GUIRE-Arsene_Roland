 Installation et lancement
 
 Cloner le dépôt:
   git clone https://github.com/rolandarseneguire/L3INFO-2526-GUIRE-Arsene_Roland.git
   cd projet



#  Projet Django - RETRO-INGENIERIE

Ce projet est un site web développé avec **Django** dans le cadre de la Licence 3 Informatique.  
Il illustre la rétro‑ingénierie et la mise en place d’un site dynamique où toutes les sections (slider, vidéo, services, portfolio, blog, contact, etc.) sont gérées depuis l’admin Django.



##  Fonctionnalités principales

- Gestion dynamique des sections** : toutes les parties du site (bannières, sliders, vidéos, services, portfolio, blog, etc.) sont alimentées depuis la base de données.
- Administration complète : ajout, modification et suppression des contenus via l’interface admin Django.
- Portfolio filtrable : affichage dynamique des projets avec filtres.
- Blog : gestion des articles avec titres, dates et images.
- Support & Contact : formulaires dynamiques reliés à la base.
- Design responsive : intégration de Bootstrap et Line Awesome pour un rendu moderne.
- etc



##  Technologies utilisées

- Backend : Django (Python)
- Frontend : HTML5, CSS3, Bootstrap, Line Awesome
- Base de données : SQLite (par défaut Django)
- Outils : Git, GitHub, Virtualenv

---

##Structure du projet


projet/ 
│── application/ 
# App principale Django 
│ ├── models.py # Définition des modèles (Slider, Video, Blog, etc.) 
│ ├── views.py # Logique des vues 
│ ├── urls.py # Routage des URLs 
│ └── templates/ # Templates HTML 
  │── static/ # Fichiers CSS, JS, images
│── manage.py # Commandes Django 
│── README.md # Documentation du projet

etc 

