# 第12章 APP 数据的爬取与逆向

本目录中的文件从书稿对应章节原样抽出，只在支持注释的语言里加了来源说明。
片段示例不一定能单独运行，请对照书中上下文阅读。

## 12.1 ADB：Android 调试桥

- `12.1_ADB：Android_调试桥/01.sh`：12.1.1 安装 ADB（bash）
- `12.1_ADB：Android_调试桥/02.sh`：12.1.1 安装 ADB（bash）
- `12.1_ADB：Android_调试桥/03.sh`：12.1.2 连接设备（bash）
- `12.1_ADB：Android_调试桥/04.sh`：12.1.2 连接设备（bash）
- `12.1_ADB：Android_调试桥/05.sh`：12.1.2 连接设备（bash）
- `12.1_ADB：Android_调试桥/06.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/07.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/08.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/09.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/10.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/11.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/12.sh`：12.1.3 常用命令速查（bash）
- `12.1_ADB：Android_调试桥/13.sh`：12.1.4 提取 APK 的完整流程（bash）
- `12.1_ADB：Android_调试桥/14.sh`：12.1.4 提取 APK 的完整流程（bash）
## 12.2 Root 与刷机：搭建逆向分析环境

- `12.2_Root_与刷机：搭建逆向分析环境/01.sh`：12.2.4 解锁 Bootloader（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/02.sh`：12.2.4 解锁 Bootloader（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/03.sh`：12.2.5 Magisk 刷入与 Root（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/04.sh`：12.2.5 Magisk 刷入与 Root（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/05.sh`：12.2.5 Magisk 刷入与 Root（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/06.sh`：12.2.6 系统证书信任：解决 HTTPS 抓包问题（bash）
- `12.2_Root_与刷机：搭建逆向分析环境/07.sh`：12.2.6 系统证书信任：解决 HTTPS 抓包问题（bash）
## 12.4 jadx：APK 静态反编译

- `12.4_jadx：APK_静态反编译/01.txt`：12.4.1 安装与使用（text）
- `12.4_jadx：APK_静态反编译/02.txt`：12.4.2 分析加密参数的完整流程（text）
- `12.4_jadx：APK_静态反编译/03.txt`：12.4.2 分析加密参数的完整流程（java）
- `12.4_jadx：APK_静态反编译/04.py`：12.4.2 分析加密参数的完整流程（python）
- `12.4_jadx：APK_静态反编译/05.sh`：12.4.3 jadx 常用技巧（bash）
## 12.6 Frida：动态插桩框架

- `12.6_Frida：动态插桩框架/01.sh`：12.6.2 环境搭建（bash）
- `12.6_Frida：动态插桩框架/02.sh`：12.6.2 环境搭建（bash）
- `12.6_Frida：动态插桩框架/03.sh`：12.6.2 环境搭建（bash）
- `12.6_Frida：动态插桩框架/04.js`：12.6.3 第一个 Hook 脚本：观察 MD5 方法（javascript）
- `12.6_Frida：动态插桩框架/05.sh`：12.6.3 第一个 Hook 脚本：观察 MD5 方法（bash）
- `12.6_Frida：动态插桩框架/06.py`：12.6.3 第一个 Hook 脚本：观察 MD5 方法（python）
- `12.6_Frida：动态插桩框架/07.js`：12.6.4 Hook Java 层常见场景（javascript）
- `12.6_Frida：动态插桩框架/08.js`：12.6.4 Hook Java 层常见场景（javascript）
- `12.6_Frida：动态插桩框架/09.js`：12.6.4 Hook Java 层常见场景（javascript）
- `12.6_Frida：动态插桩框架/10.js`：12.6.4 Hook Java 层常见场景（javascript）
## 12.8 Frida-RPC：直接调用 APP 内部函数

- `12.8_Frida-RPC：直接调用_APP_内部函数/01.txt`：12.8.1 Frida-RPC 工作原理（text）
- `12.8_Frida-RPC：直接调用_APP_内部函数/02.js`：12.8.2 最小签名调用（javascript）
- `12.8_Frida-RPC：直接调用_APP_内部函数/03.sh`：12.8.2 最小签名调用（bash）
- `12.8_Frida-RPC：直接调用_APP_内部函数/04.py`：12.8.2 最小签名调用（python）
## 12.10 IDA Pro：SO 文件静态逆向分析

- `12.10_IDA_Pro：SO_文件静态逆向分析/01.txt`：12.10.2 加载 SO 文件（text）
- `12.10_IDA_Pro：SO_文件静态逆向分析/02.txt`：12.10.3 快速定位 JNI 函数（text）
- `12.10_IDA_Pro：SO_文件静态逆向分析/03.txt`：12.10.3 快速定位 JNI 函数（text）
- `12.10_IDA_Pro：SO_文件静态逆向分析/04.txt`：12.10.4 使用 F5 查看伪代码（asm）
- `12.10_IDA_Pro：SO_文件静态逆向分析/05.txt`：12.10.4 使用 F5 查看伪代码（c）
- `12.10_IDA_Pro：SO_文件静态逆向分析/06.txt`：12.10.5 常用分析技巧（text）
- `12.10_IDA_Pro：SO_文件静态逆向分析/07.js`：12.10.5 常用分析技巧（javascript）
## 12.11 综合实战：完整的 APP 数据爬取流程

- `12.11_综合实战：完整的_APP_数据爬取流程/01.txt`：12.11.1 阶段一：抓包分析接口（text）
- `12.11_综合实战：完整的_APP_数据爬取流程/02.txt`：12.11.2 阶段二：jadx 静态分析（java）
- `12.11_综合实战：完整的_APP_数据爬取流程/03.txt`：12.11.2 阶段二：jadx 静态分析（java）
- `12.11_综合实战：完整的_APP_数据爬取流程/04.js`：12.11.3 阶段三：Frida 动态验证（javascript）
- `12.11_综合实战：完整的_APP_数据爬取流程/05.txt`：12.11.3 阶段三：Frida 动态验证（text）
- `12.11_综合实战：完整的_APP_数据爬取流程/06.py`：12.11.4 阶段四：验证签名复现（python）
## 12.12 iOS 数据分析入门

- `12.12_iOS_数据分析入门/01.py`：12.12.2 从操作定位到请求复现（python）
- `12.12_iOS_数据分析入门/02.sh`：12.12.4 连接已配置的 Frida 设备（bash）
- `12.12_iOS_数据分析入门/03.txt`：12.12.5 观察一个 Objective-C 字符串方法（objectivec）
- `12.12_iOS_数据分析入门/04.js`：12.12.5 观察一个 Objective-C 字符串方法（javascript）
- `12.12_iOS_数据分析入门/05.sh`：12.12.5 观察一个 Objective-C 字符串方法（bash）
