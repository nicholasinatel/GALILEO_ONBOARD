# Uma lista de instrumentos musicais
instrumentos = ['Baixo', 'Bateria', 'Guitarra'] 
# Para cada nome na lista de instrumentos
for instrumento in instrumentos:
  print instrumento # printa todos os instrumentos


A=2
print A+2,"Sempre usar esses tracinhos que nao sei o nome"  

#!/usr/bin/env isto eh o caminho para o interpretador
#interpretador compila o codigo e armazena o bytecode em disco para nao precisa compilar novamente na proxima execucao

#Eh possivel quebrar linhas de expressoes
a=7*3+\
5/2
#Lista quebrada por vírgula
b=['a','b',
'c']
#chamada de funcao quebrada por virgula
c = range(1,
11)

#Indentacao, o padrao sao quatro espacos
#a linha anterior que tera indentacao sempre termina com :
#exemplo

for i in[234,654,378,798]: #para i indo nos valores especificos da esquerda para direita, veja o :
    if i%3==0: #resto da divisao : mais uma indentacao
        print i,'/=',i/3 #4 espacos e fim da indentacao 

temp=int(raw_input('Entre com a temperatura'))

if temp<0:
    print 'Congelando...'
elif 0 <= temp <= 20:
    print 'Frio'
elif 21<=temp<=25:
    print 'Quente'
else:
    print 'Tudo de bom pra voce'

VAR=5 if temp < 10 else 0
#Variavel recebe o valor 5 se temperatura menor que 10 senao recebe valor 0

#Continua ate o final da sequencia depois da break e executa condicao ELSE
for i in [1,2,3,4,5,6,7,8,9,10]:
    X=X+1
    continue
    break
else:
    Y=X-20

#estrutura while adequada quando nao ha como determinar quantas iteracoes vao ocorrer e nao ha sequencia a seguir
S=0
X=1
while X<100:
	S=S+X
	X=X+1
	continue
	break
else:
    W=1

 print X
    	
#Python aceita numeros de ponto flutuante e complexos
i=1
f=3.14
c=3+4j

#Python tambem aceita conversoes
#convertendo para inteiro
print int(3.14)
#convertendo de inteiro para real
print float(5)
#calculo entre inteiro e real resulta em real
print 5.0/2+3

#Printa 20 na base OITO
print "int('20',8) =",int('20',8)
#Printa 20 na base HEXADECIMAL
print "int('20',16) =",int('20',16)

#concatenacao de strings
s='Camel'
print 'The'+s+'run away!'

#Plotar caracteres em colunas, string tratada como sequencia
for ch in s: print ch
# s eh objeto string posso trabalhar orientado ao objeto
if s.startswith('C'): print s.upper()

#olha que loucura treinar ssaporra
musicos=[('Page','guitarrista','Led Zeppelin'),
('Fripp','guitarrista','King Crimson')]
msg='{0} eh {1} do {2}'
for nome,funcao,banda in musicos:
     print(msg.format(nome,funcao,banda))
