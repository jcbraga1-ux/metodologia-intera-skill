# Desenho ético do OA: sem dark patterns e com respeito à LGPD

Todo OA deve respeitar quem aprende. Isso inclui não manipular o aluno para usar mais, gastar ou entregar dados, e tratar os dados pessoais conforme a lei. Esta seção é uma **proposta desta skill**, coerente com a base humanista da Intera (ver `alinhamento-pedagogico.md`). Ela **não substitui orientação jurídica**: em projetos reais, confirme as decisões com o encarregado de dados (DPO) ou com o setor jurídico da instituição.

Fontes legais: Lei nº 13.709/2018 (LGPD), especialmente o art. 14, sobre dados de crianças e adolescentes; Lei nº 15.211/2025 (ECA Digital), em vigor desde março de 2026, para produtos digitais direcionados a crianças e adolescentes ou de acesso provável por eles.

## Dark patterns a evitar

Dark patterns são escolhas de design que levam a pessoa a fazer algo que ela não faria se entendesse bem a situação. Num OA, eles também atrapalham a aprendizagem.

| Padrão | Exemplo num OA | Alternativa ética |
| --- | --- | --- |
| Culpar quem sai ou recusa | "Tem certeza? Seus amigos vão ficar para trás!" | Botão de sair simples, sem chantagem |
| Pressão de tempo falsa | Contagem regressiva para "não perder" um prêmio | Tempo livre, ou ajustável quando a atividade precisar de tempo |
| Recompensas aleatórias | Baú surpresa ou roleta de prêmios | Recompensas previsíveis, ligadas ao que foi aprendido; caixas de recompensa são proibidas em jogos para crianças e adolescentes pelo ECA Digital |
| Sequência de dias que pune a pausa | "Você perdeu sua sequência de 10 dias!" | Progresso que fica guardado e respeita o ritmo do aluno |
| Notificações insistentes | Lembretes repetidos para voltar ao app | Lembretes desligados por padrão e configuráveis |
| Uso sem fim | Próxima fase ou vídeo começa sozinho, sem parada | Pausas naturais e fim de sessão claro |
| Ranking que expõe | Lista pública com quem ficou por último | Progresso individual, conquistas coletivas e cooperação |
| Compras e anúncios | Moedas compradas, propaganda dentro do OA | Nenhum anúncio e nenhuma compra; tudo liberado para aprender |
| Consentimento disfarçado | Caixa de autorização já marcada, texto longo e difícil | Pedido claro, em linguagem simples, com a caixa desmarcada |
| Difícil de sair ou apagar | Conta que não pode ser excluída | Sair e apagar os dados em poucos passos |
| Coleta além do necessário | Pedir nome completo, escola e foto para jogar | Coletar só o indispensável, de preferência nada |

## LGPD e ECA Digital no OA

- **Colete o mínimo.** Prefira OAs que funcionem sem login e sem dados pessoais. Se precisar de identificação, use apelidos ou códigos.
- **Diga para que serve.** Explique, em linguagem simples e acessível, quais dados são coletados, para quê, por quanto tempo e quem acessa.
- **Crianças.** O tratamento de dados de crianças exige o consentimento específico e em destaque de pelo menos um dos pais ou do responsável legal, e deve atender ao melhor interesse da criança (LGPD, art. 14). Para adolescentes, vale também o melhor interesse.
- **Privacidade por padrão.** Em produtos para crianças e adolescentes, a configuração inicial deve ser a mais protetiva (ECA Digital).
- **Sem perfilamento para publicidade.** O ECA Digital proíbe direcionar publicidade comercial por perfilamento a crianças e adolescentes. No OA, a recomendação é não ter publicidade nenhuma.
- **Cuidado com dados que revelam deficiência ou saúde.** Preferências de acessibilidade, como leitor de tela ou janela de Libras, podem revelar uma deficiência, que é dado sensível. Guarde essas preferências no próprio aparelho, sem enviar para servidores, e nunca as use para outra finalidade.
- **Sem rastreadores de terceiros.** Evite ferramentas de análise, plugins e serviços que coletam dados dos alunos para outras empresas. Isso vale também na escolha das tecnologias gratuitas (`tecnologias-gratuitas.md`).
- **Segurança e exclusão.** Proteja os dados guardados, defina por quanto tempo ficam e como serão apagados.
- **Pesquisa.** Se o OA for usado em pesquisa, siga o termo de consentimento dos responsáveis, o assentimento da criança e a aprovação do comitê de ética (ver `avaliacao-pedagogica.md`).

## Como a skill aplica o desenho ético em cada etapa

- **Contextualização:** registre a idade do público e se haverá crianças ou adolescentes, porque isso muda as exigências legais.
- **Requisitos:** gere requisitos não funcionais de ética e privacidade (RNF-ET), cada um com critério de aceite. Por exemplo: "RNF-ET-01: o OA funciona sem login. Aceite: é possível concluir todas as atividades sem informar dados pessoais." Faça ao professor as perguntas sobre dados no bloco de **Acesso** do guia de requisitos, como complemento proposto por esta skill.
- **Esboço e desenvolvimento:** confira mecânicas, recompensas, notificações e telas de consentimento com a tabela de dark patterns.
- **Teste e Qualidade:** inclua um teste de desenho ético, percorrendo a tabela acima, e verifique se o OA envia dados para terceiros.
- **Disponibilização:** publique junto com o OA um aviso de privacidade em linguagem simples.
- **Avaliação pedagógica:** colete só os dados necessários para a avaliação, com consentimento.

## Antes de entregar qualquer artefato

Confira:

1. Há algum dark pattern da tabela?
2. O OA coleta só o necessário, de preferência nada?
3. Para crianças e adolescentes, a configuração inicial é a mais protetiva e não há caixas de recompensa nem publicidade?
4. As tecnologias escolhidas não enviam dados dos alunos para terceiros?

Se algo falhar, aponte em "Pontos de atenção".
