---
title: 坐标轴刻度自适应算法
published: true
categories: [algorithm]
---

## 依据指定数据组生成合适的坐标刻度

```cpp
double calcMajorUnit(double & cormin, double & cormax, int & cornumber) {
    double corstep = (cormax - cormin) / cornumber; // 刻度步长
    double temp = 0.0;  // 数量级
    if (pow(10, (int) (log(corstep) / log(10))) == corstep) {
        temp = pow(10,  floor(log(corstep) / log(10)));
    } else {
        temp = pow(10, floor((log(corstep) / log(10)) + 1));
    }

    // 选取合适的步长
    corstep /= temp;
    if (corstep >= 0 && corstep <= 0.1) {
        corstep = 0.1;
    } else if (corstep >= 0.100001 && corstep <= 0.2) {
        corstep = 0.2;
    } else if (corstep >= 0.200001 && corstep <= 0.25) {
        corstep = 0.25;
    } else if (corstep >= 0.250001 && corstep <= 0.5) {
        corstep = 0.5;
    } else {
        corstep = 1;
    }
    corstep *= temp;

    // 选取合适的最大值和最小值
    if ((int) (cormin / tmpstep) != (cormin / tmpstep)) {
        if (cormin < 0) {
            cormin = (-1) * ceil(abs(cormin / tmpstep)) * tmpstep;
        } else {
            cormin = (int) (abs(cormin / tmpstep)) * tmpstep;
        }
    }
    auto tmpnumber = (cormax - cormin) / tmpstep;
    if (tmpnumber < cornumber) {
        int extranumber = cornumber - tmpnumber;
        tmpnumber = cornumber;
        if (extranumber % 2 == 0) {
            cormax = cormax + tmpstep * (int) (extranumber / 2);
        } else {
            cormax = cormax + tmpstep * (int) (extranumber / 2 + 1);
        }
        cormin = cormin - tmpstep * (int) (extranumber / 2);
    }
    cornumber = tmpnumber;

    return corstep;
}
```