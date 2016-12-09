import smtplib
def maillogin_163(username,password,url):
    smtp_host = "smtp.163.com"
    smtp_port = "25"
    smtp_user = username
    smtp_pass = password
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_host,smtp_port)
        smtp.login(smtp_user,smtp_pass)
        print 'Analysis :' + url
        print 'Loading 163mail Module'
        print smtp_user+':'+smtp_pass+'  Login OK!'
    except Exception:
        pass
def maillogin_qq(username,password,url):
    smtp_host = "smtp.qq.com"
    smtp_port = "25"
    smtp_user = username
    smtp_pass = password
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_host,smtp_port)
        smtp.login(smtp_user,smtp_pass)
        print 'Analysis :' + url
        print 'Loading qq mail Module'
        print smtp_user+':'+smtp_pass+'  Login OK!'
    except Exception:
        pass
def maillogin_sina(username,password,url):
    smtp_host = "smtp.sina.com"
    smtp_port = "25"
    smtp_user = username
    smtp_pass = password
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_host,smtp_port)
        smtp.login(smtp_user,smtp_pass)
        print 'Analysis :' + url
        print 'Loading Sina mail Module'
        print smtp_user+':'+smtp_pass+'  Login OK!'
    except Exception:
        pass
def maillogin_126(username,password,url):
    smtp_host = "smtp.126.com"
    smtp_port = "25"
    smtp_user = username
    smtp_pass = password
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_host,smtp_port)
        smtp.login(smtp_user,smtp_pass)
        print 'Analysis :' + url
        print 'Loading 126 mail Module'
        print smtp_user+':'+smtp_pass+'  Login OK!'
    except Exception:
        pass