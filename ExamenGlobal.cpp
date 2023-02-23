//Este es mi examen global de fundamentos de programacion de el primer semestre del CETI

#include<iostream>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
using namespace std;

int main(){
	int n1,n2, eleccion, result;
	
	while(true){
		cout<<"Elije una opcion:\n1.suma de dos numeros\n2.elevar al cubo\n3.tabla de multiplicar\n>>";cin>>eleccion; 

		switch(eleccion){
			case 1: cout<<"Elije el primer numero: ";cin>>n1;cout<<"Elije el segundo numero: ";cin>>n2; result = n1 + n2; cout<<"El resultado es: "<<result;break;
			case 2: cout<<"Elije un numero: ";cin>>n1;result = pow(n1, 3);cout<<"El resultado es: "<<result;break;
			case 3: cout<<"Elije un numero: ";cin>>n1;
			for(int i=0;i<10;i++){
				result = i * n1;
				printf("%i x %i = %i\n", n1, i, result);
			}
		}
		getch();
		system("cls");
	}
}
