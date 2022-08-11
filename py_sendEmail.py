import smtplib
import email.message


def enviar_email():
  email_content = "Texto do email."
  msg = email.message.Message()
  msg['Subject'] = 'Assunto'
  msg['From'] = 'mail@domain.com'
  msg['To'] = 'destination@domain.com'
  password = 'password'
  msg.add_header('Content-Type', 'txt/html')
  msg.set_payload(email_content)

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print('Email Enviado.')


enviar_email()
