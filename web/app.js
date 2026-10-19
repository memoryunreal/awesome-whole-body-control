/* Paper Watch — deliberately buildless. All source text is rendered as text nodes. */
"use strict";

const app = document.querySelector("#app");
const state = {
  data: { papers: [], edges: [], runs: [] }, config: {}, health: {}, loaded: false,
  mode: "loading", loadError: "", busy: false, poll: null, toastTimer: null,
  filters: { papers: { query: "", status: "", category: "", page: 1 }, intake: { query: "", status: "", page: 1 } },
  graph: { seed: "", status: "", selection: "", view: { x: 0, y: 0, w: 1000, h: 610 } },
  focus: null, focusError: "", focusFilters: { deep: true, group: "", query: "" },
};
const labels = { library: "已有文献", pending: "待筛选", target: "目标论文", review: "待复核", excluded: "已排除", ready: "已生成", blocked: "等待条件", failed: "生成失败", running: "运行中", completed: "已完成", seed: "种子论文" };
const navItems = [
  ["overview", "研究概览", "grid"], ["focus", "移动操作精选", "branch"], ["intake", "论文收件箱", "inbox"], ["papers", "论文库", "book"],
  ["graph", "引用网络", "network"], ["reports", "深读报告", "document"], ["subscriptions", "订阅与设置", "sliders"],
];
const pageMeta = {
  overview: ["RESEARCH OVERVIEW", "研究概览", "从新的研究线索，到值得深入的下一篇论文。"],
  focus: ["HUMANOID LOCO-MANIPULATION", "人形全身移动操作精选", "从全库收敛到约 5% 的相关工作，再精读其中约 20%。"],
  intake: ["RESEARCH INTAKE", "论文收件箱", "汇集引用提醒与手动添加的论文，保留每一次筛选的依据。"],
  papers: ["PAPER LIBRARY", "论文库", "在已有文献与新收录的研究之间，找到你需要的知识。"],
  graph: ["CITATION NETWORK", "引用网络", "围绕种子论文追踪研究的延伸，每条引用都保留来源证据。"],
  reports: ["DEEP READING", "深读报告", "从研究问题、方法与实验，到与你的研究方向的联系。"],
  subscriptions: ["WORKSPACE SETTINGS", "订阅与设置", "管理研究范围与发现来源，让论文追踪成为日常工作的一部分。"],
};

function node(tag, attrs, ...children) {
  const element = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs || {})) {
    if (value === null || value === undefined || value === false) continue;
    if (key === "class") element.className = value;
    else if (key === "text") element.textContent = value;
    else if (key.startsWith("on") && typeof value === "function") element.addEventListener(key.slice(2).toLowerCase(), value);
    else if (key === "value") element.value = value;
    else if (value === true) element.setAttribute(key, "");
    else element.setAttribute(key, String(value));
  }
  for (const child of children.flat(Infinity)) {
    if (child !== null && child !== undefined && child !== false) element.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
  return element;
}

function svgNode(tag, attrs, ...children) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attrs || {})) element.setAttribute(key, String(value));
  for (const child of children.flat()) element.append(child instanceof Node ? child : document.createTextNode(String(child)));
  return element;
}

function icon(name, size = 17) {
  const paths = {
    grid: ["M3 3h7v7H3z", "M14 3h7v7h-7z", "M3 14h7v7H3z", "M14 14h7v7h-7z"],
    inbox: ["M4 4h16l2 10v6H2v-6z", "M2 14h6l2 3h4l2-3h6"],
    book: ["M3 4h7l2 2 2-2h7v16h-7l-2 1-2-1H3z", "M12 6v15"],
    network: ["M12 8v8", "M5 8l7 8 7-8", "M5 8h14"],
    document: ["M5 2h9l5 5v15H5z", "M14 2v6h5", "M8 12h8M8 16h8"],
    sliders: ["M4 7h5m4 0h7M4 17h9m4 0h3", "M9 4v6m4 4v6"],
    search: ["M21 21l-5-5"], arrow: ["M5 12h14m-5-5 5 5-5 5"],
    plus: ["M12 5v14M5 12h14"], refresh: ["M20 8a8 8 0 1 0 1 7M20 3v6h-6"],
    clock: ["M12 7v5l3 2"], check: ["m5 12 4 4L19 6"],
    external: ["M14 3h7v7M21 3 10 14", "M10 3H3v18h18v-7"],
    mail: ["M3 5h18v14H3z", "m3 5 9 7 9-7"], shield: ["m12 2 8 3v6c0 6-8 11-8 11S4 17 4 11V5z", "m8 11 3 3 5-6"],
    chevron: ["m9 6 6 6-6 6"], menu: ["M4 6h16M4 12h16M4 18h16"],
    download: ["M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"],
    minus: ["M5 12h14"], expand: ["M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"],
    branch: ["M6 6v12M18 6v2c0 4-12 4-12 8"], circle: [],
  };
  const el = svgNode("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", "stroke-width": 1.55, "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true" });
  (paths[name] || paths.document).forEach(d => el.append(svgNode("path", { d })));
  if (name === "search") el.append(svgNode("circle", { cx: 10.5, cy: 10.5, r: 6.5 }));
  if (name === "clock") el.append(svgNode("circle", { cx: 12, cy: 12, r: 9 }));
  if (name === "network") [[5, 6], [19, 6], [12, 18]].forEach(([cx, cy]) => el.append(svgNode("circle", { cx, cy, r: 3, fill: "currentColor", stroke: "none" })));
  return el;
}

function str(value, fallback = "") {
  if (value === null || value === undefined || value === "") return fallback;
  if (Array.isArray(value)) return value.map(item => str(item)).filter(Boolean).join(" · ");
  if (typeof value === "object") return value.name ? str(value.name) : JSON.stringify(value);
  return String(value);
}
function shorten(value, length = 100) { const text = str(value); return text.length > length ? `${text.slice(0, length)}…` : text; }
function count(value) { return Number(value || 0).toLocaleString("zh-CN"); }
function safeUrl(value) { try { const url = new URL(String(value)); return ["http:", "https:"].includes(url.protocol) ? url.href : null; } catch { return null; } }
function link(text, url, attrs = {}) { const safe = safeUrl(url); return safe ? node("a", { href: safe, target: "_blank", rel: "noopener noreferrer", ...attrs }, text) : node("span", attrs, text); }
function routeLink(text, route, attrs = {}) { return node("a", { href: `#/${route}`, ...attrs }, text); }
function dateTime(value, brief = false) {
  if (!value) return "尚未运行";
  const date = new Date(typeof value === "number" ? (value < 1e12 ? value * 1000 : value) : value);
  return Number.isNaN(date.getTime()) ? str(value) : date.toLocaleString("zh-CN", { month: "2-digit", day: "2-digit", ...(brief ? {} : { hour: "2-digit", minute: "2-digit", hour12: false }) });
}
function paperStatus(paper) { return paper.is_seed ? "seed" : (Object.hasOwn(labels, paper.status) ? paper.status : "library"); }
function pill(value, text) { const type = Object.hasOwn(labels, value) || value === "live" ? value : "library"; return node("span", { class: `pill ${type}` }, text || labels[value] || value); }
function button(text, handler, attrs = {}) { return node("button", { type: "button", class: "button", onclick: handler, ...attrs }, text); }
function actionLink(text, path, primary = false, symbol = "arrow") { return routeLink([text, icon(symbol, 14)], path, { class: `button${primary ? " primary" : ""}` }); }
function empty(title, text, symbol = "inbox", compact = false, action = null) { return node("div", { class: `empty${compact ? " compact" : ""}` }, node("div", { class: "empty-icon" }, icon(symbol, compact ? 20 : 25)), node("h3", {}, title), node("p", {}, text), action); }
function notice(text, tone = "") { return node("div", { class: `inline-note ${tone}` }, text); }
function sectionHead(title, right = null, symbol = null) { return node("div", { class: "section-head" }, node("div", { class: "section-label" }, symbol ? icon(symbol, 16) : null, node("h2", {}, title)), right); }
function screeningEvidence(item) {
  if (!item || typeof item !== "object") return node("li", {}, str(item));
  const fieldNames = { title: "标题", abstract: "摘要", summary: "研究笔记" };
  const keyword = item.term || item.keyword;
  return node("li", {}, node("div", { class: "screening-evidence-head" },
    node("strong", {}, keyword || "匹配依据"),
    item.field ? node("span", { class: "muted" }, `来源：${fieldNames[item.field] || str(item.field)}`) : null,
    item.polarity === "negative" ? pill("excluded", "排除词") : item.priority ? pill("target", "重点词") : null),
  node("p", { class: "screening-evidence-excerpt" }, item.excerpt || item.quote || item.text || "未提供原文摘录。"));
}
function smallLink(text, route) { return routeLink([text, icon("arrow", 13)], route, { class: "text-link" }); }
function toast(text) { const el = document.querySelector("#toast"); el.textContent = text; el.classList.add("show"); clearTimeout(state.toastTimer); state.toastTimer = setTimeout(() => el.classList.remove("show"), 5000); }
function papers() { return Array.isArray(state.data.papers) ? state.data.papers : []; }
function regularPapers() { return papers().filter(p => !p.is_seed); }
function candidates() { return regularPapers().filter(p => p.status && p.status !== "library"); }
function isReportReady(paper) { return paper.report?.status === "ready" && !paper.report.stale && Boolean(str(paper.report.markdown).trim()); }
function reports() { return papers().filter(isReportReady).sort((a, b) => (a.report.priority ?? 100) - (b.report.priority ?? 100)); }
function reportPill(paper) { return paper.report?.stale ? pill("blocked", "报告需重新生成") : paper.report?.status ? pill(paper.report.status, paper.report.status === "ready" ? "深读报告" : labels[paper.report.status]) : null; }
function seeds() {
  const found = papers().filter(p => p.is_seed);
  const used = new Set(found.map(p => p.id));
  for (const seed of state.config.seeds || []) {
    const existing = papers().find(p => p.id === seed.id || (seed.arxiv_id && p.arxiv_id === seed.arxiv_id));
    const entry = existing ? { ...seed, ...existing, is_seed: true } : { ...seed, is_seed: true };
    if (!used.has(entry.id)) { found.push(entry); used.add(entry.id); }
  }
  return found;
}
function seedName(seed) {
  const configured = (state.config.seeds || []).find(s => s.id === seed.id || (s.arxiv_id && s.arxiv_id === seed.arxiv_id));
  return str(configured?.aliases?.[0] || seed.aliases?.[0] || seed.short_name || str(seed.title).split(":")[0] || seed.id);
}
function byId(id) { return papers().find(p => p.id === id) || seeds().find(p => p.id === id); }
function validEdges() { const ids = new Set([...papers(), ...seeds()].map(p => p.id)); return (state.data.edges || []).filter(e => e.kind === "cites" && ids.has(e.source) && ids.has(e.target)); }
function latestRun() { return (state.data.runs || []).slice().sort((a, b) => str(b.started_at || b.created_at).localeCompare(str(a.started_at || a.created_at)))[0]; }
function lastRunTime() { const run = latestRun(); return dateTime(run?.finished_at || run?.started_at || run?.created_at || state.data.last_run_at); }
function runErrors(value) { return Array.isArray(value) ? value.map(item => typeof item === "object" ? `${item.source ? `${item.source}：` : ""}${item.message || item.error || str(item)}` : str(item)).join("；") : str(value); }
function route() {
  const [name, ...ids] = location.hash.replace(/^#\/?/, "").split("/");
  let id = ""; try { id = decodeURIComponent(ids.join("/")); } catch { /* malformed hash is handled by the missing-record view */ }
  return { name: ["paper", "report", ...navItems.map(n => n[0])].includes(name) ? name : "overview", id };
}
function canMutate() { return state.mode === "live" && !state.busy; }
function publicLibrary() { return state.mode === "static" && Boolean(state.config.publication); }
function healthFlag(...keys) { for (const key of keys) { if (state.health[key] !== undefined) return Boolean(state.health[key]); } return null; }
function llmStatus() {
  const flag = healthFlag("llm_configured", "openai_configured", "has_openai_key", "model_configured");
  if (flag === true) return "已配置";
  if (flag === false) return "尚未配置密钥";
  if (state.health.llm && typeof state.health.llm === "object") return state.health.llm.configured ? "已配置" : "尚未配置密钥";
  return state.mode === "live" ? "状态未提供" : "静态快照 · 无法检测";
}
function runButton(compact = false) {
  return button([icon(state.busy ? "clock" : "refresh", 14), publicLibrary() ? "每周自动更新" : state.busy ? "正在同步…" : "立即同步"], startRun, { class: `button${compact ? " small-button" : ""}`, disabled: !canMutate(), title: publicLibrary() ? "公开站点展示已发布快照；每周统计和主分支更新后自动发布" : state.mode !== "live" ? "静态快照不支持同步，请启动本地服务" : "抓取新论文、筛选并生成深读报告" });
}

async function fetchJSON(path, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 15000);
  try {
    const response = await fetch(path, { cache: "no-store", signal: controller.signal, ...options });
    if (!response.ok) { let detail = ""; try { detail = str((await response.json()).error); } catch {} throw new Error(detail || `请求失败 (${response.status})`); }
    return await response.json();
  } finally { clearTimeout(timer); }
}

