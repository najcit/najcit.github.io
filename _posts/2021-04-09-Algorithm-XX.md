---
title: 数据排列问题
published: true
categories: [algorithm]
---

# 描述
```
输入一组数据 A，和间隔数值 N;
A 可能含有相同数字; 
相同数字间排列隔需要间隔 N 个空间;
每个数字占据1个空间；
不同数字可以相邻排列;
求排列数组需要的最小的空间S。
例子：
A = 2 2 2 3
N = 2
S = 7
```

# 解答
```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    string str; 
    int n;
    cin >> str >> n;
    vector<int> data;
    while (!str.empty()) {
        auto i = str.find(',');
        if (i == string::npos) {
            data.push_back(atoi(str.c_str()));
            str.erase(0);
        }
        else {
            data.push_back(atoi(str.substr(0, i).c_str()));
            str.erase(0, i + 1);
        }
    }

    map<int, int> mdata;
    for (auto & d : data)
        mdata[d]++;

    int count = 0;
    vector<int> cache(n, -1);
    while (!data.empty()) {
        auto it = find_if(data.begin(), data.end(),
            [&cache, &mdata](const int& v) {
            auto mit = mdata.end();
            int max = 0;
            for (auto i = mdata.begin(); i != mdata.end(); ++i) {
                auto it = find(cache.begin(), cache.end(), i->first);
                if (it != cache.end())
                    continue;
                if (i->second > max) {
                    max = i->second;
                    mit = i;
                }
            }
            return mit->first == v;
        });
        if (it != data.end()) {
            cout << *it << endl;
            cache[count % n] = (*it);
            mdata[*it]--;
            data.erase(it);
        }
        else {
            cout << -1 << endl;
            cache[count % n] = -1;
        }
        count++;
    }
    cout << count;

    return 0;
}
```