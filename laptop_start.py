import cv2, time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase 
#to capture the image 
video = cv2.VideoCapture(0)

check, frame = video.read()

cv2.imwrite(filename="sample.jpg",img=frame)

cv2.waitKey(0)

video.release()

img = cv2.imread('sample.jpg',0)
re = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[1]/4)))
cv2.imwrite(filename="sample.jpg",img=re)

time.sleep(600)

#to send mail with image attachment
now = datetime.now()
today = datetime.today()
current_time = now.strftime("%H:%M:%S")
date = today.strftime("%d/%m/%Y")

email_sender = 'xyz@gmail.com'
email_receiver = 'xyz@gmail.com'
app_password = 'abcdefghijklmnop'

subject = "Your Machine turned ON!"
msg = MIMEMultipart()
body = "Your machine named xyz was turned on at " + current_time + ", " + date 
filename = 'sample.jpg'

attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject
msg.attach(part)

text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_sender,app_password)

#message = 'python_test'

server.sendmail(email_sender,email_receiver,text)

server.quit()