# Naomi AI — Public Portfolio Version

> Versão pública de portfólio do Projeto Naomi.

A Naomi AI é um projeto autoral de assistente de IA local modular desenvolvido em Python, com foco em voz, memória local, visão computacional, automação supervisionada e integração com ambientes virtuais como VRChat/VTuber.

## Aviso importante

Este repositório é uma versão pública e demonstrativa.

A implementação completa, o servidor, os módulos internos, a lógica principal, arquivos de memória, automações sensíveis e integrações reais permanecem privados.

Este repositório existe apenas para fins de portfólio, apresentação técnica e documentação arquitetural.

## O que este repositório contém

- Documentação da arquitetura.
- Explicação dos módulos em alto nível.
- Roadmap do projeto.
- Exemplos simplificados e não funcionais do fluxo.
- Descrição das tecnologias utilizadas.

## O que este repositório NÃO contém

- Código-fonte completo da Naomi.
- Servidor real.
- Módulos internos de decisão.
- Sistema real de memória.
- Voice ID real.
- Automação real.
- Tokens, credenciais ou arquivos `.env`.
- Bancos de dados.
- Áudios pessoais.
- Modelos de IA.
- Integração real com VRChat/Discord.

## Tecnologias estudadas no projeto

- Python
- Git e GitHub
- Azure Speech
- SQLite
- FastAPI
- OpenCV
- YOLO
- PyTorch
- Ollama
- CustomTkinter
- Automação desktop
- Arquitetura modular
- IA aplicada

## Arquitetura conceitual

~~~mermaid
flowchart TD
    User["Usuário"] --> Audio["Entrada de Voz"]
    Audio --> STT["Reconhecimento de Fala"]
    STT --> Core["Núcleo Naomi"]
    Core --> Memory["Memória Local"]
    Core --> Planner["Planejamento"]
    Core --> Safety["Camada de Segurança"]
    Core --> Skills["Skills"]
    Core --> Response["Resposta"]
    Response --> TTS["Síntese de Voz"]
    TTS --> User
~~~

## Estrutura pública

~~~text
naomi-ai-public/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── arquitetura.md
│   ├── modulos.md
│   ├── seguranca.md
│   └── roadmap.md
├── examples/
│   └── demo_fluxo_simplificado.py
└── assets/
~~~

## Autor

RyzenFox  
Estudante de Ciência da Computação  
GitHub: https://github.com/RyzenFox  
GitHub: https://github.com/RyzenFox
