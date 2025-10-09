console.log('Bem vindo ao cronômetro interativo.');
let nome = "Diego Bernardes";

console.log(`Olá, ${nome}!`);
alert(`Olá, ${nome}!`);

linguagemPreferida = prompt('Qual a línguagem de programação que você mais gosta?');
console.log(linguagemPreferida);

let valor1 = 10;
let valor2 = 20;
let somaValores = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é ${somaValores}.`);
let subtracaoValores = valor1 - valor2;
console.log(`A diferença de ${valor1} e ${valor2} é ${subtracaoValores}.`);

let idadeUsuario = prompt('Qual a sua idade?');
if (idadeUsuario >= 18) {
    console.log('Você é maior de idade.');
} else {
    console.log('Você é menor de idade.');
}

let numero = prompt('Digite um número:');
if (numero > 0) {
    console.log('O número é positivo.');
} else if (numero < 0) {
    console.log('O número é negativo.');
} else {
    console.log('O número é zero.');
}

let contador = 0;
while (contador <= 10) {
    console.log(contador);
    contador++;
}

let nota = 7
if (nota >= 7) {
    console.log('Aprovado');
} else {
    console.log('Reprovado');

}

let numero1 = parseInt(Math.random() * 10 + 1);
console.log(numero1);
let numero2 = parseInt(Math.random() * 100 + 1);
console.log(numero2);
let numero3 = parseInt(Math.random() * 1000 + 1);
console.log(numero3);