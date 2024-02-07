from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import View
from .forms import ContactForm
from .models import Home, About, Profile, Category, Skills, Portfolio

class DownloadPDFView(View):
        def get(self, request, *args, **kwargs):
            portfolio = get_object_or_404(Portfolio, id=kwargs['portfolio_id'])
            pdf_path = portfolio.link.path
            return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

download_pdf = DownloadPDFView.as_view()


def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    success_message = None

    if request.method == 'POST':
        # Gérer la soumission du formulaire ici
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Enregistrement réussi!'
            return HttpResponseRedirect( '?success_message=' + success_message)
    else:
        form = ContactForm()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'contact_form': form,
        'success_message': success_message,
    }

    
    return render(request, 'index.html', context)

    





    
