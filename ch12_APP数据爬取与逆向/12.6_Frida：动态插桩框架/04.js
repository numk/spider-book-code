// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.6 Frida：动态插桩框架
// 条目：12.6.3 第一个 Hook 脚本：观察 MD5 方法
// 清单：04
// 说明：摘自书稿示例，未改写。

import Java from 'frida-java-bridge';

Java.perform(() => {
  const MD5Utils = Java.use('com.example.utils.MD5Utils');
  const original = MD5Utils.md5.overload('java.lang.String');
  original.implementation = function (input) {
    const result = original.call(this, input);
    send({input: String(input), result: String(result)});
    return result;
  };
});
