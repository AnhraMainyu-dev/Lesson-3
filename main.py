import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

sender_name = "Максим"
recipient_name = "Иннокнетий"
link = "https://dvmn.org/profession-ref-program/maximheilelov/QvDnC/"
mail_from = "maximyandzen@yandex.ru"
mail_to = "maximheilelov@gmail.com"
subject = "Важно!"
sender_email = "maximyandzen@yandex.ru"
recipient_email = "maximheilelov@gmail.com"

mail = """\
From: {mail_from}
To: {mail_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, {recipient_name}! {sender_name} приглашает тебя на сайт {link}!

{link} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {link}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {link}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
""".format(mail_from=mail_from, subject = subject, recipient_name=recipient_name, link=link, sender_name=sender_name, mail_to = mail_to).encode("utf-8")


server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.environ['LOGIN'], os.environ['PASSWORD'])
server.sendmail(sender_email, recipient_email, mail)
server.quit()




