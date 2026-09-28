# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.2 Root 与刷机：搭建逆向分析环境
# 条目：12.2.5 Magisk 刷入与 Root
# 清单：04
# 说明：摘自书稿示例，未改写。

# 先刷入 TWRP
fastboot flash recovery twrp.img
fastboot reboot recovery

# 在 TWRP 界面选择 Install，刷入 Magisk.zip
