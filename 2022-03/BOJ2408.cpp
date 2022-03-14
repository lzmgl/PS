#include <iostream>
using namespace std;
main() {
    int dell;
	int a = 0, b = 0, c = 0;
    cin >> a >> b >> c;
    if (a==b && b==c){
        a=10000+a*1000;
        cout << a;
    } else if (a==b || b==c || a==c){
        a=1000+a*100;
        cout<<a;
    } else {
        if (a>b){
            if (b<c){
                if (a>c){
                    a*=100;
                    cout << a;
                } else {
                    c*=100;
                    cout << c;
                }
            } else if (b>c){
                a*=100;
                cout << a;
            }
            
        } else if (a>c)
    }
}