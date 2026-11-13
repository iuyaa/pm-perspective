# 产品视角 · PM Perspective

一个产品经理技能入口，按场景加载四个上游库的专业方法。支持内部平台需求、审批权限、跨系统流程、PRD、产品探索、策略取舍和指标验证。

## 安装与使用

在 Codex 中发送以下请求即可使用内置 skill-installer 安装。

```text
安装 https://github.com/iuyaa/pm-perspective 中的 pm-perspective 技能目录
```

也可以把本仓库的整个 `pm-perspective/` 目录复制到宿主的技能目录。安装目录中自带专业方法和相对路径索引。

```text
$pm-perspective 给审批中心增加撤回通知，梳理影响并写需求
$pm-perspective 评审这份 PRD，定位业务逻辑和验收缺口
$pm-perspective 汇总访谈，提炼有证据支持的用户问题
```

## 单入口与按需加载

本项目维护 `pm-perspective/SKILL.md` 及 `references/` 中的场景路由。Agent 在技能列表中只发现 `pm-perspective`。选中入口后读取对应路线，再打开需要的专业方法及配套资源。

上游快照保存在 `pm-perspective/library/`。同步时所有大小写形式的 `SKILL.md` 均转换为 `METHOD.md`，Markdown 中的文件名引用同步调整。其余文件字节保留，原始版本可通过来源 commit 追溯。源代码工具中写死的 `SKILL.md` 路径仍按原样保留，运行上游维护工具时需使用原仓库或适配路径。

上游 `.gitignore` 和 `.gitattributes` 分别保存为 `UPSTREAM.gitignore` 和 `UPSTREAM.gitattributes`，使快照文件完整提交并保持字节哈希一致。

```text
pm-perspective/
├── SKILL.md                 唯一发现入口
├── references/              人工维护的路线和自动生成的来源、索引
├── scripts/check_library.py 校验单入口、完整文件哈希与路由
└── library/                 四个上游的完整文件快照，专业入口名为 METHOD.md
```

## 上游与归属

| 来源 | 初始技能数 | 许可 |
| --- | ---: | --- |
| [Dean Peters / Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 77 | CC BY-NC-SA 4.0 |
| [Lin Yindong / platform-product-skills](https://github.com/linyindong/platform-product-skills) | 7 | MIT |
| [product-on-purpose / pm-skills](https://github.com/product-on-purpose/pm-skills) | 68 | Apache-2.0 |
| [Julian Oczkowski / product-manager](https://github.com/julianoczkowski/product-manager) | 18 | MIT |

当前数量、commit 和日期见 [来源记录](pm-perspective/references/library.json)，完整方法见 [索引](pm-perspective/references/catalog.tsv)。每个来源目录保留其原始 LICENSE、归属和通知。上述转换由本项目执行。

本项目维护的入口、路由、同步代码和文档采用 CC BY-NC-SA 4.0，版权归 iuyaa，2026。上游文件继续适用各自目录中的许可。

Dean Peters 仓库明确允许在营利公司的日常工作中使用这些方法，付费重包装技能需作者书面许可。分发或改编应遵守各来源条款。[原库许可说明](https://github.com/deanpeters/Product-Manager-Skills#license)

## 自动同步

`Sync upstream methods` 每日北京时间 09:23 检查四个上游默认分支，也支持 Actions 页面手动运行。GitHub 的定时运行可能排队延迟。全部来源下载成功且校验通过后，自动提交快照、来源版本和索引到 main。任一来源或路由校验失败时，运行失败并保留已有已发布版本。

同步提交的范围为 `pm-perspective/library/`、`references/library.json`、`references/snapshots.json` 和 `references/catalog.tsv`。入口和场景路由由维护者更新。使用仓库内置的 `GITHUB_TOKEN`，权限为 `contents: write`，无需个人令牌。上游文件作为资料保存，Actions 执行本项目的同步和校验代码。

上游定时检查持续无变更时，GitHub 可能在公开仓库连续 60 天无活动后停用定时工作流，可在 Actions 页面重新启用。仓库同步更新后，已复制安装的本地技能需要重新安装或拉取仓库更新。[GitHub 定时事件说明](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

## 本地维护

```shell
python -m pip install PyYAML==6.0.3
python -m unittest discover -s tests -v
python scripts/sync_upstream.py
python pm-perspective/scripts/check_library.py
```

同步输出先在临时目录构建与校验，成功后替换技能目录。没有上游版本变化时生成内容保持一致。结构校验覆盖文件完整性和路由可达性，方法内容和实际业务产物质量由维护者结合使用反馈评估。
