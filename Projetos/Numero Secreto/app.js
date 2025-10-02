alert("Bem vindo ao jogo do número secreto.")

let numeroSecreto = 10;
console.log(numeroSecreto);

let chute = prompt("Digite um número:");
console.log("Valor do chute:", chute);

// se chute for igual ao número secreto
if (chute == numeroSecreto) {
    console.log("Resultado da comparação:", chute == numeroSecreto);
    alert(`Isso aí! Você descobriu o número secreto! ${numeroSecreto}`);
} else {
    alert("Você errou! :(");
    console.log("Valor do número secreto:", numeroSecreto);
    alert(`O número secreto era ${numeroSecreto}`)
}
