from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection
from django.conf import settings


def home(request):
    if request.method == "POST":
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = request.POST.get("email")  # Use the sender's email from the form
            recipient_list = [email_from, ]  # Use the sender's email as the recipient
            
            # Get additional form data
            name = request.POST.get("name")
            tel = request.POST.get("tel")

            # Modify the message to include name and tel
            message = f"Name: {name}\nTel: {tel}\n\n{request.POST.get('message')}"

            # Use the email_from variable for both EmailMessage and send_mail
            email = EmailMessage(subject, message, email_from, recipient_list, connection=connection)

            email.send()

    return render(request, './home/homepage.html')

