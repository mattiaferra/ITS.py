function aggiungiProdotto() {
    const input = document.getElementById('inputProdotto');
    const prodotto = input.value.trim();

    if (prodotto !== '') {
        const lista = document.getElementById('listaSpesa');
        const nuovoElemento = document.createElement('li');
        nuovoElemento.textContent = prodotto;
        lista.appendChild(nuovoElemento);
        input.value = ''; // Pulisce l'input dopo l'aggiunta
    }
}


function cancellaLista() {
    const lista = document.getElementById('listaSpesa');
    lista.innerHTML = '';

}