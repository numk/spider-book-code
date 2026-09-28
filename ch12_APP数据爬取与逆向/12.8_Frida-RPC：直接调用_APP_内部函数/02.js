// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.8 Frida-RPC：直接调用 APP 内部函数
// 条目：12.8.2 最小签名调用
// 清单：02
// 说明：摘自书稿示例，未改写。

import Java from 'frida-java-bridge';
rpc.exports = {
  sign(raw) {
    return new Promise((resolve, reject) => {
      Java.perform(() => {
        try {
          const Signer = Java.use('com.example.lesson.Signer');
          resolve(Signer.sign.overload('java.lang.String').call(Signer, raw).toString());
        } catch (error) { reject(error); }
      });
    });
  }
};
