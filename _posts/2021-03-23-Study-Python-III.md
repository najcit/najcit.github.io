---
title: 如何使用 pip 生成和安装 requirements.txt
published: true
categories: [program, python]
---

生成当前环境的依赖库信息 requirements.txt
>
```
pip freeze > requirements.txt
```

利用 requirements.txt 安装依赖库
>
```
pip install -r requirements.txt
```