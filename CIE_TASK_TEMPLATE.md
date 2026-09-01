# 🚀 CIE Psychology Courseware — 任务启动完整模板

> **版本**: v3.0（2026-08-17 最终版）🆕
> **基于**: GitHub 成功版本 + 2个月实战经验总结 + Dement (1957) 最新开发经验
> **适用**: 所有新建/优化 CIE Core Studies 课件的任务

---

## 📖 使用说明

### 如何使用此模板

**场景 1：你要启动一个新任务做 CIE 课件**

直接复制以下「📌 任务指令模板」部分发给新任务，它会包含所有必要信息。

**场景 2：你自己要做 CIE 课件**

按照「✅ 质量检查清单」逐项执行，确保不遗漏任何细节。

---

## 📌 任务指令模板（可直接复制给新任务）

```
🎯 任务目标

你是 CIE Psychology 课件开发专家。请基于以下严格标准生成/优化 CIE Core Studies 的 HTML 课件。
每一个细节都必须遵守，不得偏离。这是基于 2 个月实战经验和多次踩坑总结出的成功模式。

---

📚 项目背景（必须包含）

项目位置：/Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages/cie/
GitHub仓库：https://github.com/lawrenceliu007/psychology-courseware
部署方式：git add → commit → push 到 main 分支
推送代理：HTTPS + V2rayU (端口7897)

已完成 CIE 实验（12个，按分类）：
✅ 生物类（红色 #dc2626）：
   - Hassett (2008) - Monkey Toy Preferences
   - Hölzel (2011) - Mindfulness Brain Scans
   - Dement (1957) - Sleep and Dreams ⭐ **v3.0 模板验证实验**
   - Andrade (2010) - Doodling

✅ 认知类（蓝色 #1565C0）：
   - Baron-Cohen (2001) - Eyes Test
   - Pozzulo (2011) - Child Witnesses & Line-ups

✅ 社会类（橙色 #ea580c）：
   - Milgram (1963) - Obedience ⭐⭐⭐ 最复杂最完整（v2.0 模板）
   - Piliavin (1969) - Subway Samaritans ⭐⭐⭐ 推荐参考（v2.0 模板）
   - Perry (2015) - Personal Space & Oxytocin

✅ 学习类（绿色 #2E7D32）：
   - Bandura (1961) - Bobo Doll Aggression
   - Fagen (2014) - Elephant Learning / SPR Training
   - Saavedra (2002) - Button Phobia / Disgust & Evaluative Learning

🆕 **v3.0 关键更新**（基于 Dement 开发经验，2026-08-17）：
- 🐛 **Cancel 高亮修复**：`cancelNoteInput()` 必须移除 `<mark>` 元素
- 📍 **Scroll Spy 功能**：IntersectionObserver 自动高亮 sidebar 当前章节
- 🏷️ **Header Badges 特色化**：标签要突出实验核心发现（不是通用信息）
- 📝 **Notes Panel v3 完整结构**：新增 hlPreview、nc-actions、nc-footer
- 🎨 **CSS 类名统一**：`.active` → `.sb-active`
- 🌙 **Dark Mode 无死角**：`.hl-text`, `.note-card-hl` 等新组件暗色适配

📖 **详细规范请参考**：
- `.workbuddy/memory/MILGRAM_SUCCESS_TEMPLATE.md`（v3.0 完整版，1400+行）

你的任务是：
- 新建缺失的 CIE 实验
- 或优化已有实验的质量

---

✅ 成功模式参考（必须读取）

📖 设计模式文档位置：
/Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages/DESIGN_PATTERN_SUMMARY.md（1844行完整版）

⭐ 必须读取的两个成功案例（从 GitHub 获取原始代码，不是本地文件！）：

1. Milgram（复杂模式，1884行）：
   https://raw.githubusercontent.com/lawrenceliu007/psychology-courseware/main/cie/milgram/index.html
   特点：有独立 style 块 !important、13个中文逻辑总结、Progress Bar

2. Piliavin（简单模式 ⭐推荐用于新实验，1430行）：
   https://raw.githubusercontent.com/lawrenceliu007/psychology-courseware/main/cie/piliavin/index.html
   特点：无独立 style 块、Notes Panel 只用3个属性、代码简洁

🔍 关键：必须看 GitHub 上的版本！本地文件可能不是最新或已被修改！

---

🎨 设计铁律（绝对不可违反）

═══════════════════════════════════════
1️⃣ 布局规则（CIE 用三栏布局）
═══════════════════════════════════════

✅ 正确的三栏 Grid 布局：
.page-layout {
  display: grid;
  grid-template-columns: 170px minmax(0,1fr) 250px;  /* sidebar + content + notes */
  gap: 20px;
  align-items: start;  /* 关键！让 sticky 生效 */
}

各区域定义：
- .sidebar（左侧导航）：width 由 grid 决定，overflow-y:auto, sticky top:60px
- .main-content（中间内容）：minmax(0,1fr), max-width:660px
- .notes-col（右侧笔记）：width:250px, sticky top:60px（见第2节详细规则）

❌ 绝对禁止：
- 不要用 flex 布局替代 grid
- 不要改变列宽比例（除非用户明确要求）
- 不要把 nav-bar 放在 .page-layout 外面（必须在 container 内部）

═══════════════════════════════════════
2️⃣ Notes Panel 实现黄金法则 ⭐⭐⭐
═══════════════════════════════════════

⚠️ 这是历史上踩过最大坑的地方！Perry 实验尝试了 4 次修复都失败！

✅ 正确做法（Piliavin 模式，唯一验证成功的简单方案）：

CSS（只在 <head> 中定义一次，不要有第二个定义！）：
.notes-col {
  width: 250px;
  background: {主题色的10%透明度背景};
  border: 2px solid {主题色的30%透明度};
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  position: sticky;    /* ← 核心属性1 */
  top: 60px;           /* ← 核心属性2 */
  max-height: calc(100vh - 80px);  /* ← 核心属性3 */
  box-shadow: 0 2px 12px {主题色阴影};
  /* 只有这些属性！绝对不要加其他任何属性！ */
}

❌ 绝对禁止添加的属性（100% 会导致 sticky 失效）：
- overflow: hidden / scroll / auto  → 创建新滚动容器，sticky 失效
- -webkit-sticky                   → 不需要，现代浏览器支持标准属性
- align-self: start                → 不需要，已在父元素设置 align-items: start
- position: -webkit-sticky          → 不需要
- 任何额外的 positioning 属性

💡 如果 sticky 不工作，按顺序检查：
1. .notes-col 是否有多个 CSS 定义冲突？（用浏览器 DevTools 检查）
2. 父元素 .page-layout 是否有 overflow: hidden/auto/scroll？
3. 祖先元素 .container 是否有 overflow?
4. 是否用了独立 style 块覆盖了 <head> 中的定义？

═══════════════════════════════════════
3️⃣ 文件末尾 DOM 顺序铁律 ⭐⭐⭐
═══════════════════════════════════════

⚠️ 任何偏离此顺序的操作都会导致 Notes Panel 不显示或样式被覆盖！

正确顺序（从 </main> 之后开始）：
</main>
<aside class="notes-col">...</aside>              ← ① Notes HTML
</div><!-- END PAGE LAYOUT -->
<div class="footer-note">...</div>                ← ② 引用信息（可选但推荐）
</div><!-- END CONTAINER -->                      ← ③ 关闭容器
<!-- Study Navigator HTML -->                     ← ④ 导航组件（可选）
<button class="back-to-top">↑</button>            ← ⑤ 返回顶部按钮
<script>
(function() {
  // Notes System IIFE                          ← ⑥ JS 在 style 之前！
  // ... load(), render(), save() ...
})();
</script>
<style>
/* 独立样式块 !important */                    ← ⑦ Style 在 JS 之后、</body> 之前！
/* 如果用 Piliavin 简单模式，这整个 <style> 块都不需要！ */
</style>
</body>

❌ 常见错误：
- ❌ <style> 在 <script> 之前 → JS 动态添加的元素没有样式
- ❌ 缺少 </div><!-- END CONTAINER --> → 结构不完整
- ❌ <script> 放在 <head> 中 → 执行时 DOM 还没加载完
- ❌ 缺少 IIFE 包装 → 变量污染全局作用域

═══════════════════════════════════════
4️⃣ 无障碍功能（必需组件，不是可选！）
═══════════════════════════════════════

必须在导航栏包含三个控制按钮：

HTML 结构：
<nav class="nav-bar">
  <div class="nav-breadcrumb">
    <a href="../index.html">Home</a> <span class="sep">›</span>
    <a href="index.html">CIE Core Studies</a> <span class="sep">›</span>
    <span>{实验名}</span>
  </div>
  <span class="nav-pill">{emoji} {主题标签}</span>
  <!-- 控制按钮放在这里 -->
  <div class="nav-controls">
    <button onclick="toggleDarkMode()" id="darkBtn" class="nav-btn">🌙 Dark</button>
    <button onclick="adjustFontSize(-1)" class="nav-btn">A-</button>
    <button onclick="adjustFontSize(1)" class="nav-btn">A+</button>
  </div>
</nav>

必须实现的 JavaScript 函数：

// 1. Dark Mode 切换
function toggleDarkMode() {
  const isDark = document.body.classList.toggle('dark');
  document.getElementById('darkBtn').textContent = isDark ? '☀️ Light' : '🌙 Dark';
  localStorage.setItem('{实验名}-darkMode', isDark);
}

// 2. 字体大小调整（范围：12px - 22px）
function adjustFontSize(delta) {
  const html = document.documentElement;
  let size = parseFloat(getComputedStyle(html).fontSize) + delta * 2;
  size = Math.max(12, Math.min(22, size));  // 限制范围
  html.style.fontSize = size + 'px';
  localStorage.setItem('{实验名}-fontSize', size);
}

// 3. 页面加载时恢复用户偏好（IIFE 初始化）
(function() {
  const dark = localStorage.getItem('{实验名}-darkMode') === 'true';
  if (dark) document.body.classList.toggle('dark');
  const fontSz = localStorage.getItem('{实验名}-fontSize');
  if (fontSz) document.documentElement.style.fontSize = fontSz + 'px';
})();

⚠️ 字体调整修复要点（历史踩坑）：
❌ 错误：body { font-size: 16px; }  /* 固定像素值，无法调整 */
✅ 正确：
html { font-size: 16px; }  /* 基准 - 可被 JS 修改 */
body { font-size: 1em; }   /* 继承 html 的 font-size */

必须实现的 CSS（50+ 条 .dark 规则）：

/* 暗黑模式核心变量覆盖 */
body.dark {
  --bg: #0f172a;      /* 深蓝黑背景 */
  --text: #e2e8f0;    /* 浅灰白文字 */
  --card-bg: #1e293b; /* 卡片背景 */
  --border: #334155;  /* 边框色 */
}

/* 导航栏 */
body.dark .nav-bar { background: #1e293b; border-color: #334155; }
body.dark .nav-pill { background: {主题色暗版}; }

/* Sidebar */
body.dark .sidebar { background: #1e293b; border-color: #334155; }
body.dark .sidebar a { color: #94a3b8; }
body.dark .sidebar a:hover { color: {主题色}; }

/* Section 卡片 */
body.dark .section { background: #1e293b; border-color: #334155; }
body.dark .section h2 { color: {主题色}; border-bottom-color: #334155; }

/* 表格 */
body.dark table { background: #0f172a; border-color: #334155; }
body.dark th { background: {主题色暗版}; color: #fff; }
body.dark td { border-color: #334155; color: #cbd5e1; }

/* Key Term Box */
body.dark .keyterm-box { background: #1e293b; border-left-color: {主题色}; }
body.dark .keyterm-box strong { color: {主题色亮版}; }

/* 图片 */
body.dark .figure img { border-color: #334155; }
body.dark .figure-caption { color: #94a3b8; }

/* Notes Panel */
body.dark .notes-col { background: #16213e; border-color: #334155; }
body.dark .nc-header { background: linear-gradient(135deg, {深色}, {更深色}); }
body.dark .note-card { background: #1e293b; border-left-color: {主题色}; }

/* 链接 */
body.dark a { color: #60a5fa; }
body.dark a:hover { color: #93c5fd; }

/* 按钮 */
body.dark button { background: #334155; color: #e2e8f0; border-color: #475569; }
body.dark button:hover { background: #475569; }

/* 平滑过渡 */
body, body.dark * {
  transition: background-color .3s ease, color .3s ease, border-color .3s ease;
}

═══════════════════════════════════════
5️⃣ 图片 Lightbox 功能（必需组件）
═══════════════════════════════════════

点击图片可放大查看，提升用户体验。

CSS 实现：
/* Lightbox Overlay */
.lightbox-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9);
  z-index: 9999;
  cursor: zoom-out;
  opacity: 0;
  transition: opacity .3s ease;
}
.lightbox-overlay.show {
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 1;
}
.lightbox-content {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
  transform: scale(0.95);
  transition: transform .3s ease;
}
.lightbox-overlay.show .lightbox-content {
  transform: scale(1);
}
.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 40px;
  color: #fff;
  cursor: pointer;
  z-index: 10000;
}
.lightbox-caption {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  color: #fff;
  font-size: 14px;
  text-align: center;
  max-width: 80%;
}

HTML 结构（放在 </body> 前）：
<div class="lightbox-overlay" id="lightbox" onclick="closeLightbox()">
  <span class="lightbox-close">&times;</span>
  <img class="lightbox-content" id="lightboxImg" src="" alt="">
  <p class="lightbox-caption" id="lightboxCaption"></p>
</div>

JavaScript 实现：
function openLightbox(img) {
  const overlay = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const caption = document.getElementById('lightboxCaption');
  lightboxImg.src = img.src;
  // 获取图片说明（从父元素的 .figure-caption 获取）
  const figureCaption = img.closest('.figure')?.querySelector('.figure-caption');
  caption.textContent = figureCaption ? figureCaption.textContent : '';
  overlay.classList.add('show');
  document.body.style.overflow = 'hidden';  // 防止背景滚动
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('show');
  document.body.style.overflow = '';  // 恢复滚动
}

// 为所有图片添加点击事件
document.querySelectorAll('.figure img').forEach(img => {
  img.style.cursor = 'zoom-in';
  img.addEventListener('click', () => openLightbox(img));
});

// ESC 键关闭
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeLightbox();
});

---

🌈 主题色系统

| 实验类型 | 主题色 | Hex | 渐变色 | 浅色背景 | 边框色 |
|---------|--------|-----|--------|---------|--------|
| **生物类** | 🔴 红色 | `#dc2626` | `linear-gradient(135deg, #dc2626, #991b1b)` | `rgba(220,38,38,.08)` | `rgba(220,38,38,.25)` |
| **认知类** | 🔵 蓝色 | `#1565C0` | `linear-gradient(135deg, #1565C0, #0d47a1)` | `rgba(21,101,192,.08)` | `rgba(21,101,192,.25)` |
| **社会类** | 🟠 橙色 | `#ea580c` | `linear-gradient(135deg, #ea580c, #c2410c)` | `rgba(234,88,12,.08)` | `rgba(234,88,12,.25)` |
| **学习类** | 🟢 绿色 | `#2E7D32` | `linear-gradient(135deg, #2E7D32, #1B5E20)` | `rgba(46,125,50,.08)` | `rgba(46,125,50,.25)` |

