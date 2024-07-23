from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['christian.santos92@gmail.com']

        try:

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('/contact/')  # Redirecionar após envio
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=500)

    return render(request, 'homepage/send_email_form.html')