// 对应：第12章 APP 数据的爬取与逆向
// 小节：12.12 iOS 数据分析入门
// 条目：12.12.5 观察一个 Objective-C 字符串方法
// 清单：04
// 说明：摘自书稿示例，未改写。

import ObjC from 'frida-objc-bridge';

if (!ObjC.available) {
  throw new Error('Objective-C runtime unavailable');
}
const cls = ObjC.classes.LessonGreeter;
if (!cls || !cls['- greeting:']) {
  throw new Error('请确认教学 App 已加载 LessonGreeter');
}
Interceptor.attach(cls['- greeting:'].implementation, {
  onEnter(args) {
    // args[0] 是 self，args[1] 是 selector，第一个显式参数位于 args[2]。
    this.name = args[2].isNull() ? '<nil>' : new ObjC.Object(args[2]).toString();
  },
  onLeave(retval) {
    const result = retval.isNull() ? '<nil>' : new ObjC.Object(retval).toString();
    console.log(JSON.stringify({name: this.name, result}));
  }
});
