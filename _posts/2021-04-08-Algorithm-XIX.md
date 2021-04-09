---
title: 四则运算
published: true
categories: [algorithm]
---

# 描述
```
输入一个表达式（用字符串表示），求这个表达式的值
```

# 解答
```cpp
#include <iostream>
#include <stack>

using namespace std;

int compute(const string & data, int & start) {
    stack<int> st;
    int val = 0;
    char flag = data.front() == '-' ? '-' : '+';
    int end = data.size()-1;
    int & i = start;
    while (i <= end) {
    if (data[i] == '{' || data[i] == '[' || data[i] == '(') {
            val = compute(data, ++i);
        } else {
            while (isdigit(data[i]) && i <= end) {
                val = val * 10 + (data[i++] - '0');
            };
        }
        
        switch (flag) {
            case '+':
                st.push(val);
                break;
            case '-':
                st.push(-val);
                break;
            case '*': {
                auto & v = st.top();
                v *= val;
                break;
            }
            case '/': {
                auto & v = st.top();
                v /= val;
                break;
            }
            default:
                break;
        }
        
        if (data[i] == '}' || data[i] == ']' || data[i] == ')') {
            i++;
            break;
        }

        // 下一个数字的运算符
        if (i <= end)
            flag = data[i];
        
        i++;
        val = 0;
    };
    
    int result = 0;
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    
    return result;
}

int compute(const string & data) {
    int start = 0;
    return compute(data, start);
}

int main() {
    string data;
    while (cin >> data)
        cout << compute(data) << endl;
    return 0;
}
```