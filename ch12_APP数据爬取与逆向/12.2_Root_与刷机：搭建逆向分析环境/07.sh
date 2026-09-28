# 对应：第12章 APP 数据的爬取与逆向
# 小节：12.2 Root 与刷机：搭建逆向分析环境
# 条目：12.2.6 系统证书信任：解决 HTTPS 抓包问题
# 清单：07
# 说明：摘自书稿示例，未改写。

# 导出 Charles/mitmproxy 的 CA 证书（.pem 格式）
# 计算证书的 hash 值（Android 要求文件名为 hash.0）
openssl x509 -subject_hash_old -in charles.pem | head -1
# 假设输出 a1b2c3d4

# 重命名证书文件
cp charles.pem a1b2c3d4.0

# 推送到系统证书目录（需要 root 且系统分区可写）
adb push a1b2c3d4.0 /sdcard/
adb shell su -c "mount -o rw,remount /system"
adb shell su -c "cp /sdcard/a1b2c3d4.0 /system/etc/security/cacerts/"
adb shell su -c "chmod 644 /system/etc/security/cacerts/a1b2c3d4.0"
adb reboot