async function loadData(initial = false) {
  if (initial) render();
  try {
    const data = await fetchJSON("/api/state");
    if (!Array.isArray(data.papers)) throw new Error("论文数据格式不完整");
    state.data = data; state.config = data.config || {}; state.mode = "live"; state.loadError = "";
    const results = await Promise.allSettled([fetchJSON("/api/config"), fetchJSON("/api/health")]);
    if (results[0].status === "fulfilled") state.config = results[0].value;
    if (results[1].status === "fulfilled") {
      state.health = results[1].value;
      state.busy = Boolean(state.health.busy || state.health.running || state.health.run_in_progress);
    } else {
      state.mode = "readonly";
      state.loadError = "服务状态暂不可用，操作已暂时停用。";
    }
  } catch (error) {
    try {
      const data = await fetchJSON("./data/state.json");
      if (!Array.isArray(data.papers)) throw new Error("论文快照格式不完整");
      state.data = data; state.config = data.config || {}; state.mode = "static"; state.busy = false; state.loadError = "";
    } catch (fallbackError) {
      state.mode = state.loaded ? "readonly" : "error";
      state.loadError = `暂时无法读取论文数据：${fallbackError.message || error.message}`;
      state.busy = false;
    }
  }
  try { state.focus = await fetchJSON("./focus.json"); state.focusError = ""; }
  catch { state.focus = null; state.focusError = "精选清单暂时无法读取，请稍后重新加载。"; }
  state.loaded = true;
  render();
  if (state.busy) schedulePoll(); else clearTimeout(state.poll);
}

