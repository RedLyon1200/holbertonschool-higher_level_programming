#!/usr/bin/python3

import os

"""Se listan los archivos modificados"""
try:
    os.system('git status -s . | grep \' M \' > gitstatusM.txt')
    os.system("sed -i 's/\ M //g' gitstatusM.txt")
except Exception as ex:
    print(ex)

if os.stat("gitstatusM.txt").st_size != 0:
    f = open('gitstatusM.txt', 'r')

    print('\nComentando archivos modificados...')
    while(True):
        linea = f.readline()
        if not linea:
            break

        os.system('git add {}'.format(linea))

        print('Modificar valor del commit para {}?'.format(linea))
        res = input('0 - No\n1 - Si\nOpc: ')
        if res == '1':
            commit = input('Commit: ')
        elif res == '0':
            commit = 'file {} added'.format(linea)
        else:
            raise ValueError('Opcion inválida, debe ser 0 o 1')
            os.system('git reset HEAD *')
        os.system("git commit -m '{}'".format(commit))
    os.system('git push -u origin master')
else:
    os.remove('')
    print('No hay archivos modificados')
