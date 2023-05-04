import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Postavke e-pošte
FROM_EMAIL = 'urosriznic@yahoo.com'
FROM_PASSWORD = 'password'
TO_EMAIL = 'urosriznic@yahoo.com'
SUBJECT = 'Filmovi'
HTML_FILE = 'index.html'
IMAGE_FILES = ['top_10_most_expensive_movies.png', 'most_common_actors.png']

# Čitanje HTML datoteke
with open(HTML_FILE, 'r') as f:
    html_content = f.read()

# Stvaranje MIMEMultipart objekta
msg = MIMEMultipart()

# Postavljanje zaglavlja e-pošte
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT

# Dodavanje HTML sadržaja u e-poštu
msg.attach(MIMEText(html_content, 'html'))

# Dodavanje slika u e-poštu
for image_file in IMAGE_FILES:
    with open(image_file, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<{}>'.format(image_file))
        msg.attach(img)

# Slanje e-pošte
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(FROM_EMAIL, FROM_PASSWORD)
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    smtp.quit()

print('E-pošta je poslana na adresu {}.'.format(TO_EMAIL))
