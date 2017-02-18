from django.shortcuts import render

from django.conf import settings

from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from .forms import ContactForm

def contact(request):
	company_info = CompanyInfo.objects.first()
	form = ContactForm
	if request.method == 'POST':
		form = form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				settings.EMAIL_MAIN,
				['sare117@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			messages.success(request, 'Email sent!')
			return redirect('contact')

	return render(request, 'home/contact.html', {
		'company_info': company_info,
		'form': form,
    })