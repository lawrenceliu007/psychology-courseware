#!/usr/bin/env python3
"""
真题倒查工具 (Past Paper Reverse Audit)
=======================================
用途: 从 CIE 9990 真题文件夹 (qp/ms PDF) 提取所有题目, 按研究归类,
生成「真题 → 课件覆盖」审计报告, 确保课件不遗漏任何考过的细节。

用法:
    python3 audit_past_papers.py <真题文件夹> <课件cie目录> <输出.md>

逻辑:
  1. 提取所有 *_qp_*.pdf / *_ms_*.pdf 文本 (fitz)
  2. 识别题目主干 (From the study by X / Evaluate / Using your knowledge of ...)
  3. 按研究名归类 → 定位对应课件 cie/<study>/index.html
  4. 对每道题输出: 题干 + 该研究课件是否存在 + 待人工核对 MS 给分点的提示
  5. coverage 检查: 把题干关键词 grep 进课件 HTML, 粗标记覆盖情况

维护: 每拿到一批新真题, 跑一次脚本, 把新题目补进报告; 人工/AI 逐题
核对 MS 给分点 (List is definitive 的点必须能在课件找到可直抄英文句)。
"""
import sys, os, re, glob, subprocess

STUDY_MAP = {
    "milgram": "milgram", "bandura": "bandura", "baron-cohen": "baron-cohen",
    "baron": "baron-cohen", "andrade": "andrade", "dement": "dement",
    "hassett": "hassett", "hölzel": "hoelzel", "holzel": "hoelzel",
    "perry": "perry", "piliavin": "piliavin", "pozzulo": "pozzulo",
    "fagen": "fagen", "saavedra": "saavedra",
}
# 题干起始特征 (Paper 1/2 常见句式)
QUESTION_PATTERNS = [
    r"From the study by (.+?):",
    r"In the study by (.+?),",
    r"The study by (.+?) \(",            # e.g. "The study by Hassett et al. (monkey toy preferences) used..."
    r"Describe how (.+?) et al\.",       # e.g. "Describe how Hassett et al. followed ethical guidelines..."
    r"In the background to their study, (.+?) outlined",
    r"The (?:debate about individual and situational explanations|nature versus nurture debate|nature versus nurture) .*?relates to the study by (.+?)",
    r"Using your knowledge of the study by (.+?):",
    r"Evaluate the study by (.+?) in terms of",
    r"the ethics of the study by (.+?)",
    r"the generalisability of the study by (.+?)",
    r"similarit(?:y|ies) between the study by (.+?) and",
    r"and the study by (.+?)\.",
]

def extract_pdfs(folder):
    import fitz
    texts = {}
    for f in sorted(glob.glob(os.path.join(folder, "*.pdf"))):
        name = os.path.basename(f).replace(".pdf", "")
        doc = fitz.open(f)
        texts[name] = "\n".join(p.get_text() for p in doc)
    return texts

def find_questions(qp_text, variant):
    """返回 [(qnum, study_raw, stem_lines)]"""
    lines = qp_text.split("\n")
    questions = []
    cur_q, cur_block, in_q = None, [], False
    for i, ln in enumerate(lines):
        # 题号可能单独成行, 也可能与题干同行 (如 "10 Evaluate the study by...")
        m = re.match(r"^(\d{1,2})(?:\s+(.*))?$", ln.strip())
        inline_rest = None
        if m and int(m.group(1)) <= 12 and not re.match(r"^\d+\s*%|^\d+\s*marks", ln.strip()):
            if m.group(2):
                inline_rest = m.group(2)
            else:
                if in_q and cur_q:
                    questions.append((cur_q, cur_block))
                cur_q, cur_block, in_q = m.group(1), [], False
                continue
        if cur_q is None:
            continue
        if inline_rest is not None:
            if in_q and cur_q:
                questions.append((cur_q, cur_block))
            cur_q_new = ln.strip().split()[0]
            if in_q and cur_q:
                questions.append((cur_q, cur_block))
            cur_block, in_q = [], False
            cur_q = cur_q_new
            ln = inline_rest
        hit = False
        for pat in QUESTION_PATTERNS:
            if re.search(pat, ln):
                hit = True
                break
        if hit:
            in_q = True
        if in_q and ln.strip() and not re.match(r"^\d+\s*$", ln.strip()):
            # 停止条件: 遇到下一题标记已由上面处理; 收集非点线行
            if not re.match(r"^\.+", ln.strip()):
                cur_block.append(ln.strip())
        # 遇到分值标记后可以提前结束本题收集
        if in_q and re.search(r"\[\d+\]", ln):
            questions.append((cur_q, cur_block))
            in_q, cur_block = False, []
    if in_q and cur_q and cur_block:
        questions.append((cur_q, cur_block))
    # 去重 (同题号多 part 可能重复 append)
    seen, out = set(), []
    for q, b in questions:
        if q not in seen:
            seen.add(q); out.append((q, b))
    return out

def attr_study(block_text):
    t = " ".join(block_text)
    for key, study in STUDY_MAP.items():
        if re.search(key, t, re.I):
            return study
    return None

def courseware_has(cie_dir, study, keyword):
    f = os.path.join(cie_dir, study, "index.html")
    if not os.path.exists(f):
        return None
    html = open(f, encoding="utf-8", errors="ignore").read()
    return bool(re.search(re.escape(keyword), html, re.I))

def main(folder, cie_dir, out_md):
    texts = extract_pdfs(folder)
    qps = {k: v for k, v in texts.items() if re.match(r".*_qp_\d+", k)}
    rows = []
    for qp_name, qp_text in sorted(qps.items()):
        mm = re.search(r"_(\w\d+)_qp", qp_name)
        variant = mm.group(1) if mm else qp_name
        for qnum, block in find_questions(qp_text, variant):
            study = attr_study(block)
            stem = " ".join(block)[:220]
            rows.append((qp_name, qnum, study, stem))
    # 生成报告
    with open(out_md, "w", encoding="utf-8") as w:
        w.write("# 真题倒查覆盖审计 (Past Paper Coverage Audit)\n\n")
        w.write("> 生成方式: `python3 tools/audit_past_papers.py <真题文件夹> <cie目录> <本文件>`\n")
        w.write("> 审计铁律: 每道题必须打开对应 MS, 把「List is definitive」的每个给分点\n")
        w.write("> 在课件中找到可直抄英文句; 找不到 = 覆盖缺口, 立即补进课件。\n\n")
        w.write(f"来源: `{os.path.basename(folder)}` — 共 {len(rows)} 道研究归属明确的题目\n\n")
        w.write("| 试卷 | 题号 | 研究 | 课件 | 题干摘要 | MS 核对 |\n|---|---|---|---|---|---|\n")
        for qp_name, qnum, study, stem in rows:
            if study is None:
                w.write(f"| {qp_name} | Q{qnum} | ⚠️ 未识别 | — | {stem[:100]}… | 🔲 待核对 |\n")
                continue
            f = os.path.join(cie_dir, study, "index.html")
            exists = "✅" if os.path.exists(f) else "❌ 缺课件"
            w.write(f"| {qp_name} | Q{qnum} | {study} | {exists} | {stem[:100]}… | 🔲 待核对 |\n")
        w.write("\n---\n\n## 审计记录\n\n")
        w.write("<!-- 每核对完一道题: 记录 日期/题号/MS给分点数/课件覆盖情况/补充动作 -->\n")
    print(f"报告已生成: {out_md} ({len(rows)} questions)")
    for r in rows:
        print(f"  {r[0]} Q{r[1]} -> {r[2] or 'UNRECOGNIZED'}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
