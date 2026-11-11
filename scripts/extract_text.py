#!/usr/bin/env python3
"""
extract_text.py — pull clean text out of almost any file, ready to be
turned into a braingraph brain.

Usage:
    python -I scripts/extract_text.py path/to/file [more files...]

Supported: .pdf .docx .pptx .xlsx/.xlsm .csv/.tsv .html/.htm .json .md .txt
(and any other file is read as plain UTF-8 text).

Heavy formats need an optional library; if one is missing the script tells
you exactly what to `pip install`. The braingraph HTML stays zero-dependency —
this helper is just for the extraction step.

Output: clean text on stdout. Pipe it, save it, or paste it into the brain,
then structure it as  # center / ## branch / - leaf.
"""
import sys, os, json, csv, io, html, re

def _need(pkg):
    return (f"[extract_text] missing optional library for this format.\n"
            f"               install it with:  pip install {pkg}")

def from_pdf(path):
    try:
        import pdfplumber
        out = []
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                t = page.extract_text() or ""
                if t.strip():
                    out.append(t)
        return "\n\n".join(out)
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader
        except ImportError:
            return _need("pdfplumber   (or: pypdf)")
    reader = PdfReader(path)
    return "\n\n".join((p.extract_text() or "") for p in reader.pages)

def from_docx(path):
    try:
        import docx
    except ImportError:
        return _need("python-docx")
    d = docx.Document(path)
    parts = [p.text for p in d.paragraphs if p.text.strip()]
    for tbl in d.tables:
        for row in tbl.rows:
            cells = [c.text.strip() for c in row.cells]
            if any(cells):
                parts.append(" | ".join(cells))
    return "\n".join(parts)

def from_pptx(path):
    try:
        from pptx import Presentation
    except ImportError:
        return _need("python-pptx")
    prs = Presentation(path)
    out = []
    for i, slide in enumerate(prs.slides, 1):
        lines = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    txt = "".join(r.text for r in para.runs).strip()
                    if txt:
                        lines.append(txt)
        if lines:
            out.append(f"# Slide {i}\n" + "\n".join(lines))
    return "\n\n".join(out)

def from_xlsx(path):
    try:
        import openpyxl
    except ImportError:
        return _need("openpyxl")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"# {ws.title}")
        for row in ws.iter_rows(values_only=True):
            cells = ["" if v is None else str(v) for v in row]
            if any(c.strip() for c in cells):
                out.append(" | ".join(cells).rstrip(" |"))
    return "\n".join(out)

def from_delimited(path, delim):
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        rows = list(csv.reader(f, delimiter=delim))
    return "\n".join(" | ".join(r) for r in rows if any(c.strip() for c in r))

def from_html(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)</(p|div|h[1-6]|li|tr|br)>", "\n", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    lines = [ln.strip() for ln in raw.splitlines()]
    return "\n".join(ln for ln in lines if ln)

def from_json(path):
    data = json.load(open(path, encoding="utf-8", errors="replace"))
    return json.dumps(data, ensure_ascii=False, indent=2)

def from_text(path):
    return open(path, encoding="utf-8", errors="replace").read()

HANDLERS = {
    ".pdf": from_pdf, ".docx": from_docx, ".pptx": from_pptx,
    ".xlsx": from_xlsx, ".xlsm": from_xlsx,
    ".csv": lambda p: from_delimited(p, ","),
    ".tsv": lambda p: from_delimited(p, "\t"),
    ".html": from_html, ".htm": from_html, ".json": from_json,
}

def extract(path):
    ext = os.path.splitext(path)[1].lower()
    return HANDLERS.get(ext, from_text)(path)

def main(argv):
    if not argv:
        print(__doc__); return 1
    chunks = []
    for path in argv:
        if not os.path.isfile(path):
            print(f"[extract_text] not a file: {path}", file=sys.stderr); continue
        try:
            text = extract(path)
        except Exception as e:
            print(f"[extract_text] failed on {path}: {e}", file=sys.stderr); continue
        if len(argv) > 1:
            chunks.append(f"===== {os.path.basename(path)} =====\n{text}")
        else:
            chunks.append(text)
    sys.stdout.write("\n\n".join(chunks).strip() + "\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
