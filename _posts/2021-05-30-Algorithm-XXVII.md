---
title: 判断字符串是否数值的一种方法
published: true
categories: [algorithm]
---

## 解决思路
```
简单理解就是字符串能否转化为 double 类型数值，因为正常数值都能被 double 所包含，
虽有使用 atof ，strtod 等函数即可解决，由于可能出现 "1234vh" 这种字符串，atof 会解析成 1234 ，
且没有其他信息可以知道是否完全转化成功，推荐使用 strtod 函数可完美解决此缺陷。
```

### 代码
```cpp
bool isDigitStr(const char * str)
{
    char * end = NULL;
    strtod(str, &end);
    return !*end;
}
```