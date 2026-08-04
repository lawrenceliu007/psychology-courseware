# 🧠 Psychology Courseware — GitHub Pages 部署指南

## ✅ 已完成的工作

1. **整理了全部 15 个课件** 到 `gh-pages/` 目录
2. **创建了导航首页** `index.html`（分类清晰，带颜色标签）
3. **初始化了 Git 仓库** 并完成首次提交（159 个文件）

## 📁 目录结构

```
gh-pages/
├── index.html                          ← 导航首页（自动生成）
├── cie/                                ← CIE Core Studies (11个)
│   ├── hassett/        (生物) 🔴
│   ├── hoelzel/        (生物) 🔴
│   ├── andrade/        (认知) 🔵
│   ├── baron-cohen/    (认知) 🔵
│   ├── pozzulo/        (认知) 🔵
│   ├── milgram/        (社会) 🟠
│   ├── perry/          (社会) 🟠
│   ├── piliavin/       (社会) 🟠
│   ├── bandura/        (学习) 🟢
│   ├── fagen/          (学习) 🟢
│   └── saavedra/       (学习) 🟢
├── edexcel/                            ← Edexcel IAL (2章)
│   ├── ch1-obedience/                  ← 服从
│   └── ch22-depression/                ← 单相抑郁
└── intro/                              ← 概论/临床 (2章)
    ├── ch20-diagnosis/                 ← 诊断的定义与争论
    └── ch21-schizophrenia/             ← 精神分裂症
```

## 🚀 部署步骤（3分钟搞定）

### 第一步：创建 GitHub 仓库

1. 打开 https://github.com/new
2. Repository name: **`psychology-courseware`** （或你喜欢的名字）
3. 选择 **Public**（免费用户必须公开才能用 Pages）
4. **不要勾选** "Add a README file"
5. 点击 **Create repository**

### 第二步：推送代码

打开终端（Terminal），依次执行：

```bash
# 进入项目目录
cd /Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages

# 添加远程仓库地址（把 YOUR_USERNAME 换成你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/psychology-courseware.git

# 推送到 GitHub
git push -u origin main
```

如果提示输入用户名密码：
- 用户名：你的 GitHub 用户名
- 密码：**不是 GitHub 密码**，而是 Personal Access Token (PAT)
  - 生成地址：https://github.com/settings/tokens → Generate new token (classic)
  - 勾选 `repo` 权限即可

### 第三步：启用 GitHub Pages

1. 打开刚创建的仓库页面
2. 点击 **Settings**（设置）
3. 左侧菜单找到 **Pages**
4. Source 选择 **Deploy from a branch**
5. Branch 选择 **main**，文件夹选择 **/(root)**
6. 点击 **Save**

### 第四步：访问你的网站

等待 1-2 分钟后，访问：

```
https://YOUR_USERNAME.github.io/psychology-courseware/
```

**这就是永久链接！** 只要 GitHub 在，它就在。

---

## 🔗 以后更新课件怎么办？

每次修改或新增课件后，只需 3 条命令：

```bash
cd /Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages
git add -A
git commit -m "更新了 XXX 课件"
git push
```

GitHub Pages 会自动重新部署，通常 1-2 分钟内生效。

---

## 💡 可选优化

### 自定义域名（可选）
在 Pages 设置里可以绑定自己的域名，如 `psychology.yourdomain.com`

### 添加 README（可选）
如果想给仓库加说明，创建 `README.md` 即可（不影响网站显示）

### 绑定 Google Analytics（可选）
想统计学生访问量？在 `index.html` 里加入 GA 跟踪代码即可

---

## ⚠️ 注意事项

1. **Public 仓库 = 所有人可见**：确保课件内容适合公开
2. **图片路径**：所有图片都是相对路径，不需要修改
3. **中文文件名**：已全部改为英文目录名，避免兼容性问题
4. **总大小**：约 15MB（主要是图片），GitHub 完全够用

---

## 📞 需要帮助？

如果遇到问题：
- GitHub Pages 官方文档：https://docs.github.com/pages
- Git 推送失败？检查 PAT token 权限
- 页面空白？检查分支和文件夹设置是否正确

---

**祝部署顺利！🎉**