function schedulePoll() { clearTimeout(state.poll); state.poll = setTimeout(() => loadData(), 3500); }
async function startRun() {
  if (!canMutate()) return;
  state.busy = true; render();
  try {
    await fetchJSON("/api/run", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
    toast("同步已开始。新的发现、筛选结果和报告会自动更新。"); schedulePoll();
  } catch (error) { state.busy = false; render(); toast(`同步未启动：${error.message}`); }
}

function shell(content, selected) {
  const active = selected === "paper" ? "papers" : selected === "report" ? "reports" : selected;
  const pending = candidates().filter(p => ["pending", "review"].includes(p.status)).length;
  const sidebar = node("aside", { class: "sidebar", "aria-label": "主导航" },
    routeLink([node("div", { class: "brand-mark" }, icon("network", 23)), node("div", {}, node("div", { class: "brand-title" }, "Paper Watch"), node("div", { class: "brand-subtitle" }, "RESEARCH WORKSPACE"))], "overview", { class: "brand", "aria-label": "Paper Watch 研究概览" }),
    node("div", { class: "nav-caption" }, "WORKSPACE"),
    node("nav", { class: "nav" }, navItems.map(([id, text, glyph]) => routeLink([icon(glyph, 17), text, id === "intake" && pending ? node("span", { class: "nav-count" }, count(pending)) : null], id, { class: `nav-link${active === id ? " active" : ""}`, "aria-current": active === id ? "page" : null }))),
    node("div", { class: "sidebar-bottom" }, node("div", { class: "sidebar-note" }, node("h3", {}, icon("branch", 15), "持续追踪研究脉络"), node("p", {}, "从引用开始发现线索，", node("br"), "用证据连接新的研究。")), node("div", { class: "sidebar-footer" }, node("span", { class: `status-dot${state.mode === "live" ? "" : " offline"}` }), publicLibrary() ? "每周更新 · 公开论文库" : state.mode === "live" ? "本地研究服务已连接" : state.mode === "loading" ? "正在连接研究数据" : "论文快照 · 只读模式")),
    button(icon("menu", 19), event => { sidebar.classList.toggle("open"); event.currentTarget.setAttribute("aria-expanded", sidebar.classList.contains("open")); }, { class: "mobile-toggle", "aria-label": "展开导航", "aria-expanded": "false" }),
  );
  const search = node("input", { type: "search", placeholder: "搜索论文、作者、关键词", "aria-label": "全局搜索论文", onkeydown: event => { if (event.key === "Enter") { state.filters.papers.query = event.target.value; state.filters.papers.page = 1; if (route().name === "papers") render(); else location.hash = "/papers"; } } });
  const topbar = node("header", { class: "topbar" }, node("div", { class: "breadcrumb" }, "工作空间", icon("chevron", 11), node("strong", {}, pageMeta[active]?.[1] || "研究概览")), node("div", { class: "topbar-tools" }, node("label", { class: "top-search" }, icon("search", 15), search, node("span", { class: "key-hint", "aria-hidden": "true" }, "↵")), node("div", { class: "topbar-date" }, new Date().toLocaleDateString("zh-CN", { year: "numeric", month: "long", day: "numeric" }))));
  const main = node("main", { id: "main", class: "main", tabindex: "-1" },
    state.loadError ? node("div", { class: "alert-banner", role: "alert" }, state.loadError) : null,
    state.loaded && ["static", "readonly"].includes(state.mode) && selected !== "subscriptions" ? node("div", { class: "alert-banner" }, publicLibrary() ? "公开论文库每周自动更新。无需账号或 API 密钥即可搜索论文、浏览引用网络和已发布报告；此站点为只读快照。" : state.mode === "static" ? "当前为静态论文快照。搜索、图谱与报告可正常浏览；新增论文和同步需启动本地服务。" : "当前为只读状态，连接恢复后可继续新增论文和同步。") : null,
    content,
    node("footer", { class: "page-footer" }, node("span", {}, "PAPER WATCH　/　A LIVING RESEARCH LIBRARY"), node("span", {}, `数据来自论文库与已验证引用 · 最近运行 ${lastRunTime()}`)),
  );
  return node("div", { class: "shell" }, sidebar, node("div", { class: "main-shell" }, topbar, main));
}

function pageHead(name, actions = null, customTitle = null, description = null) {
  const meta = pageMeta[name];
  return node("header", { class: "page-head" }, node("div", {}, node("div", { class: "eyebrow" }, meta[0]), node("h1", {}, customTitle || meta[1]), node("p", { class: "page-description" }, description || meta[2])), actions ? node("div", { class: "head-actions" }, actions) : null);
}
function metric(label, number, detail, symbol, detailGreen = false) { return node("div", { class: "metric" }, node("div", { class: "metric-top" }, node("span", { class: "metric-label" }, label), node("div", { class: "metric-icon" }, icon(symbol, 15))), node("div", { class: "metric-number" }, count(number)), node("div", { class: "metric-bottom" }, detailGreen ? icon("check", 11) : null, node("span", { class: detailGreen ? "green" : "" }, detail))); }
function paperTags(paper) { return node("div", { class: "tags" }, focusEntries().some(e => e.paper.id === paper.id) ? routeLink("移动操作精选", "focus", { class: "pill focus-tag" }) : null, pill(paperStatus(paper)), reportPill(paper), (paper.seed_ids || []).map(id => { const seed = seeds().find(s => s.id === id); return seed ? pill("seed", seedName(seed)) : null; })); }
function paperRow(paper) {
  return node("article", { class: "paper-row" }, node("div", { class: "paper-row-top" }, routeLink(paper.title || "未命名论文", `paper/${encodeURIComponent(paper.id)}`, { class: "paper-title" }), paper.year ? node("span", { class: "pill" }, paper.year) : null),
    node("div", { class: "paper-meta" }, shorten(paper.authors, 92) || "作者待补充", paper.category ? ` · ${paper.category}` : ""),
    paper.summary || paper.abstract ? node("p", { class: "paper-summary" }, paper.summary || paper.abstract) : null, paperTags(paper));
}

function overviewPage() {
  const all = regularPapers(), incoming = candidates(), target = incoming.filter(p => p.status === "target"), ready = reports(), waiting = incoming.filter(p => ["review", "pending"].includes(p.status));
  const latest = [...incoming].reverse().slice(0, 3);
  const metrics = node("div", { class: "metrics" }, metric("论文库", all.length, "持续积累的研究文献", "book"), metric("目标论文", target.length, "自动筛选后的研究线索", "check", true), metric("待复核", waiting.length, "保留不确定项，等待进一步判断", "inbox"), metric("深读报告", ready.length, "基于原文生成的研究分析", "document"));
  const workflow = node("section", { class: "panel workflow-hero" }, node("div", { class: "hero-label" }, "FROM SIGNALS TO INSIGHTS"), node("h2", {}, "让每一篇新论文，", node("br"), "找到它的位置。"), node("p", {}, publicLibrary() ? "每周汇总研究进展，持续整理文献与引用关系，" : "订阅种子论文的引用动态，自动筛选研究相关性，", node("br"), "让值得关注的工作进入你的研究网络。"), node("div", { class: "workflow" }, ["发现新论文", "相关性筛选", "生成深读", "连接图谱"].map((text, i) => node("div", { class: "workflow-step" }, node("div", { class: "workflow-num" }, `0${i + 1}`), node("span", {}, text), i < 3 ? node("div", { class: "workflow-line" }) : null))));
  const recent = node("section", { class: "panel panel-pad" }, sectionHead("最新研究线索", smallLink("全部收件箱", "intake"), "inbox"), latest.length ? latest.map(paperRow) : empty("新的研究线索，即将从这里开始", publicLibrary() ? "每周统计中的新论文会随站点更新发布，并保留筛选结果与来源。" : "配置引用提醒或运行一次发现任务后，新论文会进入收件箱，并显示筛选结果与来源。", "inbox", false, actionLink(publicLibrary() ? "浏览论文库" : "设置发现来源", publicLibrary() ? "papers" : "subscriptions")));
  const seedCards = seeds().map(seed => node("div", { class: "seed-card" }, node("div", { class: "seed-symbol", "aria-hidden": "true" }, seedName(seed).slice(0, 1)), node("div", { class: "seed-copy" }, routeLink(node("h3", {}, seedName(seed)), `graph`, { onclick: () => { state.graph.seed = seed.id; state.graph.selection = seed.id; } }), node("p", {}, seed.year || (seed.arxiv_id ? `arXiv ${seed.arxiv_id}` : "引用追踪已定义"))), node("div", { class: "seed-count" }, count(validEdges().filter(e => e.target === seed.id).length), node("small", {}, "已收录引用"))));
  const seedPanel = node("section", { class: "panel panel-pad" }, sectionHead("追踪中的种子论文", smallLink("引用网络", "graph"), "network"), node("div", { class: "seed-list" }, seedCards.length ? seedCards : empty("还没有种子论文", "在配置中添加需要追踪引用的论文。", "network", true)), node("div", { class: "card-foot" }, icon("shield", 13), "仅计入已经核实来源的引用关系"));
  const statusPanel = node("section", { class: "panel panel-pad" }, sectionHead("工作流状态", runButton(true), "clock"), node("div", { class: "mini-stats" }, [[incoming.length, "发现论文"], [target.length, "确认目标"], [ready.length, "完成深读"]].map(([n, label]) => node("div", {}, node("div", { class: "mini-stat-number" }, count(n)), node("div", { class: "mini-stat-label" }, label)))),
    node("div", { class: "pipeline-status" }, node("span", { class: "muted" }, "最近一次运行"), node("strong", {}, lastRunTime())),
    node("div", { class: "pipeline-status" }, node("span", { class: "muted" }, publicLibrary() ? "更新周期" : "原文分析模型"), node("strong", {}, publicLibrary() ? "每周统计后发布" : llmStatus())),
    node("div", { class: "pipeline-status" }, node("span", { class: "muted" }, "发现方式"), node("strong", {}, publicLibrary() ? "每周文献统计 / 引用检索" : state.config.discovery?.semantic_scholar === false ? "邮件 / 手动导入" : "引用检索 / 邮件导入")),
    state.busy ? notice("正在获取与处理论文，页面会自动更新。") : !ready.length ? notice(publicLibrary() ? "当前快照尚无已完成的深读报告；后续完成的报告会随站点更新发布。浏览论文与引用网络无需配置密钥。" : "深读需要可获取的论文原文与模型密钥。条件不足时会保留等待状态。") : null);
  const library = [...all].slice(0, 3);
  const libraryPanel = node("section", { class: "panel panel-pad" }, sectionHead("已有论文库", smallLink(`浏览 ${count(all.length)} 篇文献`, "papers"), "book"), library.length ? library.map(paperRow) : empty("论文库尚为空", "导入已有文献后，可在这里统一检索和阅读。", "book", true));
  return [pageHead("overview", [runButton(), publicLibrary() ? actionLink("浏览论文库", "papers", true, "book") : actionLink("添加论文", "intake", true, "plus")]), focusOverview(), metrics, node("div", { class: "overview-grid" }, node("div", { class: "stack" }, workflow, recent, libraryPanel), node("div", { class: "stack" }, seedPanel, statusPanel, latestRunErrors()))];
}

function focusEntries() {
  return (state.focus?.entries || []).map(entry => {
    const paper = byId(entry.paper_id) || papers().find(p => p.arxiv_id === entry.arxiv_id || str(p.paper_url).endsWith(`/abs/${entry.arxiv_id}`));
    return paper ? { ...entry, paper } : null;
  }).filter(Boolean).sort((a, b) => a.rank - b.rank);
}
function focusOverview() {
  if (!state.focus) return null;
  const entries = focusEntries(), deep = entries.filter(e => e.deep_read);
  return node("section", { class: "panel focus-overview" }, node("div", {}, node("div", { class: "eyebrow" }, "YOUR RESEARCH SHORTLIST"), node("h2", {}, "少读一些，读得更相关。"), node("p", {}, `${entries.length} 篇人形全身移动操作精选 · ${deep.filter(e => isReportReady(e.paper)).length}/${deep.length} 篇精读已就绪`)), actionLink("进入移动操作精选", "focus", true, "arrow"));
}
function focusPage() {
  if (!state.focus) return [pageHead("focus"), node("section", { class: "panel panel-pad" }, notice(state.focusError || "精选清单尚未发布。", "warning"))];
  const catalog = state.focus, entries = focusEntries(), deep = entries.filter(e => e.deep_read), ready = deep.filter(e => isReportReady(e.paper));
  const share = papers().length ? (100 * entries.length / papers().length).toFixed(2) : "0";
  const readingShare = entries.length ? (100 * deep.length / entries.length).toFixed(1) : "0";
  const filters = state.focusFilters, groupName = id => catalog.groups.find(group => group.id === id)?.name || id;
  const change = patch => { Object.assign(filters, patch); render(); };
  const metrics = node("div", { class: "metrics focus-metrics" }, metric("完整论文库", papers().length, "按去重后的公开论文计数", "book"), metric("相关精选", entries.length, `占当前全库 ${share}% · 目标约 5%`, "branch"), metric("精读已更新", ready.length, `计划 ${deep.length} 篇 · 占精选 ${readingShare}%`, "document", ready.length === deep.length));
  const intro = node("section", { class: "panel panel-pad focus-intro" }, node("h2", {}, "先理解控制接口，再看视觉自主与数据。"), node("p", { class: "small muted" }, catalog.description), node("div", { class: "focus-path" }, ["HOMIE · 控制与示教", "FALCON / ULC · 外力与协调", "VIRAL / WholeBodyVLA · 视觉闭环", "GRAIL / OpenHLM · 数据与系统"].map(text => node("span", {}, text))), node("p", { class: "small muted" }, `核查更新：${catalog.reviewed_on}。先读提要与证据，再按课题需要阅读原文；精读为 AI 辅助原文分析，未执行复现实验。`));
  const search = node("input", { type: "search", class: "focus-search", placeholder: "在精选中搜索，按回车确认", "aria-label": "搜索移动操作精选", value: filters.query, oninput: event => { filters.query = event.target.value; }, onkeydown: event => { if (event.key === "Enter") { event.preventDefault(); render(); } }, onsearch: event => change({ query: event.target.value }) });
  const select = node("select", { class: "select", "aria-label": "按精选主题筛选", onchange: event => change({ group: event.target.value }) }, node("option", { value: "" }, "全部主题"), catalog.groups.map(group => node("option", { value: group.id }, group.name)));
  select.value = filters.group;
  const tools = node("div", { class: "toolbar focus-toolbar" }, node("div", { class: "focus-tabs", role: "group", "aria-label": "选择阅读范围" }, button(`精读路线 ${deep.length}`, () => change({ deep: true }), { class: `button${filters.deep ? " primary" : ""}`, "aria-pressed": String(filters.deep) }), button(`精选清单 ${entries.length}`, () => change({ deep: false }), { class: `button${!filters.deep ? " primary" : ""}`, "aria-pressed": String(!filters.deep) })), select, node("label", { class: "search-field" }, icon("search", 15), search), filters.query || filters.group ? button("清除筛选", () => change({ query: "", group: "" }), { class: "button small-button" }) : null);
  const visible = entries.filter(e => (!filters.deep || e.deep_read) && (!filters.group || e.group === filters.group) && `${e.short_name} ${e.verified_title} ${e.reason} ${e.paper.report?.organization || ""}`.toLowerCase().includes(filters.query.trim().toLowerCase()));
  const cards = visible.map(entry => {
    const paper = entry.paper, reportReady = entry.deep_read && isReportReady(paper);
    return node("article", { class: `panel panel-pad focus-card${entry.deep_read ? " focus-deep" : ""}` }, node("div", { class: "focus-card-top" }, node("span", { class: "focus-rank" }, String(entry.rank).padStart(2, "0")), node("span", { class: "pill" }, groupName(entry.group)), node("span", { class: "pill" }, entry.tier === "支撑" ? "支撑工作" : "任务主线")), node("h2", {}, entry.short_name), node("p", { class: "small muted focus-title" }, entry.verified_title), node("p", { class: "paper-summary" }, entry.reason), entry.deep_read ? node("p", { class: "small muted" }, entry.reading_question || paper.report?.summary || "方法、实验与部署假设的结构化精读。") : null, node("div", { class: "focus-evidence" }, entry.deep_read ? reportReady ? "全文精读已更新" : "精读待完成" : "已核查摘要与身份 · 尚未精读", entry.evidence_note ? ` · ${entry.evidence_note}` : ""), node("div", { class: "detail-links" }, reportReady ? actionLink("阅读精读", `report/${encodeURIComponent(paper.id)}`, true, "document") : null, actionLink("论文详情", `paper/${encodeURIComponent(paper.id)}`), link(["原文", icon("external", 12)], entry.source_url, { class: "button small-button" })));
  });
  const criteria = node("details", { class: "panel panel-pad focus-criteria" }, node("summary", {}, "筛选口径与每周维护"), node("ul", {}, catalog.selection_rules.map(rule => node("li", {}, rule))), node("p", { class: "small muted" }, catalog.maintenance), node("h3", { class: "detail-label" }, "本轮未纳入的相关条目"), catalog.not_selected.map(item => node("p", { class: "small muted" }, node("strong", {}, `${item.name}：`), item.reason, item.source_url ? link(" 查看依据", item.source_url) : null)));
  const missing = catalog.entries.length - entries.length;
  return [pageHead("focus", actionLink("查看完整论文库", "papers", false, "book")), metrics, intro, tools, node("div", { class: "result-bar" }, node("span", {}, `${filters.deep ? "精读" : "精选"} · 显示 ${visible.length} 篇`), node("span", {}, "顺序体现阅读路径，非论文质量评分")), missing ? notice(`当前快照缺少 ${missing} 篇清单论文，等待文献同步。`, "warning") : null, cards.length ? node("div", { class: "report-grid focus-grid" }, cards) : node("section", { class: "panel panel-pad" }, empty("没有匹配的精选论文", "尝试清除主题或搜索条件。", "search", true)), criteria];
}

function latestRunErrors() {
  const run = [...(state.data.runs || [])].reverse().find(r => r.discovery_attempted || r.discovered > 0 || r.errors?.length) || latestRun();
  const errors = run?.errors || run?.error;
  if (!errors || (Array.isArray(errors) && !errors.length)) return null;
  return node("section", { class: "panel panel-pad" }, sectionHead("最近运行提醒", null, "clock"), node("p", { class: "small muted" }, "任务中的部分来源或步骤未完成，已成功获取的数据仍会保留。"), notice(runErrors(errors), "warning"));
}

function searchBar(key, update, withCategory = false) {
  const filter = state.filters[key];
  const field = node("input", { type: "search", placeholder: "搜索标题、作者、摘要或关键词…", "aria-label": "搜索论文", value: filter.query, oninput: event => { filter.query = event.target.value; filter.page = 1; update(); } });
  const bar = node("div", { class: "toolbar" }, node("label", { class: "search-field" }, icon("search", 16), field));
  if (withCategory) {
    const categories = [...new Set(regularPapers().map(p => p.category).filter(Boolean))].sort();
    const select = node("select", { class: "select", "aria-label": "按研究方向筛选", onchange: event => { filter.category = event.target.value; filter.page = 1; update(); } }, node("option", { value: "" }, "全部研究方向"), categories.map(c => node("option", { value: c }, c)));
    select.value = filter.category; bar.append(select);
  }
  bar.append(button([icon("refresh", 13), "重置"], () => { filter.query = ""; filter.status = ""; filter.category = ""; filter.page = 1; render(); }, { class: "button" }));
  return bar;
}
function matches(paper, filter) {
  return (!filter.status || (filter.status === "seed" ? paper.is_seed : !paper.is_seed && paper.status === filter.status)) && (!filter.category || paper.category === filter.category) && (!filter.query || [paper.title, paper.authors, paper.summary, paper.abstract, paper.category, paper.tags, paper.arxiv_id, paper.id].map(v => str(v)).join(" ").toLowerCase().includes(filter.query.toLowerCase().trim()));
}
function filterTabs(key, source, choices, update) {
  const wrap = node("div", { class: "filter-tabs", "aria-label": "按论文状态筛选" });
  for (const [value, label] of choices) {
    const total = source.filter(p => !value || (value === "seed" ? p.is_seed : !p.is_seed && p.status === value)).length;
    wrap.append(button([label, node("span", {}, count(total))], () => { state.filters[key].status = value; state.filters[key].page = 1; update(); [...wrap.children].forEach(b => b.setAttribute("aria-pressed", b.dataset.status === value ? "true" : "false")); }, { class: "filter-tab", "data-status": value, "aria-pressed": state.filters[key].status === value ? "true" : "false" }));
  }
  return wrap;
}
function pagination(filter, total, pageSize, update) {
  const pages = Math.max(1, Math.ceil(total / pageSize)); filter.page = Math.min(filter.page, pages);
  return node("div", { class: "pagination" }, node("span", {}, total ? `第 ${(filter.page - 1) * pageSize + 1}–${Math.min(filter.page * pageSize, total)} 篇，共 ${count(total)} 篇` : "暂无匹配论文"), node("div", { class: "pagination-actions" }, button("上一页", () => { filter.page--; update(); }, { class: "button small-button", disabled: filter.page <= 1, "aria-label": "上一页" }), node("span", { class: "pagination-current", "aria-live": "polite" }, `${filter.page} / ${pages}`), button("下一页", () => { filter.page++; update(); }, { class: "button small-button", disabled: filter.page >= pages, "aria-label": "下一页" })));
}

function libraryPage() {
  // Seed papers remain part of the searchable library, including historical imports.
  const source = papers(); const filter = state.filters.papers;
  const results = node("div", {});
  function update() {
    const filtered = source.filter(p => matches(p, filter)); const size = 20;
    filter.page = Math.min(filter.page, Math.max(1, Math.ceil(filtered.length / size)));
    const page = filtered.slice((filter.page - 1) * size, filter.page * size);
    const table = node("table", { class: "papers-table" }, node("thead", {}, node("tr", {}, ["论文 / 作者", "研究方向", "年份", "状态"].map(t => node("th", { scope: "col" }, t)))), node("tbody", {}, page.map(p => node("tr", {}, node("td", {}, routeLink(p.title || "未命名论文", `paper/${encodeURIComponent(p.id)}`, { class: "paper-title" }), node("div", { class: "paper-meta" }, shorten(p.authors, 120) || "作者待补充"), node("p", { class: "paper-summary" }, p.summary || p.abstract || "")), node("td", {}, node("span", { class: "category-label" }, p.category || "未分类")), node("td", { class: "muted" }, p.year || "—"), node("td", {}, pill(paperStatus(p)), isReportReady(p) ? node("div", { class: "tags" }, routeLink("阅读报告", `report/${encodeURIComponent(p.id)}`, { class: "text-link" })) : p.report?.stale ? node("div", { class: "tags" }, reportPill(p)) : null)))));
    results.replaceChildren(node("div", { class: "result-bar", "aria-live": "polite" }, node("span", {}, `找到 ${count(filtered.length)} 篇论文`), node("span", {}, "已有文献与新收录论文统一检索")), node("div", { class: "panel" }, page.length ? node("div", { class: "table-wrap" }, table) : empty("没有找到匹配的论文", "尝试更换关键词，或清除研究方向与状态筛选。", "search"), pagination(filter, filtered.length, size, update)));
  }
  update();
  return [pageHead("papers", publicLibrary() ? null : actionLink("添加论文", "intake", true, "plus")), searchBar("papers", update, true), filterTabs("papers", source, [["", "全部论文"], ["library", "已有文献"], ["target", "目标论文"], ["review", "待复核"], ["seed", "种子论文"]], update), results];
}

function intakePage() {
  const filter = state.filters.intake, source = candidates().slice().reverse(), results = node("div", {});
  const message = node("div", { class: "form-message", role: "status", "aria-live": "polite" });
  const input = node("input", { class: "input", type: "url", placeholder: "粘贴 arXiv 或论文页面链接", "aria-label": "论文链接", required: true, disabled: state.mode !== "live" });
  const submit = node("button", { type: "submit", class: "button primary", disabled: !canMutate() }, icon("plus", 14), "添加到收件箱");
  const form = node("form", { class: "intake-form", onsubmit: async event => {
    event.preventDefault(); if (!canMutate()) return;
    if (!safeUrl(input.value)) { message.textContent = "请输入以 http 或 https 开头的有效论文链接。"; message.classList.add("error"); return; }
    submit.disabled = true; message.classList.remove("error"); message.textContent = "正在提交论文…";
    try { await fetchJSON("/api/intake", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ url: input.value.trim() }) }); input.value = ""; toast("论文已添加。同步任务会完成元数据补充、筛选与深读。"); await loadData(); }
    catch (error) { message.textContent = `添加失败：${error.message}`; message.classList.add("error"); submit.disabled = !canMutate(); }
  } }, input, submit);
  const formPanel = node("section", { class: "panel panel-pad" }, sectionHead("添加一条研究线索", null, "plus"), form, node("p", { class: "form-help" }, state.mode === "live" ? "论文进入收件箱后，会按当前研究范围筛选；核实引用关系后连接到图谱。" : "静态快照支持浏览。请启动本地 Paper Watch 服务后添加论文。"), message);
  function update() {
    const filtered = source.filter(p => matches(p, filter)); const size = 10;
    filter.page = Math.min(filter.page, Math.max(1, Math.ceil(filtered.length / size)));
    const current = filtered.slice((filter.page - 1) * size, filter.page * size);
    results.replaceChildren(node("div", { class: "result-bar", "aria-live": "polite" }, node("span", {}, `${count(filtered.length)} 条研究线索`), node("span", {}, "展示最新收录的数据")), node("section", { class: "panel" }, node("div", { class: "panel-pad" }, current.length ? current.map(paperRow) : empty("收件箱很安静", publicLibrary() ? "每周统计与引用检索收录的研究线索会随站点更新发布。" : "新的引用提醒、检索结果与手动添加的论文会汇集在这里。运行一次同步，开始发现与你的研究相关的工作。", "inbox", false, actionLink(publicLibrary() ? "浏览论文库" : "配置订阅", publicLibrary() ? "papers" : "subscriptions"))), pagination(filter, filtered.length, size, update)));
  }
  update();
  const main = node("div", { class: "stack" }, publicLibrary() ? null : formPanel, node("div", {}, searchBar("intake", update), filterTabs("intake", source, [["", "全部"], ["pending", "待筛选"], ["target", "目标"], ["review", "待复核"], ["excluded", "已排除"]], update), results));
  const side = node("aside", { class: "stack" }, node("section", { class: "panel panel-pad" }, sectionHead("筛选如何进行", null, "sliders"), node("p", { class: "small muted" }, state.config.scope?.description || "根据配置中的研究方向、正向与排除关键词，判断论文与小组目标的相关性。"), node("div", { class: "pipeline-status" }, pill("target"), "进入深读流程"), node("div", { class: "pipeline-status" }, pill("review"), "信息不足或边界不清"), node("div", { class: "pipeline-status" }, pill("excluded"), "保留排除依据"), notice("筛选结论、得分与来源可在论文详情中查看。")), latestRunErrors());
  return [pageHead("intake", runButton()), node("div", { class: "intake-layout" }, main, side)];
}

