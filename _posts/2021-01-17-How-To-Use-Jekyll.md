---
title: 如何使用 Jekyll
published: true
---

Jekyll 的核心其实是一个文本转换引擎。你可以用你最喜欢的标记语言来写文章，可以是 Markdown, 也可以是 Textile, 或者就是简单的 HTML, 然后 Jekyll 就会帮你套入一个或一系列的布局中。在整个过程中你可以设置 URL 路径，你的文本在布局中的显示样式等等。这些都可以通过纯文本编辑来实现，最终生成的静态页面就是你的成品。

# [](#header-1)1. 安装准备
> Ruby  
> RubyGems  
> NodeJS  
> Python  

# [](#header-2)2. 快速上手
> 最简单的 Jekyll 模板并生成静态页面并运行的例子。
{% highlight bash %}
~ $ gem install jekyll
~ $ jekyll new myblog
~ $ cd myblog ~/myblog
~ $ jekyll serve
# => Now browse to http://localhost:4000
{% endhighlight %}
> 如果你希望把 jekyll 安装到当前目录，你可以运行 jekyll new . 来代替。  
> 如果当前目录非空，你还需要增添 --force 参数，命令应为 jekyll new . --force。

# [](#header-3)3. 基本结构
> 基本的 Jekyll 网站的根目录结构：
```bash
.
├── _config.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.textile
|   └── on-simplicity-in-technology.markdown
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
|   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _site
├── .jekyll-metadata
└── index.html
```

| 文件 / 目录 | 描述 |
|:------------|:------------------|
| _config.yml | 保存配置选项数据。很多配置选项都可以直接在命令行中进行设置 |
| _drafts | drafts（草稿）是未发布的文章|
| _includes | includes 包含零碎的模板, 可以重复加载到布局或者文章中以方便重用 | 
| _layouts | layouts（布局）是包裹在文章外部的模板    | 
| _posts | posts 是放文章的路径。文件格式很重要，必须要符合: YEAR-MONTH-DAY-title.md |
| _site | Jekyll 完成文本转换，就会将生成的页面放在这里（默认路径） |
| .jekyll-metadata | 该文件帮助 跟踪哪些文件从上次建立站点开始到现在没有被修改，哪些文件需要在下一次站点建立时重新生成 |
| index.html | 如果文件中包含 YAML 头信息 部分，Jekyll 就会自动将它们进行转换。当然，其他的如 .html, .markdown, .md, 或者 .textile 等在你的站点根目录下或者不是以上提到的目录中的文件也会被转换。 |
| other files/folders | 其他一些未被提及的目录和文件如 css 还有 images 文件夹， favicon.ico 等文件都将被完全拷贝到生成的 site 中 |