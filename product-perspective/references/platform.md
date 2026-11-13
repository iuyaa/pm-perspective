# 内部平台与业务系统

先根据交付物选择主技能。以下路径相对 `library.json` 的 `root`。

| 任务 | 主技能路径 | 交付重点 |
| --- | --- | --- |
| 目标、业务职责或平台边界尚未明确 | `linyindong/skills/platform-product-guide/METHOD.md` | 问题、能力边界、复用方案、关键决定 |
| 本期是否做、MVP、影响范围 | `linyindong/skills/platform-scope-checker/METHOD.md` | 纳入、简化、延后的依据及上下游影响 |
| 审批、生命周期、跨系统同步、取消、失败补偿、迁移 | `linyindong/skills/platform-flow-modeler/METHOD.md` | 主流程、状态、权威数据源、责任人和异常结局 |
| PRD 新建、补全或改写 | `linyindong/skills/platform-prd-builder/METHOD.md` | 指定深度的需求或段落，复用现有模板 |
| PRD 评审 | `linyindong/skills/platform-prd-reviewer/METHOD.md` | 准备度、具体矛盾、必须决定的业务事项 |
| RFC 产品功能及逻辑评审 | `linyindong/skills/platform-rfc-reviewer/METHOD.md` | 功能覆盖、失败结果、存量影响、评审会问题 |

简单增量直接进入编写或评审。有状态、跨系统或存量兼容风险时，按需先建模受影响流程。需要完整 PRD 时，再读 builder 的 `references/prd-output-contract.md`。PRD 与 RFC 的职责难以划分时，读 reviewer 的 `references/prd-vs-rfc-boundary.md`。

针对内部 HR、招聘、考勤、数据管理和运营平台，按实际需求检查这些业务问题，相关项进入正文或验收。

- 哪个角色可以查看、操作及导出哪些组织、业务线或记录。
- 每个状态允许哪些动作，重复提交、撤回、驳回和重提后产生什么结果。
- 通知或同步失败后各方看见什么，由谁处理，怎样确认结案。
- 配置变更如何作用于已有记录、在途流程及历史报表。
- 数据来源、统计口径、审计信息与人工处理责任是否能追溯。

流程建模产物回流当前主任务。单独的流程问题交付流程即可。评审引用具体段落、表格、字段或状态，缺少可读附件时保留判断边界。