每个颜色需要配套的 CSS 变量：
:root {
  --primary: {主题色};
  --primary-dark: {深色};
  --primary-light: {浅色背景};
  --bg: #ffffff;
  --text: #1f2937;
  --card-bg: #ffffff;
  --border: #e5e7eb;
}

---

📝 语言风格标准

✅ 正文语言：英文为主 + 中文辅助

原则：
1. 关键术语首次出现括号注中文：action potential（动作电位）
2. 后续使用不再重复翻译（避免文本量翻倍）
3. 复杂概念后可加简短中文总结帮助学生理解
4. 段落末尾可选加 <p class="cn-note">💡 中文提示</p>

示例：
✅ 正确：
<p>The <strong>synaptic cleft</strong>（突触间隙）is the tiny gap between neurons.</p>
<p>Neurotransmitters cross this gap to transmit signals.</p>
<p class="cn-note">💡 突触传递是神经元通信的关键过程</p>

❌ 错误：
<p>The synaptic cleft（突触间隙）is the tiny gap between neurons（神经元之间的小缝隙）.
Neurotransmitters（神经递质）cross this gap（穿过这个间隙）to transmit signals（传输信号）.</p>
<!-- 每个词都翻译 = 文本量翻倍 = 学生疲劳 -->

禁止事项：
- ❌ 不要面向教师的注释语言："必考"、"重要修正"、"⚠️"、"BUG"、"← 不是"
- ❌ 不要写 "Note: This text is organised based on..." 注释
- ❌ 不要每行都中英文重复

