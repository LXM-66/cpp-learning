# Day 02 · 一次编译到底发生了什么

日期：2026-09-25

## 今天做完的

- 搞清 `g++` 背后其实是四个程序接力，参数只是让它「在中间某一步停下」：

  | 参数 | 停在哪一步 | 产物 |
  |---|---|---|
  | `-E` | 预处理后（展开 `#include`、去掉注释） | `.i` |
  | `-S` | 编译后（C++ → 汇编） | `.s` |
  | `-c` | 汇编后（汇编 → 机器码） | `.o` |
  | 不加 | 链接后（.o + 标准库 → 可执行文件） | `.exe` |

- 同一份源文件四个阶段的产物大小（实测）：`.cpp` 108 字节 → `.i` **1322594 字节** → `.s` 1315 字节 → `.o` 1515 字节 → `.exe` 40065 字节。
  `.i` 涨了 1 万倍，是因为 `#include <iostream>` 真的把几千行头文件原样塞了进来。
- 写了 `code/day02/structure.cpp`：头文件、`using namespace std`、注释、`int main()`、`return 0`，运行时输出两个 `int` 相加的结果。
- 学会了分辨两类报错（编译期 / 链接期），并把 `main` 的返回值搞清楚了。

## 用到的命令

```powershell
cd D:\Code\cpp-learning\code\day02
g++ -E structure.cpp -o structure.i    # 预处理：看头文件被展开成什么
g++ -S structure.cpp -o structure.s    # 编译：C++ 变成汇编
g++ -c structure.cpp -o structure.o    # 汇编：变成机器码目标文件
g++ structure.o -o structure.exe       # 链接：接上标准库，得到可执行文件
.\structure.exe
```

`main` 的返回值是交给操作系统的**退出码**，不是给程序里别的代码用的：`0` = 正常结束，非 0 = 出错。
刚跑完的程序，PowerShell 里用 `$LASTEXITCODE` 就能读到它（实测：`return 3;` → 退出码 3；不写 `return` → 编译器自动补 0）。

## 今天踩的坑

### 1. 少一个分号，编译器会把后面好几行一起报错

- 现象：`structure.cpp:2:20: error: expected ';' before 'int'`，紧接着还有一条 `4:1: error: ...`
- 原因：报错里的**行号列号指向的是「编译器读不下去的位置」，不是你漏写的位置**。第 2 行末尾少一个分号，
  编译器读到第 3 行开头的 `int` 才发现上句没结束，于是把账记在了 `int` 头上；第 3 行又没分号，于是第 4 行再报一次。
- 解决：**永远先修最上面那一条**，下面的一批经常跟着一起消失。

### 2. 语句写在了函数外面

- 现象：`error: expected ',' or ';' before 'int'` 反复出现，改分号也治不好
- 原因：除了 `#include`、`using`、函数定义，所有语句都必须住在某个函数的**花括号**里。写在文件最外层编译器根本不认。
- 解决：加 `int main() { ... }` 把语句整体包进去。

### 3. `return=0` 是错的

`return` 是关键字，不是变量名，不能给它赋值；正确写法 `return 0;`（空格，不是等号）。

### 4. 链接期错误：`undefined reference to 'std::cout'`（Day 01 的老坑复发）

- 现象：4 行 `undefined reference`，最后一行 `collect2.exe: error: ld returned 1 exit status`
- 原因：VS Code 在仓库根重新生成的 `.vscode/tasks.json` 里调的是 `gcc.exe`。gcc 是 C 编译器，
  编 `.cpp` 语法能过（所以一个语法错都没报），但**默认不链接 C++ 标准库 libstdc++**，
  而 `cout` / `endl` / `operator<<` 的实现全在那里 —— 链接器找不到零件，只能喊 undefined reference。
- 解决：把任务里的 `gcc.exe` 换成 `g++.exe`（`g++` = gcc + 自动接上 C++ 标准库）。
- **一眼分辨两类报错**：
  - 带 `文件:行:列: error: ...` 的 → **编译期**，改源码语法
  - 出现 `ld.exe` / `collect2.exe` / `undefined reference` 的 → **链接期**，源码通常没错，是库或命令的问题

## 完成情况

- `structure.cpp` 编译零报错，可执行文件 57399 字节
- 运行输出（已在 PowerShell 终端实测）：

```
30
```

- 退出码 0

## 待补

- 用自己的话、不查资料，把「四步各自产出什么文件」写一遍（验收标准第一条）
