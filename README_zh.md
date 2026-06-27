本文档也有英文版：[English Version](README.md)

# AI Agent 技能索引

本仓库是 **AI 编码智能体技能（AI Coding Agent Skills）** 的集中注册与索引中心。

> [!IMPORTANT]
> **交互式展示端与技能目录**
> 想要获得更直观的交互体验——包括场景化过滤、多维搜索以及一键复制 Agent 安装 Prompt——请直接访问我们的官方展示端：
> **👉 [https://grapeot.github.io/skills/index_zh.html](https://grapeot.github.io/skills/index_zh.html)**

---

## 什么是 Skill？（核心哲学）

与 Cursor、Codex 或 Cloud Code 等平台所倡导的技能体系不同（它们通常绑定特定编辑器、使用严格类型定义的 JSON 配置或繁重的 SDK 开发包），我们的技能生态遵循以下设计原则：

1. **平台无关，自然语言优先**：Skill 的核心是一份 Markdown 格式的操作指南（`SKILL.md`），用于记录人类的工作流程、判断标准与防错教训。任何大模型或 Agent 都能直接阅读并消费它。在需要自动化执行的场景下，我们仅需为其配上一个轻量的 CLI 脚本（如 Python 命令行工具）。它在 Claude Code、Cursor、OpenCode 或自定义的终端 Agent 中完全通用。
2. **过程与结果的确定性**：AI Agent 在执行任务时容易发生幻觉或擅自简化流程。我们的 Skill 模版中明确定义了执行边界、多重验证步骤以及交付标准检查清单，以此确保 Agent 产出的结果高度可靠。
3. **文件即接口 (Files-as-Interfaces)**：技能与工作区的交互通过读写文件进行。输入和输出都是工作区里的普通文本文件（Markdown、JSON、SQLite），不依赖网络 API 服务。这让 Agent 的所有操作都处于 Git 的版本控制下，可被随时审计、修改和回滚。
4. **本地与公共隔离**：公开的 Skill 仓库仅定义通用的技术契约与 CLI 协议，所有私人路径、敏感 API Key、联系人别名均以 Overlay（覆盖层）的形式保存在用户本地的私有工作区中。

### 核心背景阅读
* **方法论**：[用好AI的第二步：先写Skill再执行](https://yage.ai/skill-first.html)（英文版：[Step Two to Using AI Well: Write the Skill Before You Execute](https://yage.ai/skill-first-en.html)）
* **架构设计**：[为什么AI只会说正确的废话，以及怎么把它逼出舒适区](https://yage.ai/context-infrastructure.html)

---

## 快速参考（独立工具仓库列表）

为方便快速浏览，以下列出了所有独立托管的技能工具仓库链接：

### 工具与 API 连接器
* [tavily-skill](https://github.com/grapeot/tavily-skill) — 针对 Agent 优化的网页搜索引擎
* [gdocs-skill](https://github.com/grapeot/gdocs-skill) — Google Docs 命令行编辑器
* [outlook_skill](https://github.com/grapeot/outlook_skill) — Outlook 邮件与日历调度 CLI
* [resend_email_skill](https://github.com/grapeot/resend_email_skill) — Resend 自定义域名邮件发送器
* [imessage_skill](https://github.com/grapeot/imessage_skill) — macOS iMessage 本地发信工具
* [pptx.skill](https://github.com/grapeot/pptx.skill) — PPTX 幻灯片大纲修改器
* [presentation_skill](https://github.com/grapeot/presentation_skill) — 默认图像生成、必要时 fallback 到 HTML 的 presentation deck skill
* [image-generation-skill](https://github.com/grapeot/image-generation-skill) — AI 画图与高清放大工具
* [tiff-icc-profile](https://github.com/grapeot/tiff-icc-profile) — TIFF 图像色彩配置文件嵌入器
* [online-media-skill](https://github.com/grapeot/online-media-skill) — 视频下载与 Whisper 转录工具

### 日常量化与生活记录
* [health-quantification](https://github.com/grapeot/health-quantification) — Apple Health 数据 SQLite 回归分析
* [roest-analysis](https://github.com/grapeot/roest-analysis) — Roest 咖啡烘焙机曲线抓取分析
* [intake-skill](https://github.com/grapeot/intake-skill) — 语音备忘录 ASR 自动化转录与整理

### Agent 运行基础设施
* [process-launcher](https://github.com/grapeot/process-launcher) — macOS 本地 HTTP 进程守护服务
* [opencode_skill](https://github.com/grapeot/opencode_skill) — OpenCode 异步任务运行管理器
* [opencode-docker](https://github.com/grapeot/opencode-docker) — OpenCode Docker 部署镜像模版

*(想要查看包含 26 个内置工作流与最佳实践指南在内的完整列表，以及获取一键 Prompt 安装协议，请直接前往 [交互式网页展示端](https://grapeot.github.io/skills/index_zh.html))*
