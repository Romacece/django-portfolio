from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.urls import reverse

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=100)
    greetings_1 = models.CharField(max_length=50)
    greetings_2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=100)
    career = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.skill_name

    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Portfolio {self.id}'
    
    def get_pdf_download_url(self):
        return reverse('download_pdf', args=[str(self.id)])


#CONTACT SECTION
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return "{} - {} - {}".format(self.name,self.email,self.message)