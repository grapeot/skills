# AI Agent 技能生态系统

本文档也有英文版：[English Version](README.md) | 想要获得更直观的视觉体验，请访问我们的 [网页展示端](https://grapeot.github.io/skills/index_zh.html)。

> **面向 AI Agent 的「渐进式披露」范式。**
> 在我们的体系中，「技能 (Skill)」不是绑死在特定厂商平台上的复杂 Schema，也不是死板的格式文件。它本质上是一份自然语言编写的 Markdown 文档，向 AI 交代任务的目标、验收标准和异常处理方法，并辅以可选的 CLI 命令行工具或连接器。

本仓库是一个公开的技能索引集散地。你可以将这里的地址直接发给你的 AI 编程助手（如 Claude Code, Cursor, Codex, OpenCode 等），它能够自主阅读并将其自动安装到你的本地工作区中。

---

## 核心哲学：什么是 Skill？

大多数 AI Agent 在执行复杂任务时容易「一本正经地胡说八道」或者重复踩坑，这是因为它们在每个会话开始时都处于“盲目状态”，缺乏本地业务背景和运行教训。
**Skill** 解决了这一难题。它将知识、规则和踩坑经验外化到 Markdown 文件中，供 Agent 自动发现与阅读。

我们采用 **「渐进式披露 (Progressive Disclosure)」** 机制：
1. **L1（全局入口）**：Agent 在会话启动时自动加载并阅读 `AGENTS.md` 或 `CLAUDE.md`，进而被引导至技能索引。
2. **L2（索引路由）**：通过类似 `rules/skills/INDEX.md` 的索引文件，列出所有可用技能和触发条件。
3. **L3（技能详情）**：具体的 Skill 详情页（例如 `skill_imessage.md`），描述具体的 CLI 命令参数、运行边界、踩坑点和安全规则。
4. **本地 Overlay 覆盖**：将敏感数据（如联系人别名、私密 API 密钥）留在本地工作区配置中，仅通过公共 Skill 仓库共享通用的命令行技术契约与实现代码。

---

## 公开技能目录

### 🛠️ 工具连接与 API 指南 (API Guides)

扩展 Agent 执行能力的专属命令行工具和接口封装。

| 技能 / 仓库名称 | 类型 | 说明 | 链接 |
|---|---|---|---|
| **tavily-skill** | 仓库 | 专为 Agent 优化设计的 Tavily 网页搜索工具，返回干净的 JSON | [GitHub](https://github.com/grapeot/tavily-skill) |
| **gdocs-skill** | 仓库 | Google Docs 创建、编辑、分享及 Tab 标签管理工具 | [GitHub](https://github.com/grapeot/gdocs-skill) |
| **outlook_skill** | 仓库 | Outlook.com 邮件拉取、Markdown 渲染及本地 SQLite 归档 | [GitHub](https://github.com/grapeot/outlook_skill) |
| **resend_email_skill** | 仓库 | Resend 邮件发送、收件箱 Webhook 解析和 Markdown 导出 | [GitHub](https://github.com/grapeot/resend_email_skill) |
| **imessage_skill** | 仓库 | macOS 发送 iMessage 的 CLI 工具，支持本地联系人别名解析 | [GitHub](https://github.com/grapeot/imessage_skill) |
| **process-launcher** | 仓库 | 本地 HTTP 进程启动器，用于桥接 macOS GUI 与 TCC 权限 | [GitHub](https://github.com/grapeot/process-launcher) |
| **ai_usage_dashboard** | 仓库 | 多平台 AI Token 用量及成本统计看板 | [GitHub](https://github.com/grapeot/ai_usage_dashboard) |
| **typefully-twitter-skill** | 仓库 | Typefully 联动工具，支持推特草稿排期与单条推文数据分析 | [GitHub](https://github.com/grapeot/typefully-twitter-skill) |
| **stripe-skill** | 仓库 | Stripe 财务、销售和增长指标只读分析 CLI | [GitHub](https://github.com/grapeot/stripe-skill) |
| **pptx.skill** | 仓库 | 专为 AI 设计的 PowerPoint 演示文稿读取、编辑和渲染库 | [GitHub](https://github.com/grapeot/pptx.skill) |
| **image-generation-skill** | 仓库 | 基于 Gemini / GPT 的文生图与图片超分辨率放大 CLI | [GitHub](https://github.com/grapeot/image-generation-skill) |
| **tiff-icc-profile** | 仓库 | 针对达芬奇静帧导出的未标记 TIFF 图片嵌入色彩配置文件的 CLI | [GitHub](https://github.com/grapeot/tiff-icc-profile) |
| **health-quantification** | 仓库 | 个人 HealthKit 数据同步服务端及健康指标命令行分析工具 | [GitHub](https://github.com/grapeot/health-quantification) |
| **roest-analysis** | 仓库 | Roest 烘焙机 API 数据抓取与烘焙曲线分析工具 | [GitHub](https://github.com/grapeot/roest-analysis) |
| **intake-skill** | 仓库 | 语音备忘录与录音数据自动化整理与转录 CLI | [GitHub](https://github.com/grapeot/intake-skill) |
| **opencode-docker** | 仓库 | OpenCode Server 的 Docker 快速部署与配置模版 | [GitHub](https://github.com/grapeot/opencode-docker) |
| **opencode_skill** | 仓库 | OpenCode 会话管理、任务提交、备份与 SQLite 维护工具 | [GitHub](https://github.com/grapeot/opencode_skill) |
| **AI CLI Agent 实用指南** | 文档 | 关于「文件即接口」设计模式及 AI 嵌套调用的核心最佳实践 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/ai_agent_cli_guide.md) |
| **给自己发邮件** | 文档 | 利用 Gmail App Password 快速向自己发送通知邮件的技能 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/send_email.md) |
| **分享报告到 Web** | 文档 | 将本地 Markdown 报告渲染为 HTML 并通过 SSH 部署发布的流程 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/share_report.md) |
| **增长数据分析 Overlay** | 文档 | 结合 GSC 搜索、GA4 流量和 Kit 邮件列表的本地分析配置 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/growth_analytics.md) |

---

### 🔄 任务工作流 (Workflows)

规范 Agent 执行复杂、多阶段或多智能体任务的标准流程。

| 技能 / 文件名称 | 说明 | 链接 |
|---|---|---|
| **并行 Subagent 工作流** | 如何将大任务拆分为子任务，并利用后台智能体并行处理（禁轮询） | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_parallel_subagents.md) |
| **深度调研工作流** | 多 Agent 并行扫描、维度重叠划分、交叉验证防胡说八道的调研规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_deep_research_survey.md) |
| **分析性写作工作流** | 将调研素材提炼为具有个人判断力、免翻译腔的深度分析文章的步骤 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_analytical_writing.md) |
| **认知画像提取** | 从非结构化对话历史或日志中，滚动提炼个人思维公理与写作风格 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_cognitive_profile_extraction.md) |
| **幻灯片渲染工作流** | Clean Ink 极简水墨风格幻灯片多进程并行渲染与 4K 放大规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_presentation_slides.md) |
| **知识飞轮设计模式** | 通过「小数据 + 笨方法 + 小模型」滚动积累精制知识库的设计模式 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_knowledge_flywheel.md) |
| **在线媒体转录** | 自动化视频下载、ASR 语音转录及元数据填充的完整工作流 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/workflow_bilibili_whisper_transcription.md) |
| **延时与定时执行** | 配置后台延时任务和 Crontab 定时器启动 Agent 的设计约束 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/delayed_execution.md) |

---

### 💡 最佳实践 (Best Practices)

软件开发、AI 编程、系统设计和故障诊断的通用方法论。

| 技能 / 文件名称 | 说明 | 链接 |
|---|---|---|
| **AI 编程核心思维** | 70% 问题、推理模型与 Agent 工作流差异、可验证性原则 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_ai_programming_mindset.md) |
| **Skill 写作指南** | 如何写出容易被 AI 理解和复用的高质量 Skill（注重使能而非机械SOP） | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_skill_writing.md) |
| **1Password 密钥管理** | 利用 1Password CLI 安全加载 API Key，避免硬编码泄露风险 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_api_key_management_1password_cli.md) |
| **面试评估框架** | 关注特质而非死板技能、探测 candidate 真实技术深度的面试框架 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_interview_evaluation.md) |
| **Markdown 转 HTML** | 转换静态页面结构和发布静态资源的本地最佳实践 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_markdown_html_conversion.md) |
| **PDF 转换为 Markdown** | 推荐使用 Docling 进行高精度表格和层级解析，弃用 MarkItDown | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_pdf_to_markdown.md) |
| **时间敏感信息验证** | 验证或抓取超出模型知识截止日期（Knowledge Cutoff）实时数据的方法 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_temporal_info_verification.md) |
| **分阶段工作法** | 贯彻「隔离-处理-验证」闭环，在执行破坏性/全局修改前强制 Dry Run | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_staged_approach.md) |
| **多 Agent 并行分析** | 对大话题拆分 50% 相互重叠区域进行多方研究并交叉验证的实践 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_multi_agent_analysis.md) |
| **GUI 自动化方法论** | 将缺乏 API 的 UI 界面通过视觉/按键脚本转化为可编程接口的思路 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_gui_automation.md) |
| **AI 编程调试与诊断** | 面对 Agent “改不好代码”时的系统化排错诊断决策树 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_ai_debugging_diagnosis.md) |
| **AI 产品设计原则** | AI 原生产品中线性 Chat 模式与 Workspace 模式的取舍与规则解耦 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_ai_product_design.md) |
| **产品技术决策逆向分析** | 五步拆解法：重构设计空间、判断约束、追溯 trade-off 与成本结构 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/bestpractice_product_decision_analysis.md) |
| **项目脚手架重整** | 将零散、不规范的脚本文件夹升级整理为标准工程模板的规范 | [查看文件](https://github.com/grapeot/context-infrastructure/blob/master/rules/skills/project_scaffold.md) |

---

## 自动安装协议

如果你想让你的 AI Agent 安装本库中的任意技能，只需向其发送以下指令：

```text
Install this public skill repo into my workspace:
<技能仓库 GitHub URL 或文件 URL>

Start from my workspace AGENTS.md or CLAUDE.md. Follow any WORKSPACE.md or skills/INDEX.md routing rules. Clone or vendor the repo under an appropriate project directory. Expose exactly one root skill to my global skill index or agent instructions. Keep private aliases, local paths, credentials, endpoint defaults, and business context in a local overlay, not in the public repo.
```

## 隐私与安全

本生态系统中的所有仓库均严格遵循 **「使用虚拟数据发布」** 原则：
- 所有公开代码或文档中绝不包含真实的邮箱、手机号、密码或 1Password 私密引用。
- 工作区相关的敏感数据（如真实联系人映射、私密 API Key、接口网关配置）必须作为本地 Overlay 保留在本地，绝对不能提交推送到公共 GitHub 仓库中。
