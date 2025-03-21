# ================
# CRIANDO UMA STRING
## Para criar uma string você pode usar aspas simples ou duplas.

print('olá, mundo')

#quebra de linha (\n)
print('testando\nstring\nem\npython')


##========================
## INDEXAÇÃO DE STRINGS


#Atribuindo uma string a uma variável

s='Data Science Academy'
print(s)

# indexação começa por 0

print(s[0]) # indicará o primeiro caracter da string s ('D')
print(s[1]) # indicará o segundo caracter da string s ('A')
print(s[2]) # indicará o terceiro caracter da string s ('T')
print(s[3]) # indicará o quarto caracter da string s ('A')
print(s[4]) # indicará o quinto caracter da string s (' ')*ESPAÇO


## Podemos usar ":" para executar um slicing que faz a leitura de tudo até um ponto designado.

print (s[:3]) # retorana tudo até a posição 3
print (s[1:]) # retorna tudo a partir da indexação ne número 1
print (s[1:5]) # retorna os valores da posição 1 té a posição 5 (porém não é retornado a posição final, é um número exclusivo)



###===============================================
## FUNÇÕES BUILT-IN DE STRINGS

s.upper()
s.lower()
s.split()
s.split('a')


## COMPARAÇÃO DE STRINGS
print ("python"=="R") # dois sinais "==" representa a igualdade
print('python'=='python')
