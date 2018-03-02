#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int main(){
    string anyWord;
    vector<char> posfixa;
    stack<char> pilha;

    cout << "Digite uma palavra: ";
    getline(cin, anyWord);

    for (int i = 0; i < anyWord.length(); i++){
        posfixa.push_back(anyWord[i]);
    }

    //cout << posfixa[0] << endl;
    for(vector<char>::iterator it = posfixa.begin(); it != posfixa.end(); it++) {
        if(*it == '+' || *it == '-' || *it == '*' || *it == '/'){
            pilha.push(*it);
        }
        
        else{
            cout << *it << endl;    
        }
        
    }
    
    while(pilha.top()){
        cout << pilha.top() << endl;
        pilha.pop();
    }
    
    

    return 0;

}
