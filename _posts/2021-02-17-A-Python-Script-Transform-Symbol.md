---
title: 一个用于中英文符号转换的Python脚本
published: true
categories: [program]
tags: [fit, c]
---

实现思路:  
半角符号符号和全角符号的编码有一个规律：  
如:,!?()[]，英文符号的unicode编码+65248＝中文符号的unicode编码。  
对待引号""需要特殊对待, 将""所包含的内容都替换“”包含内容
对待句号，就直接替换即可

英文符号 => 中文符号
```python
# -*- encoding:utf-8 *-*
import click
import os
import re

@click.command()
@click.argument('input', type=click.File('r', encoding='utf-8'))
@click.argument('output', type=click.File('w', encoding='utf-8'))
def main(input, output):
	content = input.read()
	content = re.sub('([:,!?])', lambda x: chr(ord(x.group(1))+65248), content)
	content = re.sub('([.])', lambda x: '。', content)
	content = re.sub('["](.*)["]', lambda x: '“'+x.group(1)+'”', content)
	output.write(content)

if __name__ == '__main__':
    main()
```

中文符号 => 英文符号
```python
# -*- encoding:utf-8 *-*
import click
import os
import re

@click.command()
@click.argument('input', type=click.File('r', encoding='utf-8'))
@click.argument('output', type=click.File('w', encoding='utf-8'))
def main(input, output):
	content = input.read()
	content = re.sub('([：，！？])', lambda x: chr(ord(x.group(1))-65248), content)
	content = re.sub('([。])', lambda x: '.', content)
	content = re.sub('[“](.*)[”]', lambda x: '"'+x.group(1)+'"', content)
	output.write(content)

if __name__ == '__main__':
    main()
```