
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def index(request):
    template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    # to accept the requests from the app
    return HttpResponse(template.render({}, request))

def sendMail(request):
    try:

        sender = request.POST['sender']
        password = request.POST['password']
        receiver = request.POST['receiver']
        subject = request.POST['subject']
        content = request.POST['content']
        # print(sender, receiver, password)
        mail_content = content
        # The mail addresses and password

        # gmail
        # sender 'gtest7gtest@gmail.com'  pass '@@GtestGtest' receiver 'gtest8gtest@gmail.com'
        # app password for gtest8 pfjjsahdcnbjamle
        sender_address = sender
        sender_pass = password
        receiver_address = receiver

        # Setup the MIME
        # Multipurpose Internet Mail Extension
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = subject

        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail

        # gmail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port

        # yahoo
        # session = smtplib.SMTP('smtp.mail.yahoo.com', 587) #use gmail with port

        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        #return HttpResponseRedirect(reverse('index'))
        return HttpResponseNotFound('<h1>mail is sent Successfully</h1>')
        #return HttpResponse("<h1>Email is sent Successfully</h1><br>"+"<li><a href="+"\"{% url 'index' %}\""+">Home</a></li>")
    except Exception as e:
        print(f"Error Type: {type(e)}, Error: {e}")
        #return HttpResponseRedirect(reverse('index', args=()))
        return HttpResponseNotFound('<h1>Please check your credentials or the receiver address</h1>')
        #m = '''<li><a href="{% url 'index' %}">Home</a></li>'''
        #return HttpResponse(m)
        #return reverse("index", kwargs={"message": "Error"})
