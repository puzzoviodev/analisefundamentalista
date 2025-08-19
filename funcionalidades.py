import inspect
import analisefundamentalista  # substitua pelo nome do seu arquivo sem ".py"

funcoes = [name for name, obj in inspect.getmembers(analisefundamentalista, inspect.isfunction)]
print("Funções disponíveis:", funcoes)
