let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 5000 + 1);
}

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

// Limpa campo de chute após tentativa fracassada
function limparCampo() {
    chute = document.querySelector("input")
    chute.value = ''
}

function verificarChute() {
    let chute = document.querySelector("input").value;
    if (chute == numeroSecreto) {
        exibirTextoNaTela("h1", "Acertou!");
        exibirTextoNaTela("p", "Você descobriu o número secreto!");
        let palavraTentativas = tentativas > 1 ? "tentativas" : "tentativa";
        let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${palavraTentativas}.`;
        exibirTextoNaTela("p", mensagemTentativas);
        document.getElementById("reiniciar").removeAttribute("disabled");
    } else {
        if (chute > numeroSecreto) {
            exibirTextoNaTela("p", "O número secreto é menor.");
        } else {
            exibirTextoNaTela("p", "O número secreto é maior.");
        }
        limparCampo();
        tentativas++;
    }
}

function reiniciarJogo() {
    numeroSecreto = gerarNumeroAleatorio();
    limparCampo();
    exibirMensagemInicial();
    tentativas = 1;
    console.log(numeroSecreto); 
    document.getElementById("reiniciar").setAttribute("disabled", true);
}

function exibirMensagemInicial(params) {
    exibirTextoNaTela("h1", "Jogo do número secreto");
    exibirTextoNaTela("p", "Escolha um número entre 1 e 5000");
}

// Inícialização do Jogo
gerarNumeroAleatorio();
exibirMensagemInicial();
console.log(numeroSecreto);
