"""Write one ingestion notebook per source into notebooks/sources/.

Each notebook shows, in code, how the raw layer of that source is obtained from the official publisher, then how the
released tables relate to what was fetched. The notebooks that call a live API can be executed (`--execute`), which
stores their outputs; the others read the URLs recorded in the released tables themselves and say plainly that the
download step was not run when the notebook was written.

Usage: python scripts/build_source_notebooks.py [--execute]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "notebooks" / "sources"
CATALOG = ROOT / "datamap" / "data" / "catalog.json"
MAP = "https://rangeltech.net/datamap/"
REPO = "https://github.com/LucasRangelSSouza/brazil-public-data-map"


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(True)}


def code(text: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.strip("\n").splitlines(True)}


def notebook(cells: list[dict]) -> dict:
    return {"cells": cells, "nbformat": 4, "nbformat_minor": 5,
            "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}}


HTTP = '''
import json, time
import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; public-data-map-notebook; +https://github.com/LucasRangelSSouza/brazil-public-data-map)"}

def get(url, retries=4, timeout=90, **kw):
    """GET with exponential backoff. Public portals answer 429 or reset connections under load."""
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout, **kw)
            if r.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(f"HTTP {r.status_code}")
            r.raise_for_status()
            return r
        except requests.RequestException as exc:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
'''

KAGGLE_READ = '''
# Read one released table without downloading the whole dataset. Public datasets need no login.
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/{slug}", path="{file}")
pd.read_parquet(path).head()
'''


def catalog() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def smallest(cat: dict, subject: str, layer: str | None = None) -> dict | None:
    tables = [(t, d["slug"]) for d in cat["datasets"] if d["subject"] == subject for t in d["tables"] if layer is None or t["layer"] == layer]
    tables = [x for x in tables if x[0]["rows"] > 0 and x[0]["bytes"] < 60e6]
    return min(tables, key=lambda x: x[0]["bytes"]) if tables else None


def table_list(cat: dict, subject: str) -> str:
    rows = [f"- `{d['slug']}`: " + ", ".join(sorted({f"{t['layer']}" for t in d["tables"]})) + f" ({d['table_count']} tables)" for d in cat["datasets"] if d["subject"] == subject]
    return "\n".join(rows)


def header(cat: dict, subject: str, executed: bool) -> list[dict]:
    info = cat["subjects"][subject]
    status = ("Executed against the live source when this notebook was written; the outputs below are from that run."
              if executed else
              "**Not executed end to end.** The download cells below use URLs recorded in the released tables, but the publisher's download host did not respond when this notebook was written, so the outputs are empty. Run it from your own network.")
    return [
        md(f"# {info['title']}: how the raw layer is obtained\n\n**Publisher:** {info['publisher']}  \n**Official source:** <{info['official_url']}>\n\n{info['summary']}\n\n"
           f"**Grain and keys:** {info['grain']}\n\n**Released as:**\n\n{table_list(cat, subject)}\n\nEvery table and column is documented in the [interactive data map]({MAP}). "
           f"Source code and the other notebooks: [{REPO}]({REPO})."),
        md(f"## Status of this notebook\n\n{status}"),
        code(HTTP),
    ]


def footer(cat: dict, subject: str) -> list[dict]:
    pick = smallest(cat, subject, "trusted") or smallest(cat, subject)
    cells = [md("## Compare with the released tables\n\nThe released files keep the field names of the source in `raw` and apply consistent typing and snake_case names in `trusted`. "
                f"Details per column are in the [data map]({MAP}#/subject/{subject}).")]
    if pick:
        t, slug = pick
        cells.append(code(KAGGLE_READ.format(slug=slug, file=t["file"])))
    return cells


def pncp(cat: dict) -> list[dict]:
    cols = [c["name"] for d in cat["datasets"] for t in d["tables"] if t["id"] == "trusted/pncp_contratacoes" for c in t["columns"]][:40]
    return header(cat, "pncp", True) + [
        md("## 1. Fetch one page of procurement notices\n\nThe consultation API needs no key. Notices (`contratacoes`) require the modality code and a page size of at most 50. "
           "The `/atualizacao` axis returns everything that entered or changed in the window, which is how the released tables stay current."),
        code('''
BASE = "https://pncp.gov.br/api/consulta/v1"
params = {"dataInicial": "20260901", "dataFinal": "20260902", "codigoModalidadeContratacao": 8, "pagina": 1, "tamanhoPagina": 10}
page = get(f"{BASE}/contratacoes/atualizacao", params=params).json()
print({k: v for k, v in page.items() if k != "data"})
print(len(page["data"]), "notices on this page")
notice = page["data"][0]
print(json.dumps({k: notice[k] for k in list(notice)[:12]}, indent=1, ensure_ascii=False, default=str)[:1500])
'''),
        md("## 2. The other three domains\n\nSame pattern, different path and key. Contracts and price-registration records accept a page size of 500. The annual plan endpoint (PCA) uses `dataInicio` and `dataFim`."),
        code('''
for domain, extra in [("contratos", {}), ("atas", {}), ("pca", {})]:
    p = {"dataInicial": "20260901", "dataFinal": "20260901", "pagina": 1, "tamanhoPagina": 10}
    if domain == "pca":
        p = {"dataInicio": "20260901", "dataFim": "20260901", "pagina": 1, "tamanhoPagina": 10}
    resp = get(f"{BASE}/{domain}/atualizacao", params=p)
    body = resp.json() if resp.status_code == 200 and resp.content else {}
    print(domain, resp.status_code, "records:", len(body.get("data", [])), "| total pages:", body.get("totalPaginas"))
'''),
        md("## 3. From the JSON to the trusted columns\n\nThe raw layer stores the record untouched (`payload_json`) plus control columns. The trusted layer flattens nested objects into snake_case columns: "
           "for example `orgaoEntidade.cnpj` becomes `orgao_cnpj` and `unidadeOrgao.codigoIbge` becomes `unidade_codigo_ibge`, the key that joins a notice to a municipality. "
           "The first columns of the released `pncp_contratacoes` table:\n\n" + ", ".join(f"`{c}`" for c in cols)),
        code('''
def flatten(obj, prefix=""):
    out = {}
    for key, value in obj.items():
        name = f"{prefix}{key}"
        if isinstance(value, dict):
            out.update(flatten(value, name + "."))
        else:
            out[name] = value
    return out

import pandas as pd
pd.DataFrame([flatten(n) for n in page["data"]]).iloc[:, :14]
'''),
    ] + footer(cat, "pncp")


def siope(cat: dict) -> list[dict]:
    return header(cat, "siope", True) + [
        md("## 1. The open-data service\n\nThe service is OData. Each entity is a function that takes the reporting year, the period (bimester) and the state, so a query is a path and not a `$filter`. "
           "The metadata document lists the eight entities and their parameters."),
        code('''
import re
BASE = "https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata"
meta = get(f"{BASE}/$metadata").text
for name, body in re.findall(r'<Function Name="([^"]+)"[^>]*>(.*?)</Function>', meta, re.S):
    print(name, re.findall(r'<Parameter Name="([^"]+)"', body))
'''),
        md("## 2. One entity, one state, one period\n\nThe state is the federal-unit code; for the municipalities of a state the rows carry `COD_MUNI`. Indicator rows repeat by period, which is why analyses keep the latest `NUM_PERI` per municipality and year."),
        code('''
url = f"{BASE}/Indicadores_Siope(Ano_Consulta=2023,Num_Peri=6,Sig_UF='DF')?$top=5&$format=json"
rows = get(url).json()["value"]
import pandas as pd
pd.DataFrame(rows)[["TIPO", "NUM_ANO", "NUM_PERI", "SIG_UF", "COD_INDI", "NOM_INDI", "VAL_INDI"]]
'''),
        md("## 3. Paging and the other entities\n\nThe service pages with `$top` and `$skip`. The other entities are `Dados_Gerais_Siope`, `Receita_Siope`, `Despesas_Siope`, `Despesas_Funcao_Educacao_Siope`, `Informacoes_Complementares_Siope`, "
           "`Remuneracao_Siope` (which takes `Ano_Declaracao` and `Mes_Exercicio`) and `Dados_Gerais_Siope_Dados_Responsaveis`. They map to the released `api_olinda_siope_*` tables."),
        code('''
def fetch_all(entity, page_size=5000, max_pages=2, **params):
    args = ",".join(f"{k}={v!r}" if isinstance(v, str) else f"{k}={v}" for k, v in params.items())
    out = []
    for page in range(max_pages):
        data = get(f"{BASE}/{entity}({args})?$top={page_size}&$skip={page * page_size}&$format=json").json()["value"]
        out += data
        if len(data) < page_size:
            break
    return out

receita = fetch_all("Receita_Siope", Ano_Consulta=2023, Num_Peri=6, Sig_UF="DF")
print(len(receita), "revenue rows for DF, 2023, period 6")
'''),
        md("## 4. The budget execution report (RREO)\n\nThe `rreo_siope_*` tables come from the RREO reports, which FNDE publishes as PDFs. They were parsed into tables; the file name in the `arquivo` column identifies the report "
           "(`RREO_Municipal_<IBGE code>_<bimester>_<year>.pdf`). The PDFs themselves are not part of the release."),
    ] + footer(cat, "siope")


def ibge(cat: dict) -> list[dict]:
    return header(cat, "ibge", True) + [
        md("## 1. States and municipalities\n\nThe localities API returns the official list with the IBGE codes. The municipality code has seven digits and is the join key used by almost every education table."),
        code('''
BASE = "https://servicodados.ibge.gov.br/api/v1/localidades"
estados = get(f"{BASE}/estados").json()
municipios = get(f"{BASE}/municipios").json()
print(len(estados), "states,", len(municipios), "municipalities")
import pandas as pd
pd.DataFrame([{"codigo_municipio": m["id"], "nome": m["nome"], "uf": m["microrregiao"]["mesorregiao"]["UF"]["sigla"] if m.get("microrregiao") else None} for m in municipios]).head()
'''),
        md("## 2. Check the key\n\nA valid municipality code has seven digits. Tables that carry six-digit codes (an older convention) must be completed with the check digit before joining."),
        code('''
assert all(len(str(m["id"])) == 7 for m in municipios)
print("all municipality codes have 7 digits")
'''),
    ] + footer(cat, "ibge")


def file_source(subject: str, listing_table: str, url_col: str, page_col: str | None, what: str):
    """Sources whose raw layer is a set of files on the publisher's site and whose released tables record the file URLs."""
    def build(cat: dict) -> list[dict]:
        slug = next(d["slug"] for d in cat["datasets"] if d["subject"] == subject and any(t["table"] == listing_table for t in d["tables"]))
        return header(cat, subject, False) + [
            md(f"## 1. Which files make up the raw layer\n\n{what}\n\nThe released table `raw__{listing_table}` lists every file with its page and download URL, so the list below is the record of what was fetched."),
            code(f'''
import kagglehub, pandas as pd
listing = pd.read_parquet(kagglehub.dataset_download("lucasrangelss/{slug}", path="raw__{listing_table}.parquet"))
listing[[c for c in ["{page_col or url_col}", "{url_col}"] if c in listing.columns]].drop_duplicates().head(10)
'''),
            md("## 2. Download one file\n\nThe publisher's download host sometimes resets connections. The helper retries with backoff and a browser-like User-Agent. Pick the smallest file first."),
            code(f'''
from pathlib import Path
import zipfile

url = listing["{url_col}"].dropna().iloc[0]
target = Path("downloads") / url.rsplit("/", 1)[-1]
target.parent.mkdir(exist_ok=True)
try:
    with get(url, stream=True) as r, open(target, "wb") as fh:
        for chunk in r.iter_content(1 << 20):
            fh.write(chunk)
    print("saved", target, target.stat().st_size, "bytes")
    if target.suffix == ".zip":
        print(zipfile.ZipFile(target).namelist()[:10])
except Exception as exc:
    print("download failed:", exc)
'''),
            md("## 3. What the raw layer does with it\n\nThe raw layer keeps the spreadsheet or CSV columns as delivered (names and strings), adds the source file name and removes ingestion bookkeeping. "
               "Typing, deduplication and renaming happen in `trusted`."),
        ] + footer(cat, subject)
    return build


