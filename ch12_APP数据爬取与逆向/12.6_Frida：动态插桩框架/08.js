// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.6 Frida：动态插桩框架
// 条目：12.6.4 Hook Java 层常见场景
// 清单：08
// 说明：摘自书稿示例，未改写。

Java.perform(function() {
    var MessageDigest = Java.use('java.security.MessageDigest');
    // 使用 overload 指定参数类型
    MessageDigest.update.overload('[B').implementation = function(bytes) {
        var hex = Array.from(bytes).map(b => ('0' + (b & 0xFF).toString(16)).slice(-2)).join('');
        console.log('[MessageDigest.update] bytes: ' + hex);
        return this.update(bytes);
    };
});
