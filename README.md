# ThinkPHP Lang Check

单个/批量检测目标是否存在 ThinkPHP 多语言功能漏洞 

> 如果 Thinkphp 程序开启了多语言功能，那就可以通过 get、header、cookie 等位置传入参数，实现目录穿越+文件包含，通过 pearcmd 文件包含这个 trick 即可实现 RCE。

## Usage:

```
Usage: python3 tp_lang_check.py -h
Usage: python3 tp_lang_check.py -u url
Example: python3 tp_lang_check.py -u http://
Usage: python3 tp_lang_check.py -r file
Example: python3 tp_lang_check.py -r url.txt
```

## 影响版本

- ThinkPHP 6.0.1 -  6.0.13
- ThinkPHP 5.0.0 - 5.0.12
- ThinkPHP 5.1.0 - 5.1.8

## 修复建议

- 关闭多语言
- 升级最新包