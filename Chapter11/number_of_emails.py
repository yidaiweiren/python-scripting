import poplib, getpass

# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'

username = 'Email地址'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())

email_obj.user(username)
email_obj.pass_(password)
email_stat = email_obj.stat()
print("New arrived emails are : %s (%s bytes)" % email_stat) 
