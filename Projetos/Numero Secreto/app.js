alert("Bem vindo ao jogo do número secreto.")

let numeroSecreto = 10;
console.log(numeroSecreto);
let chute = prompt("Digite um número:");

// se chute for igual ao número secreto
if (chute == numeroSecreto) {
    alert("Isso aí! Você descobriu o número secreto" + " :" + numeroSecreto + ".");
} else {
    alert("Você errou! :(");
}