---

📐 章节结构标准（CIE 考试导向）

对于 CIE Core Studies，必须包含以下章节结构：

§1 Introduction（研究背景+目的）
  - Research aim（研究目的）
  - Background context（背景上下文）
  - Hypothesis（假设，如果有）

§2 Method（方法）
  - 2.1 Research Design（研究设计：实验/相关/观察/个案）
  - 2.2 Sample（样本：人数、年龄、招募方式、抽样方法）
  - 2.3 Variables（变量：IV/DV、操作化定义、控制变量）
  - 2.4 Materials/Equipment（材料/设备，如果有特殊工具）

§3 Procedure（步骤流程）
  - 按时间顺序描述参与者经历的过程
  - 包含关键指导语（debriefing script 等）
  - 可用编号列表或流程图

§4 Results（结果）
  - 定量数据（均值、标准差、相关系数、p值）
  - 定性发现（访谈内容、观察记录）
  - 图表（表格、柱状图、折线图等）

§5 Discussion（讨论）
  - 5.1 Explanation of Findings（结果解释）
  - 5.2 Comparison with Previous Research（与前人研究对比）
  - 5.3 AO3 Evaluation（评价：优势 + 劣势，至少各3点）

§6 Exam Practice（考试练习）
  - 至少 2 道题目（AO1 描述题 + AO3 评价题）
  - Model Answer with mark scheme（评分标准的模范答案）
  - Exam Tips（应试技巧）

