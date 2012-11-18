# -*- coding: utf-8 -*-
# импортируем библиотеку для работы с
# временем и датой.
from django.utils import timezone
# и функцию, которая посылает HTTP
# ответ в браузер.
from django.http import HttpResponse

# функция index принимает аргумент request
# из него извлекаются многие нужные данные,
# например, текущий URL или POST данные
def index(request):
    # теперь просто вернем Response с текстом.
    return HttpResponse("Сейчас %s" % timezone.now())
