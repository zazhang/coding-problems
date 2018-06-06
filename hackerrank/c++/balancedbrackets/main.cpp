#include <iostream>
#include <stack>

using namespace std;

bool is_pair(char a, char b){
    auto ascii_a = int(a);
    //cout << ascii_a << endl;
    auto ascii_b = int(b);
    //cout << ascii_b << endl;
    if ((ascii_a == 125 && ascii_b == 123) || (ascii_a == 123 && ascii_b == 125)){
        return true;
    }
    else if ((ascii_a == 91 && ascii_b == 93) || (ascii_a == 93 && ascii_b == 91)){
        return true;
    } else {
        return ((ascii_a ==40 && ascii_b == 41) || (ascii_a == 41 && ascii_b == 40));
    }
}

bool is_balanced(string expression) {
    stack <char> s;
    for(auto ch : expression){
        switch (ch) {
            case '{':
                s.push(ch);
                //cout << s.top() << endl;
                break;
            case '[':
                s.push(ch);
                break;
            case '(':
                s.push(ch);
                break;
            default:
                //cout << s.top() << endl;
                //cout << ch << endl;
                if (s.empty() || !is_pair(ch, s.top())) {
                    return false;
                }
                s.pop();
        }
    }
    return s.empty();
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string expression;
        cin >> expression;
        bool answer = is_balanced(expression);
        if(answer)
            cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}