每个章节必须包含：
- ✅ Exam Key Points 按钮（Baron-Cohen 宽版风格）
  ```html
  <div class="summary-card-header" onclick="toggleSummary(this)">
    <span>▶</span>
    <span>§{N} {章节标题}</span>
    <span class="ao-badge">AO{1 or 3}</span>
  </div>
  <div class="summary-card-body">
    <ul>
      <li>Key Point 1</li>
      <li>Key Point 2</li>
      ...
    </ul>
  </div>
  ```
- ✅ 中文逻辑总结（紫色主题 .cn-summary-card）
  ```html
  <div class="cn-summary-card">
    <div class="cn-summary-header" onclick="toggleCnSummary(this)">
      📊 中文逻辑总结
    </div>
    <div class="cn-summary-content">
      <p><strong>核心逻辑：</strong>...</p>
      <p><strong>记忆口诀：</strong>...</p>
      <p><strong>考试技巧：</strong>...</p>
    </div>
  </div>
  ```

---

🚫 历史血泪教训（绝对不能重蹈覆辙）

| 教训 | 详情 | 后果 | 解决方案 |
|------|------|------|---------|
| **Notes Sticky 失败** | Perry 实验尝试了 4 种修复方案都失败 | 浪费 2 小时，用户放弃 | 用 Piliavin 模式，只保留 3 个属性 |
| **根因** | 加了多余属性（overflow/-webkit-sticky/align-self） | 越修越坏 | sticky 的黄金法则：越简单越好 |
| **字体调整失效** | body 写死 font-size: 16px | A+/A- 按钮无效 | 改为 html{font-size:16px} + body{font-size:1em} |
| **DOM 顺序错误** | `<style>` 在 `<script>` 之前 | 样式被覆盖，Notes 不显示 | 严格遵守文件末尾顺序铁律 |
| **绿色覆盖橙色** | 错误地用绿色模板覆盖已成功的橙色版本 | 用户非常生气 | 覆盖前先 git diff + 备份 |
| **未推送就认为安全** | 只存在本地文件，未 git push | 可能丢失 | 三步缺一不可：add → commit → push |
| **用户记忆 > 文件状态** | AI 用"当前文件就是这样"反驳用户 | 信任破裂 | 相信用户，调查原因 |
| **中英文过度翻译** | 每行都翻译导致文本量翻倍 | 学生阅读疲劳 | 只在首次出现时注中文 |
| **缺少无障碍功能** | 初始版本遗漏 Dark Mode 和 Font Adjuster | 用户反馈后才补充 | 作为必需组件从一开始就加入 |

