"""Monta as diretrizes de acessibilidade dentro da Intera-IA (skill metodologia-intera).

As skills separadas (wcag-sem-complicacao, mobiledu-diretrizes, rpg-du-diretrizes) são a fonte.
Este script copia o conteúdo delas para metodologia-intera/references/ a cada nova versão.
Não edite os arquivos gerados à mão: corrija na skill separada e rode o script de novo.

Uso: python montar-pacote.py <pasta-wcag> <pasta-mobiledu> <pasta-rpg-du>
Cada pasta é a skill descompactada (com SKILL.md na raiz).
"""
import re, sys, pathlib

DESTINO = pathlib.Path(__file__).parent / "metodologia-intera" / "references"
SKILLS = [
    ("wcag-sem-complicacao", "diretrizes-wcag.md", "1.0.2", "10.5281/zenodo.23837715",
     "https://github.com/jcbraga1-ux/wcag-sem-complicacao-skill"),
    ("mobiledu-diretrizes", "diretrizes-mobiledu.md", "1.0.2", "10.5281/zenodo.23809314",
     "https://github.com/jcbraga1-ux/mobiledu-skill"),
    ("rpg-du-diretrizes", "diretrizes-rpg-du.md", "1.0.1", "10.5281/zenodo.23836531",
     "https://github.com/jcbraga1-ux/rpg-du-skill"),
]

def cabecalho(nome, versao, doi, repo):
    return (f"> Este arquivo faz parte da Intera-IA (skill metodologia-intera) e reproduz a skill "
            f"`{nome}` v{versao}, licença CC BY-NC 4.0, DOI {doi} ({repo}). "
            f"Onde o texto abaixo diz \"esta skill\", leia \"este conjunto de diretrizes\". "
            f"Não edite aqui: as correções são feitas na skill separada e copiadas para cá a cada versão.\n\n")

def corpo(skill_md):
    texto = skill_md.read_text(encoding="utf-8")
    return re.sub(r"\A---\n.*?\n---\n+", "", texto, flags=re.S)

def main(pastas):
    for (nome, arquivo, versao, doi, repo), pasta in zip(SKILLS, pastas):
        pasta = pathlib.Path(pasta)
        texto = corpo(pasta / "SKILL.md")
        if nome == "rpg-du-diretrizes":
            texto = texto.replace("references/diretrizes.md", "references/diretrizes-rpg-du-completas.md")
            completas = (pasta / "references" / "diretrizes.md").read_text(encoding="utf-8")
            (DESTINO / "diretrizes-rpg-du-completas.md").write_text(
                cabecalho(nome, versao, doi, repo) + completas, encoding="utf-8")
        (DESTINO / arquivo).write_text(cabecalho(nome, versao, doi, repo) + texto, encoding="utf-8")
        print("ok", arquivo)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(sys.argv[1:])
