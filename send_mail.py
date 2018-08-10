import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_course.settings'

if __name__ == '__main__':

    send_mail(
        '来自Joe的测试邮件',
        '我就是想发个邮件',
        'a422816722@sina.com',
        ['422816722@qq.com'],
    )