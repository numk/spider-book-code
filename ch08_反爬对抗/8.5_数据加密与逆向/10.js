// 对应：第8章 反爬对抗
// 小节：8.5 数据加密与逆向
// 条目：8.5.3 JavaScript 逆向教学实战
// 清单：10
// 说明：摘自书稿示例，未改写。

export async function sign(keyword, page, timestamp) {
  const raw = JSON.stringify([keyword, page, timestamp, "classroom-salt"]);
  const bytes = new TextEncoder().encode(raw);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, "0")).join("");
}
if (typeof process !== "undefined" && process.argv[2]) {
  console.log(await sign(...JSON.parse(process.argv[2])));
}
