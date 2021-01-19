import time

from django.core.mail import send_mail
from django.http import HttpResponse

from mail_templated import send_mail as send_mail2


def index(request):

    with open('testing/students.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            send_mail(
                'Subject',
                f'Dear participant to access the olympiad please click the following link https://zipgrade.com/s/ and \
use following credentials login:{line[0]}, password:{line[1]}',
                'studentdjango@gmail.com',
                [line[2]],
                fail_silently=False,
            )

    return HttpResponse("OK")


def index2(request):
    counter = 1
    with open('testing/students.txt', encoding='utf-8') as f, open('testing/results.txt', 'w') as g:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            send_mail2(
                'hello.tpl',
                {'login': line[0], 'password': line[1], 'name': line[3]},
                'studentdjango@gmail.com',
                [line[2]]
            )
            g.write(f'{counter} - OK\n')
            time.sleep(2)

            if counter%10 == 0:
                time.sleep(70)

            counter += 1

    return HttpResponse("OK")