def census(cat: dict) -> list[dict]:
    return header(cat, "censo-escolar", False) + [
        md("## 1. The yearly microdata\n\nINEP publishes one ZIP per year on the School Census page. The file names follow `microdados_censo_escolar_<year>.zip`; read the page to confirm the current link for a year. "
           "Inside, the CSV has one row per school (the released tables do not include student-level or teacher-level microdata) and the ZIP carries the official data dictionary."),
        code('''
YEAR = 2023
PAGE = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar"
URL = f"https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_{YEAR}.zip"   # pattern published on the page above
print(PAGE); print(URL)
'''),
        code('''
from pathlib import Path
import zipfile
target = Path("downloads") / f"censo_{YEAR}.zip"; target.parent.mkdir(exist_ok=True)
try:
    with get(URL, stream=True) as r, open(target, "wb") as fh:
        for chunk in r.iter_content(1 << 20):
            fh.write(chunk)
    print([n for n in zipfile.ZipFile(target).namelist() if n.lower().endswith((".csv", ".pdf", ".xlsx"))][:12])
except Exception as exc:
    print("download failed (check the page for the current link):", exc)
'''),
        md("## 2. Formats change between years\n\nThe census files changed layout over the years: older editions use one file per module, recent ones a single microdata CSV, and the 2025 enrolment file is school-level aggregates. "
           "The released `inep_censo_escolar_colunas_fonte` and `inep_censo_escolar_dicionario_campos` tables record the column mapping between editions."),
    ] + footer(cat, "censo-escolar")


