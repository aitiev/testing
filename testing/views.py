from django.core.mail import send_mail
from django.http import HttpResponse


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