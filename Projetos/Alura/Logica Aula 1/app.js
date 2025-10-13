// console.log('Bem vindo ao cronômetro interativo.');
// let nome = "Diego Bernardes";

// console.log(`Olá, ${nome}!`);
// alert(`Olá, ${nome}!`);

// linguagemPreferida = prompt('Qual a línguagem de programação que você mais gosta?');
// console.log(linguagemPreferida);

// let valor1 = 10;
// let valor2 = 20;
// let somaValores = valor1 + valor2;
// console.log(`A soma de ${valor1} e ${valor2} é ${somaValores}.`);
// let subtracaoValores = valor1 - valor2;
// console.log(`A diferença de ${valor1} e ${valor2} é ${subtracaoValores}.`);

// let idadeUsuario = prompt('Qual a sua idade?');
// if (idadeUsuario >= 18) {
//     console.log('Você é maior de idade.');
// } else {
//     console.log('Você é menor de idade.');
// }

// let numero = prompt('Digite um número:');
// if (numero > 0) {
//     console.log('O número é positivo.');
// } else if (numero < 0) {
//     console.log('O número é negativo.');
// } else {
//     console.log('O número é zero.');
// }

// let contador = 0;
// while (contador <= 10) {
//     console.log(contador);
//     contador++;
// }

// let nota = 7
// if (nota >= 7) {
//     console.log('Aprovado');
// } else {
//     console.log('Reprovado');

// }

// let numero1 = parseInt(Math.random() * 10 + 1);
// console.log(numero1);
// let numero2 = parseInt(Math.random() * 100 + 1);
// console.log(numero2);
// let numero3 = parseInt(Math.random() * 1000 + 1);
// console.log(numero3);

// function verificarNumero(numero) {
//     if (numero > 0) {
//         console.log('O número é positivo.');
//     } else if (numero < 0) {
//         console.log('O número é negativo.');
//         } else {
//         console.log('O número é zero.');
//     }
// }

// verificarNumero(10);
// verificarNumero(-5);
// verificarNumero(0);

// function dobroDoNumero(numero) {
//     return numero * 2;
// }

// dobroDoNumero(10);
// console.log(dobroDoNumero(10));
// dobroDoNumero(20);
// console.log(dobroDoNumero(20));
// dobroDoNumero(30);
// console.log(dobroDoNumero(30));
// dobroDoNumero(40);
// console.log(dobroDoNumero(40));
// dobroDoNumero(50);
// console.log(dobroDoNumero(50));

// function mediaNumeros(numero1, numero2, numero3) {
//     return (numero1 + numero2 + numero3) / 3;
// }

// mediaNumeros(10, 20, 30);
// console.log(mediaNumeros(100, 70, 92));

// function maiorNumero(numero1, numero2) {
//     if (numero1 > numero2) {
//         return numero1;
//     } else {
//         return numero2;
//     }
// }

// maiorNumero(10, 20);
// console.log(maiorNumero(10, 20));
// maiorNumero(20, 10);
// console.log(maiorNumero(20, 10));

// function potenciaNumero(numero) {
//     return numero * numero;
// }

// potenciaNumero(2);
// console.log(potenciaNumero(2));
// potenciaNumero(3);
// console.log(potenciaNumero(3));
// potenciaNumero(4);
// console.log(potenciaNumero(4));

// function calcularMedia(nota1, nota2, nota3, nota4) {
//     let media = (nota1 + nota2 + nota3 + nota4) / 4;
//     return media;
// }

// function verificarAprovacao(media) {
//     console.log(media >= 5 ? 'Aprovado' : 'Reprovado'); 
// }
 
// let mediaCalculada = calcularMedia(7, 6, 3, 3);
// verificarAprovacao(mediaCalculada);

// function indiceMassaCorporea(peso, altura) {
//     let imc = peso / (altura * altura);
//     return imc;
// }

// let imcCalculado = indiceMassaCorporea(90, 1.80)
// console.log(imcCalculado);

// function valorReal(dolar) {
//     let conversao = (4.80 * dolar)
//     return conversao;
// }

// conversaoRealDolar = valorReal(100);
// console.log(conversaoRealDolar);

// function areaSala(altura, largura) {
//     let area = altura * largura;
//     return area;
// }

// function perimetroSala(altura, largura) {
//     let perimetro = 2 * (altura + largura);
//     return perimetro;
// }

// calculoArea = areaSala(1.80, 1.80);
// alert(`A área da sala é de ${calculoArea} m²`);
// console.log(`A área da sala é de ${calculoArea} m²`);


// calculoPerimetro = perimetroSala(1.80, 1.80);
// alert(`O perímetro da sala é de ${calculoPerimetro} metros`);
// console.log(`O perímetro da sala é de ${calculoPerimetro} metros`);

function tabuadaNumero(numero) {
    console.log(`=== Tabuada de ${numero}. ===`);
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i;
        console.log(`${numero} x ${i} = ${resultado}`);
    }
    console.log(`=== Fim da tabuada de ${numero}. ===`);
    console.log('')
}

tabuadaNumero(1);
tabuadaNumero(2);
tabuadaNumero(3);
tabuadaNumero(4);
tabuadaNumero(5);
tabuadaNumero(6);
tabuadaNumero(7);
tabuadaNumero(8);
tabuadaNumero(9);
tabuadaNumero(10);