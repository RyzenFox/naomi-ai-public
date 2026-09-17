# Estado e direção do projeto

[Início](../README.md) · [Arquitetura](arquitetura.md) · [Histórico público](changelog-publico.md)

Referência editorial: **17/09/2026**. Este roadmap comunica a direção de engenharia. Não é um cronograma de lançamento nem uma garantia de recursos em todos os pacotes distribuídos.

## Base de desenvolvimento documentada

| Componente | Estrutura existente |
| --- | --- |
| Servidor | Orquestração em Python/FastAPI, modelos configuráveis, fila de inferência e comunicação HTTP/SSE. |
| Cliente desktop | Interface Windows, runtime de voz, memória local, percepção e integrações autorizadas. |
| Mobile 3D | Cliente Unity/Android, presença 3D, conversa, áudio e contexto local. |
| Maps | Integração de GPS, mapa interativo em WebView, busca, rotas e coordenação de navegação. |
| Ecossistema web | Site oficial e apresentação pública em repositório próprio. |

## Focos de evolução

- **Servidor:** qualidade de resposta, controle de concorrência, cancelamento e diagnóstico.
- **Cliente:** latência de áudio, convivência com jogos e estabilidade das integrações.
- **Mobile 3D:** uso de memória e bateria, retorno do segundo plano e continuidade entre versões.
- **Maps:** legibilidade, estabilidade de GPS, ciclo de vida do mapa e coerência entre dados disponíveis e interface.
- **Qualidade:** ampliar validação em hardware real e distinguir resultados de testes, pacotes de teste e versões distribuídas.
- **Documentação:** publicar demonstrações revisadas e estudos de caso sem dados pessoais ou implementação proprietária.

## O que esta página não anuncia

Não são anunciados aqui uma versão iOS, disponibilidade em lojas, navegação integralmente offline, cobertura universal de trânsito, metas de desempenho garantidas ou abertura do código de produção.

A demo pública e seus testes são independentes do produto. Consulte os guias de [servidor](servidor.md), [cliente](cliente.md), [mobile](mobile-3d.md) e [Maps](naomi-maps.md) para entender as dependências de cada parte.
