# 🇧🇷 LibrasRealTime

## 🚀 Visão Geral do Projeto

O `LibrasRealTime` é um projeto de Visão Computacional em tempo real que visa explorar e aplicar técnicas de Machine Learning e Deep Learning para a detecção de gestos. Desenvolvido em Python, utiliza as capacidades de processamento de imagem de bibliotecas líderes da indústria para interagir com a câmera do notebook.

**Objetivos principais:**
* Detectar e mapear pontos-chave (landmarks) de mãos para o futuro reconhecimento de gestos (foco inicial no alfabeto LIBRAS).
* Servir como plataforma de estudo e prática em Ciência de Dados, Visão Computacional e Machine Learning.

## ⚙️ Tecnologias e Ferramentas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

* **Linguagem:** Python 🐍
* **Visão Computacional:** OpenCV (Open Source Computer Vision Library)
    * Utilizado para acesso à câmera, manipulação de imagens (conversão de cores, desenho, exibição).
* **Deep Learning/Modelos Pré-Treinados:** MediaPipe (Google)
    * Fornece modelos otimizados para detecção de mãos (`Hands`), extraindo landmarks em tempo real.
* **Processamento Numérico:** NumPy
    * Base para manipulação eficiente de dados numéricos e arrays.
* **Ambiente de Desenvolvimento Integrado (IDE):** PyCharm
* **Controle de Versão:** Git
* **Hospedagem de Repositório:** GitHub

## ✨ Funcionalidades Atuais

O projeto `LibrasRealTime` atualmente oferece o seguinte módulo:

### 🖐️ Detecção de Mãos (Módulo `hand_tracker.py`)
* Acesso em tempo real à câmera do notebook.
* Detecção precisa de uma ou mais mãos utilizando o modelo `MediaPipe Hands`.
* Mapeamento e visualização dos 21 pontos-chave (landmarks) de cada mão.
* Exibição do FPS (Frames Per Second) para monitoramento de performance.
* **Propósito:** Base para o futuro reconhecimento do alfabeto em LIBRAS.

## 🚀 Como Executar o Projeto

Para configurar e executar o projeto em seu ambiente local, siga os passos abaixo:

### 📋 Pré-requisitos
* Python 3.11 (recomendado para compatibilidade com MediaPipe)
* Git (instalado e configurado)

### ⬇️ 1. Clonar o Repositório

Abra seu terminal e execute o comando:
```bash
git clone [https://github.com/AndersonLopesDutra/LibrasRealTime.git](https://github.com/AndersonLopesDutra/LibrasRealTime.git)

Em seguida, navegue até a pasta do projeto:

Bash

cd LibrasRealTime
🐍 2. Configurar o Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto. Se estiver usando o PyCharm, ele pode ser configurado em File -> Settings -> Project -> Python Interpreter.

📦 3. Instalar as Dependências
Com o ambiente virtual ativado no seu terminal (você verá (.venv) no prompt), instale todas as bibliotecas necessárias com um único comando:

Bash

pip install -r requirements.txt
▶️ 4. Executar o Módulo
Após a instalação das dependências, você pode executar o módulo de detecção de mãos:

Bash

python main.py
Pressione ESC na janela da câmera para encerrar a execução.

🎯 Próximos Passos (Roadmap Futuro)
Implementar Detecção Facial: Desenvolver o módulo de detecção e mapeamento do rosto em uma branch separada.

Implementar Reconhecimento do Alfabeto LIBRAS: Treinar um modelo de Machine Learning (classificador) para identificar as letras do alfabeto.

Aprimoramento da Interface: Melhorias na visualização e na interação com o usuário.
