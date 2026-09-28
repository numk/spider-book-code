// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.11 综合实战：完整的 APP 数据爬取流程
// 条目：12.11.3 阶段三：Frida 动态验证
// 清单：04
// 说明：摘自书稿示例，未改写。

// verify_sign.js
Java.perform(function() {
    var SignUtils = Java.use('com.example.utils.SignUtils');
    
    // Hook computeSign 方法
    SignUtils.computeSign.implementation = function(params, timestamp) {
        var result = this.computeSign(params, timestamp);
        
        // 打印所有信息
        console.log('='.repeat(50));
        console.log('[computeSign] timestamp: ' + timestamp);
        console.log('[computeSign] result: ' + result);
        
        return result;
    };
    
    // Hook HmacSHA256，捕获密钥
    SignUtils.HmacSHA256.overload('java.lang.String', 'java.lang.String')
        .implementation = function(data, key) {
            console.log('[HmacSHA256] data: ' + data);
            console.log('[HmacSHA256] key: ' + key);  // 我们要的 SECRET_KEY！
            return this.HmacSHA256(data, key);
        };
});
