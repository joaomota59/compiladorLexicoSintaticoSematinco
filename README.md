[![Build Status](https://travis-ci.com/joaomota59/compiladorLexicoSintatico.svg?branch=main)](https://travis-ci.com/joaomota59/compiladorLexicoSintatico)
# Execução do script
* No terminal entre com os seguintes comandos:
``` shell
cd compilador
Scripts\activate
py index.py
```
# Regras Sintáticas
```
Grammar:

Rule 0     S' -> initial
Rule 1     initial -> ALGORITMO CARACTERE VAR declaracaoType INICIO blocoType FIMALGORITMO
Rule 2     blocoType -> <empty>
Rule 3     blocoType -> bloco
Rule 4     declaracaoType -> <empty>
Rule 5     declaracaoType -> declaracaoTypeAux
Rule 6     declaracaoTypeAux -> declaracao
Rule 7     declaracaoTypeAux -> declaracao declaracaoTypeAux
Rule 8     declaracao -> vartype : LOGICO
Rule 9     declaracao -> vartype : CARACTERE
Rule 10    declaracao -> vartype : REAL
Rule 11    declaracao -> vartype : INTEIRO
Rule 12    vartype -> ID , vartype
Rule 13    vartype -> ID
Rule 14    bloco -> cmd bloco
Rule 15    bloco -> cmd
Rule 16    cmd -> cmdRepeticao
Rule 17    cmd -> LIMPATELA
Rule 18    cmd -> cmdCondicao
Rule 19    cmd -> cmdleitura
Rule 20    cmd -> cmdescrita
Rule 21    cmd -> cmdattrib
Rule 22    cmdRepeticao -> ENQUANTO expressaoRelacional FACA bloco FIMENQUANTO
Rule 23    cmdleitura -> LEIA ( ID )
Rule 24    cmdCondicao -> SE expressaoRelacional ENTAO bloco SENAO bloco FIMSE
Rule 25    cmdCondicao -> SE expressaoRelacional ENTAO bloco FIMSE
Rule 26    expressaoRelacional -> termoRelacional
Rule 27    expressaoRelacional -> expressaoRelacional OP_BOOL termoRelacional
Rule 28    termoRelacional -> ( expressaoRelacional )
Rule 29    termoRelacional -> FALSO
Rule 30    termoRelacional -> VERDADEIRO
Rule 31    termoRelacional -> NAO termoRelacional
Rule 32    termoRelacional -> expr OP_REL expr
Rule 33    OP_BOOL -> XOU
Rule 34    OP_BOOL -> OU
Rule 35    OP_BOOL -> E
Rule 36    OP_REL -> EQ  [precedence=nonassoc, level=1]
Rule 37    OP_REL -> GT  [precedence=nonassoc, level=1]
Rule 38    OP_REL -> GE  [precedence=nonassoc, level=1]
Rule 39    OP_REL -> LT  [precedence=nonassoc, level=1]
Rule 40    OP_REL -> LE  [precedence=nonassoc, level=1]
Rule 41    OP_REL -> NE  [precedence=nonassoc, level=1]
Rule 42    cmdattrib -> ID ASSIGN ( typeArgs )
Rule 43    cmdattrib -> ID ASSIGN typeArgs
Rule 44    cmdattrib -> ID ASSIGN expr
Rule 45    typeArgs -> CARACTERE
Rule 46    typeArgs -> FALSO
Rule 47    typeArgs -> VERDADEIRO
Rule 48    cmdescrita -> ESCREVAL ( )
Rule 49    cmdescrita -> ESCREVAL ( typeArgsEscrita )
Rule 50    cmdescrita -> ESCREVA ( )
Rule 51    cmdescrita -> ESCREVA ( typeArgsEscrita )
Rule 52    typeArgsEscritaAux -> typeArgs
Rule 53    typeArgsEscritaAux -> expr
Rule 54    typeArgsEscrita -> typeArgsEscritaAux
Rule 55    typeArgsEscrita -> typeArgsEscrita , typeArgsEscritaAux
Rule 56    expr -> ID
Rule 57    expr -> REAL
Rule 58    expr -> INTEIRO
Rule 59    expr -> - expr  [precedence=right, level=5]
Rule 60    expr -> expr ^ expr  [precedence=right, level=4]
Rule 61    expr -> expr MOD expr  [precedence=left, level=3]
Rule 62    expr -> expr % expr  [precedence=left, level=3]
Rule 63    expr -> expr \ expr  [precedence=left, level=3]
Rule 64    expr -> expr / expr  [precedence=left, level=3]
Rule 65    expr -> expr * expr  [precedence=left, level=3]
Rule 66    expr -> expr - expr  [precedence=left, level=2]
Rule 67    expr -> expr + expr  [precedence=left, level=2]
Rule 68    expr -> ( expr )
```