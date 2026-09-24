# C++ 学习计划（12 周 / 84 天）

每天约 **2 小时**，每天中午 **12:01** 由 Hermes 自动推送当天任务。

## 路线

| 阶段 | 周次 | 天数 | 内容 |
| --- | --- | --- | --- |
| 一、语法基础 | W1–W3 | Day 1–21 | 环境与编译、类型与控制流、函数、指针与内存、面向对象（封装/继承/多态） |
| 二、标准库 | W4–W6 | Day 22–42 | STL 容器、算法库与 lambda、模板、异常、文件 IO、智能指针 |
| 三、现代 C++ 与工程化 | W7–W9 | Day 43–63 | 移动语义、optional/string_view、CMake、测试、调试工具、多线程与线程池 |
| 四、数据结构 · 算法 · 项目 | W10–W12 | Day 64–84 | 手写数据结构、排序/二分/DP/图、FASTQ 统计工具（含并行加速与性能数据） |

每 7 天有一次复盘日（Day 7、14、21 ……），用来补课、自测、写笔记。计划最终产出一个能说清性能数字的 C++ 命令行项目，配合 GitHub 与面试口径。

## 目录结构

```
D:/Code/cpp-learning/
├── plan/                # 计划数据（脚本读这里，每天 120 分钟）
│   ├── p1_foundation.json   Day 1–21
│   ├── p2_stl.json          Day 22–42
│   ├── p3_modern.json       Day 43–63
│   └── p4_project.json      Day 64–84
├── progress.json        # 进度：start_date（第 1 天）+ offset（偏移天数）
├── code/                # 每天写的代码
└── notes/               # 每天的笔记与每周复盘
```

## 手动操作

```bash
# 看今天该学什么（和推送内容一致）
python "D:/Hermes Agent CN Desktop/data/hermes-home/scripts/cpp_daily.py"

# 预览任意一天
python "D:/Hermes Agent CN Desktop/data/hermes-home/scripts/cpp_daily.py" --day 43

# 列出 84 天全部标题
python "D:/Hermes Agent CN Desktop/data/hermes-home/scripts/cpp_daily.py" --list
```

## 调整进度

改 `progress.json` 即可，下一次推送按新值算：

- `start_date`：第 1 天的日期
- `offset`：整体偏移天数。落下两天就设 `-2`（任务顺延两天），想跳过两天就设 `2`

## 参考资料

- **主教程**：learncpp.com（按主题分章，英文，顺便练英语）
- **查语法**：cppreference.com（当字典用，不要通读）
- **中文视频**：B 站「C++ 零基础」系列任选一套，只在看不懂时当补充
- **练习**：LeetCode（W4 起每周复盘日刷题）
- **工具**：MSYS2 + g++（Day 1 装）、VS Code + C/C++ 扩展、CMake（Day 51 起）
