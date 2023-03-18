from utils import *

option = True
while option:
  file = input('Informe o arquivo (0 para sair): ')
  if file == '0':
    option = False
    print("Saindo...")
    break
  else:
    print("Processando...")
    read_file(file)