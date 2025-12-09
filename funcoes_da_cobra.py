from random import randint

alfabeto = {'p' : ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                    '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                    '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}'], 
            'o': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'n': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' +'{cor}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            't': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}','{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}'],
            's': [' {cor}  {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{cor} {limpa}  ' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}','{limpa}   {limpa}' + '  {cor} {limpa}' +'{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} '],
            '1': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}','{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '2': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ','{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '  {cor} {limpa}' + '{cor}   {limpa}' + '{cor} {limpa}  ', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  ' {cor}  {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '3': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '4': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            '5': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} '],
            '6': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '7': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            '8': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '9': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '0': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            ' ': ['{limpa}   {limpa}','{limpa}   {limpa}','{limpa}   {limpa}','{limpa}   {limpa}','{limpa}   {limpa}'],
            ':': [' {limpa}   {limpa} ', ' {cor}   {limpa} ',' {limpa}   {limpa} ', ' {cor}   {limpa} ',' {limpa}   {limpa} '],
            'a': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            'j': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}','{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}'],
            'r': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            'g': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + ' {cor}  {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'l': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'y': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}', ' {cor}  {limpa}' + '{limpa}   {limpa}' + '{cor}  {limpa} ',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}', '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}'],
            'e': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            '←': ['{limpa}   {limpa}' + '  {seta_cor} {limpa}' + '{seta_cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{seta_cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{seta_cor}   {limpa}' + '{seta_cor}   {limpa}' + '{seta_cor}   {limpa}' + '{seta_cor}   {limpa}' + '{seta_cor}   {limpa}',
                  '{limpa}   {limpa}' + '{seta_cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '  {seta_cor} {limpa}' + '{seta_cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}'],
            'i': ['{cor}   {limpa}','{limpa}   {limpa}','{cor}   {limpa}','{cor}   {limpa}','{cor}   {limpa}'],
            'm': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'], 
            'c': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'v': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}',
                  '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}'], 
            'u': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'w': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}'],
            'd': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                   '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} '],
            'b': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} ', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}  {limpa} '],
            'f' : ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}','{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                    '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}',
                    '{cor}   {limpa}' + '{limpa}   {limpa}' + '{limpa}   {limpa}'],
            'h': ['{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}'],
            'q': ['{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{cor}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{cor}   {limpa}' + '{cor}   {limpa}' + '{cor}   {limpa}', '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}',
                  '{limpa}   {limpa}' + '{limpa}   {limpa}' + '{cor}   {limpa}']}


def menu_cria(ceta_local):
      global alfabeto

      texto = ['jogar 1 player','jogar 2 player', 'controles' ,'sair']
      texto[ceta_local] += ' ←'

      texto_ten = f''

      cor_ativa = '\033[41m'

      limpa = '\033[m'

      seta_cor = '\033[44m'
      
      for cc in range(len(texto)):

            for c in texto[cc]:

                  if '←' == c:
                       texto_ten += alfabeto[c][0].replace('{cor}', cor_ativa).replace('{limpa}', limpa).replace('{seta_cor}', seta_cor) + ' '

                  else:

                        texto_ten += alfabeto[c][0].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '

            texto_ten += '\n'

            for c in texto[cc]:
                  
                  if '←' == c:
                       texto_ten += alfabeto[c][1].replace('{cor}', cor_ativa).replace('{limpa}', limpa).replace('{seta_cor}', seta_cor) + ' '

                  else:

                        texto_ten += alfabeto[c][1].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '

            texto_ten += '\n'

            for c in texto[cc]:
                  
                  if '←' == c:
                       texto_ten += alfabeto[c][2].replace('{cor}', cor_ativa).replace('{limpa}', limpa).replace('{seta_cor}', seta_cor) + ' '

                  else:

                        texto_ten += alfabeto[c][2].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '

            texto_ten += '\n'

            for c in texto[cc]:
                  
                  if '←' == c:
                       texto_ten += alfabeto[c][3].replace('{cor}', cor_ativa).replace('{limpa}', limpa).replace('{seta_cor}', seta_cor) + ' '

                  else:

                        texto_ten += alfabeto[c][3].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '

            texto_ten += '\n'

            for c in texto[cc]:
                  
                  if '←' == c:
                       texto_ten += alfabeto[c][4].replace('{cor}', cor_ativa).replace('{limpa}', limpa).replace('{seta_cor}', seta_cor) + ' '

                  else:

                        texto_ten += alfabeto[c][4].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '

            texto_ten += '\n'
            texto_ten += '\n'

      return texto_ten


def pontuação1(pontos):
      global alfabeto

      cor_ativa = '\033[41m'

      limpa = '\033[m'

      texto = 'pontos:' + str(pontos)
      texto_ten = f''

      for c in texto:
            texto_ten += alfabeto[c][0].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'

      for c in texto:
            texto_ten += alfabeto[c][1].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'

      for c in texto:
        texto_ten += alfabeto[c][2].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'

      for c in texto:
        texto_ten += alfabeto[c][3].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'

      for c in texto:
            texto_ten += alfabeto[c][4].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'

      return texto_ten

def pontuação2(pontos1, pontos2):
      global alfabeto, cor

      texto = 'p1:' + str(pontos1) + ' p2:' + str(pontos2)
      texto_ten = f''

      cor_ativa = '\033[41m'

      limpa = '\033[m'

      divisa = len(str('p1:' + str(pontos1)))


      contador = 0

      for c in texto:
            contador += 1
            if contador == divisa + 1:
                 cor_ativa = '\033[42m'

            texto_ten += alfabeto[c][0].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'
      cor_ativa = '\033[41m'

      limpa = '\033[m'
      contador = 0

      for c in texto:
            contador += 1
            if contador == divisa + 1:
                 cor_ativa = '\033[42m'

            texto_ten += alfabeto[c][1].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'
      cor_ativa = '\033[41m'

      limpa = '\033[m'
      contador = 0
      
      for c in texto:
            contador += 1
            if contador == divisa + 1:
                 cor_ativa = '\033[42m'

            texto_ten += alfabeto[c][2].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'
      cor_ativa = '\033[41m'

      limpa = '\033[m'
      contador = 0

      for c in texto:
            contador += 1
            if contador == divisa + 1:
                 cor_ativa = '\033[42m'

            texto_ten += alfabeto[c][3].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'
      cor_ativa = '\033[41m'

      limpa = '\033[m'
      contador = 0

      for c in texto:
            contador += 1
            if contador == divisa + 1:
                 cor_ativa = '\033[42m'

            texto_ten += alfabeto[c][4].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
      texto_ten += '\n'
      cor_ativa = '\033[41m'

      limpa = '\033[m'
      contador = 0

      return texto_ten

def controles():
      global alfabeto

      texto = ['p1 move: cetas','p2 move: wasd','enter: sai jogo e aqui', 'esc: fecha tudo']

      cor_ativa = '\033[41m'

      limpa = '\033[m'

      texto_ten = f''

      for cc in texto:

            for c in cc:
                  texto_ten += alfabeto[c][0].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
            texto_ten += '\n'

            for c in cc:
                  texto_ten += alfabeto[c][1].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
            texto_ten += '\n'

            for c in cc:
                  texto_ten += alfabeto[c][2].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
            texto_ten += '\n'

            for c in cc:
                  texto_ten += alfabeto[c][3].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
            texto_ten += '\n'

            for c in cc:
                  texto_ten += alfabeto[c][4].replace('{cor}', cor_ativa).replace('{limpa}', limpa) + ' '
            texto_ten += '\n' + '\n' +'\n'

      return texto_ten
      


