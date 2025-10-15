# 🇧🇷 LibrasRealTime

## 🚀 Visão Geral do Projeto

O `LibrasRealTime` é um projeto de Visão Computacional em tempo real que visa explorar e aplicar técnicas de Machine Learning e Deep Learning para a detecção de gestos e características faciais. Desenvolvido em Python, utiliza as capacidades de processamento de imagem de bibliotecas líderes da indústria para interagir com a câmera do notebook.

**Objetivos principais:**
* Detectar e mapear pontos-chave (landmarks) de mãos para reconhecimento de gestos (foco inicial no alfabeto LIBRAS).
* Realizar detecção e mapeamento facial, demonstrando conceitos de biometria e análise estrutural do rosto.
* Servir como plataforma de estudo e prática em Ciência de Dados, Visão Computacional e Machine Learning.

## ⚙️ Tecnologias e Ferramentas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

* **Linguagem:** Python 🐍
* **Visão Computacional:** OpenCV (Open Source Computer Vision Library)
    * Utilizado para acesso à câmera, manipulação de imagens (conversão de cores, desenho, exibição).
* **Deep Learning/Modelos Pré-Treinados:** MediaPipe (Google)
    * Fornece modelos otimizados para detecção de mãos (`Hands`) e malha facial (`FaceMesh`), extraindo landmarks em tempo real.
* **Processamento Numérico:** NumPy
    * Base para manipulação eficiente de dados numéricos e arrays.
* **Computação Científica:** SciPy
    * Biblioteca de algoritmos e funções para computação científica, utilizada em algumas abordagens de malha geométrica.
* **Ambiente de Desenvolvimento Integrado (IDE):** PyCharm
* **Controle de Versão:** Git
* **Hospedagem de Repositório:** GitHub

## ✨ Funcionalidades Atuais

O projeto `LibrasRealTime` atualmente oferece os seguintes módulos e funcionalidades:

### 🖐️ Detecção de Mãos (Módulo `hand_tracker.py`)
* Acesso em tempo real à câmera do notebook.
* Detecção precisa de uma ou mais mãos utilizando o modelo `MediaPipe Hands`.
* Mapeamento e visualização dos 21 pontos-chave (landmarks) de cada mão.
* Exibição do FPS (Frames Per Second) para monitoramento de performance.
* **Propósito:** Base para o futuro reconhecimento do alfabeto em LIBRAS.

### 👤 Detecção e Mapeamento Facial (Módulo `face_mesh_tracker.py`)
* Acesso em tempo real à câmera do notebook.
* Detecção detalhada da malha facial utilizando o modelo `MediaPipe FaceMesh`.
* Extração de mais de 400 pontos-chave do rosto.
* Renderização de uma malha customizada e minimalista sobre o rosto (inspirada em biometria facial).
* Exibição do FPS para monitoramento de performance.
* **Propósito:** Estudo e demonstração de conceitos de biometria e análise estrutural da face.

## 🚀 Como Executar o Projeto

Para configurar e executar o projeto em seu ambiente local, siga os passos abaixo:

### 📋 Pré-requisitos
* Python 3.11 (recomendado para compatibilidade com MediaPipe)
* Git (instalado e configurado)
* PyCharm (ou sua IDE Python preferida)

### ⬇️ 1. Clonar o Repositório

Abra seu terminal e execute o comando:
```bash
git clone [https://github.com/AndersonLopesDutra/LibrasRealTime.git](https://github.com/AndersonLopesDutra/LibrasRealTime.git)

Em seguida, navegue até a pasta do projeto:

Bash

cd LibrasRealTime
🐍 2. Configurar o Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

No PyCharm:
Abra a pasta do projeto (File -> Open...).

Vá em File -> Settings... -> Project: LibrasRealTime -> Python Interpreter.

Clique em Add Interpreter -> Add Local Interpreter....

Selecione Virtualenv Environment e New environment.

Garanta que o Base interpreter seja o Python 3.11 que você instalou.

Clique em OK para criar o ambiente.

📦 3. Instalar as Dependências
Com o ambiente virtual ativado no terminal do PyCharm (você verá (.venv) no prompt), instale todas as bibliotecas necessárias com um único comando:

Bash

pip install -r requirements.txt
▶️ 4. Executar os Módulos
Após a instalação das dependências, você pode executar os módulos de detecção:

Para Detecção de Mãos:
Bash

python main.py
Para Detecção Facial:
Bash

python main_face.py
Pressione ESC em qualquer uma das janelas para encerrar a execução.

🎯 Próximos Passos (Roadmap Futuro)
Implementação do Reconhecimento do Alfabeto LIBRAS: Treinamento de um modelo de Machine Learning (classificador) utilizando os landmarks das mãos para identificar as letras do alfabeto estático em LIBRAS.

Detecção de Objeto Customizada: Treinar um modelo de Deep Learning (e.g., YOLO) para detectar objetos específicos (como um cigarro) e verificar a interação com as feições faciais.

Aprimoramento da Interface: Melhorias na visualização e na interação com o usuário.

