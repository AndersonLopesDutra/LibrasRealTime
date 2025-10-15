# main.py

# Importa a função 'main' do nosso módulo 'hand_tracker' que está dentro do pacote 'app'
from app.hand_tracker import main

if __name__ == "__main__":
    print("Iniciando o programa principal...")
    # Executa a função principal que contém o loop de vídeo
    main()
    print("Programa finalizado.")