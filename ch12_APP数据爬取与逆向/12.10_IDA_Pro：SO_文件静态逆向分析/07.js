// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.10 IDA Pro：SO 文件静态逆向分析
// 条目：12.10.5 常用分析技巧
// 清单：07
// 说明：摘自书稿示例，未改写。

// 使用 IDA 分析得到的偏移量进行 Hook
var base = Module.findBaseAddress('libnative.so');
var offset = 0x3F2C0;  // 从 IDA 的函数属性中获取
Interceptor.attach(base.add(offset), {
    onEnter: function(args) {
        console.log('[sign] 被调用，参数: ' + args[2]);
    },
    onLeave: function(retval) {
        console.log('[sign] 返回: ' + retval);
    }
});
