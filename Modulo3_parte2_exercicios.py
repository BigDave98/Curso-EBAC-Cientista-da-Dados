#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# # 1) Alturas
# i. No trecho de código abaixo, crie um ndarray chamado altura_em_centimetros transformando a lista lista_de_alturas em um ndarray do numpy com a função np.array()
# 
# ii. Crie um outro objeto altura em metros, com os valores de altura_em_centimetros convertidos para metros.

# In[20]:


#i:

lista_de_alturas = np.array((range(170, 191, 5)))
altura_em_centimetros = lista_de_alturas
altura_em_centimetros


# In[21]:


#ii:

altura_em_metros=altura_em_centimetros/100
altura_em_metros


# # 2) IMC
# i. Considere que pesos em Kg dessas pessoas, na mesma ordem, estão na lista pesos lista_pesos = [70, 75, 80, 85]. Crie um ndarray chamado pesos com a função np.array() que contenha esses valores.
# 
# ii. Utilizando o objeto que contém as alturas em metros e esse objeto que contém os respectivos pesos em quilos, calcule o IMC desses indivíduos utilizando a aritmética de arrays e guarde os resultados em um objeto chamado imc.

# In[38]:


from numpy import *
pesos=np.array((range(70, 90, 5)))
pesos
lista_imc=[]

for i in range (len(pesos)):
    imc = pesos[i]/(altura_em_metros[i]*altura_em_metros[i])
    lista_imc.append(imc)

array_imc= np.array(lista_imc)
array_imc


# ### 3) Endividamento
# 
# Cálculos de novas variáveis como endividamento total e comprometimento de renda são essenciais para a construção de modelos financeiros em ciência de dados. Áreas não financeiras terão cálculos semelhantes também. Vamos praticar:
# 
# Considere que o seguinte ndarray contém os dados de 4 pessoas, total a ser pago a empréstimos mensalmente e renda familiar:
# 
# | custo fixo | dívida financeira | renda familiar |
# |:----:|:----:|:---|
# | 3000  | 1000 | 6000 |
# | 2500  | 2500 | 5500 |
# | 1000  | 3000 | 7000 |
# | 10000 | 5000 | 16000 |
# 
# i. Transforme a lista de listas ```dados_financeiros``` no ndarray ```nd_financeiros```.
# > ``` dados_financeiros[[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]] ```
# 
# ii. Utilize o método ```.transpose ``` e certifique-se de que esse ndarray tenha uma linha por indivíduo e uma coluna por informação. Utilizando a indexação do numpy, imprima no output a segunda linha do array, depois a segunda coluna.
# 
# iii. Pratique aritmética com ndarrays e calcule o endividamento total como:
# $$endividamento\hspace{.2cm}total = \frac{custo \hspace{.2cm}fixo + dívida\hspace{.2cm}financeira}{renda\hspace{.2cm}familiar}$$
# Guarde os resultados em uma variável chamada ```endividamento_total``` e verifique os resultados imprimindo o conteúdo dessa variável no output.
# 
# iv. Considere que há um erro de digitação que precisa ser corrigido: 3o indivíduo na verdade não possui renda familiar de R\\$7.000,00, mas sim R\\$ 10.000,00. Corrija esse valor e refaça os cálculos.

# In[147]:


#i:

dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]
nd_financeiros = np.array(dados_financeiros)
nd_financeiros



# In[148]:


#ii:

nd_financeiros.transpose()
print(nd_financeiros)


# In[149]:


#iii:

for i in range(0, len(nd_financeiros)):
    custo_fixo = nd_financeiros[0]
    divida_financeira = nd_financeiros[i-1]
    renda_familiar = nd_financeiros[i]

def endividamento(custo_fixo, divida_financeira, renda_familiar):
    for x in range(len(custo_fixo),): 
        endividamento_total = (custo_fixo[x] + divida_financeira[x])/renda_familiar[x]
        print(endividamento_total)
    
endividamento(custo_fixo, divida_financeira, renda_familiar) 


# In[151]:


#iv:

renda_familiar[2]=10000
endividamento(custo_fixo, divida_financeira, renda_familiar) 


# 4) É muito comum precisarmos identificar valores especiais e darmos tratamento a eles quer seja alterando-os quer seja descartando-os.
# O trecho de código abaixo gera um ndarray com números pseudo aleatórios. Considere que para efeitos do estudo que virá, devemos desconsiderar valores iguais a zero. Sendo assim:
# 
# i) crie um objeto bool_zero que traga uma sequencia de booleanos do mesmo tamanho que o objeto poi, e que vale True quando o valor de poi é zero, e False caso contrário.
# 
# ii) Conte quantos valores zero existem. Lembre-se de que no final das contas, True vale 1 para o Python, e False vale zero, então uma boa dica seria usar a função sum().
# 
# iii) Utilize a indexação booleana que você aprendeu para criar uma variável poi_nao_zero que aponta para os elementos de poi diferentes de zero. Dica: você vai pode inverter os elementos do objeto que criou em ii) ou escrever a comparação adequada.

# In[200]:


#i:

np.random.seed(1234)
poi = np.random.poisson(3, 100)
poi
bool_zero = []

for i in range(len(poi)):
    
    if poi[i] == 0:
        resp = True
        bool_zero.append(resp)
    
    else:
        resp = False
        bool_zero.append(resp)

print(bool_zero)



# In[201]:


#ii:

sum(bool_zero)


# In[229]:


#iii:

#nao entendi esse comando poi=[~bool_zero], por favor me explique se possivel
    


# In[ ]:




