# Uma variável é um espaço na memória do computador usado para armazenar um valor que pode ser usado ou alterado ao longo do código, como se fosse uma caixa com etiqueta.
# A etiqueta é o nome da variável e o conteúdo da caixa é o valor armazenado.

nome = "João"   # variável do tipo texto (string)
idade = 25      # variável do tipo número (int)

#Com o type você identifica o tipo de variável.

type (nome) # retorno: str
type (idade) # retorno: int

# valores decimais são separados por PONTOS, não vírgulas.
decimal = 1.0923

type (decimal) # retorno: float

# Os tipos de variáveis definem que tipo de dado a "caixa" pode guardar. Os principais são:
# Inteiro (int): Números inteiros, sem casas decimais (ex: 10, -5, 0).
# Ponto Flutuante (float): Números com casas decimais (ex: 10.5, 3.14).
# Texto (string ou str): Sequências de caracteres, sempre entre aspas (ex: "Olá", "Python").
# #Booleano (bool): Valores lógicos que só podem ser verdadeiro ou falso (ex: True, False).
