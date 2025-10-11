let tentativas = 0;
let numeroSecreto = gerarNumeroAleatorio();

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
        tentativas++
        if (tentativas == 1) {
            exibirTextoNaTela('p', 'Você acertou em 1 tentativa.');
        } else {
            exibirTextoNaTela('p', `Você acertou em ${tentativas} tentativas.`);
        }
    } else {
        if (chute > numeroSecreto) {
            exibirTextoNaTela('p', 'O número secreto é menor.'); 
            tentativas++;
        } else {
            exibirTextoNaTela('p', 'O número secreto é maior.');
            tentativas++;
        }
    }

}

gerarNumeroAleatorio();
console.log(numeroSecreto);

exibirTextoNaTela('h1', 'Jogo do número secreto')

exibirTextoNaTela('p', 'Escolha um número entre 1 e 5000')
