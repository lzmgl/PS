#include <iostream>
using namespace std;
main(){
    int h=0, m=0, c=0;
    cin >> h >> m;
    cin >> c;
    m+=c;
    while(m>59){
        m-=60;
        h++;
        while(h>23){
            h-=24;
        }
    }
    cout << h << ' ' << m;
}