# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

import django
from datetime import datetime
import random
from django.db.models import Max

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


def generate_protocolo(projeto_protocolo):
    max_protocolo = Projeto.objects.filter(ano_protocolo=datetime.now().year).aggregate(Max('num_protocolo'))
    last_protocolo = max_protocolo.get('num_protocolo__max')

    if last_protocolo == None:
        new_protocolo = 1
    else:
        new_protocolo = (int(last_protocolo) + 1)

    full_protocolo = '%s/%s' % (str(new_protocolo).rjust(4, '0'), datetime.now().year)

    Projeto.objects.filter(id=projeto_protocolo.id).update(num_protocolo=new_protocolo,
                                                           ano_protocolo=datetime.now().year, protocolo=full_protocolo)

    return full_protocolo

