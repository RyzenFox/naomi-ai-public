# Segurança e publicação

## Objetivo

Este repositório apresenta a Naomi como portfólio sem transformar o projeto privado em uma distribuição copiável.

## Conteúdo proibido na versão pública

- segredos, tokens, chaves, certificados ou credenciais;
- arquivos de ambiente, sessões ou identificação de dispositivos;
- bancos, memórias, históricos, áudios ou dados pessoais;
- código de autenticação, licenciamento ou proteção comercial;
- prompts, persona completa, regras internas ou dados do criador;
- endpoints, domínios, topologia e configuração de produção;
- modelos, pesos, datasets ou artefatos de build;
- instaladores, pacotes comerciais ou mecanismos de atualização;
- código integral copiado do repositório privado.

## Conteúdo permitido

- descrições de capacidades em alto nível;
- diagramas conceituais sem topologia real;
- decisões de engenharia sem detalhes exploráveis;
- demo sintética que não compartilha algoritmos de produção;
- testes exclusivos da demo pública;
- screenshots previamente revisadas e sem dados pessoais.

## Checklist antes de publicar

1. Revisar todos os arquivos adicionados e o diff completo.
2. Procurar padrões de segredos no conteúdo e no histórico relevante.
3. Confirmar que nenhum arquivo veio diretamente do núcleo privado.
4. Remover caminhos locais, nomes civis, URLs internas e dados de usuários.
5. Validar que exemplos usam somente valores fictícios.
6. Publicar por branch e Pull Request para manter revisão auditável.

## Comunicação responsável

Não publique possíveis vulnerabilidades, credenciais ou dados pessoais em issues públicas. Entre em contato com o mantenedor pelo perfil [RyzenFox](https://github.com/RyzenFox).
