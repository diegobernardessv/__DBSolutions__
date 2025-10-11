let tentativas = 1;
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
        let palavraTentativas = tentativas > 1 ? 'tentativas' : 'tentativa';
        let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${palavraTentativas}.`;
        exibirTextoNaTela('p', mensagemTentativas);
    } else {
        if (chute > numeroSecreto) {
            exibirTextoNaTela('p', 'O número secreto é menor.'); 
            tentativas++;
        } else {
            exibirTextoNaTela('p', 'O número secreto é maior.');
            
        }
    }
    tentativas++;

}

gerarNumeroAleatorio();
console.log(numeroSecreto);

exibirTextoNaTela('h1', 'Jogo do número secreto')

exibirTextoNaTela('p', 'Escolha um número entre 1 e 5000')
