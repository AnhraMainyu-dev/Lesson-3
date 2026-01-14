import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_name = "Максим"
friend_name = "Иннокнетий"
link = "https://dvmn.org/profession-ref-program/maximheilelov/QvDnC/"
mail_from = "maximyandzen@yandex.ru"
mail_to = "maximheilelov@gmail.com"
subject = "Важно!"

mail = """\
From: {mailfrom}
To: {mailto}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, {name2}! {myname} приглашает тебя на сайт {link}!

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
""".format(mailfrom=mail_from, subject = subject, name2=friend_name, link=link, myname=my_name, mailto = mail_to).encode("utf-8")


server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.environ['LOGIN'], os.environ['PASSWORD'])
server.sendmail('maximyandzen@yandex.ru', 'maximheilelov@gmail.com', mail)
server.quit()



