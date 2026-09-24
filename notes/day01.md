# Day 01 · 装好工具链，跑通第一个 C++ 程序

日期：2026-09-24

## 今天做完的

- 装好 MSYS2 + g++ 16.2.0（过程与坑见 `notes/环境说明.md`）
- 写了第一个源文件 `code/day01/hello.cpp`，编译通过、能运行
- 跑通 VS Code 的 F5 调试：打断点、F10 单步、在「变量」面板看值的变化
- 认识 `//` 行注释：把三行 `cout` 加上 `//` 之后，程序照样编译通过，但什么都不输出

## 用到的命令

在 VS Code 终端（PowerShell）里：

```powershell
cd D:\Code\cpp-learning\code\day01
g++ hello.cpp -o hello     # 编译：.cpp 源文件 → hello.exe
.\hello.exe                # 运行
chcp                       # 查当前终端编码，65001 = UTF-8
```

编译选项 `-g` 的作用：把行号等调试信息写进 exe，gdb 才知道第几行对应哪条指令（`tasks.json` 里已带）。

## 今天踩的坑

### 1. 程序里的中文输出是乱码

- 我看到的乱码原文：`鏉庢灄宄� 鐢熺墿绉戝��`（把「李林峻 生物科学」的 UTF-8 字节按 GBK 解码就得到它，已复现）
- 原因：源文件是 UTF-8 存的，`cout` 输出的就是 UTF-8 字节；而 PowerShell 终端默认按 GBK（代码页 936）去解码这些字节，字对不上就成了乱码。实测：同一串字节按 UTF-8 解码是「工具链验证」，按 GBK 解码是「宸ュ叿閾鹃獙璇」。
- 结论：**代码和编译器都没错，错的是终端用哪本字典**。
- 解决：VS Code 用户设置里加了一个 `PowerShell (UTF-8)` 终端配置（开终端时自动 `chcp 65001` + 设 `[Console]::OutputEncoding`）。
- 临时办法：在终端先敲 `chcp 65001`，只对当前这个终端窗口有效。

### 2. PowerShell 里运行程序必须写 `.\hello.exe`

只写 `hello` 不行，会报「无法将"hello"项识别为 cmdlet…」。`./hello` 这种写法是 Linux 的，在 Git Bash / MSYS2 终端里才行。

### 3. VS Code 自动生成的编译任务用的是 `gcc.exe`

C/C++ 扩展默认生成的任务调 `gcc.exe`，而 gcc 是 C 编译器、不带 C++ 标准库，编 `.cpp` 会报链接错误。已改成 `g++.exe`（见 `.vscode/tasks.json`）。

## 完成情况

- `hello.cpp` 已写完并保存，输出三行：姓名 / 专业 / 学号（第三行按自己的选择用了学号）
- 编译零报错，可执行文件 41217 字节
- 运行输出（已在 PowerShell 终端实测）：

```
李林峻
生物科学
202340470329
```