function graphPage() {
  const edges = validEdges(), allSeeds = seeds();
  const selection = node("select", { class: "select", "aria-label": "选择种子论文", onchange: e => { state.graph.seed = e.target.value; state.graph.selection = e.target.value; state.graph.view = { x: 0, y: 0, w: 1000, h: 610 }; render(); } }, node("option", { value: "" }, "全部种子论文"), allSeeds.map(s => node("option", { value: s.id }, seedName(s)))); selection.value = state.graph.seed;
  const status = node("select", { class: "select", "aria-label": "图谱论文状态", onchange: e => { state.graph.status = e.target.value; state.graph.selection = ""; render(); } }, node("option", { value: "" }, "全部引用论文"), node("option", { value: "target" }, "仅目标论文"), node("option", { value: "review" }, "仅待复核论文")); status.value = state.graph.status;
  const chosenSeeds = state.graph.seed ? allSeeds.filter(s => s.id === state.graph.seed) : allSeeds;
  const seedIds = new Set(chosenSeeds.map(s => s.id));
  let activeEdges = edges.filter(e => !state.graph.seed || e.source === state.graph.seed || e.target === state.graph.seed);
  if (state.graph.status) activeEdges = activeEdges.filter(e => [byId(e.source), byId(e.target)].some(p => p && !p.is_seed && p.status === state.graph.status));
  const activeIds = new Set([...seedIds, ...activeEdges.flatMap(e => [e.source, e.target])]);
  if (!state.graph.seed) reports().filter(p => p.report.curated && (!state.graph.status || p.status === state.graph.status)).forEach(p => activeIds.add(p.id));
  const visibleNodes = [...activeIds].map(byId).filter(Boolean);
  const candidatesForGraph = visibleNodes.filter(p => !seedIds.has(p.id));
  const canvas = svgNode("svg", { class: "graph-svg", role: "group", "aria-label": "论文引用网络。方向为引用论文指向被引用论文。使用按钮缩放，拖动空白区域平移。", viewBox: "0 0 1000 610" });
  const defs = svgNode("defs", {}, svgNode("marker", { id: "citation-arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" }, svgNode("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: "#8da582" })), svgNode("pattern", { id: "dot-grid", x: 0, y: 0, width: 25, height: 25, patternUnits: "userSpaceOnUse" }, svgNode("circle", { cx: 1, cy: 1, r: .7, fill: "#dfe6d7" })));
  canvas.append(defs, svgNode("rect", { x: -5000, y: -5000, width: 12000, height: 12000, fill: "url(#dot-grid)" }));
  const positions = new Map();
  const n = chosenSeeds.length;
  chosenSeeds.forEach((s, i) => positions.set(s.id, { x: candidatesForGraph.length ? 790 : 500, y: (i + 1) * 610 / (n + 1), seed: true }));
  const bySeed = new Map(chosenSeeds.map(s => [s.id, []]));
  candidatesForGraph.forEach(p => { const connected = activeEdges.find(e => e.source === p.id && bySeed.has(e.target)) || activeEdges.find(e => e.target === p.id && bySeed.has(e.source)); const group = connected ? (bySeed.has(connected.target) ? connected.target : connected.source) : chosenSeeds[0]?.id; if (!bySeed.has(group)) bySeed.set(group, []); bySeed.get(group).push(p); });
  // A shared grid uses the full canvas height even when every citation targets one seed.
  const orderedCandidates = [...bySeed.values()].flat();
  const candidateCount = orderedCandidates.length;
  const columns = candidateCount <= 8 ? 1 : candidateCount <= 15 ? 2 : Math.ceil(Math.sqrt(candidateCount * 1.2));
  const rows = Math.ceil(candidateCount / columns);
  orderedCandidates.forEach((paper, index) => {
    const column = index % columns, row = Math.floor(index / columns);
    const rowSize = Math.min(columns, candidateCount - row * columns);
    const gapX = columns <= 1 ? 0 : 470 / (columns - 1);
    const x = columns === 1 ? 330 : 95 + (columns - rowSize) * gapX / 2 + column * gapX;
    const y = rows <= 1 ? 305 : 70 + row * 470 / (rows - 1);
    positions.set(paper.id, { x, y, seed: false });
  });
  const compactLabels = visibleNodes.length > 15;
  const edgeEls = [];
  activeEdges.forEach(e => {
    const a = positions.get(e.source), b = positions.get(e.target); if (!a || !b) return;
    const dx = b.x - a.x, dy = b.y - a.y, distance = Math.hypot(dx, dy) || 1;
    const startX = a.x + dx / distance * (a.seed ? 24 : 12), startY = a.y + dy / distance * (a.seed ? 24 : 12);
    const endX = b.x - dx / distance * (b.seed ? 28 : 17), endY = b.y - dy / distance * (b.seed ? 28 : 17);
    const path = svgNode("path", { class: "graph-edge", d: `M${startX},${startY} C${startX + dx * .4},${startY} ${endX - dx * .4},${endY} ${endX},${endY}`, "marker-end": "url(#citation-arrow)" });
    path.append(svgNode("title", {}, `${byId(e.source)?.title || e.source} 引用了 ${byId(e.target)?.title || e.target}`)); canvas.append(path); edgeEls.push([path, e]);
  });
  const details = node("section", { class: "panel panel-pad" });
  const nodeEls = [];
  function bringToFront(group) {
    if (canvas.lastElementChild === group) return;
    const focused = document.activeElement === group;
    canvas.append(group);
    if (focused) group.focus({ preventScroll: true });
  }
  function selectPaper(id) {
    state.graph.selection = id; const paper = byId(id); if (!paper) return;
    const connected = new Set([id]); activeEdges.filter(e => e.source === id || e.target === id).forEach(e => { connected.add(e.source); connected.add(e.target); });
    nodeEls.forEach(([el, p]) => { el.classList.toggle("selected", p.id === id); el.classList.toggle("dim", !connected.has(p.id)); });
    const selectedNode = nodeEls.find(([, p]) => p.id === id)?.[0];
    if (selectedNode) bringToFront(selectedNode);
    edgeEls.forEach(([el, e]) => el.classList.toggle("dim", e.source !== id && e.target !== id));
    const citing = edges.filter(e => e.target === id), references = edges.filter(e => e.source === id);
    details.replaceChildren(node("div", { class: "eyebrow" }, paper.is_seed ? "SEED PAPER" : "SELECTED PAPER"), pill(paperStatus(paper)), node("h2", { class: "detail-name" }, paper.title || paper.id), node("div", { class: "detail-meta" }, node("span", { class: "small muted" }, paper.year || "年份待补充"), node("span", { class: "small muted" }, `${citing.length} 条收录引用`)), node("p", { class: "detail-description" }, shorten(paper.summary || paper.abstract, 420) || "暂无摘要。可以打开论文详情查看已有的元数据与来源。"), node("div", { class: "detail-links" }, actionLink("论文详情", `paper/${encodeURIComponent(id)}`, false), isReportReady(paper) ? actionLink("深读报告", `report/${encodeURIComponent(id)}`, true) : paper.report?.stale ? reportPill(paper) : null), node("h3", { class: "detail-label" }, "已验证引用关系"), [...references, ...citing].length ? node("ul", { class: "evidence-list" }, [...references, ...citing].slice(0, 12).map(e => node("li", {}, node("p", {}, shorten(byId(e.source)?.title || e.source, 70), " → ", shorten(byId(e.target)?.title || e.target, 70)), link("查看引用证据 ↗", e.evidence_url, { class: "text-link" })))) : node("p", { class: "detail-description" }, "尚未收录该论文的已验证引用。孤立节点表示追踪起点，不代表没有引用。"));
  }
  visibleNodes.forEach(paper => {
    const pos = positions.get(paper.id); if (!pos) return;
    const color = pos.seed ? "#284c40" : paper.status === "target" ? "#779c68" : paper.status === "review" ? "#c4a06a" : "#a9b9a0";
    const group = svgNode("g", { class: `graph-node${!pos.seed && compactLabels ? " compact-label" : ""}`, transform: `translate(${pos.x} ${pos.y})`, role: "button", tabindex: 0, "aria-label": `${paper.title}，${labels[paperStatus(paper)]}，打开详情` });
    group.append(svgNode("circle", { class: "node-outline", r: pos.seed ? 30 : 18 }), svgNode("circle", { r: pos.seed ? 23 : 10, fill: color, stroke: "#fff", "stroke-width": 3 }));
    if (pos.seed) group.append(svgNode("text", { x: 0, y: 4, "text-anchor": "middle", style: "fill:#eaf1df;font-size:10px;font-weight:600" }, seedName(paper).slice(0, 1)));
    const title = pos.seed ? seedName(paper) : shorten(paper.title, compactLabels ? 52 : 28);
    const textAnchor = !pos.seed && compactLabels ? (pos.x < 240 ? "start" : pos.x > 420 ? "end" : "middle") : "middle";
    group.append(svgNode("text", { class: "node-label", x: 0, y: pos.seed ? 47 : compactLabels ? -23 : 30, "text-anchor": textAnchor }, title), svgNode("title", {}, paper.title));
    group.addEventListener("pointerenter", () => bringToFront(group));
    group.addEventListener("focus", () => bringToFront(group));
    group.addEventListener("click", () => selectPaper(paper.id)); group.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); selectPaper(paper.id); } });
    canvas.append(group); nodeEls.push([group, paper]);
  });
  function setView() { const v = state.graph.view; canvas.setAttribute("viewBox", `${v.x} ${v.y} ${v.w} ${v.h}`); }
  function zoom(factor) { const v = state.graph.view; const width = Math.min(4000, Math.max(250, v.w * factor)); const ratio = width / v.w; v.x += (v.w - width) / 2; v.y += (v.h - v.h * ratio) / 2; v.w = width; v.h *= ratio; setView(); }
  setView();
  canvas.addEventListener("wheel", e => { e.preventDefault(); zoom(e.deltaY > 0 ? 1.12 : .89); }, { passive: false });
  let drag = null;
  canvas.addEventListener("pointerdown", e => { if (e.target.closest(".graph-node")) return; drag = { x: e.clientX, y: e.clientY, vx: state.graph.view.x, vy: state.graph.view.y }; canvas.setPointerCapture(e.pointerId); });
  canvas.addEventListener("pointermove", e => { if (!drag) return; const rect = canvas.getBoundingClientRect(); state.graph.view.x = drag.vx - (e.clientX - drag.x) * state.graph.view.w / rect.width; state.graph.view.y = drag.vy - (e.clientY - drag.y) * state.graph.view.h / rect.height; setView(); });
  canvas.addEventListener("pointerup", () => { drag = null; }); canvas.addEventListener("pointercancel", () => { drag = null; });
  const controls = node("div", { class: "graph-controls" }, button(icon("plus", 14), () => zoom(.8), { class: "button icon-only small-button", "aria-label": "放大图谱" }), button(icon("minus", 14), () => zoom(1.25), { class: "button icon-only small-button", "aria-label": "缩小图谱" }), button(icon("expand", 14), () => { state.graph.view = { x: 0, y: 0, w: 1000, h: 610 }; setView(); }, { class: "button icon-only small-button", "aria-label": "重置图谱视图" }));
  const panel = node("section", { class: "panel graph-panel" }, node("div", { class: "graph-topline" }, node("h2", {}, `${count(visibleNodes.length)} 个节点 · ${count(activeEdges.length)} 条已验证引用`), controls), canvas, !activeEdges.length ? node("div", { class: "graph-overlay-note" }, "当前范围尚无已验证引用。种子论文显示为独立节点；同步发现并核实引用后，连线会自动出现。") : null, node("div", { class: "graph-legend" }, [["seed", "种子论文"], ["target", "目标论文"], ["review", "待复核"]].map(([cls, text]) => node("span", { class: "legend-item" }, node("i", { class: `legend-dot ${cls}` }), text)), node("span", { class: "legend-item" }, "引用论文 → 被引用论文")));
  if (state.graph.selection && visibleNodes.some(p => p.id === state.graph.selection)) selectPaper(state.graph.selection);
  else details.append(empty("沿着引用发现研究", "点击任意节点，查看论文、筛选依据与引用证据。拖动空白处平移，使用按钮或滚轮缩放。", "network", true));
  const help = node("section", { class: "panel panel-pad" }, sectionHead("图谱中的证据", null, "shield"), node("p", { class: "small muted" }, "连线方向是“引用者 → 被引用者”。图谱仅呈现已有引用证据的关系。论文库中的其他文献不会因主题相似而自动连线。"), node("div", { class: "card-foot" }, `${count(regularPapers().length)} 篇论文在库 · ${count(edges.length)} 条已验证引用`));
  return [pageHead("graph", runButton()), node("div", { class: "toolbar" }, selection, status, node("span", { class: "small muted" }, compactLabels ? "悬停显示标题，点击节点查看关系与证据" : "点击节点查看关系与证据")), node("div", { class: "graph-layout" }, panel, node("aside", { class: "stack" }, details, help))];
}

