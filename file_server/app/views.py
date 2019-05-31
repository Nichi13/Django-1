import datetime
from django.conf import settings
from django.shortcuts import render
import os

def file_list(request):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    f = os.listdir('files')
    info = os.stat('files\\%s' % f[0])
    t_make = info.st_ctime
    t_remake = info.st_mtime
    ctime =(datetime.datetime.fromtimestamp(t_make))
    mtime =(datetime.datetime.fromtimestamp(t_remake))
    context = {
        'files': [
            {'name': f[0]}]
        #      'ctime': ctime,
        #      'mtime': mtime}],
        # 'date': ctime # Я так понимаю тут ошибка вылетает:
        #Reverse for 'file_list' with keyword arguments '{'date': datetime.datetime(2018, 1, 2, 0, 0)}' not found. 1 pattern(s) tried: ['$']
        # я так понимаю я в url не определил дату, но я немного не понимаю где она там нужна
    }
    return render(request, template_name, context)


def file_content(request, name='server.01'):
    f = os.listdir('files')
    q = settings.FILES_PATH
    text_str = ''
    fi = open('%s\\%s' % (q, f[0]), 'r')
    for line in fi:
        text_str += line
    return render(
        request,
        'file_content.html',
        context={'file_name': f[0], 'file_content': text_str}
    )

