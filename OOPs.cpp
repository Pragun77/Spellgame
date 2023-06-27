#include <iostream>
using namespace std;

enum shape{ circle, triangle, rectangle};

int main(){
    cout << "Enter shape code:";
    int code;
    cin >> code;
    while(code>= circle && code<= triangle)
    {
        switch (code)
        {
        case circle:
        .......
        .......
        break;
        case rectangle:
        .......
        .......
        break;
        case triangle;
        .......
        .......
        break;
        }
        cout << "Enter shape code:";
        cin >> code;
    }
    cout << "BYE \n";
    return 0;
}