function reportsPage() {
  const ready = reports(), waiting = papers().filter(p => p.report && (p.report.stale || ["blocked", "failed"].includes(p.report.status)));
  const cards = ready.map(p => node("article", { class: "panel report-card" }, node("div", { class: "report-mark" }, icon("document", 16), p.report.curated ? "精选精读 · 方法与实验拆解" : "DEEP RESEARCH REPORT"), routeLink(p.title, `report/${encodeURIComponent(p.id)}`, { class: "paper-title" }), p.report.organization ? node("p", { class: "small muted" }, p.report.organization) : null, node("p", { class: "paper-summary" }, p.report.summary || p.summary || p.abstract || "基于论文原文的结构化研究分析。"), node("div", { class: "tags" }, pill("ready", "原文深读"), node("span", { class: "pill" }, p.report.evidence_level || "证据等级未标注")), node("div", { class: "report-card-footer" }, dateTime(p.report.generated_at), smallLink("开始阅读", `report/${encodeURIComponent(p.id)}`))));
  return [pageHead("reports", [actionLink("移动操作精读路线", "focus", false, "branch"), runButton()]), node("div", { class: "result-bar" }, node("span", {}, `${count(ready.length)} 篇已完成报告`), node("span", {}, "仅展示已完成且包含正文的报告")), cards.length ? node("div", { class: "report-grid" }, cards) : node("section", { class: "panel" }, empty("让深读建立在原文之上", publicLibrary() ? "当前快照尚无已完成的深读报告。后续报告会随站点更新发布，读者无需配置模型密钥。" : "确认目标论文后，系统会获取原文并生成有依据的分析。缺少原文或模型密钥时，任务会保留为等待状态。", "document", false, actionLink(publicLibrary() ? "浏览论文库" : "查看工作流配置", publicLibrary() ? "papers" : "subscriptions"))),
    waiting.length ? node("section", { class: "panel panel-pad", style: "margin-top:22px" }, sectionHead("等待条件或需要重试", node("span", { class: "small muted" }, `${waiting.length} 篇`)), waiting.map(p => node("article", { class: "paper-row" }, node("div", { class: "paper-row-top" }, routeLink(p.title, `paper/${encodeURIComponent(p.id)}`, { class: "paper-title" }), reportPill(p)), node("p", { class: "paper-summary" }, p.report.stale ? "论文信息或分析配置已有更新，这篇报告需要重新生成。" : p.report.reason || "等待原文或分析模型。")))) : null];
}

