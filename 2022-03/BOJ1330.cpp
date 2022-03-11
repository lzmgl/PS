#include <iostream>
using namespace std;
main() {
    int a=0,b=0;
    cin >> a >> b;
    if (a>b){
        cout << ">";
    } else if (a<b){
        cout << "<";
    } else {
        cout << "==";
        
    }
}