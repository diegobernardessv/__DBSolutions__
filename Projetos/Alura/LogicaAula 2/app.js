function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1', 'Jogo do número secreto')
exibirTextoNaTela('p', 'Escolha um número de 1 a 5000')

function verificarChute() {
    console.log('O botão foi clicado!')
}
