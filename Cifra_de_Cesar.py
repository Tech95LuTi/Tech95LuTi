alfabeto='abcdefghijklmnopqrstuvwxyz'

texto=input('digite o texto:')

chave=int(input('digite o valor da chave numérica:'))

opcao=input('escolha a opção --> C - para cifrar ou D - para decifrar:')


if opcao.upper()=='C':
  x='mensagem cifrada'
  resposta=x
  m=''
  for c in texto:
     if c in alfabeto:
        ind=alfabeto.index(c)
        m+=alfabeto[(ind+chave)%len(alfabeto)]
     else:
        m+=c
elif opcao.upper()=='D':
  x='mensagem decifrada'
  resposta=x
  m=''
  for c in texto:
     if c in alfabeto:
        ind=alfabeto.index(c)
        m+=alfabeto[(ind-chave)%len(alfabeto)]
     else:
        m+=c
        
        
print('{} --> {}'.format(x,m))
