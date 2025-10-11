function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 5000 + 1);
}

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function verificarChute() {
    let chute = document.querySelector('input').value;

    if (chute == numeroSecreto) {
        exibirTextoNaTela('h1', 'Acertou!');
        exibirTextoNaTela('p', 'Você descobriu o número secreto!');
    } else {
        if (chute > numeroSecreto) {
            exibirTextoNaTela('p', 'O número secreto é menor.');
        } else {
            exibirTextoNaTela('p', 'O número secreto é maior.');
        }
    }

}

let numeroSecreto = gerarNumeroAleatorio();

gerarNumeroAleatorio();
console.log(numeroSecreto);

exibirTextoNaTela('h1', 'Jogo do número secreto')

exibirTextoNaTela('p', 'Escolha um número entre 1 e 5000')

verificarChute();