---

✅ 质量检查清单（完成后逐项确认）

🔧 布局检查
- [ ] Grid 三栏布局正确（grid-template-columns: 170px minmax(0,1fr) 250px）
- [ ] Nav-bar 在 .container 内部、.page-layout 之前
- [ ] Notes Panel sticky 生效（在 Chrome/Safari 中实测）
- [ ] 主内容区 max-width: 660px
- [ ] 响应式断点 900px 工作正常（隐藏 sidebar 和 notes）

🎨 功能检查
- [ ] 🌙 Dark Mode 切换正常（测试 50+ 条 CSS 规则是否全部生效）
- [ ] A-/A+ 字体调整正常（实际缩放效果，不只是按钮响应）
- [ ] 图片点击放大功能正常（Lightbox 显示大图 + 说明文字）
- [ ] Lightbox 可通过 X 按钮/点击背景/ESC 键关闭
- [ ] Notes 双击添加笔记功能正常
- [ ] Notes 删除/导出/清空功能正常
- [ ] 返回顶部按钮正常（滚动 >400px 时显示）
- [ ] 设置刷新后保留（localStorage 工作正常）

📝 内容检查
- [ ] 英文为主 + 关键术语中文注释（不过度翻译）
- [ ] 无面向教师的注释语言
- [ ] AO1/AO3 分区清晰（Exam Key Points 明确标记）
- [ ] 每个章节都有 Exam Key Points + 中文逻辑总结
- [ ] 至少 2 道考试练习题带 Model Answer
- [ ] 研究细节准确（样本量、程序、结果数据）
- [ ] 引用信息完整（作者、年份、期刊、DOI 如有）

