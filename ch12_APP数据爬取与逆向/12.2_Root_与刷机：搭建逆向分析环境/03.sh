# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.2 Root 与刷机：搭建逆向分析环境
# 条目：12.2.5 Magisk 刷入与 Root
# 清单：03
# 说明：摘自书稿示例，未改写。

# 第一步：获取当前系统对应版本的完整 OTA 包或线刷包
# 解压后找到 boot.img 文件，将其传入手机
adb push boot.img /sdcard/

# 第二步：在手机上安装 Magisk APP
# 下载地址：https://github.com/topjohnwu/Magisk/releases

# 第三步：打开 Magisk APP → 安装 → 选择并修补一个文件 → 选择 boot.img
# Magisk 会生成 magisk_patched_xxxx.img，将其拉取到电脑
adb pull /sdcard/Download/magisk_patched_xxxx.img .

# 第四步：刷入修补后的 boot.img
adb reboot bootloader
fastboot flash boot magisk_patched_xxxx.img
fastboot reboot
