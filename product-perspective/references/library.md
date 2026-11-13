# 完整原库与补充检索

读取同目录的 `library.json` 获得 `root`。四个来源 ID 为 `deanpeters`、`linyindong`、`product-on-purpose`、`julianoczkowski`。版本固定在 manifest 记录的 commit。内置快照将上游技能文件重命名为 METHOD.md，Markdown 中相应引用同步调整，其他文件字节保留，包含脚本、模板、根级资源和许可证。

## 按需定位

`catalog.tsv` 每行含来源、技能名、相对路径、技能文件 SHA-256 和原始描述。使用 `rg -n -i '关键词|技能名' <当前技能目录>/references/catalog.tsv` 定向检索，再读取 `<root>/<匹配路径>`。中文任务可用对应英文概念检索，例如 `pricing`、`stakeholder`、`eol`、`sprint`、`AI`。指定原技能名时精确匹配该行。同名歧义用来源区分。

## 扩展场景

- AI 产品准备度、上下文工程和 Agent 编排，检索 deanpeters 的 `ai-shaped-readiness-advisor`、`context-engineering-advisor`、`agent-orchestration-advisor`。具体 AI 产品 PRD 优先使用 delivery 路线。
- 产品生命周期与下线，检索 deanpeters 的 `lifecycle-play-advisor`、`eol-*`。
- Foundation Sprint 和 Design Sprint，检索 product-on-purpose 的 `tool-foundation-sprint-*`、`tool-design-sprint-*`。按用户要求执行具体步骤或完整工作坊。
- 会议整理、产品团队流程和专项分析，从索引选择对应技能。
- 产品职业发展，检索 deanpeters 的 `director-readiness-advisor` 或 `vp-cpo-readiness-advisor`。

原库里的 `platform-product-orchestrator`、`pm-copilot` 及 `utility-pm-workflow-orchestrator` 全部保留。统一入口下默认选择叶子专业技能。只有用户要求对应原始工作流时才读取这些编排器，沿用当前环境的权限和统一协作约定。

库维护技能如 `utility-update-pm-skills`、`utility-pm-skill-*`、`pm-skill-creator` 属于明确的技能维护任务。实际执行前核对改动范围。自动更新会改变审阅过的版本，须同步更新 manifest、索引并重新校验。

## 安装结构

安装整个 `product-perspective` 目录。该目录仅有入口 `SKILL.md`，专业方法保存在 `library/` 中，使用 `METHOD.md` 文件名。`library.json` 使用相对路径，复制或从 GitHub 安装后即可按需读取。同步脚本自动刷新快照、来源版本和索引，并验证单入口及路由完整性。

原库维护脚本中写死的 `SKILL.md` 路径保留原样，执行此类工具时使用原始仓库或先适配路径。方法与文档的按需读取使用快照中的 `METHOD.md`。

## 来源许可

deanpeters 为 CC BY-NC-SA 4.0，其 README 明确允许营利公司的日常工作使用，付费重包装需作者书面许可。linyindong 与 julianoczkowski 为 MIT，product-on-purpose 为 Apache-2.0。保留每个原库的 LICENSE、归属和通知，分发时按各来源条款处理。
