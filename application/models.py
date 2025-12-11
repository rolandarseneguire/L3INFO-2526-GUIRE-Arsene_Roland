from django.db import models
class Slider(models.Model):
    image = models.ImageField(upload_to='images/Slider/')
class Slider(models.Model):
#Slider1
    image1 = models.ImageField(upload_to='images/Slider/')
    Titre1 = models.CharField(max_length=100)
    Titre2 = models.CharField(max_length=100)
#Slider2
    image2 = models.ImageField(upload_to='images/Slider/')
    Titre3 = models.CharField(max_length=100)
    Titre4 = models.CharField(max_length=100)


#Slider2
    image3 = models.ImageField(upload_to='images/Slider/')
    video = models.FileField(upload_to='videos/Slider/')
    Titre5 = models.CharField(max_length=100)
    Titre6 = models.CharField(max_length=100)
#bouton
    bouton =models.CharField(max_length=100)
    class Meta:
        db_table = 'slider'
    def __str__(self):
           return f"{self.image1} {self.Titre1} {self.Titre2} {self.image2} {self.Titre3} {self.Titre4} {self.image3} {self.video} {self.Titre5} {self.Titre6} {self.bouton}"


class Aboutaccueil(models.Model):
    image1 = models.ImageField(upload_to='images/Aboutaccueil/')
    titre = models.CharField(max_length=100)
    sousTitre1 = models.CharField(max_length=100)
    sousTitre2 = models.CharField(max_length=100)
    description = models.TextField()
    nom_person = models.CharField(max_length=100)
    role= models.CharField(max_length=100)

#Informations suplementaitre
    icon1 = models.ImageField(upload_to='images/Aboutaccueil/')
    info1= models.TextField()
    contenu1= models.TextField()


    icon2 = models.ImageField(upload_to='icons/Aboutaccueil/')
    info2= models.TextField()
    contenu2= models.TextField()


    icon3 = models.ImageField(upload_to='icons/Aboutaccueil/')
    info3= models.TextField()
    contenu3= models.TextField()
    class Meta:
        db_table = 'about_accueil'

    def __str__(self):
        return f"{self.image1} {self.titre} {self.sousTitre1} {self.sousTitre2} {self.description} {self.nom_person} {self.role} {self.icon1} {self.info1} {self.contenu1} {self.icon2} {self.info2} {self.contenu2} {self.icon3} {self.info3} {self.contenu3}"


