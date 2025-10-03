alert("Bem vindo ao jogo do número secreto.")

let numeroSecreto = 6;
let palpite; 
let tentativas = 1;

// enquanto palpite não for igual ao n° secreto
while(palpite != numeroSecreto) {
    palpite = prompt("Escolha um número de 1 a 10");
// se palpite for igual ao número secreto
    if (palpite == numeroSecreto) {
        alert(`Isso aí! Você descobriu o número secreto! O número secreto é o ${numeroSecreto}!`);
        alert(`Você acertou em ${tentativas} tentativas.`)
    } else {
        if (palpite > numeroSecreto) {
            alert(`O número secreto é menor do que o ${palpite}.`);
        } else {
            alert(`O número secreto é maior do que o ${palpite}.`);
            }
            // tentativas = tentativas + 1
            tentativas++;
    }
 }