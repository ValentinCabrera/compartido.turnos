from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
from threading import Thread

def async_email(**kwargs):
    t = Thread(target=handle_send_email, kwargs=kwargs)
    t.start()

def get_message(subject, context):
    message = f"""
         <!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title>{subject}</title>
             <style>
                 body {{
                     font-family: 'Arial', sans-serif;
                     background-color: #f2f2f2;
                     color: #333;
                     margin: 20px;
                 }}
                 p {{
                     font-size: 18px;
                     line-height: 1.6;
                     color: #555;
                 }}
                 h1 {{
                     color: #e74c3c;
                 }}
                 .button-container {{
                     margin-top: 15px;
                 }}
                 .button {{
                     display: inline-block;
                     padding: 10px 20px;
                     font-size: 16px;
                     color: #fff;
                     text-decoration: none;
                     background-color: #3498db;
                     border-radius: 5px;
                     transition: background-color 0.3s;
                 }}
                 .button:hover {{
                     background-color: #258cd1;
                 }}
             </style>
         </head>
         <body>
             <h1>¡Hola, {context['name']}!</h1>
             <p>Estas a un paso de ser parte de TurnosTomiVale. Haz click para verificar el mail:</p>
             <div class="button-container">
                 <a class="button" href="{context['url']}">Verificar</a>
                 <p>{context["token"]}</p>
             </div>
             <p>¡Esperamos que disfrutes de la experiencia!</p>
             <p>Saludos,<br>El equipo de TurnosTomiVale</p>
         </body>
         </html>
     """
    return message
def handle_send_email(subject, recipient_list, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message_html = get_message(subject, context)

    send_mail(
        subject,
        strip_tags(message_html),
        from_email,
        recipient_list,
        html_message=message_html,
        fail_silently=False,
    )
