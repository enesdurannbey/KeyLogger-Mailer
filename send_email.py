import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	sender_email = "enter sender mail here"#your mail
	password = "enter sender mail password here"#your password
	receiver_email = "enter receiver mail here"#receiver mail 

	ssl_context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,smtp_port)
	    server.ehlo()
	    server.starttls(context=ssl_context)
	    server.ehlo()
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)

#Err
	except Exception as d:
	    print(d)
	finally:
	    server.quit()


#SMTP mail sender by Enes Duran #
