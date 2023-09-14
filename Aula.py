"""
try, except - Tratamento de erros
"""
try:  # tente
    a = 1 / 0
except:  # Erro
    pass
# Não é bom tratar seus erros no formado basico!


# Você pode ter varias exceções
try:
    a = 1 / 0
except NameError as erro:
    print('Erro:', erro)
except (ZeroDivisionError, IndexError) as erro:
    print('Erro:', erro)
except Exception as erro:
    print('Erro inesperado:', erro)
else:  # Será executado se não houve uma excessão
    pass
finally:  # Sempre será executado!
    a = None  # Tratando o erro
print(a)
