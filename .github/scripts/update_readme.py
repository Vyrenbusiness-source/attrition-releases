#!/usr/bin/env python3
"""Writes the latest releases into README.md between the update markers.

Runs inside the GitHub Action (.github/workflows/latest-updates.yml). It reads the
public releases of this repository, takes the newest ones (no drafts, no pre-releases)
and renders a short list in English and German. Only the text between
<!-- updates:en:start --> / <!-- updates:en:end --> and the matching :de: markers
is replaced, everything else in the README stays untouched.
"""
import json
import os
import re
import sys
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "Vyrenbusiness-source/attrition-releases")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
COUNT = int(os.environ.get("UPDATE_COUNT", "8"))
SUMMARY_MAX = 220
README = os.environ.get("README_PATH", "README.md")

MONTHS_EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_releases():
    url = f"https://api.github.com/repos/{REPO}/releases?per_page=30"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "attrition-readme-updates",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    rel = [x for x in data if not x.get("draft") and not x.get("prerelease")]
    rel.sort(key=lambda x: x.get("published_at") or "", reverse=True)
    return rel[:COUNT]


def summary(body):
    """First paragraph of the release text, plain, cut at a word boundary."""
    text = (body or "").replace("\r", "")
    para = next((p for p in re.split(r"\n\s*\n", text) if p.strip()), "")
    para = re.sub(r"^#+\s*", "", para.strip(), flags=re.M)
    para = re.sub(r"[*_`]", "", para)
    para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
    para = re.sub(r"\s*\n\s*[-*]?\s*", " · ", para)
    para = re.sub(r"\s+", " ", para).strip()
    if len(para) > SUMMARY_MAX:
        cut = para[:SUMMARY_MAX].rsplit(" ", 1)[0].rstrip(",;:–- ")
        para = cut + " …"
    return para.replace("|", "/")


def version(rel):
    name = rel.get("name") or rel.get("tag_name") or ""
    m = re.search(r"\d+\.\d+\.\d+", name) or re.search(r"\d+\.\d+\.\d+", rel.get("tag_name", ""))
    return m.group(0) if m else name


def render(rels, lang):
    if lang == "en":
        head = "| Version | Date | What changed |\n|---|---|---|"
    else:
        head = "| Version | Datum | Was ist neu |\n|---|---|---|"
    rows = []
    for r in rels:
        d = (r.get("published_at") or "")[:10]
        if len(d) == 10:
            y, mo, dd = d.split("-")
            date = f"{MONTHS_EN[int(mo) - 1]} {int(dd)}, {y}" if lang == "en" else f"{dd}.{mo}.{y}"
        else:
            date = "–"
        rows.append(f"| [**{version(r)}**]({r.get('html_url')}) | {date} | {summary(r.get('body'))} |")
    if not rows:
        rows.append("| – | – | – |")
    return "\n".join([head] + rows)


def replace_block(text, lang, block):
    start = f"<!-- updates:{lang}:start -->"
    end = f"<!-- updates:{lang}:end -->"
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        print(f"marker for {lang} not found", file=sys.stderr)
        return text
    return pat.sub(lambda _m: f"{start}\n{block}\n{end}", text)


def main():
    rels = fetch_releases()
    with open(README, encoding="utf-8") as f:
        old = f.read()
    new = replace_block(old, "en", render(rels, "en"))
    new = replace_block(new, "de", render(rels, "de"))
    if new != old:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
        print(f"README updated with {len(rels)} releases")
    else:
        print("README already up to date")


if __name__ == "__main__":
    main()
