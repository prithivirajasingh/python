import imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = '#####'
password = '#####'
M.login(email, password)

M.list()
M.select('inbox')

typ, data = M.search(None, 'SUBJECT "App password - Python on my Kali"')
email_id = data[0]

result, email_data = M.fetch(email_id, '(RFC822)')
print(email_data)
print('\n')

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
        body = part.get_payload(decode=True)
        print(body)

M.logout()
