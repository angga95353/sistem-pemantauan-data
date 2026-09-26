from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

basis_data = [
    {"id": 1, "jenis": "Masuk", "jumlah": 8500, "waktu": "2026-09-24"},
    {"id": 2, "jenis": "Keluar", "jumlah": 3200, "waktu": "2026-09-25"},
    {"id": 3, "jenis": "Masuk", "jumlah": 6700, "waktu": "2026-09-26"},
]

@app.get("/api/ringkasan")
def dapatkan_data():
    total_masuk = sum(d["jumlah"] for d in basis_data if d["jenis"] == "Masuk")
    total_keluar = sum(d["jumlah"] for d in basis_data if d["jenis"] == "Keluar")
    return {
        "data": basis_data,
        "total_masuk": total_masuk,
        "total_keluar": total_keluar,
        "selisih": total_masuk - total_keluar
                      }
  
