// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.6 Frida：动态插桩框架
// 条目：12.6.4 Hook Java 层常见场景
// 清单：07
// 说明：摘自书稿示例，未改写。

Java.perform(function() {
    var URL = Java.use('java.net.URL');
    // $init 代表构造函数
    URL.$init.overload('java.lang.String').implementation = function(url) {
        console.log('[URL] 创建连接：' + url);
        return this.$init(url);
    };
});
