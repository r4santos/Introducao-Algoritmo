# AP04 - Estruturas Condicionais

## Sobre a lista
Nesta lista, você irá praticar o uso de estruturas condicionais em Python. Essas estruturas permitem que um programa tome decisões diferentes dependendo dos valores informados pelo usuário ou dos resultados de cálculos realizados durante a execução.

Ao longo dos exercícios, você trabalhará com situações em que o programa precisa avaliar condições e decidir qual caminho seguir. Os problemas foram organizados em ordem crescente de dificuldade, começando com verificações simples e evoluindo para cenários com condições compostas, exclusão mútua e condicionais aninhadas.

Em alguns casos, é possível implementar duas versões da mesma lógica para comparar abordagens:

- utilizando múltiplos comandos if/elif
- utilizando operadores lógicos (and e or)

Essa prática ajuda a desenvolver uma compreensão mais profunda sobre avaliação de condições e organização da lógica do programa.

## Estrutura esperada em cada solução
Todo programa deve seguir a organização lógica:

Entrada -> Processamento -> Saída

## Objetivos de aprendizagem
Ao concluir a AP04, você deve ser capaz de:

- usar if, elif e else para tomada de decisão
- interpretar regras de negócio e transformá-las em condições
- criar condições compostas com operadores lógicos
- evitar sobreposição de regras com exclusão mútua
- aplicar condicionais aninhadas quando necessário

## Lista de exercícios

### 1. Número dentro de um intervalo
Escreva um programa que leia um número inteiro e verifique se ele está entre 10 e 20.

Saídas esperadas:

- Número dentro do intervalo
- Número fora do intervalo

Arquivo: num_dentro_intervalo.py

### 2. Classificação de temperatura
Escreva um programa que leia a temperatura atual em graus Celsius e classifique:

- menor que 10 -> Temperatura baixa
- entre 10 e 25 -> Temperatura agradável
- maior que 25 -> Temperatura alta

Arquivo: class_temp.py

### 3. Elegibilidade para desconto
Uma loja oferece desconto para clientes que atendem a pelo menos uma condição:

- idade maior ou igual a 60 anos
- valor da compra maior que 200 reais

O programa deve ler idade e valor da compra.

Saídas esperadas:

- Cliente elegível para desconto
- Cliente sem desconto

Arquivo: elegibilidade_p_desconto.py

### 4. Classificação de desempenho
Um sistema classifica a nota final (0 a 100) nas faixas:

- 90 a 100 -> Excelente
- 70 a 89 -> Bom
- 50 a 69 -> Regular
- abaixo de 50 -> Insuficiente

O programa deve mostrar apenas uma classificação.

Arquivo: class_desempenho.py

### 5. Sistema de aprovação em disciplina
A aprovação depende de média final e frequência.

Entradas:

- média do aluno
- percentual de frequência

Regras:

- frequência menor que 75% -> reprovado por falta
- caso contrário, analisar média:
- média maior ou igual a 60 -> aprovado
- média entre 40 e 59 -> recuperação
- média abaixo de 40 -> reprovado por nota

Arquivo: sistema_aprov_disciplina.py

### 6. Controle de acesso ao laboratório
O programa deve ler:

- idade do usuário
- possui matrícula ativa (1 = sim, 0 = não)
- possui autorização especial (1 = sim, 0 = não)

Regras de acesso:

- matrícula ativa e idade maior ou igual a 18 -> acesso permitido
- matrícula ativa e menor de 18 -> só entra com autorização
- sem matrícula ativa -> só entra com autorização

Saídas:

- Acesso permitido
- Acesso negado

Arquivo: controle_acess_lab.py

### 7. Sistema de classificação em uma competição
O programa deve ler:

- pontuação total
- tempo total (em minutos)

Classificação:

- pontuação maior ou igual a 90 -> Ouro
- pontuação maior ou igual a 70 -> Prata
- pontuação maior ou igual a 50 -> Bronze
- caso contrário -> sem medalha

Regra adicional:

- se obtiver Ouro e tempo menor que 120 minutos, também exibir:
- Participante destaque da competição

O programa deve mostrar a classificação e, quando aplicável, o título de destaque.

Arquivo: sistema_class_comp.py

## Exemplos de entrada e saída

### Exemplo 1 - Número dentro do intervalo
Entrada:

```
Informe um número: 15
```

Saída:

```
Número dentro do intervalo
```

### Exemplo 2 - Elegibilidade para desconto
Entrada:

```
Informe a idade: 30
Informe o valor da compra: 250
```

Saída:

```
Cliente elegível para desconto
```

### Exemplo 3 - Sistema de aprovação em disciplina
Entrada:

```
Informe a média: 58
Informe a frequência (%): 80
```

Saída:

```
Recuperação
```

### Exemplo 4 - Classificação da competição
Entrada:

```
Informe a pontuação: 95
Informe o tempo (min): 110
```

Saída:

```
Classificação: Ouro
Participante destaque da competição
```

## Observações

- Priorize clareza na leitura das condições.
- Em exercícios com várias regras, valide primeiro os casos mais restritivos.
- Teste entradas de fronteira, como 10 e 20, 25, 50, 70, 90, 75% e 120 minutos.
