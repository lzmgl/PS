#include <iostream>
using namespace std;
main() {
	int a = 0, b = 0;
    cin >> a;
    cin >> b;
    int d=b%10;
    cout << a*d << endl;
    d = (b/10)%10;
    cout << a*d << endl;
    d = (b/100)%10;
    cout << a*d << endl;
    cout << a*b << endl;
}