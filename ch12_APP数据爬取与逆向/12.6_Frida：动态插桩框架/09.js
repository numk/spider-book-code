// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.6 Frida：动态插桩框架
// 条目：12.6.4 Hook Java 层常见场景
// 清单：09
// 说明：摘自书稿示例，未改写。

Java.perform(function() {
    Java.enumerateLoadedClasses({
        onMatch: function(name) {
            // 过滤包含关键词的类名
            if (name.indexOf('Sign') !== -1 || name.indexOf('Encrypt') !== -1) {
                console.log('[Class] ' + name);
            }
        },
        onComplete: function() {
            console.log('[*] 枚举完成');
        }
    });
});
