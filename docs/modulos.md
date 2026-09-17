# Capacidades e responsabilidades

[Início](../README.md) · [Arquitetura](arquitetura.md)

Esta matriz mostra quem participa de cada capacidade. Não é uma lista de recursos garantidos em toda versão, nem uma relação de arquivos do projeto privado.

| Capacidade | Cliente desktop | Servidor | Mobile 3D | Maps |
| --- | --- | --- | --- | --- |
| Conversa | Entrada e apresentação no PC. | Contexto, modelos e resposta. | Entrada e apresentação no celular. | Pode coexistir com a conversa; navegação tem fluxo próprio. |
| Voz | Captura, reconhecimento e síntese conforme configuração. | Atende os fluxos de áudio que utilizam serviços remotos. | Integra áudio do aparelho e respostas. | Coordena instruções de navegação. |
| Memória | Contexto local e recuperação semântica. | Usa o recorte de contexto permitido. | Contexto local próprio e continuidade compatível. | Mantém estado de rota, distinto da memória de conversa. |
| Presença visual | Interface e integrações de avatar. | Pode fornecer resultados usados na apresentação. | Cenas, avatar e interface Unity. | Renderização cartográfica e controles de navegação. |
| Percepção | Recursos visuais supervisionados. | Processamento conforme o serviço disponível. | Capacidades dependem da versão e do dispositivo. | GPS e dados de navegação têm tratamento específico. |
| Ferramentas | Ações locais autorizadas e integrações. | Coordenação de serviços compartilhados. | Recursos e permissões Android. | Busca, rotas e informações cartográficas. |
| Desempenho | Perfis de hardware e controle de recursos. | Fila e capacidade de inferência. | Qualidade gráfica, áudio e ciclo de vida. | Custo de mapa, atualização e recursos gráficos. |

## Camadas compartilhadas

**Identidade e autorização** delimitam a conta, a sessão e os recursos permitidos. Estar conectado em dois dispositivos não dá acesso irrestrito aos dados locais de ambos.

**Eventos, tarefas e filas** coordenam os trabalhos assíncronos. Interface, voz, rede e integrações não precisam executar no mesmo ritmo.

**Observabilidade e testes** ajudam a distinguir falhas de rede, áudio, renderização e processamento. Diagnósticos de produção e dados de usuários não fazem parte do portfólio.

## Guias por componente

- [Servidor: processamento e serviços](servidor.md)
- [Cliente: experiência desktop](cliente.md)
- [Mobile 3D: experiência Android](mobile-3d.md)
- [Maps: localização e navegação](naomi-maps.md)

Os detalhes de implementação seguem a [política de publicação](seguranca.md).
