[![Build Status](https://travis-ci.com/joaomota59/compiladorLexicoSintaticoSematinco.svg?branch=main)](https://travis-ci.com/joaomota59/compiladorLexicoSintaticoSematinco)
# Execução do script
* No terminal entre com os seguintes comandos:
``` shell
cd compilador
Scripts\activate
py index.py algoritmo.txt
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
Rule 28    cmdCondicao -> SE expressaoRelacional ENTAO ; bloco SENAO ; bloco FIMSE
Rule 29    cmdCondicao -> SE expressaoRelacional ENTAO ; bloco FIMSE
Rule 30    expressaoRelacional -> termoRelacional
Rule 31    expressaoRelacional -> expressaoRelacional OP_BOOL termoRelacional
Rule 32    termoRelacional -> ( expressaoRelacional )
Rule 33    termoRelacional -> FALSO
Rule 34    termoRelacional -> VERDADEIRO
Rule 35    termoRelacional -> NAO termoRelacional
Rule 36    termoRelacional -> expr OP_REL expr
Rule 37    OP_BOOL -> OU  [precedence=nonassoc, level=1]
Rule 38    OP_BOOL -> E  [precedence=nonassoc, level=1]
Rule 39    OP_REL -> EQ  [precedence=nonassoc, level=1]
Rule 40    OP_REL -> GT  [precedence=nonassoc, level=1]
Rule 41    OP_REL -> GE  [precedence=nonassoc, level=1]
Rule 42    OP_REL -> LT  [precedence=nonassoc, level=1]
Rule 43    OP_REL -> LE  [precedence=nonassoc, level=1]
Rule 44    OP_REL -> NE  [precedence=nonassoc, level=1]
Rule 45    cmdattrib -> ID ASSIGN ( typeArgs )
Rule 46    cmdattrib -> ID ASSIGN typeArgs
Rule 47    cmdattrib -> ID ASSIGN expr
Rule 48    typeArgs -> expr OP_REL expr
Rule 49    typeArgs -> FALSO
Rule 50    typeArgs -> VERDADEIRO
Rule 51    cmdescrita -> ESCREVAL ( )
Rule 52    cmdescrita -> ESCREVAL ( typeArgsEscrita )
Rule 53    cmdescrita -> ESCREVA ( )
Rule 54    cmdescrita -> ESCREVA ( typeArgsEscrita )
Rule 55    typeArgsEscritaAux -> typeArgs
Rule 56    typeArgsEscritaAux -> expr
Rule 57    typeArgsEscrita -> typeArgsEscritaAux
Rule 58    typeArgsEscrita -> typeArgsEscrita , typeArgsEscritaAux
Rule 59    expr -> CARACTERE
Rule 60    expr -> ID
Rule 61    expr -> REAL
Rule 62    expr -> INTEIRO
Rule 63    expr -> - expr  [precedence=right, level=5]
Rule 64    expr -> + expr  [precedence=right, level=5]
Rule 65    expr -> expr ^ expr  [precedence=right, level=4]
Rule 66    expr -> expr MOD expr  [precedence=left, level=3]
Rule 67    expr -> expr % expr  [precedence=left, level=3]
Rule 68    expr -> expr \ expr  [precedence=left, level=3]
Rule 69    expr -> expr / expr  [precedence=left, level=3]
Rule 70    expr -> expr * expr  [precedence=left, level=3]
Rule 71    expr -> expr - expr  [precedence=left, level=2]
Rule 72    expr -> expr + expr  [precedence=left, level=2]
Rule 73    expr -> ( expr )
```


Obs: Todas regras sintáticas e o passo a passo das operações de shift e reduce podem ser encontradas no arquivo: parser.out 
> ./compilador/parser.out

Obs2: O arquivo tokens.txt guarda todos tokens após a leitura do programa em Visualg.
> ./compilador/tokens.txt

Obs3: O arquivo algoritmo.txt é o programa de entrada, em Visualg, que será verificado as regras léxicas(Lexer) e sintáticas(Parser).
> ./compilador/algoritmo.txt