function inlineMarkdown(text) {
  const result = document.createDocumentFragment();
  const pattern = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`/g;
  let start = 0, match;
  while ((match = pattern.exec(text))) {
    result.append(document.createTextNode(text.slice(start, match.index)));
    if (match[1]) result.append(link(match[1], match[2]));
    else if (match[3]) result.append(node("strong", {}, match[3]));
    else result.append(node("code", {}, match[4]));
    start = match.index + match[0].length;
  }
  result.append(document.createTextNode(text.slice(start))); return result;
}
function markdown(markdownText) {
  const body = node("article", { class: "report-markdown" }), headings = [];
  const lines = str(markdownText).replace(/\r/g, "").split("\n"); let paragraph = [], list = null, fenced = false, code = [];
  function flush() { if (paragraph.length) { body.append(node("p", {}, inlineMarkdown(paragraph.join("\n")))); paragraph = []; } list = null; }
  const cells = line => line.trim().replace(/^\|/, "").replace(/\|$/, "").split(/(?<!\\)\|/).map(cell => cell.trim().replace(/\\\|/g, "|"));
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (/^\s*```/.test(line)) { flush(); if (fenced) { body.append(node("pre", {}, node("code", {}, code.join("\n")))); code = []; } fenced = !fenced; continue; }
    if (fenced) { code.push(line); continue; }
    if (line.includes("|") && index + 1 < lines.length) {
      const separators = cells(lines[index + 1]);
      const headers = cells(line);
      if (headers.length === separators.length && separators.every(cell => /^:?-{3,}:?$/.test(cell))) {
        flush();
        const table = node("table", { class: "report-table" }, node("thead", {}, node("tr", {}, headers.map(cell => node("th", { scope: "col" }, inlineMarkdown(cell))))));
        const rows = node("tbody");
        index += 1;
        while (index + 1 < lines.length && lines[index + 1].trim() && lines[index + 1].includes("|")) {
          const values = cells(lines[++index]);
          rows.append(node("tr", {}, headers.map((_, column) => node("td", {}, inlineMarkdown(values[column] || "")))));
        }
        table.append(rows); body.append(node("div", { class: "report-table-scroll", tabindex: 0, "aria-label": "实验与证据表格" }, table));
        continue;
      }
    }
    const heading = line.match(/^(#{1,4})\s+(.+)$/);
    if (heading) { flush(); const id = `section-${headings.length}`; headings.push({ id, title: heading[2], level: heading[1].length }); body.append(node(`h${heading[1].length}`, { id }, inlineMarkdown(heading[2]))); continue; }
    if (/^\s*([-*_])\1\1+\s*$/.test(line)) { flush(); body.append(node("hr")); continue; }
    if (/^>\s?/.test(line)) { flush(); body.append(node("blockquote", {}, inlineMarkdown(line.replace(/^>\s?/, "")))); continue; }
    const item = line.match(/^\s*(?:([-*+])|(\d+)\.)\s+(.+)$/);
    if (item) { if (paragraph.length) flush(); const type = item[2] ? "OL" : "UL"; if (!list || list.tagName !== type) { list = node(type.toLowerCase()); body.append(list); } list.append(node("li", {}, inlineMarkdown(item[3]))); continue; }
    if (!line.trim()) { flush(); continue; }
    if (list) list = null; paragraph.push(line);
  }
  flush(); if (code.length) body.append(node("pre", {}, code.join("\n")));
  return { body, headings };
}
function downloadReport(paper) {
  const blob = new Blob([paper.report.markdown], { type: "text/markdown;charset=utf-8" }); const url = URL.createObjectURL(blob);
  const anchor = node("a", { href: url, download: `${str(paper.title).replace(/[<>:"/\\|?*]/g, "_").slice(0, 120) || "report"}.md` }); document.body.append(anchor); anchor.click(); anchor.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
}
function reportPage(id) {
  const paper = byId(id);
  if (!paper || !isReportReady(paper)) return [pageHead("reports"), node("section", { class: "panel" }, empty(paper?.report?.stale ? "这篇报告需要重新生成" : "这篇报告尚未准备好", paper?.report?.stale ? "论文信息或分析配置已有更新。重新生成完成前，旧报告不会计入当前深读报告。" : paper?.report?.reason || "报告可能仍在等待原文、模型配置或处理完成。", "document", false, actionLink("返回报告库", "reports")))];
  const rendered = markdown(paper.report.markdown);
  const reportMetadata = paper.report.curated ? [
    node("div", { class: "detail-label" }, "研究团队"), node("p", { class: "small muted" }, paper.report.organization),
    node("div", { class: "detail-label" }, "核读版本"), node("p", { class: "small muted" }, paper.report.source_version),
    node("div", { class: "detail-label" }, "入选理由"), node("p", { class: "small muted" }, paper.report.selection_reason),
  ] : [];
  const side = node("aside", { class: "stack report-toc" }, node("section", { class: "panel panel-pad" }, sectionHead("报告信息", null, "document"), pill("ready", "原文深读已完成"), node("div", { class: "detail-label" }, paper.report.curated ? "核查时间" : "生成时间"), node("p", { class: "small muted" }, dateTime(paper.report.generated_at)), node("div", { class: "detail-label" }, "证据等级"), node("p", { class: "small muted" }, paper.report.evidence_level || "报告未提供"), reportMetadata, node("div", { class: "detail-links" }, actionLink("论文详情", `paper/${encodeURIComponent(id)}`), link(["论文原文", icon("external", 12)], paper.paper_url, { class: "button small-button" }))), rendered.headings.length ? node("section", { class: "panel panel-pad" }, sectionHead("阅读目录"), rendered.headings.map(h => node("a", { href: `#${h.id}`, onclick: e => { e.preventDefault(); document.getElementById(h.id)?.scrollIntoView({ behavior: "smooth", block: "start" }); } }, h.title))) : null);
  return [pageHead("reports", [smallLink("所有报告", "reports"), button([icon("download", 14), "导出 Markdown"], () => downloadReport(paper))], "深读报告", paper.title), node("div", { class: "report-reader" }, node("section", { class: "panel report-article" }, rendered.body), side)];
}

