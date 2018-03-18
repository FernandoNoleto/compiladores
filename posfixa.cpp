/**
 * Trabalho acadêmico de compiladores
 * Infixa 2 Posfixa
 * Acadêmicos Fernando Noleto e Thiago Silva
 */

#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

/**
 * Precedência entre operadores: * + .
 * 
 */

bool maior_precedencia(char x, char y){
    if(x == '*' && y == '*' || x == '*' && y == '+' || x == '*' && y == '.')
        return true;
    else if(x == '+' && y == '+' || x == '+' && y == '.')
        return true;
    else if (x == '.' && y == '.')
        return true;
    else 
        return false;
}

void in2pos(vector<char> expressao){
    stack <char> pilha;
    vector <char> posfixa;

    for(vector<char>::iterator it = expressao.begin(); it != expressao.end(); it++) {
        
        if(*it == '*' || *it == '+' || *it == '.'){ // Caso seja operador
            if(!pilha.empty()){
                while(maior_precedencia(pilha.top(), *it)){//Verifica precedência de operadores
                    posfixa.push_back(pilha.top()); //copia o topo para a posfixa
                    pilha.pop();
                }
                //pilha.push(*it);
            }
            pilha.push(*it);
        }
        else if (*it == '('){ //Se for '(' então empilhe '('
            pilha.push(*it);
        }
        else if (*it == ')'){ //Se caractere for igual a ')'
            while(pilha.top() != '('){
                posfixa.push_back(pilha.top());
                pilha.pop();
            }
            if(pilha.top() == '(')
                pilha.pop(); //Descartar o '('
        }
        else { //Caso seja operando
            posfixa.push_back(*it); //Copiar para a posfixa
        }
        
    }
    
    while(!pilha.empty()){
        posfixa.push_back(pilha.top());
        pilha.pop();
    }

    for (vector<char>::iterator it = posfixa.begin(); it != posfixa.end(); it++){
        cout << *it << " ";
    }

}

bool validar_expressao(string expr){
    
    int count = 0;
    for(int i = 0; i < expr.length(); i++){
        if(expr[i] == '(')
            count++;
        if(expr[i] == ')')
            count--;
    }
    
    return (count == 0)? true : false;
}

vector<char> tratar_expressao(string expr){

    vector<char> expressao; //expressão em vetor de caracteres //expressão já validada

    char aux = '+'; //aux é o caracter anterior
    for (int i = 0; i < expr.length(); i++) { //tratando a concatenação implícita
        if(expr[i] != ' '){
            if(expr[i] != '*' && expr[i] != '+' && expr[i] != '.' && expr[i] != '(' && expr[i] != ')' && aux != '*' && aux != '+' && aux != '.' && aux != '(' && aux != ')') //xx
                expressao.push_back('.');
            else if(aux != '*' && aux != '+' && aux != '.' && expr[i] == '(') //x(
                expressao.push_back('.');
            else if(aux == ')' && expr[i] != '*' && expr[i] != '+' && expr[i] != '.') //)x
                expressao.push_back('.');
            else if(aux == '*' && expr[i] != '*' && expr[i] != '+' && expr[i] != '.' && expr[i] != '(' && expr[i] != ')') //*x
                expressao.push_back('.');
            else if(aux == ')' && expr[i] == '(') //)(
                expressao.push_back('.');
        }
        if(expr[i] != ' ')
            expressao.push_back(expr[i]);
        aux = expr[i];
    }

    for (vector<char>::iterator it = expressao.begin(); it != expressao.end(); it++){
        cout << *it;    
    }
    cout << "" << endl;

    return expressao;
}

void limpar_tela(){
    #ifdef LINUX
	system("clear");
	#elif defined WIN32
	system("cls");
	#endif
}

int main(){

    limpar_tela();
	
    string expr; //expressão em string //entrada do usuário

    cout << "Digite uma palavra: ";
    getline(cin, expr);

    if(!validar_expressao(expr)){//verificar número de abre e fecha parenteses
        cout << "EXPRESSÃO INVÁLIDA!" << endl;
        cout << "O número de abre e fecha parenteses é imcompatível" << endl;
        return 0;
    }

    vector<char> expressao = tratar_expressao(expr);
    
    //imprimir expressão já validada
    #ifdef LINUX
    cout << "Na notação posfixa: ";
    #elif defined WIN32
    cout << "Na notacao posfixa: ";
    #endif

    in2pos(expressao);//função de coversão

    cout << "" << endl;

    #ifdef WIN32
    system("pause");
    #endif

    
    return 0;

}
