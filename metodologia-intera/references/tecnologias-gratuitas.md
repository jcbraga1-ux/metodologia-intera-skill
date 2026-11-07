# Tecnologias gratuitas para desenvolver o OA

Nas escolhas tecnológicas do OA, que cabem ao designer técnico nas etapas de Arquitetura e Desenvolvimento, a skill propõe **sempre tecnologias e plataformas gratuitas**. Assim, qualquer escola pública consegue criar, usar, adaptar e reutilizar o OA sem custo. Esta seção é uma **proposta desta skill**. Os nomes de ferramentas são exemplos: confira na época do projeto se continuam gratuitos e disponíveis.

## Critérios de escolha, em ordem de preferência

1. **Código aberto e gratuito**, de preferência com formatos abertos. É o que melhor combina com recursos educacionais abertos (REA) e com o reúso (ver `reuso-e-rea.md`).
2. **Gratuito, mas não aberto**, só quando não houver alternativa aberta adequada. Nesse caso, registre os riscos em "Pontos de atenção":
   - o plano gratuito pode mudar ou acabar;
   - pode haver limites de uso;
   - pode ser difícil exportar os arquivos;
   - o serviço pode coletar dados dos alunos.
3. **Nunca proponha ferramenta paga como caminho principal.** Se o professor já tiver uma licença paga, registre como opção dele e indique a alternativa gratuita.

Antes de recomendar, confira também:

- **Acessibilidade:** a ferramenta gera um OA que atende ao Desenho Universal (`desenho-universal.md`)?
- **Dados:** a ferramenta envia dados dos alunos para terceiros (`desenho-etico.md`)?
- **Arquivos-fonte:** é possível entregar arquivos editáveis, para que outra pessoa adapte o OA?
- **Funcionamento:** o OA roda no navegador, em celulares simples e com pouca internet?

## Exemplos por tipo de OA

| Necessidade | Exemplos gratuitos |
| --- | --- |
| Atividades interativas (quiz, arrastar, linha do tempo, vídeo interativo) | H5P, de código aberto (no Moodle, ou no computador com o aplicativo Lumi). Atenção: não permite menu de acessibilidade próprio e nem todos os tipos atendem à WCAG; veja o aviso em `prototipo-e-desenvolvimento.md` |
| Jogos sem programação | GDevelop (código aberto; exporta para navegador e Android) |
| Jogos com programação | Godot (código aberto) |
| Histórias interativas e jogos de escolha | Twine (código aberto) |
| Animações e jogos simples feitos pelos próprios alunos | Scratch |
| Cursos a distância e ambiente virtual | Moodle (código aberto) |
| Textos, apresentações e documentos | LibreOffice (código aberto; formatos abertos ODF) |
| Imagens e ilustrações | Inkscape (vetor), Krita (desenho), GIMP (edição de imagem), todos de código aberto |
| Áudio e narração | Audacity (código aberto) |
| Vídeo | Kdenlive ou Shotcut (edição) e OBS Studio (gravação de tela), de código aberto |
| Publicação na web | GitHub Pages (gratuito), com o OA feito em HTML |
| Repositório e DOI | Zenodo (gratuito), eduCAPES e a Plataforma MEC RED |

## Como a skill conduz

- **Arquitetura (esboço):** ao sugerir o tipo de esboço ou protótipo, sugira também a ferramenta gratuita adequada ao tipo de OA e à equipe disponível. Para professores sem experiência em programação, prefira ferramentas sem código, como H5P, GDevelop e Twine, sempre conferindo a acessibilidade de cada uma. Quando o assistente gera o OA, o HTML5 com menu de acessibilidade é a opção mais flexível.
- **Desenvolvimento:** registre no documento de arquitetura técnica cada tecnologia escolhida, a licença dela e por que atende aos critérios acima.
- **Disponibilização:** prefira hospedagem e repositórios gratuitos, com link persistente.
