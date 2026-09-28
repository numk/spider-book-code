-- 对应：第11章 爬虫系统的设计
-- 小节：11.3 任务调度设计
-- 条目：11.3.3 任务状态管理
-- 清单：03
-- 说明：摘自书稿示例，未改写。

CREATE TABLE crawl_tasks (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    task_name   VARCHAR(100)  NOT NULL COMMENT '任务名称',
    params      TEXT          COMMENT '任务参数（JSON）',
    status      VARCHAR(20)   NOT NULL DEFAULT 'pending' COMMENT '任务状态',
    error_msg   TEXT          COMMENT '失败原因',
    created_at  DATETIME      NOT NULL,
    updated_at  DATETIME,
    INDEX idx_task_name (task_name),
    INDEX idx_status (status)
);
