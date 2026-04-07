# AP06 - Lista de Exercicios: Estruturas de Repeticao com `for`

Nesta lista, voce pratica o uso da estrutura de repeticao `for` em Python.

A proposta e evoluir de repeticoes simples para problemas com:
- acumuladores
- contadores
- condicionais dentro do loop
- `for` aninhado
- analise de strings caractere por caractere

## Objetivos da AP06

Durante os exercicios, voce deve aplicar:
- `for in range()` para percorrer intervalos numericos
- `for` em strings para analisar caracteres
- `for` aninhado para padroes bidimensionais

## Estrutura recomendada para cada programa

Todo exercicio deve seguir a logica:

**Entrada -> Processamento -> Saida**

## Boas praticas

Antes de codar, tente sempre:
- identificar quantas vezes o loop deve executar
- definir o papel das variaveis (contador, acumulador, controle)
- simular mentalmente as iteracoes passo a passo

---

## Exercicios

### 1) Contagem crescente com `for`
Mostre os numeros de 1 ate 10, um por linha, utilizando `for in range()`.

### 2) Contagem regressiva
Mostre os numeros de 10 ate 1 utilizando `for`. Ao final, exiba: `Fim da contagem.`

### 3) Soma de `n` ate `m`
Leia dois inteiros positivos `n` e `m`, onde `n < m`, e calcule a soma de `n` ate `m` usando `for`.

Exemplo: para entradas `4` e `8`, calcular `4+5+6+7+8`.

### 4) Contagem de vogais
Leia uma palavra e conte quantas vogais ela possui usando `for` na string e `if`.

### 5) Contagem de caractere
Leia uma string e um caractere, e conte quantas vezes ele aparece na string utilizando `for` e `if`.

### 6) Maior valor
Leia 5 numeros e determine o maior valor informado utilizando `for`.

### 7) Palindromo
Leia uma palavra e verifique se ela e um palindromo utilizando `for in range()`.

### 8) Moldura numerica
Leia um inteiro positivo `n` e desenhe uma matriz `n x n` com:
- borda = `1`
- interior = `0`

Resolver com `for` aninhado.

Exemplo para `n = 4`:

```text
1111
1001
1001
1111
```

Exemplo para `n = 5`:

```text
11111
10001
10001
10001
11111
```

### 9) Prefixos palindromos
Leia uma palavra e verifique quais prefixos sao palindromos usando `for` aninhado.

### 10) Analisador de senha textual
Leia uma senha e, em uma unica passagem pela string, informe:
- quantidade total de caracteres
- quantidade de letras maiusculas
- quantidade de letras minusculas
- quantidade de digitos
- quantidade de caracteres especiais

Considere especial todo caractere que nao for letra nem numero.

No final, diga se a senha e forte. Criterios:
- pelo menos 8 caracteres
- pelo menos 1 maiuscula
- pelo menos 1 minuscula
- pelo menos 1 digito
- pelo menos 1 especial

### 11) Contador de blocos de palavras
Conte quantas palavras existem em um texto **sem usar `split()`**.

Regras:
- palavra = sequencia de caracteres diferentes de espaco
- pode haver espacos no inicio, no fim e entre palavras
- espacos extras nao contam como palavra

Dica: detectar transicao de "espaco" para "letra/caractere de palavra".

---

## Desafio - Sistema de simulacao de investimentos com juros compostos

Implemente um sistema de terminal para simular investimentos com juros compostos e aporte mensal.

### Menu

```text
1 - Configurar simulacao
2 - Executar simulacao
3 - Mostrar relatorio geral
4 - Mostrar evolucao mes a mes
0 - Encerrar sistema
```

### Requisitos das opcoes

1. **Configurar simulacao**
- ler e armazenar:
  - valor inicial investido
  - aporte mensal
  - taxa de juros mensal (em %)
  - quantidade de meses

2. **Executar simulacao**
- usar `for in range()`
- para cada mes:
  1) somar aporte ao saldo atual
  2) aplicar juros no novo saldo

3. **Mostrar relatorio geral**
- exibir:
  - valor inicial
  - aporte mensal
  - taxa de juros
  - meses simulados
  - total investido
  - saldo final
  - lucro total
  - saldo medio ao longo da simulacao
  - maior saldo registrado
  - mes do maior saldo

4. **Mostrar evolucao mes a mes**
- exibir o saldo acumulado ao final de cada mes

0. **Encerrar sistema**
- encerrar o programa
- se simulacao ja tiver sido executada, mostrar resumo final com:
  - total investido
  - saldo final
  - lucro total
  - rendimento percentual

### Regras importantes

- o menu deve repetir ate o usuario escolher `0`
- opcao `2` so funciona se a configuracao (opcao `1`) ja tiver sido feita
- opcao invalida deve mostrar erro e voltar ao menu
- nova configuracao + nova execucao substituem os dados anteriores

### Conceitos obrigatorios no desafio

- `for in range()`
- condicionais
- menu com repeticao
- acumuladores
- variaveis de controle
- calculo de porcentagem

---

## Exemplo 1 (resumo)

Entrada simulada:

```text
1
Valor inicial: 1000
Aporte mensal: 200
Taxa de juros mensal: 1
Meses: 3
2
3
4
0
```

Saida esperada (campos principais):

```text
Simulacao executada com sucesso.

Relatorio geral
Valor inicial: 1000
Aporte mensal: 200
Taxa de juros mensal: 1
Meses simulados: 3
Total investido: 1600
Saldo final: 1642.3812
Lucro total: 42.3812
Saldo medio na simulacao: 1426.8337333333334
Maior saldo registrado: 1642.3812
Mes do maior saldo: 3

Evolucao mes a mes
Mes 1: 1212.0
Mes 2: 1426.12
Mes 3: 1642.3812

Resumo final
Total investido: 1600
Saldo final: 1642.3812
Lucro total: 42.3812
```

## Exemplo 2 (resumo)

Entrada simulada:

```text
1
Valor inicial: 500
Aporte mensal: 150
Taxa de juros mensal: 2
Meses: 4
2
3
0
```

Saida esperada (campos principais):

```text
Simulacao executada com sucesso.

Relatorio geral
Valor inicial: 500
Aporte mensal: 150
Taxa de juros mensal: 2
Meses simulados: 4
Total investido: 1100
Saldo final: 1171.822104
Lucro total: 71.822104
Saldo medio na simulacao: 915.731826
Maior saldo registrado: 1171.822104
Mes do maior saldo: 4

Resumo final
Total investido: 1100
Saldo final: 1171.822104
Lucro total: 71.822104
```

---

## Observacao final

A maior dificuldade geralmente nao e a sintaxe do `for`, mas entender corretamente o padrao de repeticao e a evolucao das variaveis em cada iteracao.
