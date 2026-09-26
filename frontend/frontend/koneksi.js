fetch("http://127.0.0.1:8000/api/ringkasan")
    .then(res => res.json())
    .then(hasil => {
        document.getElementById("masuk").textContent = hasil.total_masuk.toLocaleString("id-ID");
        document.getElementById("keluar").textContent = hasil.total_keluar.toLocaleString("id-ID");
        document.getElementById("selisih").textContent = hasil.selisih.toLocaleString("id-ID");

        const tabel = document.getElementById("daftar");
        hasil.data.forEach(baris => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${baris.id}</td>
                <td>${baris.jenis}</td>
                <td>Rp ${baris.jumlah.toLocaleString("id-ID")}</td>
                <td>${baris.waktu}</td>
            `;
            tabel.appendChild(tr);
        });
    });
