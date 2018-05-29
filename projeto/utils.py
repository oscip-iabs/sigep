# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

import django
import datetime
import random

from projeto.models import Projeto

def random_gen_key():
    newkey = random.randrange(1000, 9999)

    return newkey


def generate_project_key():
    nextkey = random_gen_key()
    existingkey = len(Projeto.objects.filter(chave=nextkey))
    if existingkey == 0:
        return nextkey
    else:
        generate_project_key()