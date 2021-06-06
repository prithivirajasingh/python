import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email = '#####'
password = '#####'
smtp_object.login(email, password)

from_address = email
to_address = email

subject = 'Hi1'
body = 'Bye1'
message = 'Subject: {}\n{}'.format(subject,body)

smtp_object.sendmail(from_address, to_address, message)
smtp_object.quit()
