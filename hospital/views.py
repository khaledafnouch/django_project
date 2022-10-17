from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .models import Produits
from django.core.paginator import Paginator
from .forms import ContactForm
from django.utils.translation import gettext as _

# Create your views here.
def index(responce):
  return render(responce, 'hospital/index.html')
  
  
def produits(request):
	allproduit = Produits.objects.all()
	item_name = request.GET.get('item-name')
	if item_name != '' and item_name is not None:
		allproduit = Produits.objects.filter(title__icontains =item_name)
	paginator = Paginator(allproduit,4)
	page = request.GET.get('page')
	allproduit = paginator.get_page(page)  
	return render(request, 'hospital/produits.html', {'allproduit':allproduit})
	
def detail(request, pk):
	allproduit = Produits.objects.get(id=pk)  
	return render(request, 'hospital/detail.html', {'produit':allproduit}) 
  
  
  
  
def contact(request):
  form = ContactForm(request.POST or None)
  if request.method == 'POST':
      form = ContactForm(request.POST)
  if form.is_valid():
			subject = "rendez-vous" 
			body = {
			'name': form.cleaned_data['name'], 
			'subject': form.cleaned_data['subject'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'khaledafnouch@gmail.com', ['khaledafnouch@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			
      
  form = ContactForm()
  return render(request,'hospital/contact.html')
  
  
  
def services(responce):
  return render(responce,'hospital/services.html')
  
  
  
  
def about(responce):
  return render(responce,'hospital/about.html')