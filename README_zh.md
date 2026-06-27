本文档也有英文版：[English Version](README.md) | 想要获得更直观的视觉体验，请访问我们的 [网页展示端](https://grapeot.github.io/skills/index_zh.html)。

# AI Agent 技能仓库与索引

本仓库是 **AI 编码智能体技能（AI Coding Agent Skills）** 的集中展示与注册中心。

---

## 1. 什么是 Skill？（核心哲学）

与 Cursor、Codex 或 Cloud Code 等平台所倡导的技能体系不同（它们通常绑定特定编辑器、使用严格类型定义的 JSON 配置或繁重的 SDK 开发包），我们的技能生态遵循以下设计原则：

1.  **平台无关，自然语言优先**：Skill 的核心是一份 Markdown 格式的操作指南（`SKILL.md`），用于记录人类的工作流程、判断标准与防错教训。任何大模型或 Agent 都能直接阅读并消费它。在需要自动化执行的场景下，我们仅需为其配上一个轻量的 CLI 脚本（如 Python 命令行工具）。它在 Claude Code、Cursor、OpenCode 或自定义的终端 Agent 中完全通用。
2.  **过程与结果的确定性**：AI Agent 在执行任务时容易发生幻觉或擅自简化流程。我们的 Skill 模版中明确定义了执行边界、多重验证步骤以及交付标准检查清单，以此确保 Agent 产出的结果高度可靠。
3.  **文件即接口 (Files-as-Interfaces)**：技能与工作区的交互通过读写文件进行。输入和输出都是工作区里的普通文本文件（Markdown、JSON、SQLite），不依赖网络 API 服务。这让 Agent 的所有操作都处于 Git 的版本控制下，可被随时审计、修改和回滚。
4.  **本地与公共隔离**：公开的 Skill 仓库仅定义通用的技术契约与 CLI 协议，所有私人路径、敏感 API Key、联系人别名均以 Overlay（覆盖层）的形式保存在用户本地的私有工作区中。

### 核心背景阅读
*   **方法论**：[用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html)（英文版：[Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html)）
*   **架构设计**：[为什么AI只会说正确的废话，以及怎么把它逼出舒适区](https://yage.ai/context-infrastructure.html)

---

## 2. 常见问题与安装指引

### 问：我该如何安装一个技能？
我们的技能安装是完全由 **Prompt 驱动**的。不需要编译安装包或配置浏览器插件。你只需要将该技能的 GitHub 地址复制下来，并在你的 AI 编码工具（如 Cursor 或 Claude Code）中输入以下提示词：
```text
Install this public skill repo into my workspace:
<技能仓库的 GitHub 地址>

Read the rules in this repo, clone/vendor it under 'adhoc_jobs/', create a relative symlink under 'rules/skills/', and register it in the rules index.
```
Agent 会自动在本地执行 `git clone`，挂载软链接并将其注册到工作区的索引中。

### 问：它支持我目前使用的编辑器和大模型吗？
完全支持。因为交互的媒介仅仅是工作区文件与标准的终端命令行，所以只要你的 Agent 拥有阅读工作区文件并运行命令的权限，就能无缝调用这些技能。

---

## 3. 技能注册表

### 📈 社交媒体、销售与用量分析
| 技能名称 | 类型 | 描述 | 链接 |
|---|---|---|---|
| **typefully-twitter-skill** | 仓库 | 联动 Typefully，支持推特草稿排期与单条推文数据分析 | [GitHub](https://github.com/grapeot/typefully-twitter-skill) |
| **stripe-skill** | 仓库 | Stripe 财务、销售和增长指标只读分析 CLI，支持本地 mock 运行 | [GitHub](https://github.com/grapeot/stripe-skill) |
| **ai_usage_dashboard** | 仓库 | 多平台 AI token 消耗追踪、成本估算与本地可视化面板 | [GitHub](https://github.com/grapeot/ai_usage_dashboard) |

### 🏠 日常量化与生活记录
| 技能名称 | 类型 | 描述 | 链接 |
|---|---|---|---|
| **health-quantification** | 仓库 | 聚合 HealthKit 数据与每日咖啡因/酒精日志，于 SQLite 中跑 sleep 影响回归分析 | [GitHub](https://github.com/grapeot/health-quantification) |
| **roest-analysis** | 仓库 | 自动抓取 Roest 烘焙机 API 样本日志，分析一爆集聚点并绘制温度曲线 | [GitHub](https://github.com/grapeot/roest-analysis) |
| **intake-skill** | 仓库 | 自动化整理本地语音备忘录，执行 ASR 转录并滚动维护索引日志 | [GitHub](https://github.com/grapeot/intake-skill) |

### 💼 工作流自动化与多媒体创作
| 技能名称 | 类型 | 描述 | 链接 |
|---|---|---|---|
| **gdocs-skill** | 仓库 | 通过 Markdown 文档在 Google Docs 中执行发布、搜索、修改和团队分享 | [GitHub](https://github.com/grapeot/gdocs-skill) |
| **outlook_skill** | 仓库 | Outlook 邮件下载归档、Markdown 渲染发信、日历邀请处理与忙闲查询 | [GitHub](https://github.com/grapeot/outlook_skill) |
| **resend_email_skill** | 仓库 | 基于 Resend 自定义域名发信，支持附件格式检查与收件箱状态读取 | [GitHub](https://github.com/grapeot/resend_email_skill) |
| **imessage_skill** | 仓库 | macOS iMessage 命令行发信工具，联系人别名配置文件存放在本地 Overlay 中 | [GitHub](https://github.com/grapeot/imessage_skill) |
| **pptx.skill** | 仓库 | 专为 AI 设计的 PPTX 文稿读取、内容替换与幻灯片极简水墨风格渲染器 | [GitHub](https://github.com/grapeot/pptx.skill) |
| **image-generation-skill** | 仓库 | 快速生成图画 Prompt、编辑局部图像并执行超分辨率放大（Gemini/GPT 后端） | [GitHub](https://github.com/grapeot/image-generation-skill) |
| **tiff-icc-profile** | 仓库 | 为未标记的 TIFF 图像（如达芬奇静帧）批量嵌入默认 P3-D65 或自定义 ICC 色彩配置文件 | [GitHub](https://github.com/grapeot/tiff-icc-profile) |
| **online-media-skill** | 仓库 | 自动化视频下载、ASR 语音转录、关键词匹配与 Query 检索工作流 | [GitHub](https://github.com/grapeot/online-media-skill) |

### ⚙️ Agent 运行基础设施与本地守护
| 技能名称 | 类型 | 描述 | 链接 |
|---|---|---|---|
| **process-launcher** | 仓库 | 本地 HTTP 任务守护进程，用以解决 macOS GUI 权限限制并管理长时间延迟任务 | [GitHub](https://github.com/grapeot/process-launcher) |
| **opencode_skill** | 仓库 | 提交 OpenCode 异步任务、编排 recurring cron 工作流并真空整理 SQLite | [GitHub](https://github.com/grapeot/opencode_skill) |
| **opencode-docker** | 仓库 | Docker 部署配置文件，用以容器化并快速部署 OpenCode Server 运行环境 | [GitHub](https://github.com/grapeot/opencode-docker) |

### 🧠 内置方法论、自动化工作流与最佳实践
| 技能名称 | 类型 | 描述 | 链接 |
|---|---|---|---|
| **AI CLI 交互指南** | 文档 | CLI 交互式文件接口的设计约束、Agent 嵌套调用与防死锁设计规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/ai_agent_cli_guide.md) |
| **分享报告到 Web** | 文档 | 将本地 Markdown 报告通过 Pandoc 渲染为 HTML 并通过 SSH 部署发布的流程 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/share_report.md) |
| **向量语义搜索** | 文档 | 利用向量数据库与 Embedding 接口，在本地工作区内对对话历史与背景知识进行检索 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/semantic_search.md) |
| **并行 Subagent 工作流** | 文档 | 调用后台智能体、对大任务在隔离的工作空间内进行并行分析的执行规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_parallel_subagents.md) |
| **深度调研工作流** | 文档 | 多 Agent 并行扫描、维度重叠划分、交叉验证防胡说八道的深度采集规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_deep_research_survey.md) |
| **认知画像提取工作流** | 文档 | 从非结构化对话历史或日志中，滚动提炼个人思维公理与认知画像的操作指南 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/workflow_cognitive_profile_extraction.md) |
| **AI 编程核心思维** | 文档 | 剖析 70% 边界问题，阐明为什么「先写脚本，再让 Agent 跑脚本」的确定性更优 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_ai_programming_mindset.md) |
| **Skill 写作指南（Meta）** | 文档 | 教授如何以「成功交付标准」和「异常限制」定义技能，避免写成教条 SOP | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_skill_writing.md) |
| **PDF 转换为 Markdown** | 文档 | 推荐使用 Docling 进行高精度表格和层级解析，弃用 MarkItDown / PyMuPDF | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_pdf_to_markdown.md) |
| **时间敏感信息验证** | 文档 | 验证或抓取超出模型知识截止日期（Knowledge Cutoff）实时数据的方法 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_temporal_info_verification.md) |
| **分阶段工作法** | 文档 | 贯彻「隔离-处理-验证」闭环，在执行破坏性/全局修改前强制 Dry Run | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/bestpractice_staged_approach.md) |
| **项目脚手架与重整** | 文档 | 规范如何将散装脚本升级为拥有 docs/、src/、scripts/ 和 tests/ 目录的标准仓库 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/main/rules/skills/project_scaffold.md) |