class Service(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre1 = models.CharField(max_length=100)
    sousTitre2 = models.CharField(max_length=100)
    motivation= models.TextField()

#les services
    nom1=models.CharField(max_length=100)
    description1= models.TextField()
    image1= models.ImageField(upload_to='images/Service/')

    nom2 = models.CharField(max_length=100)
    description2 = models.TextField()
    image2 = models.ImageField(upload_to='images/Service/')

    nom3 = models.CharField(max_length=100)
    description3 = models.TextField()
    image3 = models.ImageField(upload_to='images/Service/')

    nom4 = models.CharField(max_length=100)
    description4 = models.TextField()
    image4 = models.ImageField(upload_to='images/Service/')

    nom5 = models.CharField(max_length=100)
    description5 = models.TextField()
    image5 = models.ImageField(upload_to='images/Service/')

    nom6 = models.CharField(max_length=100)
    description6 = models.TextField()
    image6 = models.ImageField(upload_to='images/Service/')

#Bouton
    bouton=models.CharField(max_length=100)
    class Meta:
        db_table ="service"

    def __str__(self):
        return f"{self.titre} {self.sousTitre1} {self.sousTitre2} {self.motivation} {self.nom1} {self.description1} {self.image1} {self.nom2} {self.description2} {self.image2} {self.nom3} {self.description3} {self.image3} {self.nom4} {self.description4} {self.image4} {self.nom5} {self.description5} {self.image5} {self.nom6} {self.description6} {self.image6} {self.bouton}"


class Feature(models.Model):
    image = models.ImageField(upload_to='images/Feature/')
    titre = models.CharField(max_length=100)
    sousTitre1 = models.CharField(max_length=100)
    sousTitre2 = models.CharField(max_length=100)
    description = models.TextField()

#section debaler
    titre1= models.CharField(max_length=100)
    description1= models.TextField()
    titre2= models.CharField(max_length=100)
    description2= models.TextField()
    titre3 = models.CharField(max_length=100)
    description3= models.TextField()
    class Meta:
        db_table = 'feature'
    def __str__(self):
        return f"{self.titre} {self.sousTitre1} {self.sousTitre2} {self.description} {self.titre1} {self.description1} {self.titre2}  {self.description2} {self.titre3} {self.description3} "


class Parallax(models.Model):
      titre = models.CharField(max_length=100)
      sousTitre = models.CharField(max_length=100)
      description = models.TextField()
      message=models.CharField(max_length=100)
      numero=models.CharField(max_length=100)
      class Meta:
        db_table = 'parallax'
      def __str__(self):
          return f"{self.titre} {self.sousTitre} {self.message} {self.numero}"


class Portfolio(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=100)
    motivation= models.TextField()
    categorie1= models.CharField(max_length=100)
    categorie2= models.CharField(max_length=100)
    categorie3= models.CharField(max_length=100)
    categorie4= models.CharField(max_length=100)
    categorie5= models.CharField(max_length=100)

#Aire plane image (Cat3)
    aireplane1=models.ImageField(upload_to='images/Portfolio/Aireplan/')
    aireplane2= models.ImageField(upload_to='images/Portfolio/Aireplan/')
    aireplane3= models.ImageField(upload_to='images/Portfolio/Aireplan/')
    aireplane4= models.ImageField(upload_to='images/Portfolio/Aireplan/')

#Maritime (cat4)
    maritime1=models.ImageField(upload_to='images/Portfolio/Maritime/')
    maritime2= models.ImageField(upload_to='images/Portfolio/Maritime/')
    maritime3= models.ImageField(upload_to='images/Portfolio/Maritime/')
    maritime4= models.ImageField(upload_to='images/Portfolio/Maritime/')

#Road & truck (2)
    roadtruck1=models.ImageField(upload_to='images/Portfolio/RoadTruck/')
    roadtruck2= models.ImageField(upload_to='images/Portfolio/RoadTruck/')
    roadtruck3= models.ImageField(upload_to='images/Portfolio/RoadTruck/')
    roadtruck4= models.ImageField(upload_to='images/Portfolio/RoadTruck/')

#videos (cat5)
    video1=models.FileField(upload_to='images/Portfolio/Video/')
    video2= models.FileField(upload_to='images/Portfolio/Video/')
    video3= models.FileField(upload_to='images/Portfolio/Video/')
    video4= models.FileField(upload_to='images/Portfolio/Video/')
    class Meta:
        db_table = 'portfolio'
    def __str__(self):
        return f"{self.titre} {self.sousTitre} {self.motivation} {self.categorie1} {self.categorie2} {self.categorie3} {self.categorie4} "

class Team(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=100)
    motivation= models.TextField()

    photo1= models.ImageField(upload_to='images/Team/membre1')
    prenom1=models.CharField(max_length=100)
    role1=models.CharField(max_length=100)

    photo2= models.ImageField(upload_to='images/Team/membre2')
    prenom2= models.CharField(max_length=100)
    role2=models.CharField(max_length=100)

    photo3= models.ImageField(upload_to='images/Team/membre3')
    prenom3= models.CharField(max_length=100)
    role3= models.CharField(max_length=100)

    photo4= models.ImageField(upload_to='images/Team/membre4')
    prenom4= models.CharField(max_length=100)
    role4= models.CharField(max_length=100)

    photo5= models.ImageField(upload_to='images/Team/membre5')
    prenom5= models.CharField(max_length=100)
    role5= models.CharField(max_length=100)
    class Meta:
        db_table = 'team'
    def __str__(self):
        return f"{self.titre} {self.sousTitre} {self.motivation} {self.prenom1} {self.prenom2} {self.prenom3}  "




class Pricing(models.Model):
      titre = models.CharField(max_length=100)
      sousTitre = models.CharField(max_length=100)
      motivation= models.TextField()
      par=models.CharField(max_length=100)
      avantage=models.TextField()
      utilisateur=models.CharField(max_length=100)
      temps=models.TextField(max_length=100)
      discution=models.CharField(max_length=100)
      bouton=models.CharField(max_length=100)

      niveau1=models.CharField(max_length=100)
      prix1=models.CharField(max_length=100)
      nombre_projet1=models.CharField(max_length=100)
      espace1=models.CharField(max_length=100)
      securite = models.CharField(max_length=100)

      niveau2= models.CharField(max_length=100)
      prix2 = models.CharField(max_length=100)
      nombre_projet2 = models.CharField(max_length=100)
      espace2 = models.CharField(max_length=100)



      niveau3= models.CharField(max_length=100)

      prix3 = models.CharField(max_length=100)
      nombre_projet3 = models.CharField(max_length=100)
      espace3 = models.CharField(max_length=100)
      class Meta:
        db_table = 'pricing'
      def __str__(self):
          return f"{self.titre} {self.sousTitre} {self.motivation} {self.par} {self.avantage} {self.utilisateur} {self.temps} {self.discution} {self.bouton}"


class Blogaccueil(models.Model):
      titre = models.CharField(max_length=100)
      sousTitre = models.CharField(max_length=100)
      motivation= models.TextField()
      vers = models.CharField(max_length=100)

#blog 1
      image1=models.ImageField(upload_to='images/Blogaccueil/blog1/')
      nom1= models.CharField(max_length=200)
      contenu1= models.TextField()
      auteur1= models.CharField(max_length=100)
      date1= models.DateField(auto_now_add=True)
      nombre_commentaire1= models.CharField(max_length=100)
      nombre_vue1= models.CharField(max_length=100)

# blog 2
      image2 = models.ImageField(upload_to='images/Blogaccueil/blog2/')
      nom2= models.CharField(max_length=200)
      contenu2 = models.TextField()
      auteur2 = models.CharField(max_length=100)
      date2 = models.DateField(auto_now_add=True)
      nombre_commentaire2 = models.CharField(max_length=100)
      nombre_vue2 = models.CharField(max_length=100)

# blog 3
      image3 = models.ImageField(upload_to='images/Blogaccueil/blog3/')
      nom3= models.CharField(max_length=200)
      contenu3 = models.TextField()
      auteur3 = models.CharField(max_length=100)
      date3 = models.DateField(auto_now_add=True)
      nombre_commentaire3 = models.CharField(max_length=100)
      nombre_vue3 = models.CharField(max_length=100)
      class Meta:
          db_table = 'blogaccueil'
      def __str__(self):
          return f"{self.titre} {self.sousTitre} {self.motivation}"




class Testimonial(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images/Testimonial/')

#Temoignage1
    image1=models.ImageField(upload_to='images/Testimonial1/')
    client1= models.CharField(max_length=200)
    provenance1= models.CharField(max_length=100)
    temoignage1= models.CharField(max_length=500)
# Temoignage1
    image2= models.ImageField(upload_to='images/Testimonial2/')
    client2= models.CharField(max_length=200)
    provenance2= models.CharField(max_length=100)
    temoignage2= models.CharField(max_length=500)

# Temoignage3
    image3= models.ImageField(upload_to='images/Testimonial3/')
    client3= models.CharField(max_length=200)
    provenance3= models.CharField(max_length=100)
    temoignage3= models.CharField(max_length=500)
    class Meta:
        db_table = 'testimonial'
    def __str__(self):
        return f"{self.titre} {self.sousTitre} {self.client1} {self.provenance1} {self.temoignage1} {self.client2} {self.provenance2} {self.temoignage2} {self.client3} {self.provenance3} {self.temoignage3}"


class Client(models.Model):
     titre = models.CharField(max_length=100)
     sousTitre = models.CharField(max_length=100)
     photo1=models.ImageField(upload_to='images/Client/')
     photo2= models.ImageField(upload_to='images/Client/')
     photo3= models.ImageField(upload_to='images/Client/')
     photo4= models.ImageField(upload_to='images/Client/')
     photo5= models.ImageField(upload_to='images/Client/')
     photo6= models.ImageField(upload_to='images/Client/')
     photo7= models.ImageField(upload_to='images/Client/')
     photo8= models.ImageField(upload_to='images/Client/')

     class Meta:
         db_table = 'client'

     def __str__(self):
         return f"{self.titre} {self.sousTitre}"
class Video(models.Model):
    video= models.FileField(upload_to='Video/video/')
    class Meta:
        db_table = 'video'
    def __str__(self):
        return f"{self.video}"



class Join(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=100)
    motivation= models.TextField()
    bouton = models.CharField(max_length=100)
    class Meta:
        db_table = 'join'
    def __str__(self):
        return f"{self.titre} {self.sousTitre} {self.motivation} {self.bouton}"



############################################################FIN DE INDEX####################################################################################################################################"

class Banner(models.Model):
    page = models.CharField(max_length=100)   # nom de la page (ex: "about", "services")
    titre = models.CharField(max_length=200)  # titre principal du banner
    nom = models.CharField(max_length=200)  # sous-titre ou texte secondaire

    class Meta:
        db_table = "banner"

    def __str__(self):
        return f"{self.page} {self.titre} "


class Servicedetail(models.Model):
      service1=models.CharField(max_length=100)
      service2=models.CharField(max_length=100)
      service3 = models.CharField(max_length=100)
      service4 = models.CharField(max_length=100)
      service5 = models.CharField(max_length=100)
      service6 = models.CharField(max_length=100)

      conseilImage=models.ImageField(upload_to='images/Servicedetail/')
      nomservice= models.CharField(max_length=100)
      numero=models.CharField(max_length=100)

      sousTitr1 = models.CharField(max_length=100)
      description1 = models.CharField(max_length=100)
      Image=models.ImageField(upload_to='images/Servicedetail/')
      explication=models.TextField()

      sousTitr2 = models.CharField(max_length=100)
      description2 = models.CharField(max_length=100)

      block1=models.CharField(max_length=100)
      contenu1=models.TextField()
      block2=models.CharField(max_length=100)
      contenu2= models.TextField()
      block3= models.CharField(max_length=100)
      contenu3= models.TextField()

      sousTitr3 = models.CharField(max_length=100)
      descript1 = models.CharField(max_length=400)
      descript2 = models.CharField(max_length=400)

      ligne1=models.CharField(max_length=100)
      ligne2= models.CharField(max_length=100)
      ligne3= models.CharField(max_length=100)
      ligne4= models.CharField(max_length=100)
      ligne5= models.CharField(max_length=100)
      sousligne1= models.CharField(max_length=100)
      sousligne2= models.CharField(max_length=100)
      sousligne3= models.CharField(max_length=100)

      ligne6= models.CharField(max_length=100)
      class Meta:
          db_table = 'servicedetail'

      def __str__(self):
          return f"{self.service1} {self.service2} {self.service3} {self.service4} {self.service5} {self.service6} {self.conseilImage} {self.nomservice} {self.numero} {self.sousTitr1} {self.description1} {self.Image} {self.explication} {self.sousTitr2} {self.description2} {self.block1} {self.contenu1} {self.block2} {self.contenu2} {self.block3} {self.contenu3} {self.sousTitr3} {self.descript1} {self.descript2} {self.ligne1} {self.ligne2} {self.ligne3} {self.ligne4} {self.ligne5} {self.sousligne1} {self.sousligne2} {self.sousligne3} {self.ligne6}"


class Blog(models.Model):
    image1=models.ImageField(upload_to='images/Blog/')
    blog1=models.CharField(max_length=100)
    titre1= models.CharField(max_length=100)
    contenu1= models.TextField()
    auteur1= models.CharField(max_length=100)
    date1= models.DateField(auto_now_add=True)
    nombre_commentaire1=models.IntegerField()
    nombre_vue1= models.CharField(max_length=100)

    image2= models.ImageField(upload_to='images/Blog/')
    blog2= models.CharField(max_length=100)
    titre2= models.CharField(max_length=100)
    contenu2= models.TextField()
    auteur2= models.CharField(max_length=100)
    date2= models.DateField(auto_now_add=True)
    nombre_commentaire2= models.IntegerField()
    nombre_vue2= models.CharField(max_length=100)

    image3= models.ImageField(upload_to='images/Blog/')
    blog3= models.CharField(max_length=100)
    titre3= models.CharField(max_length=100)
    contenu3= models.TextField()
    auteur3= models.CharField(max_length=100)
    date3= models.DateField(auto_now_add=True)
    nombre_commentaire3= models.IntegerField()
    nombre_vue3= models.CharField(max_length=100)

    image4= models.ImageField(upload_to='images/Blog/')
    blog4= models.CharField(max_length=100)
    titre4= models.CharField(max_length=100)
    contenu4= models.TextField()
    auteur4= models.CharField(max_length=100)
    nombre_commentaire4= models.IntegerField()
    nombre_vue4= models.CharField(max_length=100)












