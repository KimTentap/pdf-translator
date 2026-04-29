# PDF Translator — Claude Code 技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

将学术论文 PDF 翻译为**中英对照**的 HTML 文档，保留原文结构、所有图表、公式和术语表，方便阅读和打印。

> English version: [README_EN.md](README_EN.md)

## 效果预览

| 原始 PDF | 生成 HTML |
|:---:|:---:|
| 12 页学术论文 | 中英双栏对照，图文一一对应 |

原论文 → 翻译后的效果见：[示例截图](docs/example.png)

```
原始目录/
├── paper_translation.html   ← 浏览器打开即可阅读
└── pdf_images/              ← 从 PDF 提取的所有图片
```

HTML 特性：
- **双栏对照** — 左栏英文原文 / 右栏中文译文
- **图片完整** — 全部提取并按原文位置一一对应
- **表格双语** — 表头同时显示中英文
- **公式保留** — 方程内嵌显示
- **打印友好** — 包含 `@media print` 样式

## 快速开始

### 1. 在 Claude Code 中安装

编辑 `~/.claude/settings.json` 或项目的 `.claude/settings.json`：

```json
{
  "plugins": [
    "github:KimTentap/pdf-translator"
  ]
}
```

或通过命令行安装：
```bash
claude plugins install github:KimTentap/pdf-translator
```

### 2. 安装 Python 依赖

```bash
pip3 install pdfplumber pymupdf
```

### 3. 运行技能

在 Claude Code 中输入：
```
/pdf-translate
```

指定文件：
```
/pdf-translate path/to/paper.pdf
```

## 工作流程

技能会按以下步骤自动执行：

1. **提取文本** — 使用 pdfplumber 提取 PDF 中所有页面的文字
2. **提取图片** — 使用 PyMuPDF 提取 PDF 中嵌入的所有图片
3. **识别结构** — 分析章节、图表、表格、公式、术语表
4. **翻译内容** — Claude 将全部内容译为中文
5. **生成 HTML** — 按双栏对照布局生成网页文件
6. **验证输出** — 检查图片引用和布局正确性

## 手动使用脚本

Python 提取脚本可独立运行：

```bash
# 提取全部文本
python3 scripts/extract_text.py paper.pdf --json > text.json

# 提取全部图片
python3 scripts/extract_images.py paper.pdf ./images
```

然后可使用任意 LLM 翻译文本，参考 `template/base.css` 的 CSS 类名生成 HTML。

## 技术栈

| 组件 | 工具 |
|-----------|------|
| PDF 文本提取 | [pdfplumber](https://github.com/jsvine/pdfplumber) |
| 图片提取 | [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF) |
| 翻译 | Claude (via Claude Code) |
| 输出格式 | HTML5 + CSS3 |

## 参与贡献

欢迎提交 Bug 反馈和 PR。改进方向：
- 支持更多语言对
- LaTeX 公式渲染 (MathJax)
- DOCX 输出格式
- 图片描述翻译（无障碍阅读）

## 许可

MIT © 2025