💻 技术检查
- [ ] 文件末尾顺序符合铁律（Notes HTML → footer → container关闭 → navigator → back-to-top → JS IIFE → style → /body）
- [ ] 无 console 错误（打开浏览器 DevTools Console 检查）
- [ ] 无 HTML 验证错误（使用 W3C Validator）
- [ ] localStorage key 命名正确（{实验名}-darkMode, {实验名}-fontSize, {实验名}-notes）
- [ ] 图片路径正确（相对路径 images/filename.png）
- [ ] 所有链接有效（侧边栏导航、面包屑、外部链接）
- [ ] 面包屑相对路径从**页面自身目录**算起：二级目录页面（如 edexcel/xxx/）回根 = `../../index.html`，不是 `../index.html`（2026-09-01 事故：写成 ../ 指向不存在的 edexcel/index.html → 404；检查命令 `grep -rn 'href="\.\./index\.html"' --include="*.html" .` 应为空）

🚀 部署检查
- [ ] 已 git add（添加新文件/修改）
- [ ] 已 git commit（commit message 清晰描述变更）
- [ ] 已 git push 到 GitHub main 分支
- [ ] 推送后在线访问验证（GitHub Pages URL 可访问）

---

📦 交付物要求

输出位置：/Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages/cie/{实验名小写}/index.html

