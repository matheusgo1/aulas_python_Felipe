#quero inserir o nome de uma pessoa na lista pela entrada do usuário
#quero que a aplicação imprima o tempo de execução

import time
start_time=time.time()
lista1=["Domingo", "Terca-Feira", "Quinta-Feira"]

incluir_lista=input("Incluir na lista: ")
lista1.append(incluir_lista)

end_time=time.time()
execution_time=end_time-start_time

print(lista1)
print(f"Tempo de Execucao:  {execution_time:.6f} segundos")