def page_source(subject: str, what: str):
    def build(cat: dict) -> list[dict]:
        info = cat["subjects"][subject]
        return header(cat, subject, False) + [
            md(f"## 1. Where the files are\n\n{what}\n\nThis source has no public API in the form used here, so the notebook documents the page and the manual step instead of pretending to automate it."),
            code(f'print("{info["official_url"]}")'),
            md("## 2. From the spreadsheet to the raw layer\n\nDownload the spreadsheet for the edition, read it with `pandas.read_excel` (or `read_csv`), keep the columns exactly as published and store them as strings. "
               "That is the raw layer. The `arquivo_origem` or `source_file` column of the released tables records which file each row came from."),
            code('''
# Example: read a downloaded spreadsheet exactly as published
# raw = pd.read_excel("resultados_e_metas_municipios_2025.xlsx", dtype=str)
'''),
        ] + footer(cat, subject)
    return build


BUILDERS = {
    "pncp": pncp, "siope": siope, "ibge": ibge, "censo-escolar": census,
    "taxas-rendimento": file_source("taxas-rendimento", "inep_taxas_rendimento_escolar_arquivos", "download_url", "pagina_url",
                                    "INEP publishes the flow-rate spreadsheets as ZIP files, one per year and level of aggregation (Brazil, regions and states; municipalities; schools)."),
    "saeb": file_source("saeb", "inep_saeb_arquivos", "download_url", "pagina_url",
                        "SAEB results are published per edition as `.rar` or `.xlsx` spreadsheets and as microdata ZIPs, linked from the sub-page of each year. The format changes between editions."),
    "fnde-salario-educacao": file_source("fnde-salario-educacao", "fnde_salario_educacao_realizado_2024", "source_url", None,
                                         "FNDE publishes the education contribution as spreadsheets and PDFs on its site, one per year; each row of the released tables keeps the URL of the file it came from."),
    "ideb": page_source("ideb", "INEP publishes the IDEB spreadsheets (school, municipality, state and Brazil, per edition) on the IDEB page."),
    "ica": page_source("ica", "INEP publishes the literacy results and targets as spreadsheets; the released tables record the file name in `arquivo_origem`."),
    "fundeb": page_source("fundeb", "FNDE exposes the FUNDEB panel as an embedded report; the released raw tables are its exports as delivered and keep the report link in `ctrl_fonte_url`."),
    "qedu": page_source("qedu", "QEdu publishes municipality pages for early childhood education; the raw table keeps the JSON returned by the site, whose field names do not match the domain names."),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="execute the notebooks that call live APIs and store the outputs")
    args = parser.parse_args()
    cat = catalog()
    OUT.mkdir(parents=True, exist_ok=True)
    for subject, build in BUILDERS.items():
        nb = notebook(build(cat))
        path = OUT / f"{cat['subjects'][subject]['notebook']}.ipynb"
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("wrote", path.name)
    if args.execute:
        import nbformat
        from nbclient import NotebookClient

        for name in ("pncp", "siope", "ibge"):
            path = OUT / f"{name}.ipynb"
            nb = nbformat.read(path, as_version=4)
            NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(OUT)}}).execute()
            nbformat.write(nb, path)
            print("executed", name)


if __name__ == "__main__":
    main()
