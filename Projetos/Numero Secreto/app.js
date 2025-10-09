alert("Bem vindo ao jogo do número secreto.")

let numeroSecreto = parseInt(Math.random(1, 101) * 100);
let palpite; 
let tentativas = 1;
console.log(`O número secreto é: '${numeroSecreto}`);

// enquanto palpite não for igual ao n° secreto
while(palpite != numeroSecreto) {
    palpite = prompt("Escolha um número de 1 a 100");
// se palpite for igual ao número secreto
    if (palpite == numeroSecreto) {
        break;
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

 // Diferenciando tentativa maior e menor do que 1;
    let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa'
    alert(`Isso aí! Você descobriu o número secreto! O número secreto é o ${numeroSecreto}!`);
    alert(`Você acertou em ${tentativas} ${palavraTentativa}.`)
