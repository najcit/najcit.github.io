---
title: 罗马数字转换阿拉伯数字
published: true
categories: [algorithm]
---

## 题目
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

罗马数字包含以下七种字符：I， V， X， L， C， D 和 M。

|罗马数字 | 阿拉伯数字 |
| I | 1    |
| V | 5    |
| X | 10   |
| L | 50   |
| C | 100  |
| D | 500  |
| M | 1000 |

示例如下，
2 写做 II，即为 I + I ，  
12 写做 XII ，即为 X + II ，  
27 写做 XXVII, 即为 XX + V + II 。  
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，  
4 不写做 IIII，而是 IV 。  
9 表示为 IX 。  
这个特殊的规则只适用于以下六种情况：  
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。  
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。  
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

## 解答

```cpp
// C/C++语言
int RomanToArab(const string & roman) {
    int arab = 0;
    const map<char, int> convert = 
        { {'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1} };
    for (int i = 0; i < roman.size() - 1; ++i) {
        if (convert[roman[i]] < convert[roman[i+1]])
            rarb -= convert[roman[i]];
        else 
            rarb += convert[roman[i]];
    }
    rarb += convert[roman.back()];
    return arab;
}
```

```python
# python3
def RomanToArab(roman):
    rarb = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(roman)-1):
        if convert[roman[i]] < convert[roman[i+1]]:
            rarb -= convert[roman[i]]
        else:
            rarb += convert[roman[i]]
    rarb += convert[roman[-1]]
    return rarb
```
