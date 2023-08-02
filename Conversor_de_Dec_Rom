#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//Sistema que converte números decimais em romanos de 1 até 999-Versão 1.
int main(){
   int num,c,d,u;
   char x[10],y[10],z[10],rom[100];
   char* un[]={"","I","II","III","IV","V","VI","VII","VIII","IX"};
   char* de[]={"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
   char* ce[]={"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
   
   printf("digite um numero:");
   scanf("%i",&num);
   
   c=num/100;
   d=(num/10)%10;
   u=num%10;

   if(num>=1 && num<=999){
      if(num>=100){
         sprintf(x,"%s",ce[c]);
         sprintf(y,"%s",de[d]);
         sprintf(z,"%s",un[u]);
         sprintf(rom,"%s%s%s",x,y,z);
         printf("resultado => o numero %i em algarismo romano eh:%s",num,rom);
         printf("\n");
      }
      else if(num>=10){
         sprintf(y,"%s",de[d]);
         sprintf(z,"%s",un[u]);
         sprintf(rom,"%s%s",y,z);
         printf("resultado => o numero %i em algarismo romano eh:%s",num,rom);
         printf("\n");
      }
      else{
         sprintf(z,"%s",un[u]);
         sprintf(rom,"%s",z);
         printf("resultado => o numero %i em algarismo romano eh:%s",num,rom);
         printf("\n");
      }
   }
   else{
         printf("você digitou zero ou um numero muito alto! tente novamente!");
         printf("\n");
   }
   return 0;
}
