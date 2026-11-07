# Extensão da Metodologia Intera para cursos a distância (modelo de processo BPM)

Origem: pesquisa de mestrado de Andreza Gonçalves da Silva; livro *Metodologia Intera 2.0*, cap. 8. As etapas da Intera foram mapeadas como processos de negócio (BPM), modelados em BPMN 2.0 e automatizados; validação em cenário simulado. Dados abertos sob CC BY 4.0.

Fonte: site Intera › Metodologia INTERA para EAD (BPM), consultado em 31/10/2026.

Detalhamento acadêmico: SILVA, A. G. da. *Modelo aberto de processo para implantação de um curso a distância*. Dissertação (Mestrado em Ciência da Computação), UFABC, 2024. Orientadora: Juliana Braga. Atenção:

- **Granularidade:** nesse modelo, cada disciplina do curso é tratada como um OA. Essa granularidade é específica do EaD; na Intera geral, use o tamanho do grão definido com o professor (`reuso-e-rea.md`).
- **Validação:** os modelos foram validados com especialista e personas, em simulação, sem aplicação real.
- **Legislação:** o Plano de Avaliação cita o Decreto 5.622/2005, revogado pelo Decreto 9.057/2017. Confira a legislação vigente antes de usá-lo.

## Três visões

- **Gestão acadêmica:** aprovação do projeto pedagógico do curso (subprocesso "Aprovar Curso").
- **Gestão de projetos:** as etapas da Intera que desenvolvem o curso (prazo, custo, pessoas). É a visão modelada em detalhe.
- **Gestão de processos:** métricas e avaliação para melhorar o curso e o processo; inclui o subprocesso "Realizar Curso".

No modelo, cada etapa é um subprocesso, em ordem de Contextualização a Avaliação, com laços de repetição representando o "ir e vir".

## Papéis no EaD

| Papel | Responsabilidade |
| --- | --- |
| Professor conteudista | Conteúdo, curadoria, avaliação do conteúdo nos testes, integridade e veracidade |
| Professor formador | Conduz a aula, promove diálogo e interação |
| Professor tutor | Media a aula, tira dúvidas, dá devolutivas nas atividades |
| Designer instrucional (pedagógico) | Mapa instrucional, planejamento e avaliação pedagógica do curso |
| Demandante | Solicita e/ou financia o curso |
| Professor coordenador | Garante o projeto pedagógico, monitora indicadores de qualidade, gere requisitos não atendidos |
| Gerente de projetos | Comunicação, cronograma, escopo, custo, distribuição de atividades |
| Gerente de processo | Melhoria do processo: avalia indicadores, identifica lacunas e redundâncias |
| Equipe de desenvolvimento | Ambientes (manutenção, monitoramento, recuperação), escolhas tecnológicas, publicação, conteúdos complementares (tutoriais, vídeos) |
| Designer de interface | Interface e identidade visual do curso |
| Revisor | Revisão ortográfica e de entendimento dos textos |
| Equipe de acessibilidade | Libras, audiodescrição de imagens e vídeos; testa a acessibilidade do AVA |
| Discente | Estudantes, que participam como avaliadores |

## Artefatos por etapa

| Etapa | Atividade | Papel | Artefato | Fonte | Link |
| --- | --- | --- | --- | --- | --- |
| Contextualização | Preencher avaliação de contexto | Designer instrucional | Guia de Contexto | Intera | https://docs.google.com/document/d/1CAKBQJBbTkpDSqpzgYl20fC-BZw8gzx0/edit |
| Contextualização | Gerenciar indicadores do contexto | Professor coordenador | Guia de Indicadores | INEP | https://www.interaufabc.com.br/_files/ugd/c23ed1_4d967a7585e2438a85d7ee5b3e6824c7.pdf |
| Requisitos | Especificar requisitos | Designer instrucional | Guia de Coleta de Requisitos (didático-pedagógicos, técnicos funcionais e não funcionais, acessibilidade) | Intera | https://docs.google.com/document/d/1a20BYBIqHkBoc7T0Y7otP0favIKZ8hOm/edit |
| Requisitos | Elaborar TAP do projeto | Equipe de desenvolvimento | Termo de Abertura de Projeto | PMBOK | https://www.interaufabc.com.br/_files/ugd/c23ed1_174f8fe6bb384d8f9fd0cf14c7a4bf88.pdf |
| Arquitetura | Elaborar o MAPA do curso | Professor conteudista | Guia de Elaboração do MAPA (mapa de atividades) | Intera | https://docs.google.com/document/d/1nxQ-hfDDwiODRuOo13YXNGejZxjZICMt/edit |
| Teste e Qualidade | Preencher plano/checklist de testes | Equipe de teste / revisor | Guia de Plano de Testes / Checklist de Teste e Qualidade | Intera | https://docs.google.com/document/d/1Lv97jqmo69WVDAzkqG53Hj9KsKs8y4Xl/edit |
| Teste e Qualidade | Preencher checklist de acessibilidade | Equipe de acessibilidade | Checklist de Acessibilidade | e-MAG | https://www.interaufabc.com.br/_files/ugd/c23ed1_0bf27445f9184657b77fa06ef4a1808e.pdf |
| Avaliação | Aplicar questionário de qualidade pedagógica | Designer instrucional | Plano de Avaliação | Intera | https://docs.google.com/document/d/1dhWce2KzWQyQCWDMG1H_ux6OcotbdXUu/edit |
| Avaliação | Aplicar questionário de qualidade pedagógica | Designer instrucional | Questionário de Avaliação | Intera | https://docs.google.com/document/d/1eaiXtrVT1-nmOJDb1i8iVofRfI8_oO9G/edit |

Observação: o livro (cap. 8) atribui o mapa instrucional ao designer instrucional em um quadro e ao professor conteudista em outro; o site atribui a elaboração do MAPA ao professor conteudista. Confirme com a equipe quem será responsável.

## Etapas no EaD (resumo do site)

- **Contextualização:** compreender contexto pedagógico e público; atores: coordenador, equipe docente, designer instrucional, discentes.
- **Requisitos:** didático-pedagógicos, técnicos e de acessibilidade dos OAs do curso; alinhar conteudista, designer instrucional e equipe técnica.
- **Arquitetura:** estruturar logicamente a proposta do conteudista no mapa de atividades.
- **Desenvolvimento:** construir os OAs do curso conforme contexto, requisitos e mapa; atores: conteudista, equipe técnica, equipe de acessibilidade, designer de interface.
- **Teste e Qualidade:** equilíbrio entre qualidade tecnológica, funcional e pedagógica; checklists de qualidade e de acessibilidade (e-MAG).
- **Disponibilização:** publicar em produção e em repositórios; atender oportunidades de reúso apontadas no MAPA.
- **Avaliação:** visão 360º de qualidade com coordenador, designer instrucional, tutor, formador e discentes.
- **Ambiente e Padrões:** etapa-meio que fornece ambientes de desenvolvimento, homologação e produção.

Diagramas BPMN e de automação de cada etapa: https://www.interaufabc.com.br/diagramas-bpm-ead e https://www.interaufabc.com.br/fluxos-automa%C3%A7%C3%A3o-bpm-ead