目录结构：
cie/
└── {实验名小写}/
    ├── index.html        （完整课件，预计 1400-1900 行）
    └── images/           （所有图片资源）
        ├── fig1.png
        ├── fig2.png
        └── ...

必须包含的文件：
1. ✅ index.html（完整课件，包含所有 CSS/JS/HTML）
2. ✅ images/ 文件夹（所有图片资源，已复制到正确位置）
3. ✅ Git 推送记录（commit hash，用于追溯）

推送命令（必须执行）：
cd /Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages
git add cie/{实验名小写}/
git commit -m "Add {实验名} ({年份}): {简短描述}

Content:
- {主要章节列表}
- Images: {图片数量} figures
- Features: Notes Panel, Dark Mode, Font Adjuster, Lightbox
- Lines: {总行数}"
git push https://github.com/lawrenceliu007/psychology-courseware.git main

---

💬 示例：如何下达具体任务

📌 任务示例模板：

---
任务：为 CIE Psychology 课程新建 [实验全名] ([年份]) 课件

输入材料：
- 课本截图路径：/Users/lawrenceliu/Downloads/.../
- PDF原文路径：（如果有，提供路径）
- 视觉图片：（如果有，提供路径）

要求：
1. 严格遵循 /Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages/CIE_TASK_TEMPLATE.md 中的所有标准
2. 参考 DESIGN_PATTERN_SUMMARY.md 的 Piliavin 简单模式（首选）或 Milgram 复杂模式
3. 主题色：[选择对应颜色：红/蓝/橙/绿]
4. 必须包含：Notes Panel + Dark Mode + Font Adjuster + Image Lightbox
5. 语言风格：英文为主 + 中文辅助（首次出现术语括号注中文）
6. 章节结构：§1-§6 标准 CIE 格式（Introduction → Method → Procedure → Results → Discussion → Exam Practice）
7. 完成后推送到 GitHub（add + commit + push）
8. 完成质量检查清单的所有项目

参考资源：
- 设计规范：gh-pages/DESIGN_PATTERN_SUMMARY.md（1844行完整版）
- 成功案例（GitHub 原始代码）：
  * Piliavin（简单模式 ⭐推荐）：
    https://raw.githubusercontent.com/lawrenceliu007/psychology-courseware/main/cie/piliavin/index.html
  * Milgram（复杂模式）：
    https://raw.githubusercontent.com/lawrenceliu007/psychology-courseware/main/cie/milgram/index.html
- 任务模板：gh-pages/CIE_TASK_TEMPLATE.md（本文件）

输出：
- 文件位置：gh-pages/cie/{实验名小写}/index.html
- GitHub Commit：提供 commit hash
- 质量确认：完成 ✅ 质量检查清单 的所有项目
---

📚 附录 A：快速参考卡片

### Notes Panel Sticky 快速检查
```css
/* ✅ 正确（Piliavin 模式）*/
.notes-col {
  position: sticky;
  top: 60px;
  max-height: calc(100vh - 80px);
}
/* 只有这3个属性！不要加其他！*/
```

