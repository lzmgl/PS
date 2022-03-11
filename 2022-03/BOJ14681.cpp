#include <iostream>
using namespace std;
main() {
    int a=0, b=0;
    cin >> a;
    cin >> b;
    if (a>0){
        if (b>0) 
            cout << "1";
        else if (b<0) 
            cout << "4";
    } else {
        if (b>0) 
            cout << "2";
        else if (b<0) 
            cout << "3";
    }
}