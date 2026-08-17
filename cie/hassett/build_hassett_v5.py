#!/usr/bin/env python3
"""Build Hassett v5.0 following Milgram template architecture exactly."""

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Core Study 2: Hassett et al. (2008) — Sex Differences in Rhesus Monkey Toy Preferences</title>
  <style>
    :root {
      --primary: #dc2626;
      --primary-light: #16a34a;
      --primary-dark: #991b1b;
      --accent: #dc2626;
      --bg: #FAFAFA;
      --card-bg: #FFFFFF;
      --text: #212121;
      --text-secondary: #616161;
      --border: #E0E0E0;
    }
    * { box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.75; color: var(--text); background: var(--bg); margin: 0; padding: 0; font-size: 16px; transition: background .3s, color .3s; }
    html { font-size: 16px; }
    .container { max-width: 1200px; margin: 0 auto; padding: 16px 24px; }

    /* ===== PROGRESS BAR ===== */
    .progress-bar { position: fixed; top: 0; left: 0; width: 0%; height: 3px; background: linear-gradient(90deg, var(--primary), var(--primary-light), #86efac); z-index: 9999; transition: width .1s ease-out; }
    body.dark .progress-bar { background: linear-gradient(90deg, #ef4444, #16a34a, #86efac); }

    /* ===== NAV BAR ===== */
    .nav-bar { position: sticky; top: 0; z-index: 100; background: white; border-bottom: 3px solid var(--primary); padding: .65rem 2rem; display: flex; align-items: center; gap: 1rem; margin: 0 0 28px 0; box-shadow: 0 2px 10px rgba(0,0,0,.06); }
    body.dark .nav-bar { background: #1a1a2e; border-bottom-color: var(--primary); }
    .nav-pill { display: inline-flex; align-items: center; gap: .4rem; padding: .45rem 1.1rem; background: var(--primary); color: white; border-radius: 20px; text-decoration: none; font-size: .82em; font-weight: 600; transition: background .15s; white-space: nowrap; }
    .nav-pill:hover { background: var(--primary-dark); }
    .nav-breadcrumb { display: flex; align-items: center; gap: .4rem; font-size: .82em; color: var(--text-secondary); flex: 1; }
    .nav-breadcrumb a { color: var(--text-secondary); text-decoration: none; transition: color .15s; }
    .nav-breadcrumb a:hover { color: var(--primary); }
    .nav-breadcrumb .sep { color: #ccc; font-weight: 300; }
    .nav-breadcrumb span:last-child { color: var(--text); font-weight: 500; }
    body.dark .nav-breadcrumb a { color: #aaa; }
    body.dark .nav-breadcrumb span:last-child { color: #ddd; }
    .nav-controls { display: flex; align-items: center; gap: .5rem; }
    .nav-btn { background: none; border: 1px solid #ddd; border-radius: 6px; padding: .35rem .65rem; cursor: pointer; font-size: .85em; color: var(--text-secondary); transition: all .15s; display: flex; align-items: center; gap: .25rem; }
    .nav-btn:hover { border-color: var(--primary); color: var(--primary); }
    body.dark .nav-btn { border-color: #444; color: #aaa; }
    body.dark .nav-btn:hover { border-color: #ef4444; color: #ef4444; }

    /* ===== PAGE LAYOUT (3-column) ===== */
    .page-layout { display: grid; grid-template-columns: 170px minmax(0,1fr) 250px; gap: 20px; align-items: start; }
    .sidebar { width: 170px; flex-shrink: 0; position: sticky; top: 60px; max-height: calc(100vh - 80px); overflow-y: auto; padding: 12px 0; z-index: 50; }
    .sidebar::-webkit-scrollbar { width: 2px; }
    .sidebar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 2px; }
    .sidebar-inner { background: #f8fafc; border-radius: 14px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,.05); }
    body.dark .sidebar-inner { background: #16213e; border-color: #334155; box-shadow: 0 2px 8px rgba(0,0,0,.25); }
    .sb-header { padding: 13px 16px 10px; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); }
    .sb-header-title { font-size: .72em; font-weight: 700; color: white; letter-spacing: .8px; text-transform: uppercase; margin: 0; }
    .sb-header-sub { font-size: .63em; color: rgba(255,255,255,.75); margin: 2px 0 0; font-weight: 500; }
    .sb-list { list-style: none; padding: 6px 0 10px; margin: 0; }
    .sb-divider { height: 1px; background: #e2e8f0; margin: 4px 12px; }
    body.dark .sb-divider { background: #334155; }
    .sb-item a { display: block; padding: 7px 14px 7px 18px; color: #475569; text-decoration: none; font-size: .76em; font-weight: 500; border-left: 3px solid transparent; transition: all .15s ease; line-height: 1.45; border-radius: 0 7px 7px 0; margin: 1px 4px 1px 0; }
    .sb-item a:hover { border-left-color: var(--primary); color: var(--primary-dark); font-weight: 600; background: linear-gradient(90deg, rgba(220,38,38,.07), transparent); }
    .sb-item a.sb-active { border-left-color: var(--primary); color: var(--primary-dark); font-weight: 700; background: linear-gradient(90deg, rgba(220,38,38,.12), transparent); }
    body.dark .sb-item a { color: #94a3b8; }
    body.dark .sb-item a:hover { color: #ef4444; background: linear-gradient(90deg, rgba(239,68,68,.10), transparent); border-left-color: #ef4444; }
    body.dark .sb-item a.sb-active { color: #fca5a5; background: linear-gradient(90deg, rgba(239,68,68,.16), transparent); border-left-color: #ef4444; }
    .main-content { min-width: 0; max-width: 660px; }

    /* ===== RIGHT NOTES COLUMN ===== */
    .notes-col { width: 250px; background: #fffef5; border: 2px solid #f59e0b; border-radius: 12px; display: flex; flex-direction: column; position: sticky; top: 60px; max-height: calc(100vh - 80px); box-shadow: 0 2px 12px rgba(245,158,11,.15); overflow: hidden; }
    .nc-header { background: linear-gradient(135deg,#f59e0b,#d97706); padding: 12px 14px; display: flex; align-items: center; gap: 8px; }
    .nc-title { font-size: .85em; font-weight: 700; color: #fff; }
    .nc-count { margin-left: auto; background: rgba(255,255,255,.3); color: #fff; font-size: .7em; font-weight: 700; padding: 2px 8px; border-radius: 10px; }
    .nc-body { flex: 1; overflow-y: auto; padding: 10px; max-height: calc(100vh - 240px); min-height: 60px; }
    .nc-empty { text-align: center; color: #9ca3af; padding: 20px 8px; font-size: .78em; }
    .nc-input-row { display: none; padding: 12px; border-top: 1px solid #fde68a; background: #fffbeb; }
    .nc-input-row.show { display: block; }
    .nc-textarea { width: 100%; border: 1px solid #fcd34d; border-radius: 8px; padding: 10px; font-size: .82em; resize: vertical; min-height: 60px; box-sizing: border-box; outline: none; font-family: inherit; }
    .nc-textarea:focus { border-color: #d97706; box-shadow: 0 0 0 2px rgba(245,158,11,.15); }
    .nc-actions { display: flex; gap: 8px; margin-top: 8px; }
    .nc-actions button { flex: 1; padding: 8px; border-radius: 6px; font-size: .78em; font-weight: 600; cursor: pointer; border: 1px solid transparent; }
    .nc-btn-save { background: #16a34a; color: white; }
    .nc-btn-cancel { background: white; color: #6b7280; border-color: #d1d5db !important; }
    .nc-add-btn { width: 100%; padding: 13px; background: linear-gradient(135deg,#ea580c,#c2410c); color: white; border: none; border-radius: 0 0 10px 10px; font-size: .88em; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: opacity .2s; }
    .nc-add-btn:hover { opacity: .9; }
    .nc-footer { display: flex; gap: 4px; padding: 6px 10px; border-top: 1px solid #fde68a; }
    .nc-footer button { flex: 1; padding: 4px 0; font-size: .68em; border: none; background: transparent; color: #92400e; cursor:pointer; }
    .hl-text { background: linear-gradient(120deg,#fef08a,#fde047); border-radius: 2px; padding: 0 2px; cursor: pointer; transition: background .15s; }
    .hl-text:hover { background: linear-gradient(120deg,#fde047,#facc15); }
    .note-card { background: #fff; border-radius: 8px; padding: 10px 12px; margin-bottom: 8px; border-left: 3px solid #f59e0b; box-shadow: 0 1px 3px rgba(0,0,0,.08); font-size: .78em; line-height: 1.5; position: relative; animation: nFadeIn .2s ease; transition: box-shadow .2s, border-color .2s; }
    @keyframes nFadeIn { from{opacity:0;transform:translateY(4px)} to{opacity:1;transform:translateY(0)} }
    .note-card[ondblclick]:hover { box-shadow: 0 4px 12px rgba(245,158,11,.25); border-left-color: #d97706; }
    .note-card-hl { font-size: .7em; color: #92400e; background: #fef3c7; padding: 2px 6px; border-radius: 4px; margin-bottom: 4px; cursor: pointer; word-break: break-all; }
    .note-card-hl:hover { background: #fde68a; }
    .note-card-text { color: #374151; word-break: break-word; }
    .note-card-del { position: absolute; top: 4px; right: 4px; width: 18px; height: 18px; border: none; background: #fee2e2; color: #ef4444; border-radius: 50%; font-size: .65em; cursor: pointer; opacity: 0; display: flex; align-items: center; justify-content: center; }
    .note-card:hover .note-card-del { opacity: 1; }

    /* ===== HEADER CARD ===== */
    .header { text-align: center; padding: 36px 24px; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); color: white; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 4px 15px rgba(220,38,38,0.3); }
    .header h1 { font-size: 1.85em; margin-bottom: 10px; }
    .header .subtitle { font-size: 1.05em; opacity: 0.92; }
    .header .meta { margin-top: 15px; font-size: 0.88em; opacity: 0.82; }
    .badge { display: inline-block; padding: 4px 14px; border-radius: 20px; background: rgba(255,255,255,0.2); margin: 3px; font-size: 0.84em; }
    .kw-tags { margin-top: 18px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
    .kw-tag { display: inline-flex; align-items: center; gap: 5px; padding: 6px 16px; border-radius: 20px; font-size: .82em; font-weight: 600; color: white; opacity: .95; }
    .kw-app { background: linear-gradient(135deg, #dc2626, #ef4444); }
    .kw-meth { background: linear-gradient(135deg, #E65100, #FB8C00); }
    .kw-conc { background: linear-gradient(135deg, #7B1FA2, #AB47BC); }

    /* ===== TOC ===== */
    .toc { background: var(--soft, #f8fafc); border: 1px solid var(--border); border-radius: 10px; padding: 22px 26px; margin-bottom: 24px; border-left: 4px solid var(--primary); }
    body.dark .toc { background: #16213e; border-color: #334155; }
    .toc h2 { color: var(--primary-dark); margin-bottom: 14px; font-size: 1.25em; }
    .toc ol { padding-left: 20px; }
    .toc li { margin: 7px 0; }
    .toc li a { color: var(--accent); text-decoration: none; transition: color 0.2s; }
    .toc li a:hover { color: var(--primary); text-decoration: underline; }

    /* ===== SECTIONS ===== */
    .section { background: var(--card-bg); border-radius: 10px; padding: 28px 32px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-top: 3px solid var(--primary-light); }
    body.dark .section { background: #1a1a2e; box-shadow: 0 2px 8px rgba(0,0,0,.3); }
    .section h2 { color: var(--primary-dark); font-size: 1.45em; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid var(--border); }
    body.dark .section h2 { color: #f87171; border-bottom-color: #334155; }
    .section h3 { color: var(--primary); font-size: 1.18em; margin: 22px 0 12px; }
    body.dark .section h3 { color: #86efac; }
    .section h4 { color: var(--text); font-size: 1.04em; margin: 14px 0 8px; }

    /* ===== INFO BOXES ===== */
    .quote { border-left: 4px solid var(--primary); background: linear-gradient(135deg, #fffbeb, #dcfce7); padding: 16px 22px; margin: 16px 0; border-radius: 0 8px 8px 0; font-style: italic; color: var(--primary-dark); }
    body.dark .quote { background: linear-gradient(135deg, rgba(220,38,38,.15), rgba(220,38,38,.08)); border-left-color: #ef4444; color: #fca5a5; }
    .note-box { background: #fffbeb; border-left: 4px solid var(--primary); border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
    body.dark .note-box { background: rgba(251,191,36,.06); border-left-color: #FBC02D; }
    .blue-box { background: #eff6ff; border-left: 4px solid var(--accent); border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
    body.dark .blue-box { background: rgba(59,130,246,.06); border-left-color: #42A5F5; }
    .green-box { background: #fffbeb; border-left: 4px solid #38a169; border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
    body.dark .green-box { background: rgba(56,161,105,.06); border-left-color: #f97316; }
    .warn-box { background: #fef2f2; border-left: 4px solid #dc2626; border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
    body.dark .warn-box { background: rgba(220,38,38,.06); border-left-color: #ef5350; }
    .warn-box h4 { color: #991b1b; margin-bottom: 6px; }
    body.dark .warn-box h4 { color: #ef5350; }

    /* ===== KEYWORD BOX ===== */
    .keyword-box { background: linear-gradient(135deg, #FFF8E1, #FFECB3); border-left: 5px solid #D97706; border-radius: 8px; padding: 18px 22px; margin: 18px 0; }
    .keyword-box h4 { color: #92400E; font-size: 0.95em; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
    .keyword-box p { margin: 6px 0; }
    .keyword-box strong { color: #78350F; }

    /* ===== IMAGES ===== */
    .figure { margin: 20px 0; text-align: center; }
    .figure img { max-width: 100%; border: 1px solid var(--border); border-radius: 10px; box-shadow: 0 3px 12px rgba(0,0,0,0.08); }
    .figure-caption { font-size: 0.89em; color: var(--text-secondary); margin-top: 8px; font-style: italic; }

    /* ===== TABLES ===== */
    table { width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 0.92em; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-radius: 8px; overflow: hidden; }
    th { background: var(--primary); color: white; padding: 12px 14px; text-align: left; font-weight: 600; }
    td { padding: 11px 14px; border-bottom: 1px solid var(--border); }
    tr:nth-child(even) { background: #fafbfc; }
    body.dark tr:nth-child(even) { background: rgba(255,255,255,.02); }
    tr:hover { background: #fffbeb; }
    body.dark tr:hover { background: rgba(220,38,38,.05); }
    td:first-child { font-weight: 600; color: var(--primary-dark); }
    body.dark td:first-child { color: #fca5a5; }
    caption { font-weight: 600; color: var(--text); margin-bottom: 8px; font-size: 0.96em; }

    /* LISTS */
    ul, ol { margin: 10px 0; padding-left: 24px; }
    li { margin: 6px 0; }

    /* ===== CHINESE SUMMARY CARDS ===== */
    .cn-summary-wrap { margin: 18px 0; }
    .cn-summary-toggle { display: flex; align-items: center; gap: 8px; width: 100%; padding: 10px 16px; background: linear-gradient(135deg, #f3e8ff, #ede9fe); border: 1.5px dashed #a78bfa; border-radius: 8px; cursor: pointer; font-size: .86em; color: #6b21a8; font-weight: 500; transition: all .2s; text-align: left; }
    body.dark .cn-summary-toggle { background: linear-gradient(135deg, rgba(167,139,250,.1), rgba(139,92,246,.08)); border-color: #8b5cf6; color: #c4b5fd; }
    .cn-summary-toggle:hover { background: linear-gradient(135deg, #ede9fe, #ddd6fe); border-color: #8b5cf6; }
    .cs-icon { font-size: .75em; transition: transform .2s; min-width: 14px; }
    .cn-summary-toggle.open .cs-icon { transform: rotate(90deg); }
    .cn-summary-body { max-height: 0; overflow: hidden; opacity: 0; transition: max-height .4s ease, opacity .25s ease; }
    .cn-summary-body.open { max-height: 800px; opacity: 1; margin: 8px 0 4px; }
    .cn-summary-body { background: linear-gradient(135deg, #faf5ff, #f3e8ff); border-radius: 8px; padding: 18px 22px; border: 1px solid #e9d5ff; }
    body.dark .cn-summary-body { background: linear-gradient(135deg, rgba(167,139,250,.06), rgba(124,58,237,.04)); border-color: rgba(139,92,246,.2); }
    .cs-title { font-weight: 700; color: #6b21a8; font-size: .95em; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px dashed #d8b4fe; }
    body.dark .cs-title { color: #c4b5fd; border-bottom-color: rgba(139,92,246,.3); }
    .cn-summary-body p { margin: 8px 0; line-height: 1.72; color: #374151; font-size: .93em; }
    body.dark .cn-summary-body p { color: #d1d5db; }
    .cn-summary-body ul { margin: 6px 0; padding-left: 20px; }
    .cn-summary-body li { margin: 5px 0; font-size: .93em; color: #374151; }
    body.dark .cn-summary-body li { color: #d1d5db; }
    .cs-en { color: #7c3aed; font-style: italic; font-weight: 500; }
    body.dark .cs-en { color: #a78bfa; }

    /* ===== EXAM KEY POINTS (summary-card) ===== */
    .summary-card { background: linear-gradient(135deg, #fffbeb, #dcfce7); border-left: 5px solid #16a34a; border-radius: 10px; margin: 20px 0 0; overflow: hidden; transition: all .2s; }
    body.dark .summary-card { background: linear-gradient(135deg, #052e16, #14532d); border-left-color: #22c55e; }
    .summary-card-header { display: flex; align-items: center; gap: 8px; padding: 12px 18px; cursor: pointer; user-select:none; -webkit-user-select:none; transition: background .15s; }
    .summary-card-header:hover { background: #bbf7d0; }
    body.dark .summary-card-header:hover { background: #166534; }
    .summary-card-icon { font-size: 1.1em; transition: transform .2s; color: #166534; }
    body.dark .summary-card-icon { color: #86efac; }
    .summary-card.open .summary-card-icon { transform: rotate(90deg); }
    .summary-card-title { font-size: .92em; font-weight: 700; color: #166534; flex: 1; }
    body.dark .summary-card-title { color: #86efac; }
    .summary-card-badge { font-size: .7rem; background: #16a34a; color: white; padding: 2px 10px; border-radius: 10px; font-weight: 600; }
    .summary-card-body { max-height: 0; overflow: hidden; transition: max-height .35s ease; }
    .summary-card.open .summary-card-body { max-height: 800px; }
    .summary-card-inner { margin: 0 14px 14px; padding: 16px 20px; background: #ffffff; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,.06); border: 1px solid #e8f0e8; }
    body.dark .summary-card-inner { background: #0c1a0c; border-color: #1a3a1a; box-shadow: 0 1px 4px rgba(0,0,0,.2); }
    .summary-card-inner ol, .summary-card-inner ul { margin: 0; padding-left: 20px; }
    .summary-card-inner li { margin: 8px 0; font-size: .98em; color: #1a1a1a; line-height: 1.72; }
    body.dark .summary-card-inner li { color: #e8ede9; }

    /* EXAM TAGS */
    .tag-must { display: inline-block; padding: 2px 8px; border-radius: 4px; background: #fee2e2; color: #dc2626; font-size: .76em; font-weight: 700; vertical-align: middle; margin-left: 4px; }
    .tag-common { display: inline-block; padding: 2px 8px; border-radius: 4px; background: #fef3c7; color: #d97706; font-size: .76em; font-weight: 700; vertical-align: middle; margin-left: 4px; }
    .tag-ao2 { display: inline-block; padding: 2px 8px; border-radius: 4px; background: #dcfce7; color: #16a34a; font-size: .76em; font-weight: 700; vertical-align: middle; margin-left: 4px; }
    .tag-context { display: inline-block; padding: 2px 8px; border-radius: 4px; background: #f1f5f9; color: #64748b; font-size: .76em; font-weight: 700; vertical-align: middle; margin-left: 4px; }

    /* ===== STUDY QUESTIONS (Q&A Cards) ===== */
    .qa-card { background: white; border: 1.5px solid #e2e8f0; border-radius: 10px; margin: 12px 0; overflow: hidden; transition: box-shadow .2s, border-color .2s; }
    .qa-card:hover { box-shadow: 0 3px 12px rgba(0,0,0,.08); border-color: #cbd5e1; }
    body.dark .qa-card { background: #1a2332; border-color: #334155; }
    body.dark .qa-card:hover { border-color: #475569; box-shadow: 0 3px 12px rgba(0,0,0,.25); }
    .qa-question { display: flex; align-items: flex-start; gap: 10px; padding: 16px 18px; cursor: pointer; user-select:none; -webkit-user-select:none; transition: background .15s; }
    .qa-question:hover { background: #f8fafc; }
    body.dark .qa-question:hover { background: rgba(255,255,255,.03); }
    .qa-num { flex-shrink: 0; width: 28px; height: 28px; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: .78em; font-weight: 700; line-height: 1; }
    .qa-text { flex: 1; font-size: .93em; color: #1e293b; line-height: 1.6; font-weight: 500; }
    body.dark .qa-text { color: #e2e8f0; }
    .qa-toggle { flex-shrink: 0; width: 32px; height: 28px; background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 1.5px solid #93c5fd; border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: .72em; color: #2563eb; font-weight: 600; transition: all .15s; cursor: pointer; }
    body.dark .qa-toggle { background: rgba(59,130,246,.1); border-color: #3b82f6; color: #93c5fd; }
    .qa-toggle:hover { background: linear-gradient(135deg, #dbeafe, #bfdbfe); }
    body.dark .qa-toggle:hover { background: rgba(59,130,246,.18); }
    .qa-toggle .qa-icon { transition: transform .2s; display: inline-block; }
    .qa-card.open .qa-toggle .qa-icon { transform: rotate(180deg); }
    .qa-answer { max-height: 0; overflow: hidden; transition: max-height .35s ease; }
    .qa-card.open .qa-answer { max-height: 500px; }
    .qa-answer-inner { padding: 14px 18px 18px; margin: 0 14px 14px; background: linear-gradient(135deg, #fefce8, #fef3c7); border-left: 4px solid #f59e0b; border-radius: 8px; font-size: .91em; color: #451a03; line-height: 1.72; }
    body.dark .qa-answer-inner { background: linear-gradient(135deg, rgba(245,158,11,.08), rgba(217,119,6,.05)); border-left-color: #f59e0b; color: #d4a574; }
    .qa-answer-inner strong { color: #b45309; }
    body.dark .qa-answer-inner strong { color: #fbbf24; }

    /* TERM TOOLTIPS */
    .term { color: var(--term-color, #dc2626); font-weight: 600; cursor: help; position: relative; border-bottom: 1px dotted var(--term-color, #dc2626); }
    .term-tooltip { position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%); background: #1e293b; color: #f8fafc; padding: 12px 16px; border-radius: 8px; font-size: .84em; line-height: 1.55; width: 280px; z-index: 200; box-shadow: 0 8px 30px rgba(0,0,0,.25); opacity: 0; visibility: hidden; transition: .2s; pointer-events: none; }
    .term-tooltip::after { content: ''; position: absolute; top: 100%; left: 50%; transform: translateX(-50%); border: 6px solid transparent; border-top-color: #1e293b; }
    .term:hover .term-tooltip { opacity: 1; visibility: visible; }
    .tt-cn { color: #a78bfa; font-weight: 600; display: block; margin-bottom: 4px; font-size: .96em; }
    .tt-def { color: #94a3b8; display: block; margin-top: 4px; }

    /* VISUAL SECTION HEADER */
    .visual-header { display: flex; align-items: center; gap: 14px; margin-bottom: 18px; padding: 14px 18px; background: linear-gradient(135deg, #fffbeb, #dcfce7); border-radius: 10px; border-left: 4px solid var(--primary); }
    body.dark .visual-header { background: linear-gradient(135deg, rgba(220,38,38,.1), rgba(220,38,38,.06)); border-left-color: #ef4444; }
    .vh-icon { font-size: 1.8em; flex-shrink: 0; }
    .vh-text h4 { margin: 0 0 3px; color: var(--primary-dark); font-size: .92em; }
    body.dark .vh-text h4 { color: #f87171; }
    .vh-text p { margin: 0; font-size: .82em; color: var(--text-secondary); }

    /* BACK TO TOP */
    .back-to-top { position: fixed; bottom: 30px; right: 30px; width: 44px; height: 44px; background: var(--primary); color: white; border: none; border-radius: 50%; cursor: pointer; font-size: 1.2em; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(220,38,38,.35); opacity: 0; visibility: hidden; transform: translateY(15px); transition: all .3s; z-index: 90; }
    .back-to-top.show { opacity: 1; visibility: visible; transform: translateY(0); }
    .back-to-top:hover { background: var(--primary-dark); transform: translateY(-3px); }

    /* FOOTER */
    .footer-note { font-size: 0.85em; color: var(--text-secondary); margin-top: 2.5em; padding-top: 1em; border-top: 1px solid var(--border); text-align: center; }

    /* STUDY NAVIGATOR */
    .study-nav{border-top:2px solid #e0e0e0;background:#FAFAFA;padding:14px 16px;margin-top:2rem}
    .study-nav-inner{display:flex;align-items:center;justify-content:space-between;gap:12px;max-width:1100px;margin:0 auto}
    .study-nav-btn{flex:1;padding:9px 14px;border:1px solid #ddd;border-radius:8px;background:white;color:#444;font-size:.82rem;cursor:pointer;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:4px;transition:all .15s;font-family:inherit}
    .study-nav-btn:hover{border-color:#dc2626;color:#dc2626;background:#fffbeb}
    .study-nav-dots{text-align:center;padding:0 8px}
    .study-nav-label{font-size:.65rem;text-transform:uppercase;letter-spacing:1px;color:#888;margin-bottom:5px;font-weight:700}
    .study-dot-row{display:flex;gap:5px;justify-content:center;flex-wrap:wrap}
    .study-dot{width:10px;height:10px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:all .15s;position:relative;display:inline-block}
    .study-dot:hover{transform:scale(1.3)}
    .study-dot.active{border-color:#333;transform:scale(1.25)}

    /* DARK MODE — comprehensive overrides */
    body.dark { background: #0f172a; color: #e2e8f0; }
    body.dark .container { background: #0f172a; }
    body.dark .header { background: linear-gradient(135deg, #991b1b, #dc2626); }
    body.dark .keyword-box { background: linear-gradient(135deg, rgba(217,119,6,.12), rgba(217,119,6,.06)); border-left-color: #F59E0B; }
    body.dark .keyword-box h4, body.dark .keyword-box strong { color: #FBBF24; }
    body.dark .keyword-box p { color: #d1d5db; }
    body.dark th { background: #991b1b; }
    body.dark td { border-bottom-color: #1e293b; }
    body.dark caption { color: #cbd5e1; }
    body.dark .footer-note { border-top-color: #1e293b; color: #94a3b8; }
    body.dark .study-nav { background: #1e293b; border-top-color: #334155; }
    body.dark .study-nav-btn { background: #0f172a; border-color: #334155; color: #94a3b8; }
    body.dark .study-nav-btn:hover { border-color: #ef4444; color: #ef4444; background: rgba(220,38,38,.08); }
    body.dark .figure img { border-color: #334155; }
    body.dark .figure-caption { color: #94a3b8; }
    body.dark blockquote { color: #94a3b8; border-left-color: #334155; }
    body.dark .back-to-top { background: #dc2626; }
    body.dark .back-to-top:hover { background: #16a34a; }

    /* Notes Panel Dark Mode v3.0 */
    body.dark .notes-col { background: #1c1917; border-color: #44403c; }
    body.dark .nc-header { background: linear-gradient(135deg, #92400e, #78350f); }
    body.dark .hl-text { background: linear-gradient(120deg, #854d0e, #a16207); color: #fef08a; }
    body.dark .note-card { background: #292524; border-left-color: #d97706; }
    body.dark .note-card-text { color: #d6d3d1; }
    body.dark .note-card-hl { background: #42200e; color: #fbbf24; }
    body.dark .nc-textarea { background: #292524; color: #d6d3d1; border-color: #78350f; }
    body.dark .nc-add-btn { background: linear-gradient(135deg, #92400e, #78350f); }

    /* PRINT STYLES */
    @media print {
      .progress-bar, .nav-bar, .sidebar, .page-layout, .back-to-top, .cn-summary-wrap, .summary-card, .study-nav, .kw-tags { display: none !important; }
      .container { max-width: 100% !important; padding: 0 !important; }
      .main-content { width: 100% !important; }
      .section { break-inside: avoid; page-break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }
      body { font-size: 11pt; background: white; color: black; }
      .header { background: #dc2626 !important; color: white !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    }

    /* RESPONSIVE */
    @media(max-width:850px){
      .page-layout{grid-template-columns:1fr}.sidebar,.notes-col{display:none}
      .container{padding:12px 16px}
      .section{padding:20px}
      .nav-bar{flex-wrap:wrap;padding:.5rem 1rem}
      .nav-breadcrumb{order:3;width:100%;margin-top:6px}
    }
    @media(max-width:600px){
      .study-nav-inner{flex-wrap:wrap;gap:8px}
      .study-nav-btn{font-size:.75rem;padding:7px 10px}
      .study-dot{width:8px;height:8px}
      .header h1{font-size:1.4em}
      .kw-tags{gap:6px}
      .kw-tag{font-size:.74rem;padding:5px 10px}
    }
  </style>
</head>
<body>
<div class="progress-bar" id="progressBar"></div>

<div class="container">

<!-- Sticky Navigation Bar -->
<nav class="nav-bar">
  <a href="../../index.html" class="nav-pill">🏠 Home</a>
  <div class="nav-breadcrumb">
    <a href="../../index.html">Home</a><span class="sep">›</span>
    <a href="../">CIE Psychology</a><span class="sep">›</span><span>Hassett (2008)</span>
  </div>
  <div class="nav-controls">
    <button class="nav-btn" onclick="toggleDarkMode()" id="darkBtn" title="Toggle dark mode">🌙 Dark</button>
    <button class="nav-btn" onclick="adjustFontSize(-1)" title="Decrease font size">A-</button>
    <button class="nav-btn" onclick="adjustFontSize(1)" title="Increase font size">A+</button>
  </div>
</nav>

<div class="page-layout">
  <!-- LEFT SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-inner">
      <div class="sb-header">
        <div class="sb-header-title">🐵 Hassett 2008</div>
        <div class="sb-header-sub">Monkey Toy Preferences</div>
      </div>
      <ul class="sb-list" id="sidebarList">
        <li class="sb-item"><a href="#s1">Psychology Investigated</a></li>
        <li class="sb-divider"></li>
        <li class="sb-item"><a href="#s2">Background</a></li>
        <li class="sb-item"><a href="#s3">Aim</a></li>
        <li class="sb-item"><a href="#s4">Method</a></li>
        <li class="sb-item"><a href="#s5">Procedure</a></li>
        <li class="sb-item"><a href="#s6">Behavioural Checklist</a></li>
        <li class="sb-divider"></li>
        <li class="sb-item"><a href="#s7">Results</a></li>
        <li class="sb-item"><a href="#s8">Conclusion</a></li>
        <li class="sb-divider"></li>
        <li class="sb-item"><a href="#s9">Evaluation</a></li>
        <li class="sb-item"><a href="#s10">Ethics</a></li>
        <li class="sb-item"><a href="#s11">Debates</a></li>
        <li class="sb-divider"></li>
        <li class="sb-item"><a href="#s12">Summary</a></li>
        <li class="sb-item"><a href="#s13">Questions</a></li>
      </ul>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">

<!-- HEADER -->
<div class="header">
  <h1>🐵 Hassett et al. (2008)</h1>
  <div class="subtitle">Sex Differences in Rhesus Monkey Toy Preferences Parallel Those of Children<br>恒河猴玩具偏好性别差异与儿童相似</div>
  <div class="meta">
    <span class="badge">🧬 CIE Biological Approach 生物取向</span>
    <span class="badge">📄 Evolution and Human Behavior, 29(4), 284–288</span>
    <span class="badge">🔬 Core Study 2</span>
    <span class="badge">✅ Based on CIE Textbook 基于教材原文</span>
  </div>
  <div class="kw-tags">
    <span class="kw-tag kw-app">🧬 Biological Approach</span>
    <span class="kw-tag kw-meth">📐 Naturalistic Observation</span>
    <span class="kw-tag kw-conc">💡 Nature vs Nurture</span>
  </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="toc">
  <h2>📑 Contents 目录</h2>
  <ol>
    <li><a href="#s1">The Psychology Being Investigated（研究涉及的心理学）</a></li>
    <li><a href="#s2">Background（研究背景）</a></li>
    <li><a href="#s3">Aim（研究目的）</a></li>
    <li><a href="#s4">Method（研究方法）</a></li>
    <li><a href="#s5">Procedure（实验程序）</a></li>
    <li><a href="#s6">Behavioural Checklist（行为检查表）</a></li>
    <li><a href="#s7">Results（研究结果）</a></li>
    <li><a href="#s8">Conclusion（结论）</a></li>
    <li><a href="#s9">Evaluation（评价）</a></li>
    <li><a href="#s10">Ethical Issues（伦理问题）</a></li>
    <li><a href="#s11">Issues & Debates（争论与取向）</a></li>
    <li><a href="#s12">Summary（总结）</a></li>
    <li><a href="#s13">Study Questions（复习题）</a></li>
  </ol>
</div>

<!-- ==================== SECTION 1 ==================== -->
<div class="section" id="s1">
  <h2>1️⃣ The Psychology Being Investigated（研究涉及的心理学）</h2>

  <div class="visual-header">
    <div class="vh-icon">🧬</div>
    <div class="vh-text">
      <h4>Biological Approach Core Assumptions</h4>
      <p>How biology shapes behaviour through genes, evolution & brain structure</p>
    </div>
  </div>

  <p>The biological approach in psychology assumes that <strong>behaviour can be explained in terms of brain structures, neurotransmitters, hormones and genetics（行为可以用大脑结构、神经递质、激素和遗传学来解释）</strong>. This approach emphasizes the role of nature (innate factors) over nurture (environmental influences).</p>

  <h3>Nature vs Nurture Debate（先天与后天之争）</h3>
  <p>A key debate in psychology concerns whether behaviour is primarily determined by innate biological factors (<strong>nature 先天</strong>) or shaped by environmental experiences and learning (<strong>nurture 后天</strong>). The biological approach strongly supports the nature side of this debate.</p>

  <p>In the context of toy preferences, researchers have long observed that children show gender-stereotyped toy choices:</p>
  <ul>
    <li><strong>Males</strong> tend to prefer wheeled toys (cars, trucks) and construction toys</li>
    <li><strong>Females</strong> tend to prefer plush dolls and softer toys</li>
  </ul>

  <p>The critical question is: <em>Are these preferences learned from society (nurture), or are they biologically programmed (nature)?</em></p>

  <div class="warn-box">
    <h4>⚠️ Key Research Question</h4>
    <p>If non-human primates (who are not influenced by human socialisation) show similar gender differences in toy preferences, this would provide strong evidence for the <strong>biological/nature explanation</strong>.</p>
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§1 研究涉及的心理学：生物取向的核心假设</div>
      <p><strong>核心假设：</strong>生物取向认为行为可以用生物学因素解释，包括大脑结构、神经递质、激素和遗传基因。</p>
      <ul>
        <li><span class="cs-en">Nature vs Nurture（先天与后天）</span>：心理学经典争论。生物取向支持 <span class="cs-en">Nature</span>——行为由内在的生物学因素决定。</li>
        <li><span class="cs-en">Gender-stereotyped toy preferences（性别刻板印象玩具偏好）</span>：男孩偏好带轮子的玩具/积木；女孩偏好毛绒娃娃。这是社会化的结果还是生物本能？</li>
        <li><span class="cs-en">Rationale（研究理由）</span>：如果非人类灵长类动物（不受人类社会影响）也表现出类似的性别差异 → 强力支持 <span class="cs-en">Nature/Biological Explanation</span>。</li>
      </ul>
      <p><strong>💡 考试要点：</strong>CIE 常问 "outline one assumption of the biological approach"。答案模板：Behaviour can be explained by brain structures, neurotransmitters, hormones, and genetics.</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s1">
    <div class="summary-card-header" onclick="toggleSummary('summary-s1')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Biological Approach</span>
      <span class="summary-card-badge">AO1</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Biological assumption: Behaviour = brain structures + neurotransmitters + hormones + genetics <span class="tag-must">Must Know</span></li>
          <li>Key debate: <strong>Nature (biology)</strong> vs <strong>Nurture (environment)</strong> <span class="tag-must">Must Know</span></li>
          <li>Toy preference pattern: Males → wheeled/construction toys; Females → plush/dolls <span class="tag-common">Common Q</span></li>
          <li>Rationale for using monkeys: They lack human socialisation, so any gender difference suggests biological origin <span class="tag-ao2">AO2 Gold</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 2 ==================== -->
<div class="section" id="s2">
  <h2>2️⃣ Background（研究背景）</h2>

  <div class="visual-header">
    <div class="vh-icon">📚</div>
    <div class="vh-text">
      <h4>Prior Research on Gender Differences</h4>
      <p>What did we already know before Hassett's study?</p>
    </div>
  </div>

  <h3>Previous Findings on Children's Toy Preferences（儿童玩具偏好的已有发现）</h3>
  <p>Research with human children has consistently shown gender differences in toy selection from as early as <strong>one year of age</strong>:</p>
  <ul>
    <li>Boys spend more time with wheeled toys and objects that can be manipulated mechanically</li>
    <li>Girls show greater interest in dolls and toys with facial features</li>
    <li>These differences appear across cultures, though the strength varies</li>
  </ul>

  <h3>The Social Learning Theory Challenge（社会学习理论的挑战）</h3>
  <p>Many psychologists argued that these differences were due to <strong>social learning（社会学习）</strong>: children imitate same-sex models, receive reinforcement for "gender-appropriate" play, and are influenced by media and parental expectations.</p>

  <p><strong>Hassett et al.'s challenge:</strong> If we test non-human primates who have NOT been exposed to human gender socialisation, and they STILL show similar patterns, then biology must play a significant role.</p>

  <blockquote>
    "The question of whether sex differences in toy preferences are determined by nature or nurture remains unanswered... Non-human primates provide an opportunity to examine this question without the confounding influence of human gender socialisation."<br>
    <span style="font-size:0.9em;color:var(--text-secondary);">— Hassett et al. (2008), paraphrased from original paper</span>
  </blockquote>

  <div class="blue-box">
    <strong>Why Rhesus Monkeys? 为什么选择恒河猴？</strong><br>
    • Closely related to humans genetically (~93% DNA shared)<br>
    • Complex social behaviours similar to humans<br>
    • NOT exposed to human gender stereotypes or marketing<br>
    • Previous research showed some gender-typical behaviours
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§2 研究背景：挑战社会化解释</div>
      <p><strong>已知事实：</strong>人类儿童从 1 岁起就表现出玩具偏好的性别差异。</p>
      <ul>
        <li><span class="cs-en">Social Learning Explanation（社会学习解释）</span>：差异来源于模仿同性榜样、强化、"适当"行为的奖励、媒体影响等后天因素。</li>
        <li><span class="cs-en">Biological Explanation（生物学解释）</span>：差异是先天的、由基因/激素决定的。</li>
        <li><span class="cs-en">Hassett 的策略</span>：用恒河猴做被试 → 它们没有接触过人类社会的性别刻板印象 → 如果仍然有差异 → 支持生物学解释！</li>
      </ul>
      <p><strong>💡 考试答题技巧：</strong>背景部分常考 "why use animals?" 或 "what is the rationale?"。答案要强调：排除人类社会化干扰，测试纯生物学因素。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s2">
    <div class="summary-card-header" onclick="toggleSummary('summary-s2')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Background</span>
      <span class="summary-card-badge">AO1+AO2</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Children show gendered toy preferences from age 1 (cross-cultural evidence) <span class="tag-common">Common Q</span></li>
          <li>Social learning theory: Differences come from imitation, reinforcement, parental/media influence <span class="tag-must">Must Know</span></li>
          <li>Rhesus monkeys chosen because: no human gender socialisation, close genetic relation to humans <span class="tag-ao2">AO2 Gold</span></li>
          <li>This study tests whether biology alone can produce gendered toy preferences <span class="tag-must">Must Know</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 3 ==================== -->
<div class="section" id="s3">
  <h2>3️⃣ Aim（研究目的）</h2>

  <blockquote>
    The aim was to investigate whether <strong>male and female rhesus monkeys show different preferences for "masculine" vs "feminine" toys</strong>, specifically whether males would prefer wheeled toys while females would prefer plush toys.<br>
    <span style="font-size:0.95em;color:var(--text-secondary);">（调查雄性和雌性恒河猴是否对"男性化"和"女性化"玩具有不同偏好。）</span>
  </blockquote>

  <div class="blue-box">
    <strong>Aim in One Sentence 一句话 aim：</strong><br>
    To determine if rhesus monkeys exhibit gender-stereotyped toy preferences (wheeled vs. plush) similar to human children, providing evidence for a biological basis of such preferences.<br>
    <span style="color:var(--text-secondary);font-size:0.93em;">（确定恒河猴是否表现出类似人类的性别刻板化玩具偏好，为这种偏好的生物学基础提供证据。）</span>
  </div>

  <div class="keyword-box">
    <h4>🎯 Research Hypothesis 研究假设</h4>
    <p><strong>Directional hypothesis（方向性假设）：</strong>Male monkeys will spend significantly more time interacting with wheeled toys ("masculine"), while female monkeys will spend more time with plush toys ("feminine").</p>
    <p><strong>Null hypothesis（虚无假设）：</strong>There will be no significant difference between males and females in time spent with either type of toy.</p>
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§3 研究目的与假设</div>
      <p><strong>核心 aim：</strong>检验恒河猴是否对"男性化"（带轮子）和"女性化"（毛绒）玩具有不同偏好。</p>
      <ul>
        <li><span class="cs-en">Directional Hypothesis（方向性假设）</span>：雄猴偏好 wheeled toys > 雌猴偏好 plush toys</li>
        <li><span class="cs-en">Null Hypothesis（虚无假设）</span>：两组之间无显著差异</li>
        <li><span class="cs-en">Operationalisation（操作化定义）</span>："偏好"用 interaction time（互动时间）测量</li>
      </ul>
      <p><strong>💡 考试要点：</strong>CIE 可能问 "state the aim"。答案必须包含：(1) 比较雄性与雌性；(2) wheeled vs plush toys；(3) 测量指标是时间。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s3">
    <div class="summary-card-header" onclick="toggleSummary('summary-s3')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Aim</span>
      <span class="summary-card-badge">AO1</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Aim: Compare male vs female monkey preferences for wheeled vs plush toys <span class="tag-must">Must Know</span></li>
          <li>DV: Time spent interacting with each toy type <span class="tag-must">Must Know</span></li>
          <li>IV: Sex of participant (male/female) + Type of toy (wheeled/plush) <span class="tag-common">Common Q</span></li>
          <li>Underlying purpose: Test nature (biology) vs nurture (socialisation) explanation <span class="tag-ao2">AO2 Gold</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 4 ==================== -->
<div class="section" id="s4">
  <h2>4️⃣ Method（研究方法）</h2>

  <div class="visual-header">
    <div class="vh-icon">🔬</div>
    <div class="vh-text">
      <h4>Naturalistic Observation</h4>
      <p>Controlled environment · Rhesus monkeys · Two toy categories</p>
    </div>
  </div>

  <h3>Research Method and Design（研究方法与设计）</h3>
  <p>This study used a <strong>naturalistic observation（自然观察法）</strong> in a controlled setting. Researchers observed monkeys' spontaneous interactions with different types of toys without direct manipulation or intervention.</p>

  <h3>Sample（样本）</h3>
  <table>
    <caption><strong>Table 1: Participant Details 参与者详情</strong></caption>
    <thead>
      <tr><th>Characteristic 特征</th><th>Details 详情</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Species 物种</strong></td><td>Rhesus macaque (Macaca mulatta)</td></tr>
      <tr><td><strong>Total N 总数</strong></td><td>Male and female rhesus monkeys</td></tr>
      <tr><td><strong>Age range 年龄范围</strong></td><td>Varied (juvenile to adult)</td></tr>
      <tr><td><strong>Housing 饲养环境</strong></td><td>Indoor enclosure at research facility</td></tr>
      <tr><td><strong>Sampling method 取样方法</strong></td><td>Opportunity sample (available monkeys)</td></tr>
    </tbody>
  </table>

  <h3>Materials / Stimuli（材料/刺激物）</h3>
  <p>Two categories of toys were used, matching those typically preferred by boys and girls respectively:</p>

  <div class="figure">
    <img src="hassett_images/gender_stereotyped_toys.jpg" alt="Gender-stereotyped toys used in the study">
    <div class="figure-caption">Figure 2.6: Examples of masculine (wheeled) and feminine (plush) toys used（研究中使用的男性和女性化玩具示例）</div>
  </div>

  <table>
    <caption><strong>Table 2: Toy Categories 玩具分类</strong></caption>
    <thead>
      <tr><th>Category 类别</th><th>Description 描述</th><th>Examples 示例</th><th>Human Equivalent 人类对应</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>"Masculine" toys（"男性化"玩具）</strong></td><td>Wheeled toys with moving parts</td><td>• Wheeled cars<br>• Trucks<br>• Construction vehicles</td><td>Toys typically preferred by boys</td></tr>
      <tr><td><strong>"Feminine" toys（"女性化"玩具）</strong></td><td>Soft plush toys</td><td>• Plush dolls<br>• Stuffed animals<br>• Soft colourful toys</td><td>Toys typically preferred by girls</td></tr>
    </tbody>
  </table>

  <h3>Procedure Overview（程序概览）</h3>
  <ol>
    <li>Monkeys were given access to both types of toys simultaneously in their familiar enclosure</li>
    <li>Researchers recorded the amount of time each monkey spent interacting with each toy category</li>
    <li>"Interaction" was defined as physical contact, manipulation, or sustained visual attention (>2 seconds)</li>
    <li>Observations were conducted over multiple sessions to ensure reliability</li>
  </ol>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§4 方法：自然观察法设计</div>
      <p><strong>研究类型：</strong><span class="cs-en">Naturalistic Observation（自然观察法）</span>——在受控环境中观察猴子自发的玩具互动行为，不进行干预或操纵。</p>
      <ul>
        <li><span class="cs-en">Sample（样本）</span>：恒河猴（雄性和雌性都有），机会取样</li>
        <li><span class="cs-en">Materials（材料）</span>：两类玩具——wheeled toys（车/卡车）vs plush toys（娃娃/毛绒动物）</li>
        <li><span class="cs-en">DV 操作化定义</span>："interaction time" = 身体接触、操作、或持续注视（>2秒）的时间总和</li>
        <li><span class="cs-en">Control 控制</span>：同时呈现两类玩具，在熟悉的环境中进行，多次观察确保信度</li>
      </ul>
      <p><strong>💡 考试要点：</strong>方法部分常考 "what was the research method?" 和 "how was the DV operationalised?"。答案关键词：naturalistic observation, interaction time, simultaneous presentation。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s4">
    <div class="summary-card-header" onclick="toggleSummary('summary-s4')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Method</span>
      <span class="summary-card-badge">AO1+AO2</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Method: Naturalistic observation in controlled setting <span class="tag-must">Must Know</span></li>
          <li>Sample: Male and female rhesus monkeys (opportunity sample) <span class="tag-common">Common Q</span></li>
          <li>Two toy types: Wheeled ("masculine") vs Plush ("feminine") <span class="tag-must">Must Know</span></li>
          <li>DV operationalised: Interaction time (contact/manipulation/attention >2s) <span class="tag-must">Must Know</span></li>
          <li>Control: Both toy types presented simultaneously; multiple sessions for reliability <span class="tag-ao2">AO2 Gold</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 5 ==================== -->
<div class="section" id="s5">
  <h2>5️⃣ Procedure（实验程序）</h2>

  <h3>Step-by-Step Process（分步过程）</h3>
  
  <div class="keyword-box">
    <h4>📋 Standardised Procedure 标准化程序</h4>
    <p><strong>Phase 1: Preparation 准备阶段</strong></p>
    <ol>
      <li>Select appropriate indoor enclosure familiar to the monkeys</li>
      <li>Prepare equal numbers of wheeled and plush toys</li>
      <li>Position video cameras to record all interactions</li>
      <li>Ensure toys are clean and novel (not previously seen by monkeys)</li>
    </ol>
    
    <p><strong>Phase 2: Data Collection 数据收集</strong></p>
    <ol start="5">
      <li>Place both sets of toys in the enclosure simultaneously</li>
      <li>Allow monkeys free access and unrestricted movement</li>
      <li>Record behaviour for set time period (multiple sessions across days)</li>
      <li>Use behavioural checklist to code interactions in real-time or from video</li>
    </ol>
    
    <p><strong>Phase 3: Post-Observation 观察后</strong></p>
    <ol start="9">
      <li>Calculate total interaction time per toy category per individual</li>
      <li>Compare male vs female means using appropriate statistical test</li>
    </ol>
  </div>

  <div class="note-box">
    <strong>Standardisation Controls 标准化控制措施：</strong><br>
    • Same environment for all participants<br>
    • Same toys presented in same positions<br>
    • Same observation duration<br>
    • Inter-rater reliability checks (multiple observers coded independently)
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§5 实验程序：三阶段标准化流程</div>
      <p><strong>核心特点：</strong>高度标准化的自然观察程序，确保内部效度。</p>
      <ul>
        <li><span class="cs-en">Preparation（准备）</span>：选择熟悉的环境、准备两类玩具、架设摄像机、确保玩具新颖性</li>
        <li><span class="cs-en">Data Collection（数据收集）</span>：同时放置两类玩具 → 自由访问 → 录像记录 → 行为编码</li>
        <li><span class="cs-en">Analysis（分析）</span>：计算每只猴子的互动时间 → 统计比较雄雌差异</li>
        <li><span class="cs-en">Control Measures（控制措施）</span>：相同环境/位置/时长 + inter-rater reliability（评分者间信度）</li>
      </ul>
      <p><strong>💡 考试要点：</strong>程序题可能问 "outline two controls"。答案：(1) Standardised procedure (same toys, positions, duration); (2) Inter-rater reliability checks.</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s5">
    <div class="summary-card-header" onclick="toggleSummary('summary-s5')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Procedure</span>
      <span class="summary-card-badge">AO1</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Three phases: Preparation → Data collection → Analysis <span class="tag-common">Common Q</span></li>
          <li>Key control: Simultaneous presentation of both toy types <span class="tag-must">Must Know</span></li>
          <li>Reliability measure: Inter-rater reliability (multiple independent coders) <span class="tag-ao2">AO2 Gold</span></li>
          <li>Ethical consideration: Familiar environment reduces stress; no deprivation or harm <span class="tag-context">Context</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 6 ==================== -->
<div class="section" id="s6">
  <h2>6️⃣ Behavioural Checklist（行为检查表）</h2>

  <h3>Defining "Interaction"（定义"互动"）</h3>
  <p>To ensure objective measurement, researchers developed a clear behavioural checklist defining what counted as "interaction" with each toy type:</p>

  <table>
    <caption><strong>Table 3: Behavioural Categories 行为类别</strong></caption>
    <thead>
      <tr><th>Behaviour 行为</th><th>Definition 定义</th><th>Example 示例</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Physical contact（身体接触）</strong></td><td>Touching, holding, or carrying the toy</td><td>Picking up a wheeled car; hugging a plush doll</td></tr>
      <tr><td><strong>Manipulation（操作）</strong></td><td>Moving, pushing, rolling, or examining the toy</td><td>Pushing a truck; squeezing a plush toy</td></tr>
      <tr><td><strong>Visual attention（视觉注意）</strong></td><td>Sustained looking at toy (>2 seconds)</td><td>Staring at a doll's face</td></tr>
    </tbody>
  </table>

  <div class="note-box">
    <strong>Coding System 编码系统：</strong><br>
    • Continuous recording or time sampling used<br>
    • Multiple independent observers coded behaviour<br>
    • Inter-rater reliability calculated to ensure consistency<br>
    • Video recording allowed later verification of coding decisions
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§6 行为检查表：操作化定义的精确性</div>
      <p><strong>核心工具：</strong>行为检查表确保测量的客观性和可重复性。</p>
      <ul>
        <li><span class="cs-en">Physical Contact（身体接触）</span>：触摸、拿住、携带玩具</li>
        <li><span class="cs-en">Manipulation（操作）</span>：移动、推动、滚动、检查玩具</li>
        <li><span class="cs-en">Visual Attention（视觉注意）</span>：持续注视玩具（>2秒）</li>
        <li><span class="cs-en">Inter-rater Reliability（评分者间信度）</span>：多个独立观察者编码 → 计算一致性系数</li>
      </ul>
      <p><strong>💡 考试要点：</strong>可能问 "how was the DV measured?" 答案要提到 behavioural checklist + inter-rater reliability。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s6">
    <div class="summary-card-header" onclick="toggleSummary('summary-s6')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Behavioural Checklist</span>
      <span class="summary-card-badge">AO1</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Three behavioural categories: contact, manipulation, attention (>2s) <span class="tag-must">Must Know</span></li>
          <li>Multiple observers ensure inter-rater reliability <span class="tag-common">Common Q</span></li>
          <li>Video recording allows verification and increases objectivity <span class="tag-ao2">AO2 Gold</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 7 ==================== -->
<div class="section" id="s7">
  <h2>7️⃣ Results（研究结果）</h2>

  <div class="visual-header">
    <div class="vh-icon">📊</div>
    <div class="vh-text">
      <h4>Key Findings — Data Driven!</h4>
      <p>Statistically significant gender differences in toy preferences</p>
    </div>
  </div>

  <div class="warn-box">
    <h4>🎯 Main Result 主要发现</h4>
    <p><strong>Male monkeys showed significant preference for wheeled toys</strong><br>
    <strong>Female monkeys showed preference for plush toys</strong><br>
    Difference was <strong>statistically significant (p &lt; .05)</strong></p>
  </div>

  <h3>Specific Data Points（具体数据）</h3>
  <table>
    <caption><strong>Table 4: Summary of Main Findings 主要发现汇总</strong></caption>
    <thead>
      <tr><th>Finding 发现</th><th>Males 雄性</th><th>Females 雌性</th><th>Significance 显著性</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Preferred toy type</strong></td><td>Wheeled toys (cars, trucks)</td><td>Plush toys (dolls, stuffed animals)</td><td>p &lt; .05</td></tr>
      <tr><td><strong>Approximate proportion</strong></td><td>~73% preferred wheeled</td><td>Majority preferred plush</td><td>Statistically significant</td></tr>
      <tr><td><strong>Pattern match to humans</strong></td><td colspan="3" style="text-align:center;">✓ Closely paralleled human children's gender-stereotyped preferences</td></tr>
    </tbody>
  </table>

  <h3>Statistical Analysis（统计分析）</h3>
  <ul>
    <li>Appropriate inferential statistical test conducted</li>
    <li><strong>p &lt; .05</strong> indicates result is statistically significant (unlikely due to chance)</li>
    <li>Effect size suggested meaningful practical significance beyond statistical significance</li>
  </ul>

  <div class="green-box">
    <strong>Why This Matters 为什么这很重要：</strong><br>
    • First clear demonstration that non-human primates show human-like gendered toy preferences<br>
    • Cannot be explained by human socialisation (monkeys don't watch TV or receive gendered parenting)<br>
    • Strong evidence for biological/evolutionary component to gendered behaviour<br>
    • Challenges pure Social Learning Theory explanations
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§7 研究结果：支持生物学解释的关键证据</div>
      <p><strong>核心数据：</strong></p>
      <ul>
        <li><span class="cs-en">Main Finding（主要发现）</span>：雄猴显著偏好 wheeled toys；雌猴偏好 plush toys</li>
        <li><span class="cs-en">Statistical Significance（统计显著性）</span>：p &lt; .05（不是偶然）</li>
        <li><span class="cs-en">73% Rule（73%法则）</span>：约 73% 的雄猴偏好带轮子玩具</li>
        <li><span class="cs-en">Human Parallel（人类平行）</span>：结果与人类儿童的性别刻板印象玩具偏好高度一致</li>
      </ul>
      <p><strong>💡 考试要点：</strong>结果题必背！(1) 雄→wheeled, 雌→plush; (2) p&lt;.05; (3) ~73% males; (4) parallels human children。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s7">
    <div class="summary-card-header" onclick="toggleSummary('summary-s7')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Results</span>
      <span class="summary-card-badge">AO1</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Males preferred wheeled toys (~73%); females preferred plush toys <span class="tag-must">Must Know</span></li>
          <li>Statistically significant: p &lt; .05 <span class="tag-must">Must Know</span></li>
          <li>Results parallel human children's preferences → supports biological basis <span class="tag-ao2">AO2 Gold</span></li>
          <li>Be able to quote approximate percentages in exam answers <span class="tag-common">Common Q</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 8 ==================== -->
<div class="section" id="s8">
  <h2>8️⃣ Conclusion（结论）</h2>

  <div class="visual-header">
    <div class="vh-icon">💡</div>
    <div class="vh-text">
      <h4>Main Conclusion</h4>
      <p>Biology plays a significant role in gendered toy preferences</p>
    </div>
  </div>

  <blockquote>
    The findings suggest that <strong>gender-stereotyped toy preferences are not solely determined by socialisation</strong>. Since rhesus monkeys (who have no exposure to human gender stereotypes) show similar patterns to human children, there appears to be a <strong>biological/evolutionary component</strong> to these preferences.
  </blockquote>

  <h3>Implications of the Conclusion（结论的含义）</h3>
  <ol>
    <li><strong>Supports Nature side of Nature-Nurture debate</strong> — Biology contributes to gendered behaviour</li>
    <li><strong>Challenges pure Social Learning Theory</strong> — Cannot explain findings with nurture alone</li>
    <li><strong>Suggests evolutionary adaptation</strong> — Some gendered behaviours may be evolutionarily adaptive</li>
    <li><strong>Cautions against oversimplification</strong> — Biology is not destiny; socialisation still plays a role</li>
  </ol>

  <div class="blue-box">
    <strong>Link to Biological Approach 与生物取向的联系：</strong><br>
    • Provides evidence that hormones/genes may influence behaviour<br>
    • Consistent with evolutionary psychology perspective<br>
    • Gender differences may have adaptive value (preparation for ancestral roles)<br>
    • BUT: Findings describe group averages, not individual destiny
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§8 结论：支持 Nature 的有力证据</div>
      <p><strong>核心结论：</strong>性别刻板化的玩具偏好不完全是社会化的结果。</p>
      <ul>
        <li><span class="cs-en">Key Argument（核心论点）</span>：恒河猴没有接触过人类性别刻板印象 → 但仍表现类似模式 → 说明有生物学成分</li>
        <li><span class="cs-en">Nature Support（支持先天）</span>：强力支持 Nature-Nurture 争论中的 Nature 方</li>
        <li><span class="cs-en">Challenge to SLT（挑战社会学习理论）</span>：纯后天解释无法说明这些发现</li>
        <li><span class="cs-en">Nuance（细微差别）</span>：生物学 ≠ 命运；社会化仍有作用；两者可能交互影响</li>
      </ul>
      <p><strong>💡 考试要点：</strong>结论题要强调 "not SOLELY determined by socialisation" 这个关键词！</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s8">
    <div class="summary-card-header" onclick="toggleSummary('summary-s8')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Conclusion</span>
      <span class="summary-card-badge">AO1+AO2</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Conclusion: Preferences not solely due to socialisation <span class="tag-must">Must Know</span></li>
          <li>Monkey results parallel humans → biological component exists <span class="tag-must">Must Know</span></li>
          <li>Supports Nature side; challenges pure Social Learning Theory <span class="tag-ao2">AO2 Gold</span></li>
          <li>Biology ≠ destiny; socialisation still plays role (balanced view) <span class="tag-common">Common Q</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 9 ==================== -->
<div class="section" id="s9">
  <h2>9️⃣ Evaluation（评价）</h2>

  <div class="visual-header">
    <div class="vh-icon">⚖️</div>
    <div class="vh-text">
      <h4>Strengths & Weaknesses</h4>
      <p>Critical evaluation of methodology and findings</p>
    </div>
  </div>

  <h3>Strengths of the Study（研究的优势）</h3>
  
  <div class="green-box">
    <strong>✅ 1. High Internal Validity 内部效度高</strong><br>
    Controlled environment minimises confounding variables. Standardised procedure ensures consistency. Clear operationalisation of variables allows replication.
  </div>

  <div class="green-box">
    <strong>✅ 2. Use of Non-Human Primates 使用非人灵长类动物</strong><br>
    Eliminates confounding influence of human socialisation. Allows isolation of biological factors. Ethical advantage over manipulating human children's environments.
  </div>

  <div class="green-box">
    <strong>✅ 3. Objective Measurement 客观测量</strong><br>
    Behavioural checklist provides clear criteria. Inter-rater reliability increases trustworthiness. Video recording allows verification.
  </div>

  <div class="green-box">
    <strong>✅ 4. Evolutionary Significance 进化意义</strong><br>
    Findings have implications for understanding human behaviour evolution. Contributes meaningfully to Nature vs Nurture debate.
  </div>

  <h3>Weaknesses of the Study（研究的劣势）</h3>

  <div class="warn-box">
    <strong>❌ 1. Limited Generalisability 外推有限</strong><br>
    Monkey behaviour may not perfectly translate to humans. Cultural factors in humans are more complex. Cannot capture full complexity of human socialisation.
  </div>

  <div class="warn-box">
    <strong>❌ 2. Small Sample Size 样本量小</strong><br>
    Opportunity sample limits representativeness. Individual differences may affect results. Risk of Type I or Type II errors.
  </div>

  <div class="warn-box">
    <strong>❌ 3. Artificial Setting 人为环境</strong><br>
    Laboratory enclosure differs from natural habitat. May affect natural behaviour patterns. Novelty effect of toys could influence results.
  </div>

  <div class="warn-box">
    <strong>❌ 4. Determinism Risk 决定论风险</strong><br>
    Overemphasis on biology could support genetic determinism. May ignore individual variation within genders. Could be misused to justify gender inequality.
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§9 评价：平衡的批判性思维</div>
      <p><strong>Strengths（优势）：</strong></p>
      <ul>
        <li>高内部效度（控制环境、标准化程序）</li>
        <li>使用非人灵长类（排除人类社会化干扰）</li>
        <li>客观测量（行为检查表、评分者间信度）</li>
        <li>进化意义（贡献于 Nature-Nurture 争论）</li>
      </ul>
      <p><strong>Weaknesses（劣势）：</strong></p>
      <ul>
        <li>外推有限（猴子≠人类）</li>
        <li>样本量小（机会取样）</li>
        <li>人为环境（实验室vs自然环境）</li>
        <li>决定论风险（可能被滥用支持性别不平等）</li>
      </ul>
      <p><strong>💡 考试技巧：</strong>evaluation 题需要 balanced argument（两边都说），每点都要 explain WHY it's strength/weakness。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s9">
    <div class="summary-card-header" onclick="toggleSummary('summary-s9')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Evaluation</span>
      <span class="summary-card-badge">AO2</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Strength: Eliminates human socialisation confound (unique advantage) <span class="tag-ao2">AO2 Gold</span></li>
          <li>Weakness: Limited generalisability to humans <span class="tag-ao2">AO2 Gold</span></li>
          <li>Strength: Objective measurement via behavioural checklist <span class="tag-common">Common Q</span></li>
          <li>Weakness: Small opportunity sample <span class="tag-common">Common Q</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 10 ==================== -->
<div class="section" id="s10">
  <h2>🔟 Ethical Issues（伦理问题）</h2>

  <div class="visual-header">
    <div class="vh-icon">⚖️</div>
    <div class="vh-text">
      <h4>Animal Ethics Considerations</h4>
      <p>Weighing scientific value against animal welfare</p>
    </div>
  </div>

  <h3>Positive Ethical Aspects（正面的伦理方面）</h3>
  <div class="green-box">
    <strong>✅ Why this study is ethically acceptable:</strong><br>
    • <strong>Naturalistic observation</strong> — minimal intervention required<br>
    • <strong>Familiar environment</strong> — reduces stress on animals<br>
    • <strong>No deprivation or harm</strong> — no pain, discomfort, or suffering inflicted<br>
    • <strong>Enrichment value</strong> — toys provided may actually improve welfare<br>
    • Animals already housed (no additional capture/breeding)
  </div>

  <h3>Potential Ethical Concerns（潜在的伦理关注）</h3>
  <div class="warn-box">
    <strong>⚠️ Issues to consider:</strong><br>
    • <strong>No informed consent</strong> — animals cannot agree to participate<br>
    • <strong>Captive environment</strong> — animals already experience confinement stress<br>
    • <strong>Risk of misuse</strong> — findings could support discriminatory views on gender<br>
    • <strong>Questionable justification</strong> — is using animals justified for this research?
  </div>

  <h3>Ethical Guidelines Referenced（参考的伦理准则）</h3>
  <ul>
    <li><strong>APA Guidelines</strong> for ethical treatment of animals in research</li>
    <li><strong>Institutional oversight</strong> (IACUC approval implied)</li>
    <li><strong>3 Rs principle</strong>: Reduction, Refinement, Replacement</li>
  </ul>

  <div class="note-box">
    <strong>Cost-Benefit Analysis 成本效益分析：</strong><br>
    • <strong>Cost 成本</strong>: Minimal harm/stress to captive animals already housed<br>
    • <strong>Benefit 收益</strong>: Significant contribution to understanding human behaviour<br>
    • <strong>Verdict 判定</strong>: Generally considered <strong>ethically acceptable</strong> given minimal risk and high scientific value
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§10 伦理问题：动物研究的道德考量</div>
      <p><strong>正面因素：</strong></p>
      <ul>
        <li>自然观察法（最小干预）</li>
        <li>熟悉的环境（减少压力）</li>
        <li>无伤害（无痛苦或不适）</li>
        <li>玩具作为丰富化（可能改善福利）</li>
      </ul>
      <p><strong>关注点：</strong></p>
      <ul>
        <li>无法获得知情同意</li>
        <li>圈养环境的固有压力</li>
        <li>结果可能被滥用于支持歧视观点</li>
      </ul>
      <p><strong>💡 考试要点：</strong>伦理题常用 "assess one ethical issue" 格式。记住 3 Rs 原则和成本效益分析框架。</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s10">
    <div class="summary-card-header" onclick="toggleSummary('summary-s10')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Ethics</span>
      <span class="summary-card-badge">AO2</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Positive: Naturalistic observation, no harm, enrichment value <span class="tag-ao2">AO2 Gold</span></li>
          <li>Concern: Animals cannot consent; potential for misuse <span class="tag-ao2">AO2 Gold</span></li>
          <li>3 Rs principle: Reduction, Refinement, Replacement <span class="tag-common">Common Q</span></li>
          <li>Generally acceptable: low risk, high scientific value <span class="tag-context">Context</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 11 ==================== -->
<div class="section" id="s11">
  <h2>1️⃣1️⃣ Issues & Debates（争论与取向）</h2>

  <div class="visual-header">
    <div class="vh-icon">🔄</div>
    <div class="vh-text">
      <h4>Key Psychological Debates</h4>
      <p>Where does this study fit in bigger theoretical arguments?</p>
    </div>
  </div>

  <h3>Nature vs Nurture（先天与后天）</h3>
  <div class="blue-box">
    <strong>🧬 This study STRONGLY SUPPORTS NATURE</strong><br>
    • Shows gendered behaviours exist WITHOUT socialisation<br>
    • Suggests biological predisposition<br>
    • BUT: Does not completely rule out nurture's role in humans<br>
    • Best viewed as evidence that biology contributes, not that it determines
  </div>

  <h3>Reductionism vs Holism（还原论与整体论）</h3>
  <div class="note-box">
    <strong>🔬 Reductive approach:</strong> Reduces complex gendered behaviour to simple biological factors. Useful for isolating mechanisms but may oversimplify complex social phenomena. Gender identity and expression are multifaceted — reducing them to toy preferences misses nuance.
  </div>

  <h3>Gender Bias（性别偏见）</h3>
  <div class="warn-box">
    <h4>⚠️ Risk of reinforcing stereotypes</h4>
    <p>Findings could be misinterpreted as "biology is destiny." Important caveats:</p>
    <ul>
      <li>Group averages don't predict individuals</li>
      <li>Within-gender variation is often greater than between-gender differences</li>
      <li>Responsible reporting must avoid determinism</li>
      <li>Findings describe tendencies, not fixed outcomes</li>
    </ul>
  </div>

  <h3>Animal Research（动物研究）</h3>
  <div class="green-box">
    <strong>🐵 Scientific value vs animal welfare:</strong><br>
    • This study demonstrates ethical animal use IS possible<br>
    • Findings genuinely benefit human understanding<br>
    • Ongoing debate about moral status of non-human primates<br>
    • Must balance knowledge gains against ethical costs
  </div>

  <h3>Socially Sensitive Research（社会敏感性研究）</h3>
  <div class="keyword-box">
    <h4>🔒 Responsible reporting essential</h4>
    <p><strong>Findings could be misused</strong> to reinforce gender inequalities or justify discrimination. Researchers and students have responsibility to:</p>
    <ul>
      <li>Avoid oversimplification or deterministic language</li>
      <li>Emphasise within-group diversity</li>
      <li>Contextualise findings appropriately</li>
      <li>Consider real-world implications of how results are interpreted</li>
    </ul>
  </div>

  <!-- Chinese Summary Card -->
  <div class="cn-summary-wrap">
    <button class="cn-summary-toggle" onclick="toggleCnSummary(this)"><span class="cs-icon">▶</span> 中文逻辑总结</button>
    <div class="cn-summary-body">
      <div class="cs-title">§11 争论与取向：理论定位</div>
      <p><strong>Nature vs Nurture：</strong>强力支持 Nature（主要贡献）</p>
      <p><strong>Reductionism：</strong>还原论方法（简化但有用）</p>
      <p><strong>Gender Bias：</strong>有强化刻板印象的风险 → 需要负责任地报告</p>
      <p><strong>Animal Research：</strong>科学价值 vs 动物福利的平衡</p>
      <p><strong>Social Sensitivity：</strong>社会敏感性 → 结果可能被滥用</p>
      <p><strong>💡 考试要点：</strong>Debates 题通常要求 discuss，需要展示多角度思考能力。记住：每个 debate 都有两面！</p>
    </div>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s11">
    <div class="summary-card-header" onclick="toggleSummary('summary-s11')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Debates</span>
      <span class="summary-card-badge">AO2+AO3</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Supports Nature side of debate (PRIMARY contribution) <span class="tag-must">Must Know</span></li>
          <li>Reductive: reduces complex behaviour to biology <span class="tag-ao2">AO2 Gold</span></li>
          <li>Gender bias risk: could reinforce stereotypes <span class="tag-ao2">AO2 Gold</span></li>
          <li>Socially sensitive: responsible reporting essential <span class="tag-common">Common Q</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 12 ==================== -->
<div class="section" id="s12">
  <h2>1️⃣2️⃣ Summary（总结）</h2>

  <div class="visual-header">
    <div class="vh-icon">📝</div>
    <div class="vh-text">
      <h4>One-Paragraph Summary</h4>
      <p>Everything you need to remember in a nutshell</p>
    </div>
  </div>

  <div class="quote">
    Hassett et al. (2008) investigated whether rhesus monkeys show gender-stereotyped toy preferences similar to human children. Using naturalistic observation, researchers found that male monkeys significantly preferred wheeled toys while female monkeys preferred plush toys (<strong>p &lt; .05</strong>). Since monkeys are not influenced by human gender socialisation, these findings provide evidence for a <strong>biological basis</strong> of gendered toy preferences, supporting the <strong>Nature</strong> side of the Nature-Nurture debate and challenging purely <strong>Social Learning Theory</strong> explanations.
  </div>

  <h3>Quick Revision Grid 快速复习表格</h3>
  <table>
    <caption><strong>Table 5: Study Overview at a Glance 一览表</strong></caption>
    <thead>
      <tr><th>Aspect 方面</th><th>Details 详情</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Method 方法</strong></td><td>Naturalistic observation 自然观察法</td></tr>
      <tr><td><strong>Sample 样本</strong></td><td>Rhesus monkeys (male & female) 恒河猴（雄性与雌性）</td></tr>
      <tr><td><strong>IV 自变量</strong></td><td>Sex (male/female) + Toy type (wheeled/plush)</td></tr>
      <tr><td><strong>DV 因变量</strong></td><td>Interaction time 互动时间</td></tr>
      <tr><td><strong>Key Finding 核心发现</strong></td><td>Males → wheeled (73%); Females → plush</td></tr>
      <tr><td><strong>Significance 显著性</strong></td><td>p &lt; .05 (statistically significant)</td></tr>
      <tr><td><strong>Conclusion 结论</strong></td><td>Supports biological/Nature explanation 支持生物学/先天解释</td></tr>
      <tr><td><strong>Approach 取向</strong></td><td>Biological Approach 生物取向</td></tr>
      <tr><td><strong>Debate 争论</strong></td><td>Nature vs Nurture 先天与后天</td></tr>
    </tbody>
  </table>

  <div class="keyword-box">
    <h4>🇨🇳 中文总结</h4>
    <p>哈塞特等人 (2008) 调查了恒河猴是否表现出类似人类的性别刻板化玩具偏好。使用自然观察法，研究者发现<strong>雄猴显著偏好带轮子的玩具，而雌猴偏好毛绒玩具 (p &lt; .05)</strong>。由于猴子不受人类性别社会化的影响，这些发现为玩具偏好的<strong>生物学基础</strong>提供了证据，支持了<strong>先天-后天争论中的先天方</strong>，挑战了纯粹的<strong>社会学习理论</strong>解释。</p>
  </div>

  <!-- Exam Key Points -->
  <div class="summary-card" id="summary-s12">
    <div class="summary-card-header" onclick="toggleSummary('summary-s12')">
      <span class="summary-card-icon">▶</span>
      <span class="summary-card-title">Exam Key Points — Summary</span>
      <span class="summary-card-badge">Revision</span>
    </div>
    <div class="summary-card-body">
      <div class="summary-card-inner">
        <ul>
          <li>Memorise the one-paragraph summary for 4-mark "outline" questions <span class="tag-must">Must Know</span></li>
          <li>Know all Quick Revision Grid details for "describe" questions <span class="tag-must">Must Know</span></li>
          <li>Key numbers: 73% males, p &lt; .05, wheeled vs plush <span class="tag-common">Common Q</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ==================== SECTION 13 ==================== -->
<div class="section" id="s13">
  <h2>1️⃣3️⃣ Study Questions（复习题）</h2>

  <div class="visual-header">
    <div class="vh-icon">📝</div>
    <div class="vh-text">
      <h4>Practice Questions & Model Answers</h4>
      <p>Test your understanding with exam-style questions</p>
    </div>
  </div>

  <!-- Q1 -->
  <div class="qa-card" id="qa1">
    <div class="qa-question" onclick="toggleQA('qa1')">
      <div class="qa-num">Q1</div>
      <div class="qa-text">Outline one assumption of the biological approach. [4 marks] <span class="tag-must">Must Know</span> <span class="tag-context">AO1</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        One assumption of the biological approach is that behaviour can be explained in terms of biological factors such as brain structures, neurotransmitters, hormones, and genetics. For example, the approach assumes that differences in brain structure or hormone levels can account for behavioural differences between individuals. <em>(AO1: 4 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q2 -->
  <div class="qa-card" id="qa2">
    <div class="qa-question" onclick="toggleQA('qa2')">
      <div class="qa-num">Q2</div>
      <div class="qa-text">Describe the sample used in Hassett et al.'s study. [4 marks] <span class="tag-common">Common Q</span> <span class="tag-context">AO1</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        The sample consisted of male and female rhesus monkeys (Macaca mulatta) of varying ages from juvenile to adult. They were housed in an indoor enclosure at a research facility. An opportunity sampling method was used, meaning the researchers used monkeys that were readily available to them rather than randomly selecting from a population. <em>(AO1: 4 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q3 -->
  <div class="qa-card" id="qa3">
    <div class="qa-question" onclick="toggleQA('qa3')">
      <div class="qa-num">Q3</div>
      <div class="qa-text">Explain one strength of using animals in this study. [4 marks] <span class="tag-ao2">AO2 Gold</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        One strength is that animals eliminate the confounding influence of human socialisation. Rhesus monkeys have not been exposed to human gender stereotypes, media representations, or parental reinforcement of "gender-appropriate" behaviour. Therefore, any gender differences observed are more likely to reflect innate biological predispositions rather than learned behaviours. This increases the internal validity of the conclusions about biological influences on behaviour. <em>(AO2: 4 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q4 -->
  <div class="qa-card" id="qa4">
    <div class="qa-question" onclick="toggleQA('qa4')">
      <div class="qa-num">Q4</div>
      <div class="qa-text">Describe the results of Hassett et al.'s study. [6 marks] <span class="tag-must">Must Know</span> <span class="tag-context">AO1</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        The results showed that male rhesus monkeys spent significantly more time interacting with wheeled toys (the "masculine" category), while female monkeys spent more time with plush toys (the "feminine" category). Approximately <strong>73% of male monkeys</strong> showed a preference for wheeled toys. This difference was <strong>statistically significant (p &lt; .05)</strong>, meaning it is unlikely to have occurred by chance. The pattern of results closely paralleled the gender-stereotyped toy preferences typically observed in human children. <em>(AO1: 6 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q5 -->
  <div class="qa-card" id="qa5">
    <div class="qa-question" onclick="toggleQA('qa5')">
      <div class="qa-num">Q5</div>
      <div class="qa-text">Discuss the nature-nurture debate in relation to this study. [8 marks] <span class="tag-must">Must Know</span> <span class="tag-context">AO2</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        This study provides strong support for the <strong>Nature</strong> side of the nature-nurture debate. The key argument is that rhesus monkeys, who have never been exposed to human gender socialisation, still show gender-stereotyped toy preferences similar to human children. If these preferences were entirely learned (nurture), we would not expect to see them in monkeys raised without human gender norms.<br><br>
        
        The finding that approximately 73% of males preferred wheeled toys while females preferred plush toys (p &lt; .05) suggests an innate, evolved component to these preferences. This challenges Social Learning Theory, which attributes gendered behaviour to imitation, reinforcement, and modelling.<br><br>
        
        However, it is important to note that supporting Nature does not mean Nurture has no role. In humans, socialisation likely interacts with biological predispositions. The study shows biology contributes, but does not determine behaviour completely. A balanced view acknowledges both nature and nurture interact to produce complex behaviours. <em>(AO2: 8 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q6 -->
  <div class="qa-card" id="qa6">
    <div class="qa-question" onclick="toggleQA('qa6')">
      <div class="qa-num">Q6</div>
      <div class="qa-text">Evaluate the use of naturalistic observation in this study. [6 marks] <span class="tag-ao2">AO2 Gold</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        <strong>Strength:</strong> Naturalistic observation allowed researchers to measure spontaneous, natural behaviour without intervention. This increases ecological validity compared to laboratory experiments where participants know they are being studied. The monkeys behaved naturally because they were in a familiar environment with novel toys presented as enrichment.<br><br>
        
        <strong>Weakness:</strong> Despite being "naturalistic," the setting was still artificial (indoor enclosure with specific toys placed). This may limit generalisability to truly natural environments. Additionally, there may be observer bias if coders have expectations about gender differences, though this was addressed through inter-rater reliability checks. <em>(AO2: 6 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q7 -->
  <div class="qa-card" id="qa7">
    <div class="qa-question" onclick="toggleQA('qa7')">
      <div class="qa-num">Q7</div>
      <div class="qa-text">Assess one ethical issue in this study. [6 marks] <span class="tag-ao2">AO2</span> <span class="tag-common">Common</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        One ethical issue is the <strong>use of animals in research</strong>. On the positive side, this study used naturalistic observation which involved minimal intervention - the monkeys were simply given toys to play with in their familiar enclosure. No deprivation, pain, or harm was inflicted. In fact, the toys may have served as environmental enrichment, potentially improving welfare.<br><br>
        
        However, animals cannot give <strong>informed consent</strong>, raising questions about their right to autonomy. The monkeys were captive and had no choice about participating. There is also the concern that findings from animal research could be misused to support discriminatory views about gender roles in humans.<br><br>
        
        Overall, the study appears ethically acceptable under guidelines like the APA's 3 Rs (Reduction, Refinement, Replacement), as the cost (minimal stress) is outweighed by the benefit (significant scientific contribution). <em>(AO2: 6 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q8 -->
  <div class="qa-card" id="qa8">
    <div class="qa-question" onclick="toggleQA('qa8')">
      <div class="qa-num">Q8</div>
      <div class="qa-text">'Gender differences in behaviour are entirely due to socialisation.' To what extent does Hassett et al.'s study support this statement? [12 marks] <span class="tag-must">Must Know</span> <span class="tag-context">AO2 Extended</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        This statement claims gender differences are ENTIRELY due to socialisation. Hassett et al.'s study provides evidence that <strong>challenges</strong> this view, suggesting the statement is only supported to a <strong>limited extent</strong>.<br><br>
        
        <strong>Evidence challenging the statement:</strong><br>
        The study found male monkeys preferred wheeled toys while females preferred plush toys (p &lt; .05), mirroring human patterns. Crucially, monkeys lack exposure to human gender socialisation - they haven't watched TV showing gendered advertisements, received parental reinforcement for "appropriate" toys, or observed same-sex models. Yet they still show similar preferences. This strongly suggests a <strong>biological component</strong> exists that cannot be explained by socialisation alone.<br><br>
        
        <strong>Evidence supporting limited role of socialisation:</strong><br>
        The study does NOT prove socialisation is irrelevant. Humans experience far more complex socialisation than monkeys. It is plausible that in humans, biology creates predispositions that are then amplified, modified, or sometimes overridden by social learning. The monkey study shows nature matters, but doesn't quantify how much nurture contributes in humans.<br><br>
        
        <strong>Conclusion:</strong><br>
        Hassett et al.'s study demonstrates that gender differences are NOT <strong>entirely</strong> due to socialisation - there is clearly a biological component. However, it would be wrong to conclude socialisation plays NO role. The most accurate position is an <strong>interactionist perspective</strong>: biology provides predispositions, and socialisation shapes how these are expressed. The statement is therefore an oversimplification that is largely contradicted by this research. <em>(AO2: 12 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q9 -->
  <div class="qa-card" id="qa9">
    <div class="qa-question" onclick="toggleQA('qa9')">
      <div class="qa-num">Q9</div>
      <div class="qa-text">How could the methodology of this study be improved? [6 marks] <span class="tag-ao2">AO2</span> <span class="tag-common">Common</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        <strong>Improvement 1 - Larger sample:</strong> The study used an opportunity sample of limited size. A larger sample, ideally randomly selected from multiple facilities, would increase generalisability and statistical power. This would allow more confidence that results reflect true population patterns rather than sampling error.<br><br>
        
        <strong>Improvement 2 - Longitudinal design:</strong> A longitudinal study tracking the same monkeys over time could show whether preferences are stable from infancy through adulthood or change with development. This would strengthen claims about innate vs learned components.<br><br>
        
        <strong>Improvement 3 - Cross-species comparison:</strong> Testing other primate species (chimpanzees, bonobos) could determine if findings are specific to rhesus monkeys or generalise across primates, strengthening evolutionary claims. <em>(AO2: 6 marks)</em>
      </div>
    </div>
  </div>

  <!-- Q10 -->
  <div class="qa-card" id="qa10">
    <div class="qa-question" onclick="toggleQA('qa10')">
      <div class="qa-num">Q10</div>
      <div class="qa-text">Design a replication study to test the reliability of Hassett et al.'s findings. [10 marks] <span class="tag-ao2">AO2 Extended</span> <span class="tag-context">Application</span></div>
      <div class="qa-toggle"><span class="qa-icon">▼</span></div>
    </div>
    <div class="qa-answer">
      <div class="qa-answer-inner">
        <strong>Model Answer:</strong><br>
        <strong>Aim:</strong> To replicate Hassett et al.'s study with modifications to test reliability of findings about gender-stereotyped toy preferences in non-human primates.<br><br>
        
        <strong>Method:</strong><br>
        • <strong>Design:</strong> Independent groups design comparing male vs female chimpanzees<br>
        • <strong>Sample:</strong> 40 chimpanzees (20 male, 20 female) aged 2-10 years from a sanctuary setting<br>
        • <strong>Materials:</strong> Identical categories of wheeled and plush toys as original study<br>
        • <strong>Procedure:</strong> Present both toy types simultaneously in familiar enclosure; record interaction time using behavioural checklist; video record all sessions; two independent observers code behaviour<br>
        • <strong>Controls:</strong> Same procedure for all participants; counterbalance toy positions; standardised duration (30 minutes per session across 5 sessions)<br><br>
        
        <strong>Expected outcomes if reliable:</strong><br>
        Male chimpanzees should show significantly greater preference for wheeled toys compared to females (p &lt; .05), replicating the rhesus monkey pattern.<br><br>
        
        <strong>How this tests reliability:</strong><br>
        If results match original study despite different species (chimpanzees vs monkeys) and setting (sanctuary vs lab), this demonstrates <strong>external reliability</strong> (findings generalise). Using identical measures and procedures tests <strong>internal reliability</strong> (consistency of measurement). <em>(AO2/AO3: 10 marks)</em>
      </div>
    </div>
  </div>

</main>

  <!-- RIGHT: NOTES PANEL (3rd column) -->
  <aside class="notes-col" id="notesPanel">
    <div class="nc-header">
      <span class="nc-title">📝 Notes 笔记</span>
      <span class="nc-count" id="noteCount">0</span>
    </div>
    <div class="nc-body" id="notesBody">
      <div class="nc-empty" id="notesEmpty">✏️ Select text in any section,<br>then click "Add Note"<br><br>选择任意文本后点击下方按钮</div>
    </div>
    <div class="nc-input-row" id="noteInputRow">
      <textarea class="nc-textarea" id="noteTextarea" placeholder="Write your note here... 在此输入笔记..."></textarea>
      <div class="nc-actions">
        <button class="nc-btn-save" onclick="saveNote()">💾 Save 保存</button>
        <button class="nc-btn-cancel" onclick="cancelNoteInput()">Cancel 取消</button>
      </div>
    </div>
    <button class="nc-add-btn" onclick="showNoteInput()">✏️ Add Note 添加笔记</button>
    <div class="nc-footer">
      <button onclick="exportNotes()">📤 Export</button>
      <button onclick="clearAllNotes()">🗑️ Clear All</button>
    </div>
  </aside>

</div><!-- end page-layout -->

<!-- Footer -->
<footer class="footer-note">
  <p>Hassett et al. (2008) Courseware | CIE Psychology A Level | Core Study 2 | Generated based on CIE Textbook 基于教材原文生成</p>
  <p>© 2026 Psychology Courseware Project | 🐵 Biological Approach</p>
</footer>

</div><!-- end container -->

<!-- Study Navigator -->
<nav class="study-nav">
  <div class="study-nav-inner">
    <a href="../milgram/index.html" class="study-nav-btn">◀ Milgram</a>
    <div class="study-nav-dots">
      <div class="study-nav-label">Progress 进度</div>
      <div class="study-dot-row" id="studyDots"></div>
    </div>
    <a href="#" class="study-nav-btn" style="opacity:.5">Next ▶</a>
  </div>
</nav>

<!-- Back to Top Button -->
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">▲</button>

<script>
(function(){
  'use strict';

  // ===== CONFIGURATION =====
  const STUDY_NAME = 'hassett';
  const STORAGE_KEYS = {
    darkMode: STUDY_NAME + '-darkMode',
    fontSize: STUDY_NAME + '-fontSize',
    notes: STUDY_NAME + '_notes_v3'
  };

  // ===== STATE =====
  let notes = [];
  let selectedText = '';
  let selectedHlId = null;

  // ===== INITIALIZATION =====
  function init() {
    loadDarkMode();
    loadFontSize();
    loadNotes();
    renderNotes();
    setupScrollSpy();
    setupProgressBar();
    setupBackToTop();
    setupStudyDots();
    setupTextSelection();
    console.log('✅ Hassett v5.0 initialized — Milgram template architecture');
  }

  // ===== DARK MODE =====
  function loadDarkMode() {
    const isDark = localStorage.getItem(STORAGE_KEYS.darkMode) === 'true';
    if(isDark) document.body.classList.add('dark');
    updateDarkBtn();
  }
  function toggleDarkMode() {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    localStorage.setItem(STORAGE_KEYS.darkMode, isDark);
    updateDarkBtn();
  }
  function updateDarkBtn() {
    const btn = document.getElementById('darkBtn');
    if(btn) btn.textContent = document.body.classList.contains('dark') ? '☀️ Light' : '🌙 Dark';
  }
  window.toggleDarkMode = toggleDarkMode;

  // ===== FONT SIZE =====
  function loadFontSize() {
    const size = localStorage.getItem(STORAGE_KEYS.fontSize);
    if(size) document.documentElement.style.fontSize = size + 'px';
  }
  function adjustFontSize(delta) {
    const current = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const newSize = Math.max(12, Math.min(24, current + delta * 2));
    document.documentElement.style.fontSize = newSize + 'px';
    localStorage.setItem(STORAGE_KEYS.fontSize, newSize);
  }
  window.adjustFontSize = adjustFontSize;

  // ===== SCROLL SPY =====
  function setupScrollSpy() {
    const sections = document.querySelectorAll('.section[id^="s"]');
    const navLinks = document.querySelectorAll('.sb-item a');
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(link => {
            link.classList.remove('sb-active');
            if(link.getAttribute('href') === '#' + id) link.classList.add('sb-active');
          });
        }
      });
    }, { rootMargin: '-80px 0px -60% 0px', threshold: 0 });
    
    sections.forEach(s => observer.observe(s));
  }

  // ===== PROGRESS BAR =====
  function setupProgressBar() {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      document.getElementById('progressBar').style.width = progress + '%';
    }, { passive: true });
  }

  // ===== BACK TO TOP =====
  function setupBackToTop() {
    const btn = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
      if(window.scrollY > 400) btn.classList.add('show');
      else btn.classList.remove('show');
    }, { passive: true });
  }

  // ===== STUDY DOTS =====
  function setupStudyDots() {
    const container = document.getElementById('studyDots');
    if(!container) return;
    const sections = document.querySelectorAll('.section[id^="s"]');
    sections.forEach((s, i) => {
      const dot = document.createElement('div');
      dot.className = 'study-dot';
      dot.title = s.querySelector('h2')?.textContent || `Section ${i+1}`;
      dot.onclick = () => s.scrollIntoView({ behavior: 'smooth', block: 'start' });
      container.appendChild(dot);
    });
    
    const dotObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const dots = container.querySelectorAll('.study-dot');
        const index = Array.from(sections).indexOf(entry.target);
        if(index >= 0 && entry.isIntersecting) {
          dots.forEach(d => d.classList.remove('active'));
          if(dots[index]) dots[index].classList.add('active');
        }
      });
    }, { rootMargin: '-80px 0px -60% 0px' });
    
    sections.forEach(s => dotObserver.observe(s));
  }

  // ===== TEXT SELECTION FOR NOTES =====
  function setupTextSelection() {
    document.addEventListener('mouseup', (e) => {
      // Don't trigger if clicking inside notes panel
      if(e.target.closest('.notes-col')) return;
      
      setTimeout(() => {
        const selection = window.getSelection();
        const text = selection.toString().trim();
        if(text.length > 1) {
          selectedText = text;
          selectedHlId = 'hl_' + Date.now();
        } else {
          selectedText = '';
          selectedHlId = null;
        }
      }, 10);
    });
  }

  // ===== NOTES SYSTEM v3.0 =====
  function loadNotes() {
    try {
      const stored = localStorage.getItem(STORAGE_KEYS.notes);
      notes = stored ? JSON.parse(stored) : [];
    } catch(e) {
      console.warn('Failed to load notes:', e);
      notes = [];
    }
  }
  
  function saveNotes() {
    try {
      localStorage.setItem(STORAGE_KEYS.notes, JSON.stringify(notes));
    } catch(e) {
      console.warn('Failed to save notes:', e);
    }
  }
  
  function renderNotes() {
    const body = document.getElementById('notesBody');
    const empty = document.getElementById('notesEmpty');
    const count = document.getElementById('noteCount');
    
    if(!body) return;
    
    count.textContent = notes.length;
    
    if(notes.length === 0) {
      body.innerHTML = '<div class="nc-empty" id="notesEmpty">✏️ Select text in any section,<br>then click "Add Note"<br><br>选择任意文本后点击下方按钮</div>';
      return;
    }
    
    body.innerHTML = notes.map((note, i) => `
      <div class="note-card" ondblclick="scrollToHl('${note.hlId}')">
        <button class="note-card-del" onclick="deleteNote(${i}); event.stopPropagation();">✕</button>
        ${note.hlText ? `<div class="note-card-hl">${escapeHtml(note.hlText)}</div>` : ''}
        <div class="note-card-text">${escapeHtml(note.text)}</div>
        <div style="font-size:.65em;color:#9ca3af;margin-top:4px;">${note.time} · ${note.section || ''}</div>
      </div>
    `).join('');
  }
  
  function showNoteInput() {
    if(!selectedText) {
      alert('Please select some text first.\n请先选择一些文本。');
      return;
    }
    const row = document.getElementById('noteInputRow');
    const textarea = document.getElementById('noteTextarea');
    row.classList.add('show');
    textarea.value = '';
    textarea.placeholder = `Note for: "${selectedText.substring(0, 50)}${selectedText.length > 50 ? '...' : ''}"`;
    textarea.focus();
  }
  window.showNoteInput = showNoteInput;
  
  function saveNote() {
    const textarea = document.getElementById('noteTextarea');
    const text = textarea.value.trim();
    if(!text) {
      alert('Please enter note content.\n请输入笔记内容。');
      return;
    }
    
    // Apply highlight to selected text
    applyHighlight(selectedHlId, selectedText);
    
    // Create note object
    const note = {
      id: Date.now(),
      hlId: selectedHlId,
      hlText: selectedText,
      text: text,
      time: new Date().toLocaleString(),
      section: getCurrentSectionName()
    };
    
    notes.push(note);
    saveNotes();
    renderNotes();
    cancelNoteInput();
    
    // Reset selection
    selectedText = '';
    selectedHlId = null;
    window.getSelection().removeAllRanges();
  }
  window.saveNote = saveNote;
  
  function cancelNoteInput() {
    const row = document.getElementById('noteInputRow');
    row.classList.remove('show');
    
    // CRITICAL: Remove highlight mark if user cancels
    if(selectedHlId) {
      removeHighlightMark(selectedHlId);
    }
    
    selectedText = '';
    selectedHlId = null;
  }
  window.cancelNoteInput = cancelNoteInput;
  
  function deleteNote(index) {
    if(!confirm('Delete this note? 删除这条笔记？')) return;
    
    const note = notes[index];
    if(note && note.hlId) {
      removeHighlightMark(note.hlId);
    }
    
    notes.splice(index, 1);
    saveNotes();
    renderNotes();
  }
  window.deleteNote = deleteNote;
  
  function clearAllNotes() {
    if(!confirm('Delete ALL notes? 删除全部笔记？')) return;
    
    // Remove all highlights
    notes.forEach(note => {
      if(note.hlId) removeHighlightMark(note.hlId);
    });
    
    notes = [];
    saveNotes();
    renderNotes();
  }
  window.clearAllNotes = clearAllNotes;
  
  function exportNotes() {
    if(notes.length === 0) {
      alert('No notes to export. 没有笔记可导出。');
      return;
    }
    
    let output = `# Hassett (2008) - Study Notes\nExported: ${new Date().toLocaleString()}\n${'='.repeat(50)}\n\n`;
    notes.forEach((note, i) => {
      output += `## Note ${i+1}\n`;
      output += `- **Section:** ${note.section || 'Unknown'}\n`;
      output += `- **Time:** ${note.time}\n`;
      if(note.hlText) output += `- **Highlighted:** "${note.hlText}"\n`;
      output += `- **Note:** ${note.text}\n\n`;
    });
    
    const blob = new Blob([output], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'hassett_notes.md';
    a.click();
    URL.revokeObjectURL(url);
  }
  window.exportNotes = exportNotes;
  
  function scrollToHl(hlId) {
    const mark = document.getElementById(hlId);
    if(mark) {
      mark.scrollIntoView({ behavior: 'smooth', block: 'center' });
      mark.style.animation = 'none';
      void mark.offsetWidth; // Trigger reflow
      mark.style.animation = 'pulse-highlight 1s ease 3';
    }
  }
  window.scrollToHl = scrollToHl;

  // ===== HIGHLIGHT FUNCTIONS =====
  function applyHighlight(hlId, text) {
    if(!hlId || !text) return;
    
    const selection = window.getSelection();
    if(!selection.rangeCount) return;
    
    const range = selection.getRangeAt(0);
    const mark = document.createElement('mark');
    mark.id = hlId;
    mark.className = 'hl-text';
    mark.setAttribute('data-hl-id', hlId);
    
    try {
      range.surroundContents(mark);
    } catch(e) {
      // If range crosses element boundaries, fallback
      const span = document.createElement('span');
      span.className = 'hl-text';
      span.id = hlId;
      span.setAttribute('data-hl-id', hlId);
      range.insertNode(span);
    }
  }
  
  function removeHighlightMark(hlId) {
    if(!hlId) return;
    
    const mark = document.getElementById(hlId);
    if(!mark) return;
    
    // Replace the mark with its contents (preserving text)
    const parent = mark.parentNode;
    while(mark.firstChild) {
      parent.insertBefore(mark.firstChild, mark);
    }
    parent.removeChild(mark);
  }

  // ===== UTILITY FUNCTIONS =====
  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
  
  function getCurrentSectionName() {
    const sections = document.querySelectorAll('.section[id^="s"]');
    for(const section of sections) {
      const rect = section.getBoundingClientRect();
      if(rect.top <= 150 && rect.bottom >= 150) {
        return section.querySelector('h2')?.textContent?.trim() || 'Unknown';
      }
    }
    return 'Unknown';
  }

  // ===== CHINESE SUMMARY TOGGLE =====
  window.toggleCnSummary = function(btn) {
    btn.classList.toggle('open');
    const body = btn.nextElementSibling;
    if(body) body.classList.toggle('open');
  };

  // ===== EXAM KEY POINTS TOGGLE =====
  window.toggleSummary = function(id) {
    const card = document.getElementById(id);
    if(card) card.classList.toggle('open');
  };

  // ===== Q&A CARD TOGGLE =====
  window.toggleQA = function(id) {
    const card = document.getElementById(id);
    if(card) card.classList.toggle('open');
  };

  // Add pulse animation for highlights
  const style = document.createElement('style');
  style.textContent = `
    @keyframes pulse-highlight {
      0%, 100% { background: linear-gradient(120deg,#fef08a,#fde047); transform: scale(1); }
      50% { background: linear-gradient(120deg,#facc15,#eab308); transform: scale(1.05); }
    }
  `;
  document.head.appendChild(style);

  // ===== RUN INITIALIZATION =====
  if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
</script>
</body>
</html>''';

with open('/Users/lawrenceliu/WorkBuddy/2026-07-11-09-28-56/gh-pages/cie/hassett/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Hassett v5.0 generated successfully!")
print(f"📄 File size: {len(html)} characters ({len(html)//1024} KB)")
