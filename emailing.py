from PIL import Image
import smtplib
from email.message import EmailMessage

password = "zmovcfqldcaytwnf"
SENDER = "albertobarbanog@gmail.com"
RECEIVER = "albertobarbanog@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()

    # Use Pillow to determine the image subtype
    image = Image.open(image_path)
    image_subtype = image.format.lower()

    email_message.add_attachment(content, maintype='image', subtype=image_subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, password)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/23.png")
