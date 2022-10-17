from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	subject= forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)

	def __str__(self):
		return self.name