### 字体调整快速修复
```css
/* ✅ 正确 */
html { font-size: 16px; }
body { font-size: 1em; }
/* JS 修改 html.style.fontSize 即可 */
```

### 文件末尾快速检查
```
</main>
<aside class="notes-col">...</aside>     ← 1. Notes
</div><!-- END PAGE LAYOUT -->
</div><!-- END CONTAINER -->            ← 2. Close containers
<button class="back-to-top">↑</button>  ← 3. Back to top
<script>(function(){ ... })()</script>  ← 4. JS IIFE
<style>/* !important */</style>         ← 5. Style block
</body>                                  ← 6. End
```

### localStorage Key 命名规范
```
{实验名小写连字符}-darkMode     例：milgram-darkMode
{实验名小写连字符}-fontSize     例：milgram-fontSize
{实验名小写连字符}-notes        例：milgram-notes
```

### 主题色快速选择
- 生物类实验 → 🔴 #dc2626（红）
- 认知类实验 → 🔵 #1565C0（蓝）
- 社会类实验 → 🟠 #ea580c（橙）
- 学习类实验 → 🟢 #2E7D32（绿）

---

📚 附录 B：常见问题排查（FAQ）

**Q1: Notes Panel 不显示？**
A: 检查文件末尾顺序是否正确（JS 在 style 之前）。检查是否有多个 .notes-col CSS 定义冲突。

**Q2: Notes Panel 不跟随滚动（sticky 不工作）？**
A: 删除所有额外属性，只保留 position:sticky; top:60px; max-height:calc(100vh-80px); 检查父元素和祖先元素是否有 overflow:hidden/auto/scroll。

**Q3: Dark Mode 切换后部分元素没变化？**
A: 检查是否为该元素写了 body.dark .elementName 规则。可能遗漏了某些组件的暗黑模式样式。

**Q4: 字体调整按钮点了但文字大小不变？**
A: 检查 body 的 font-size 是否写的固定 px 值（如 16px）。改为 html{font-size:16px} + body{font-size:1em}。

**Q5: 图片点击后没反应？**
A: 检查 JS 是否在 DOM 加载完后执行（用 IIFE 或 DOMContentLoaded）。检查选择器是否正确（.figure img）。

**Q6: 推送失败 SSL_ERROR_SYSCALL？**
A: 检查代理是否开启（V2rayU 端口 7897）。重试命令。

**Q7: 本地预览正常但 GitHub Pages 上样式错乱？**
A: 检查文件路径是否用相对路径（不用绝对路径）。检查文件权限。清除浏览器缓存后刷新。

---

📚 附录 C：Edexcel vs CIE 差异对照表

| 特性 | CIE（三栏布局） | Edexcel（两栏布局） |
|------|----------------|-------------------|
| **Grid 列数** | 3列（sidebar + content + notes） | 2列（sidebar + content） |
| **主内容宽度** | max-width: 660px | max-width: 900px |
| **Notes Panel** | ✅ 有（右侧 250px） | ❌ 移除（用户明确要求） |
| **主题色** | 按实验类型分色 | 统一橙色 #ea580c |
| **章节结构** | §1-§6（Method/Procedure 分开） | Chapter X（连续编号） |
| **侧边栏** | 全英文 + 渐变 header | 同左 |
| **无障碍功能** | 相同（Dark Mode + Font + Lightbox） | 相同 |

如果任务是 Edexcel 课件：
- 使用两栏布局（删除 Notes Panel）
- 主内容区增宽至 900px
- 其他标准相同

---

**文档版本**: v3.0 Final 🆕
**最后更新**: 2026-08-17 12:49 (基于 Dement v3.0 开发经验)
**维护者**: AI Assistant (WorkBuddy)
**状态**: ✅ 生产可用（已包含所有截至今天的经验教训，包括 Cancel 高亮修复）
