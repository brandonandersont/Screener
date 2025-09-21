from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load once at startup (fast thereafter)
_df = pd.read_excel("Daftar Saham  - 20250920.xlsx")  # columns: Kode, Nama Perusahaan, Tanggal Pencatatan
_df = _df.rename(columns={
    "Kode": "code",
    "Nama Perusahaan": "name",
    "Tanggal Pencatatan": "date"
})
_df["code_l"] = _df["code"].str.lower()
_df["name_l"] = _df["name"].str.lower()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/stocks")
def api_stocks():
    page = max(int(request.args.get("page", 1)), 1)
    size = min(max(int(request.args.get("page_size", 200)), 1), 500)
    q = (request.args.get("query") or "").strip().lower()

    df = _df
    if q:
        m = df["code_l"].str.contains(q, na=False) | df["name_l"].str.contains(q, na=False)
        df = df[m]

    total = len(df)
    start = (page - 1) * size
    items = df.iloc[start:start+size][["code", "name", "date"]].to_dict(orient="records")
    return jsonify({"total": total, "items": items})
