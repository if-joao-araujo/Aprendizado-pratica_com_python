import os
#retona a pagina atual
print(os.getcwd())
#lista arquivos e pastas
print(os.listdir())

os.system('cat /etc/*release')#mostra a versão do sistema operacional(linux)
#mostra informações do linux
print("\nInformações do sistema (CPU, Memória, etc.):")
os.system('lscpu')       # Informações da CPU
os.system('free -h')     # Uso de memória
os.system('uname -a')    # Informações do kernel
#desliga o computador
os.system('shutdown /s /t 60')
