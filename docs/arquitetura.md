# Arquitetura pública da Naomi AI

Este documento apresenta somente decisões arquiteturais de alto nível. A topologia real, os protocolos, as rotas, as regras de autenticação e os módulos proprietários não fazem parte da documentação pública.

## Camadas conceituais

### 1. Superfícies de interação

Representam os pontos de contato com o usuário, como desktop, voz, mobile e experiências virtuais. Cada superfície traduz eventos para um contrato interno controlado.

### 2. Orquestração

Coordena estado, prioridade, cancelamento, filas e contexto. Essa camada evita que interface, áudio e integrações dependam diretamente umas das outras.

### 3. Serviços de inteligência

Agrupam capacidades de voz, memória, percepção e geração de resposta. São tratados como serviços substituíveis, com limites de recursos e caminhos de fallback.

### 4. Segurança e autorização

Valida identidade, escopo e risco antes de qualquer ação. Dados privados permanecem separados por usuário e por superfície.

### 5. Integrações supervisionadas

Conectam a Naomi a aplicações externas somente por interfaces autorizadas. Falhas externas devem degradar a experiência sem interromper o núcleo.

## Princípios de engenharia

- separação entre interface, estado e integração;
- dados pessoais locais por padrão;
- operações sensíveis supervisionadas;
- recursos pesados carregados sob demanda;
- fallbacks explícitos para hardware e serviços indisponíveis;
- filas limitadas e cancelamento cooperativo;
- observabilidade sem registrar segredos;
- validação automatizada dos fluxos críticos.

## Limite desta documentação

Não são publicados diagramas de implantação, nomes de serviços internos, formatos de token, detalhes de memória, prompts, políticas de persona ou mecanismos de proteção. Esses elementos permanecem no repositório privado.
