import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from comm import Log


log = Log.Log()
logger = log.get_logger()

def send_email(result_report):
    with open(result_report,'r',encoding='utf-8')as f:
        mail_body = f.read()

    sender = 'lzy972296345@163.com' #发件人
    receiver = ['972296345@qq.com','1141347750@qq.com']
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = Header('测试人员','utf-8')
    mail_server = 'smtp.163.com'
    subject = '自动化测试报告'
    message['Subject'] = Header(subject, charset='utf-8')

    #邮件正文
    message.attach(MIMEText('自动化测试报告，请查收！','plain','utf-8'))

    #构造附件
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="report.html"'
    message.attach(att)

    user_name = 'lzy972296345@163.com' #邮箱名邮箱密码
    passwd = 'Aa123456'

    #邮箱登录
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(user_name,passwd)
    #发送邮件
    for i in receiver:
        smtp.sendmail(sender,str(i),message.as_string())
        logger.info('邮箱：'+i+',发送邮件成功! \n')
    smtp.quit()