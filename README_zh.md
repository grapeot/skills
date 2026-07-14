本文档也有英文版：[English Version](README.md)

# AI Agent 技能索引

本仓库收录了适用于 **AI 编码智能体（AI Coding Agents）** 的常用技能与工作流。

> [!IMPORTANT]
> **直观展示与技能目录**
> 支持按场景过滤、快速搜索，并提供一键复制 Agent 安装 Prompt：
> **👉 [https://grapeot.github.io/skills/index_zh.html](https://grapeot.github.io/skills/index_zh.html)**

---

## 什么是 Skill？（核心哲学）

与 Cursor、Codex 或 Cloud Code 等平台所倡导的技能体系不同（它们通常绑定特定编辑器、使用严格类型定义的 JSON 配置或复杂的 SDK），我们的技能生态遵循以下原则：

1. **平台无关，自然语言优先**：Skill 的核心是一份 Markdown 格式的操作指南（`SKILL.md`），用于记录人类的工作流程、判断标准与防错经验。任何大模型或 Agent 都能直接理解和运行它。如果需要自动化执行，只需配上轻量的 CLI 脚本（如 Python 工具），即可在 Claude Code、Cursor、OpenCode 或自定义终端 Agent 中通用。
2. **过程与结果的确定性**：AI Agent 执行任务时容易出现幻觉或自行简化步骤。我们的 Skill 模板定义了清晰的执行边界、验证步骤和核对清单，让 Agent 产出的结果稳定可靠。
3. **文件即接口 (Files-as-Interfaces)**：技能与本地工作区的交互完全通过读写文件进行。输入和输出都是普通的文本文件（Markdown、JSON、SQLite），不依赖特定的网络服务。这也使得 Agent 的操作能完美接入 Git，随时可以审计与回滚。
4. **本地与公共隔离**：公开仓库只定义通用的技术契约与 CLI 接口。私人的本地路径、API Key、联系人别名等隐私信息，都以 Overlay（覆盖层）的形式保存在本地私有工作区中。

### 核心背景阅读
* **方法论**：[用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html)（英文版：[Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html)）
* **架构设计**：[为什么AI只会说正确的废话，以及怎么把它逼出舒适区](https://yage.ai/context-infrastructure.html)

### 维护或 Fork 这套技能索引

本仓库自带一份可复用的 [Skill Registry Lifecycle](skills/skill_registry_lifecycle.md)。增加、删除、fork 或从零搭建 registry 前应先读取这份 Skill。它定义了设计原则、必要上下文、成功标准、隐私审查、发布门槛和已经发生过的维护陷阱。

---

## 快速参考（独立工具仓库列表）

为了方便浏览，以下列出了独立托管的技能工具仓库：

### 工具与 API 连接器
* [tavily-skill](https://github.com/grapeot/tavily-skill) — 面向 Agent 优化的网页搜索引擎
* [gdocs-skill](https://github.com/grapeot/gdocs-skill) — Google Docs 命令行编辑器
* [outlook_skill](https://github.com/grapeot/outlook_skill) — Outlook 邮件与日历同步 CLI
* [resend_email_skill](https://github.com/grapeot/resend_email_skill) — 基于 Resend 的自定义域名邮件发送工具
* [imessage_skill](https://github.com/grapeot/imessage_skill) — macOS iMessage 本地发信工具
* [pptx.skill](https://github.com/grapeot/pptx.skill) — PPTX 幻灯片修改工具
* [presentation_skill](https://github.com/grapeot/presentation_skill) — 可预览 slide deck 搭建 skill（默认整页图像幻灯片，按需 HTML 模块；非 PPTX）
* [image-generation-skill](https://github.com/grapeot/image-generation-skill) — AI 绘图与高清放大工具
* [genai_portrait_skill](https://github.com/grapeot/genai_portrait_skill) — 保持人物身份与摄影整体一致性的人像、头像和证件照编辑 skill
* [tiff-icc-profile](https://github.com/grapeot/tiff-icc-profile) — TIFF 图像色彩配置文件（ICC）嵌入工具
* [online-media-skill](https://github.com/grapeot/online-media-skill) — 网络视频下载与 Whisper 语音转文字工具
* [open_router_data_scraper](https://github.com/grapeot/open_router_data_scraper) — OpenRouter 模型流量数据抓取工具（token 用量、排名、benchmark）

### 日常量化与生活记录
* [health-quantification](https://github.com/grapeot/health-quantification) — Apple Health 健康数据本地 SQLite 分析工具
* [roest-analysis](https://github.com/grapeot/roest-analysis) — Roest 咖啡烘焙曲线抓取与分析工具
* [intake-skill](https://github.com/grapeot/intake-skill) — 语音备忘录自动转录与整理工具

### 创新与研究
* [innovation-assistant-skill](https://github.com/grapeot/innovation-assistant-skill) — 结构化创新引擎（SIT + Think Bigger），可执行流水线

### Agent 运行基础设施
* [process-launcher](https://github.com/grapeot/process-launcher) — macOS 本地 HTTP 进程守护服务
* [opencode_skill](https://github.com/grapeot/opencode_skill) — OpenCode 异步任务运行管理器
* [opencode-docker](https://github.com/grapeot/opencode-docker) — OpenCode Docker 部署配置模板

*(欲查看完整技能列表（包含 27 个内置工作流与最佳实践）并一键复制 Prompt 安装指引，请直接访问 [直观展示页面](https://grapeot.github.io/skills/index_zh.html))*