function paperDetailPage(id) {
  const paper = byId(id);
  if (!paper) return [pageHead("papers"), node("section", { class: "panel" }, empty("没有找到这篇论文", "该链接可能已变更。可返回论文库重新搜索。", "book", false, actionLink("返回论文库", "papers")))];
  const details = node("section", { class: "panel paper-detail-body" },
    paperTags(paper),
    node("h2", { style: "margin-top:16px" }, paper.title),
    node("p", { class: "small muted", style: "margin-top:13px" }, paper.authors || "作者信息待补充"),
    node("div", { class: "detail-meta", style: "margin-top:12px" }, paper.year ? node("span", { class: "pill" }, paper.year) : null, paper.category ? node("span", { class: "pill" }, paper.category) : null, paper.arxiv_id ? node("span", { class: "pill" }, `arXiv:${paper.arxiv_id}`) : null),
    node("div", { class: "detail-links" }, [["论文原文", paper.paper_url], ["项目主页", paper.project_url], ["开源代码", paper.code_url]].filter(([, url]) => safeUrl(url)).map(([label, url]) => link([label, icon("external", 12)], url, { class: "button small-button" }))),
    node("h3", { class: "detail-label" }, "研究摘要"),
    node("p", { class: "paper-abstract" }, paper.abstract || paper.summary || "尚未获取摘要。运行同步任务后，将尝试补充论文元数据。"),
    paper.abstract && paper.summary && paper.abstract !== paper.summary ? [node("h3", { class: "detail-label" }, "文献库笔记"), node("p", { class: "paper-abstract" }, paper.summary)] : null);
  const screen = paper.screening || {};
  const reviewPanel = node("section", { class: "panel panel-pad" }, sectionHead("人工复核", null, "check"));
  if (!paper.is_seed && paper.status !== "library") {
    const reason = node("input", { class: "input", type: "text", placeholder: "复核依据（选填）", "aria-label": "人工复核依据", disabled: !canMutate(), style: "width:100%" });
    const actions = node("div", { class: "detail-links" });
    for (const decision of ["target", "review", "excluded"]) actions.append(button(labels[decision], async () => {
      if (!canMutate()) return;
      [...actions.children].forEach(el => { el.disabled = true; });
      try {
        await fetchJSON("/api/decision", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id: paper.id, decision, reason: reason.value.trim() || "通过研究工作台人工复核" }) });
        toast(`已标记为${labels[decision]}。`); await loadData();
      } catch (error) { toast(`复核未保存：${error.message}`); [...actions.children].forEach(el => { el.disabled = !canMutate(); }); }
    }, { class: `button small-button${decision === "target" ? " primary" : ""}`, disabled: !canMutate() }));
    reviewPanel.append(node("p", { class: "small muted", style: "margin-bottom:12px" }, "根据小组研究目标复核自动筛选结果。标记为目标后，下次同步会继续深读。"), reason, actions);
    if (state.mode !== "live") reviewPanel.append(node("p", { class: "form-help" }, "在本地服务中打开后可保存复核。"));
  }
  const sourceList = (paper.sources || []).map(source => node("li", {}, node("p", {}, `${source.kind || "来源"}${source.relation === "cites" ? " · 已验证引用" : ""}`), link(shorten(source.evidence_url || source.url || "来源链接未提供", 90), source.evidence_url || source.url, { class: "text-link" })));
  const sidebar = node("aside", { class: "stack" }, node("section", { class: "panel panel-pad" }, sectionHead("筛选依据", null, "sliders"), pill(paperStatus(paper)), screen.reason ? node("p", { class: "detail-description", style: "margin-top:12px" }, screen.reason) : notice(paper.status === "library" ? "这是原有论文库中的文献，尚未经过新增论文筛选流程。" : paper.is_seed ? "这是引用追踪的种子论文。" : "尚未产生筛选结果。"), screen.score !== undefined ? node("div", { class: "pipeline-status" }, node("span", { class: "muted" }, "相关性得分"), str(screen.score)) : null, screen.method ? node("div", { class: "pipeline-status" }, node("span", { class: "muted" }, "筛选方式"), str(screen.method)) : null, screen.evidence?.length ? node("ul", { class: "evidence-list" }, screen.evidence.map(screeningEvidence)) : null),
    !paper.is_seed && paper.status !== "library" ? reviewPanel : null,
    node("section", { class: "panel panel-pad" }, sectionHead("深读报告", null, "document"), isReportReady(paper) ? actionLink("阅读完整报告", `report/${encodeURIComponent(id)}`, true) : paper.report?.stale ? [reportPill(paper), notice("论文信息或分析配置已有更新。下一次同步将重新生成报告。", "warning")] : notice(paper.report?.reason || "目标论文将在获取原文后进入深读流程。", paper.report?.status === "failed" ? "warning" : ""), node("div", { class: "detail-links" }, routeLink([icon("network", 13), "在引用网络中查看"], "graph", { class: "button small-button", onclick: () => { state.graph.selection = id; state.graph.seed = paper.is_seed ? id : ""; } }))),
    node("section", { class: "panel panel-pad" }, sectionHead("来源与证据", null, "shield"), sourceList.length ? node("ul", { class: "evidence-list" }, sourceList) : node("p", { class: "small muted" }, "原有文献保留在论文库中。尚未收录额外发现来源或引用证据。")));
  return [pageHead("papers", smallLink("返回论文库", "papers"), "论文详情"), node("div", { class: "paper-detail-layout" }, details, sidebar)];
}

