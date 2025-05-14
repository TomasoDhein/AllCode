#include <stdio.h>

void main() {
    int num, soma = 0, qtd = 0;

    printf("Digite valores positivos (Caso digite um valor negativo o bloco encerrará)!!!\n\n");
    printf("==========================================================\n\n");

    do{
        printf("Valor: ");
        scanf("%d", &num);

            if (num < 0) break;

        soma += num;
        qtd++;
    }
    while (1==1);
    float media = soma / qtd;
        
        printf("A média dos valores é: %.2f\n", media);
        
    printf("\n====================================================");
    }
