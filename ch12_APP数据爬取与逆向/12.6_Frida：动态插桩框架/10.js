// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.6 Frida：动态插桩框架
// 条目：12.6.4 Hook Java 层常见场景
// 清单：10
// 说明：摘自书稿示例，未改写。

Java.perform(function() {
    // 获取类实例
    var MD5Utils = Java.use('com.example.utils.MD5Utils');
    
    // 直接调用静态方法
    var result = MD5Utils.md5('hello world');
    console.log('MD5("hello world") = ' + result);
});
