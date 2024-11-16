function convertir() {
    const cantidad = parseFloat(document.getElementById("cantidad").value);
    const moneda1 = document.getElementById("moneda1").value;
    const moneda2 = document.getElementById("moneda2").value;

    if (isNaN(cantidad)) {
        alert("Ingresa una cantidad válida");
        return;
    }

    const tasaCambio = {
        usd: { mxn: 20, eur: 0.85 },
        mxn: { usd: 0.05, eur: 0.043 },
        eur: { usd: 1.18, mxn: 23.5 }
    };

    let resultado = 0;

    if (moneda1 === moneda2) {
        resultado = cantidad;
    } else {
        resultado = cantidad * tasaCambio[moneda1][moneda2];
    }

    document.getElementById("resultado").innerHTML = `<h3><hr> ${cantidad} ${moneda1.toUpperCase()} = ${resultado.toFixed(2)} ${moneda2.toUpperCase()}</h3>`;

    // Selección de imagen según la moneda de destino
    const imagenesMoneda = {
        usd: "img/dolar.png",
        mxn: "img/peso.png",
        eur: "img/euro.png"
    };
    document.getElementById("imagen-moneda").innerHTML = `<img src="${imagenesMoneda[moneda2]}" alt="${moneda2.toUpperCase()}">`;
}
