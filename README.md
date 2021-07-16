[![Build Status](https://travis-ci.com/joaomota59/compiladorLexicoSintaticoSematinco.svg?branch=main)](https://travis-ci.com/joaomota59/compiladorLexicoSintaticoSematinco)
# Execução do script
* Para compilar, no terminal, entre com os seguintes comandos:
``` shell
cd compilador
Scripts\activate
py index.py algoritmo.txt
```
* Após o processo de compilação, para executar o código objeto, no terminal, entre com os seguintes comandos:
``` shell
py codigoObjeto.py
```

# Regras Sintáticas
```
Grammar:

Rule 0     S' -> initial
Rule 1     initial -> ALGORITMO CARACTERE ; varAux INICIO ; blocoType FIMALGORITMO ;
Rule 2     varAux -> VAR ; declaracaoType
Rule 3     varAux -> <empty>
Rule 4     blocoType -> <empty>
Rule 5     blocoType -> bloco
Rule 6     declaracaoType -> <empty>
Rule 7     declaracaoType -> declaracaoTypeAux
Rule 8     declaracaoTypeAux -> declaracao ;
Rule 9     declaracaoTypeAux -> declaracao ; declaracaoTypeAux
Rule 10    declaracao -> vartype : LOGICO
Rule 11    declaracao -> vartype : CARACTERE
Rule 12    declaracao -> vartype : REAL
Rule 13    declaracao -> vartype : INTEIRO
Rule 14    vartype -> ID , vartype
Rule 15    vartype -> ID
Rule 16    bloco -> cmd ; bloco
Rule 17    bloco -> cmd ;
Rule 18    cmd -> cmdRepeticao
Rule 19    cmd -> LIMPATELA
Rule 20    cmd -> cmdCondicao
Rule 21    cmd -> cmdleitura
Rule 22    cmd -> cmdescrita
Rule 23    cmd -> cmdattrib
Rule 24    cmdRepeticao -> ENQUANTO expressaoRelacional FACA ; bloco FIMENQUANTO
Rule 25    cmdleitura -> LEIA ( idAux )
Rule 26    idAux -> ID , idAux
Rule 27    idAux -> ID
Rule 28    regraVazia -> ;
Rule 29    cmdCondicao -> SE expressaoRelacional regraVazia ENTAO ; bloco SENAO regraVazia bloco FIMSE
Rule 30    cmdCondicao -> SE expressaoRelacional regraVazia ENTAO ; bloco FIMSE
Rule 31    expressaoRelacional -> termoRelacional
Rule 32    expressaoRelacional -> expressaoRelacional OP_BOOL termoRelacional
Rule 33    termoRelacional -> ( expressaoRelacional )
Rule 34    termoRelacional -> FALSO
Rule 35    termoRelacional -> VERDADEIRO
Rule 36    termoRelacional -> ID
Rule 37    termoRelacional -> ( termoRelacional )
Rule 38    termoRelacional -> NAO termoRelacional
Rule 39    termoRelacional -> exprC OP_REL exprC
Rule 40    termoRelacional -> expr OP_REL expr
Rule 41    OP_BOOL -> OU  [precedence=nonassoc, level=1]
Rule 42    OP_BOOL -> E  [precedence=nonassoc, level=1]
Rule 43    OP_REL -> EQ  [precedence=nonassoc, level=1]
Rule 44    OP_REL -> GT  [precedence=nonassoc, level=1]
Rule 45    OP_REL -> GE  [precedence=nonassoc, level=1]
Rule 46    OP_REL -> LT  [precedence=nonassoc, level=1]
Rule 47    OP_REL -> LE  [precedence=nonassoc, level=1]
Rule 48    OP_REL -> NE  [precedence=nonassoc, level=1]
Rule 49    cmdattrib -> ID ASSIGN expressaoRelacional
Rule 50    cmdattrib -> ID ASSIGN exprC
Rule 51    cmdattrib -> ID ASSIGN expr
Rule 52    cmdescrita -> ESCREVAL ( )
Rule 53    cmdescrita -> ESCREVAL ( typeArgsEscrita )
Rule 54    cmdescrita -> ESCREVA ( )
Rule 55    cmdescrita -> ESCREVA ( typeArgsEscrita )
Rule 56    typeArgsEscritaAux -> expressaoRelacional
Rule 57    typeArgsEscritaAux -> exprC
Rule 58    typeArgsEscritaAux -> expr
Rule 59    typeArgsEscrita -> typeArgsEscritaAux
Rule 60    typeArgsEscrita -> typeArgsEscrita , typeArgsEscritaAux
Rule 61    expr -> ID
Rule 62    expr -> REAL
Rule 63    expr -> INTEIRO
Rule 64    expr -> - expr  [precedence=right, level=5]
Rule 65    expr -> + expr  [precedence=right, level=5]
Rule 66    expr -> expr ^ expr  [precedence=right, level=4]
Rule 67    expr -> expr MOD expr  [precedence=left, level=3]
Rule 68    expr -> expr % expr  [precedence=left, level=3]
Rule 69    expr -> expr \ expr  [precedence=left, level=3]
Rule 70    expr -> expr / expr  [precedence=left, level=3]
Rule 71    expr -> expr * expr  [precedence=left, level=3]
Rule 72    expr -> expr - expr  [precedence=left, level=2]
Rule 73    expr -> expr + expr  [precedence=left, level=2]
Rule 74    expr -> ( expr )
Rule 75    exprC -> CARACTERE
Rule 76    exprC -> ID
Rule 77    exprC -> exprC + exprC  [precedence=left, level=2]
Rule 78    exprC -> ( exprC )
```


Obs: Todas regras sintáticas e o passo a passo das operações de shift e reduce podem ser encontradas no arquivo: parser.out 
> ./compilador/parser.out

Obs2: O arquivo tokens.txt guarda todos tokens após a leitura do programa em Visualg.
> ./compilador/tokens.txt

Obs3: O arquivo algoritmo.txt é o programa de entrada, em Visualg, que será verificado as regras léxicas(Lexer) e sintáticas(Parser).
> ./compilador/algoritmo.txt

Obs4: Após o compilador ser executado o arquivo com o nome codigoObjeto.py será gerado, esse arquivo é o código objeto resultante do processo de compilação.
> ./compilador/codigoObjeto.py