function settingsPage() {
  const config = state.config, scope = config.scope || {}, discovery = config.discovery || {}, recentRuns = (state.data.runs || []).slice(-5).reverse();
  function row(label, value, help = "") { return node("div", { class: "setting-row" }, node("div", {}, node("strong", {}, label), help ? node("p", {}, help) : null), node("div", { class: "value" }, value)); }
  const mailboxConfigured = healthFlag("gmail_configured") === true || healthFlag("imap_configured", "email_configured") === true;
  const sources = publicLibrary()
    ? node("section", { class: "panel panel-pad" }, sectionHead("发现与更新", null, "refresh"), row("文献统计", "每周自动运行", "沿用项目的定期文献整理流程"), row("引用网络", "已验证的引用关系", "根据快照中保留的来源证据展示"), row("浏览方式", "无需账号或 API 密钥", "论文搜索、引用网络与已发布深读报告均可直接访问"), notice("此公开站点展示已发布的数据快照，不接收新增论文、同步或复核写入。"))
    : node("section", { class: "panel panel-pad" }, sectionHead("发现与订阅", null, "mail"), row("引用检索", discovery.semantic_scholar === false ? pill("blocked", "未启用") : pill("ready", "已启用"), "Semantic Scholar · 获取已验证的引用元数据"), row("每个种子检索上限", `${discovery.limit_per_seed || 25} 篇`), row("Google Scholar 邮件", mailboxConfigured ? pill("ready", "邮箱已配置") : state.mode === "live" ? pill("blocked", "需配置邮箱") : "静态快照无法检测", "通过 Gmail / IMAP 读取引用提醒，保留原始邮件"), row("手动导入", "论文链接 / EML 邮件", "补充尚未被自动发现的研究"), notice("在 Google Scholar 中为每篇种子论文创建“被引用”提醒，发送到配置的邮箱。定时任务负责读取提醒、合并重复论文并筛选。"));
  const seedPanel = node("section", { class: "panel panel-pad" }, sectionHead("种子论文", node("span", { class: "small muted" }, `${seeds().length} 篇`), "network"), seeds().map(seed => node("div", { class: "setting-row" }, node("div", {}, node("strong", {}, seedName(seed)), node("p", {}, seed.title)), link(["原文", icon("external", 12)], seed.paper_url, { class: "text-link" }))));
  const research = node("section", { class: "panel panel-pad" }, sectionHead("小组研究范围", null, "sliders"), node("p", { class: "small muted" }, scope.description || "尚未定义研究范围。修改配置后，新增论文将按新的范围进行筛选。"), node("h3", { class: "detail-label" }, "关注关键词"), node("div", { class: "keyword-list" }, (scope.positive_terms || []).length ? scope.positive_terms.map(word => node("span", { class: "keyword" }, word)) : node("span", { class: "small muted" }, "尚未配置")), node("h3", { class: "detail-label" }, "排除关键词"), node("div", { class: "keyword-list" }, (scope.negative_terms || []).length ? scope.negative_terms.map(word => node("span", { class: "keyword" }, word)) : node("span", { class: "small muted" }, "无")), node("div", { style: "margin-top:18px" }, row("目标 / 复核阈值", `${scope.target_threshold ?? "—"} / ${scope.review_threshold ?? "—"}`)));
  const schedule = config.schedule || state.health.schedule || {};
  const plannedTime = schedule.hour !== undefined ? `每日 ${String(schedule.hour).padStart(2, "0")}:${String(schedule.minute || 0).padStart(2, "0")} · ${schedule.timezone || "本地时区"}` : str(schedule.description || schedule.time || schedule.cron || "未设置");
  const runtime = publicLibrary()
    ? node("section", { class: "panel panel-pad" }, sectionHead("发布与更新", runButton(true), "clock"), row("当前模式", pill("ready", "公开只读站点")), row("最近运行", lastRunTime()), row("数据更新", "每周文献统计"), row("站点发布", "主分支更新后自动发布", "每周统计产生的仓库更新也会触发发布"), notice("最近运行时间来自快照内的实际记录。网页不会在浏览器中发起研究任务或保存修改。"))
    : node("section", { class: "panel panel-pad" }, sectionHead("运行与模型", runButton(true), "clock"), row("当前模式", state.mode === "live" ? pill("ready", "本地服务") : pill("blocked", "只读快照")), row("最近运行", lastRunTime()), row("模型", config.llm?.model || "未指定"), row("模型密钥", llmStatus()), row("计划时间", plannedTime), row("自动运行", "由系统定时任务触发", "定时任务由运行环境配置；计划时间不代表已安装调度"), notice("模型与邮箱密钥通过环境变量配置，不会写入网页快照。缺少原文或密钥时，报告会保留明确的等待原因。"));
  const instructions = publicLibrary()
    ? node("section", { class: "panel panel-pad" }, sectionHead("项目与站点", null, "document"), row("项目仓库", link(["GitHub", icon("external", 12)], config.publication.repository_url, { class: "text-link" })), row("公开地址", link(["访问站点", icon("external", 12)], config.publication.site_url, { class: "text-link" })), node("p", { class: "small muted" }, "文献与配置由项目仓库维护。此页面供公开浏览，内容以最近成功发布的快照为准。"))
    : node("section", { class: "panel panel-pad" }, sectionHead("配置入口", null, "document"), node("p", { class: "small muted" }, "研究方向、种子论文与检索上限在项目配置中管理。使用命令行启动服务后，即可在页面同步或添加论文。"), node("pre", { class: "code-block" }, "config/paper-watch.json"), node("p", { class: "small muted" }, "详细初始化与每日调度步骤见项目 README。当前页面展示的是生效配置，不会在浏览器中保存密钥。"));
  const runs = node("section", { class: "panel panel-pad" }, sectionHead("最近运行记录", null, "clock"), recentRuns.length ? node("div", { class: "run-list" }, recentRuns.map(run => node("div", { class: "run-item" }, node("strong", {}, dateTime(run.started_at || run.created_at)), node("p", {}, labels[run.status] || (run.status === "partial" ? "部分完成" : run.status) || (run.finished_at ? "已结束" : "状态未提供")), run.errors?.length ? node("p", {}, runErrors(run.errors)) : null))) : empty("尚无运行记录", "第一次同步完成后，可在这里查看处理状态。", "clock", true));
  return [pageHead("subscriptions"), node("div", { class: "settings-grid" }, node("div", { class: "stack" }, sources, seedPanel, research), node("div", { class: "stack" }, runtime, instructions, runs))];
}

function render() {
  const current = route(); let content;
  if (!state.loaded) content = [pageHead("overview"), node("section", { class: "panel" }, empty("正在连接研究数据", "读取论文库、引用关系与最近运行状态。", "refresh"))];
  else if (state.mode === "error") content = [pageHead("overview"), node("section", { class: "panel" }, empty("研究数据暂时不可用", "请启动本地服务，或先构建带有 data/state.json 的静态站点。", "inbox", false, button("重新加载", () => loadData())))];
  else {
    const views = { overview: overviewPage, focus: focusPage, intake: intakePage, papers: libraryPage, graph: graphPage, reports: reportsPage, subscriptions: settingsPage };
    content = current.name === "paper" ? paperDetailPage(current.id) : current.name === "report" ? reportPage(current.id) : views[current.name]();
  }
  app.replaceChildren(shell(content, current.name));
  document.title = `${current.name === "paper" ? "论文详情" : current.name === "report" ? "深读报告" : pageMeta[current.name]?.[1] || "研究概览"} · Paper Watch`;
}

window.addEventListener("hashchange", () => { render(); window.scrollTo(0, 0); });
loadData(true);
