#include<iostream>
#include<string>
#include <vector>

using namespace std;

int main(){
    string anyWord;
    vector<char> posfixa;

    cout << "Digite uma palavra: ";
    getline(cin, anyWord);

    for (int i = 0; i < anyWord.length(); i++){
        posfixa.push_back(anyWord[i]);
    }

    cout << posfixa[0] << endl;

    return 0;

} //end main
