#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

bool menor_precedencia(char x, char y){
    if(x == '+' && y == '*' || x == '+' && y == '/'){
        return true;
    }
    else if(x == '-' && y == '*' || x == '-' && y == '/'){
        return true;
    }
    else {
        return false;
    }
}

void in2pos(vector<char> posfixa){
    stack <char> pilha;

    for(vector<char>::iterator it = posfixa.begin(); it != posfixa.end(); it++) {
        if(*it == '+' || *it == '-' || *it == '*' || *it == '/'){
            if(!pilha.empty()){
                if(menor_precedencia(*it, pilha.top())){//Verifica precedência de operadores
                    cout << pilha.top() << "";
                    pilha.pop();
                }
            }
            pilha.push(*it);
        }
        else if(*it == ' '){
            continue;
        }
        else if (*it == '('){
            pilha.push(*it);
            //continue;
        }
        else if (*it == ')'){
            while(pilha.top() != '('){
                if(pilha.top() != '(')
                    cout << pilha.top() << "";
                pilha.pop();
            }
        }
        else{
            cout << *it << " ";    
        }
        
    }
    
    while(!pilha.empty()){
        if(pilha.top() != '(')
            cout << pilha.top() << "";
        pilha.pop();
    }

}

int main(){
    system("clear");
    string expr;//expressão 
    vector<char> posfixa; //vetor posfixa
    //stack<char> pilha; //

    cout << "Digite uma palavra: ";
    getline(cin, expr);

    for (int i = 0; i < expr.length(); i++){
        posfixa.push_back(expr[i]);
    }

    cout << "Na notação posfixa: ";

    in2pos(posfixa);

    cout << "" << endl;
    

    return 0;

}
