import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Potential Intelligence™ | Sales Architecture Pilot",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSESSMENT_URL = "https://tally.so/r/jaGY4J"
SAMPLE_REPORT_PATH = Path("reports/sample_report.html")
NURLAN_REPORT_PATH = Path("reports/nurlan_report.html")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, .stApp {
  background:#0d0f15 !important;
  color:white !important;
  font-family:'Outfit', sans-serif;
}

.stApp {
  background:
    radial-gradient(circle at 82% -8%, rgba(232,168,50,.10), transparent 36%),
    radial-gradient(circle at 0% 100%, rgba(192,125,32,.055), transparent 34%),
    #0d0f15 !important;
}

[data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none !important;}
#MainMenu, footer {visibility:hidden;}
header[data-testid="stHeader"] {background:transparent!important;height:0!important;}

.block-container {
  padding-top:0 !important;
  padding-bottom:4rem;
  max-width:1180px;
}

h1,h2,h3 {
  font-family:'Cormorant Garamond', serif !important;
  color:white !important;
  letter-spacing:-.02em;
}

h1 {font-size:4.4rem!important;line-height:.98!important;font-weight:700!important;}
h2 {font-size:2.8rem!important;line-height:1.08!important;font-weight:700!important;}

.pi-topbar {
  position:sticky;
  top:0;
  z-index:999;
  margin:0 -999px 2rem -999px;
  padding:0 999px;
  background:rgba(13,15,21,.88);
  backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(255,255,255,.08);
}

.pi-topbar-inner {
  max-width:1180px;
  margin:0 auto;
  padding:18px 0;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:24px;
}

.pi-brand {
  font-family:'Cormorant Garamond',serif;
  color:white;
  font-size:27px;
  font-weight:700;
  line-height:.9;
  white-space:nowrap;
}

.pi-brand span {color:#e8a832;}

.pi-brand-sub {
  font-size:9px;
  letter-spacing:2.6px;
  text-transform:uppercase;
  color:rgba(255,255,255,.35);
  margin-top:6px;
}

.pi-nav {
  display:flex;
  align-items:center;
  justify-content:flex-end;
  gap:8px;
  flex-wrap:wrap;
}

.pi-nav a {
  color:rgba(255,255,255,.64)!important;
  text-decoration:none!important;
  font-size:12px;
  font-weight:600;
  padding:8px 11px;
  border-radius:3px;
}

.pi-nav a:hover {
  color:#e8a832!important;
  background:rgba(232,168,50,.07);
}

.pi-nav a.cta {
  color:#1e2130!important;
  background:#e8a832;
  font-weight:800;
  letter-spacing:.6px;
  text-transform:uppercase;
}

.pi-hero {
  background:#1e2130;
  color:white;
  border:1px solid rgba(255,255,255,.10);
  border-radius:8px;
  padding:4.4rem 4rem;
  position:relative;
  overflow:hidden;
  margin-bottom:2.2rem;
  box-shadow:0 40px 120px rgba(0,0,0,.32);
}

.pi-hero:before {
  content:'';
  position:absolute;
  right:-130px;
  top:-190px;
  width:610px;
  height:610px;
  border-radius:50%;
  border:1px solid rgba(232,168,50,.10);
}

.pi-hero * {position:relative;z-index:1;}

.pi-badge {
  display:inline-flex;
  font-size:10px;
  font-weight:800;
  letter-spacing:3px;
  text-transform:uppercase;
  color:#e8a832;
  background:rgba(192,125,32,.11);
  border:1px solid rgba(192,125,32,.26);
  padding:7px 14px;
  border-radius:2px;
  margin-bottom:1.6rem;
}

.pi-gold {color:#e8a832;}

.pi-sub {
  font-size:1.25rem;
  color:rgba(255,255,255,.76);
  line-height:1.65;
  max-width:780px;
  margin:1.2rem 0 1.8rem;
}

.pi-note {
  color:rgba(255,255,255,.46);
  font-size:.86rem;
  line-height:1.6;
}

.pi-btn-row {
  display:flex;
  gap:.8rem;
  flex-wrap:wrap;
  margin-top:1.5rem;
}

.pi-btn {
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:.88rem 1.3rem;
  border-radius:3px;
  font-size:.76rem;
  font-weight:800;
  letter-spacing:.9px;
  text-transform:uppercase;
  text-decoration:none!important;
}

.pi-btn-primary {
  background:#e8a832;
  color:#1e2130!important;
}

.pi-btn-secondary {
  border:1px solid rgba(255,255,255,.22);
  color:rgba(255,255,255,.86)!important;
}

.pi-anchor {
  height:1px;
  margin-top:-88px;
  padding-top:88px;
}

.pi-section {
  margin:4rem 0 1.8rem;
}

.pi-kicker {
  font-size:9px;
  font-weight:800;
  letter-spacing:2.4px;
  text-transform:uppercase;
  color:#e8a832;
  margin-bottom:.6rem;
}

.pi-section-title {
  font-family:'Cormorant Garamond',serif;
  font-size:2.75rem;
  line-height:1.08;
  font-weight:700;
  color:white;
  margin-bottom:.8rem;
}

.pi-lead {
  font-size:1.08rem;
  color:rgba(255,255,255,.58);
  line-height:1.72;
  max-width:860px;
  margin-bottom:2rem;
}

.pi-card,
.pi-row {
  background:rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.10);
  border-radius:6px;
}

.pi-card {
  padding:1.6rem;
  height:100%;
}

.pi-card-solid {
  background:#1e2130;
  border:1px solid rgba(255,255,255,.10);
  border-radius:6px;
  padding:1.8rem;
  height:100%;
}

.pi-title {
  font-size:1.08rem;
  font-weight:800;
  color:white;
  margin-bottom:.55rem;
  line-height:1.32;
}

.pi-muted {
  color:rgba(255,255,255,.58);
}

.pi-quote {
  background:#1e2130;
  color:white;
  border:1px solid rgba(255,255,255,.10);
  border-radius:6px;
  padding:2rem;
  height:100%;
}

.pi-quote-main {
  font-family:'Cormorant Garamond',serif;
  font-size:1.95rem;
  line-height:1.28;
  color:rgba(255,255,255,.94);
  margin-bottom:1rem;
}

.pi-quote-small {
  color:rgba(255,255,255,.46);
  font-size:.86rem;
}

.pi-row {
  padding:1.05rem 1.2rem;
  margin-bottom:.8rem;
}

.pi-pill {
  display:inline-block;
  font-size:.7rem;
  font-weight:800;
  color:#e8a832;
  background:rgba(232,168,50,.10);
  border:1px solid rgba(232,168,50,.18);
  padding:.25rem .62rem;
  border-radius:2px;
  margin-top:.6rem;
}

.pi-step-num {
  font-family:'Cormorant Garamond',serif;
  font-size:2.7rem;
  font-weight:700;
  color:#e8a832;
  line-height:1;
  margin-bottom:.75rem;
}

.pi-final {
  background:#1e2130;
  border:1px solid rgba(255,255,255,.10);
  border-radius:8px;
  padding:3.6rem 3rem;
  text-align:center;
  margin-top:4rem;
}

.pi-final h2 {
  font-size:3.4rem!important;
}

.pi-footer {
  text-align:center;
  color:rgba(255,255,255,.40);
  font-size:.86rem;
  padding:2.2rem 0;
  border-top:1px solid rgba(255,255,255,.08);
  margin-top:3rem;
}

iframe {
  border-radius:6px;
  background:#fff;
}

@media(max-width:900px) {
  h1 {font-size:3rem!important;}
  .pi-hero {padding:2.4rem 1.8rem;}
  .pi-section-title {font-size:2.2rem;}
  .pi-final h2 {font-size:2.5rem!important;}
  .pi-topbar-inner {flex-direction:column;align-items:flex-start;}
  .pi-nav {justify-content:flex-start;}
}
</style>
""", unsafe_allow_html=True)


def section_header(anchor, kicker, title, lead=None):
    st.markdown(f"""
    <div id="{anchor}" class="pi-anchor"></div>
    <div class="pi-section">
      <div class="pi-kicker">{kicker}</div>
      <div class="pi-section-title">{title}</div>
      {f'<div class="pi-lead">{lead}</div>' if lead else ''}
    </div>
    """, unsafe_allow_html=True)


def render_html_file(path: Path, height=720):
    if path.exists():
        components.html(path.read_text(encoding="utf-8"), height=height, scrolling=True)
    else:
        st.info(f"Add HTML file here: `{path}`")


st.markdown(f"""
<div class="pi-topbar">
  <div class="pi-topbar-inner">
    <div>
      <div class="pi-brand">Potential <span>Intelligence™</span></div>
      <div class="pi-brand-sub">Validation Hub</div>
    </div>
    <div class="pi-nav">
      <a href="#problem">Problem</a>
      <a href="#scenario">Scenario</a>
      <a href="#report">Report</a>
      <a href="#process">Process</a>
      <a href="#methodology">Methodology</a>
      <a href="#team">Team</a>
      <a href="#faq">FAQ</a>
      <a class="cta" href="{ASSESSMENT_URL}" target="_blank">Take Assessment</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="pi-hero">
  <div class="pi-badge">Pilot validation · Sales architecture</div>
  <h1>A new way to understand <span class="pi-gold">why sales performance varies</span>.</h1>
  <div class="pi-sub">
    Two reps can have the same product, same training, and same quota — but very different outcomes.
    Potential Intelligence™ helps reveal the behavioral pattern behind that difference.
  </div>
  <div class="pi-btn-row">
    <a class="pi-btn pi-btn-primary" href="{ASSESSMENT_URL}" target="_blank">Take the assessment — free</a>
    <a class="pi-btn pi-btn-secondary" href="#report">See what you receive</a>
  </div>
  <div class="pi-note">Validation pilot for Sales Leaders, HR Partners, founders, and revenue teams. This is validation, not evaluation.</div>
</div>
""", unsafe_allow_html=True)


section_header(
    "problem",
    "The problem",
    "Sales teams often coach the behavior they can see — not the architecture that creates it.",
    "A rep misses follow-up. Another avoids urgency. A third builds trust easily but struggles to close. The usual answer is more training, more scripts, or more pressure. Often it does not explain why the pattern keeps repeating.",
)

col1, col2 = st.columns([0.95, 1.05])
with col1:
    st.markdown("""
    <div class="pi-quote">
      <div class="pi-quote-main">“Same product. Same training. Same CRM. Different outcomes.”</div>
      <div class="pi-quote-small">The pilot starts from this practical question: what is different in the rep’s natural sales architecture?</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    points = [
        ("1", "Performance variance is not always a skill gap.", "Sometimes the issue is role fit, energy cost, decision style, buyer-reading pattern, or the way a seller naturally creates trust and action."),
        ("2", "Generic coaching can miss the real friction point.", "One rep needs structure. Another needs urgency. Another needs emotional trust-building. Same coaching rarely unlocks everyone."),
        ("3", "Managers need better language for 1:1 conversations.", "The goal is not to label the rep. The goal is to have a more precise conversation about how they actually sell."),
    ]
    for n, title, body in points:
        st.markdown(f"""
        <div class="pi-row">
          <div class="pi-kicker">Point {n}</div>
          <div class="pi-title">{title}</div>
          <div class="pi-muted">{body}</div>
        </div>
        """, unsafe_allow_html=True)


section_header(
    "scenario",
    "Concrete scenario",
    "Two AEs. Same onboarding. Same quota. Different results.",
    "Sarah closes 78% of her qualified pipeline. Marcus closes 41%. Both know the product. Both attended the same training. The difference is not only skill — it may be how each rep naturally reads buyers, creates urgency, builds trust, and follows through.",
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="pi-card-solid">
      <div class="pi-kicker">Sarah</div>
      <div class="pi-title">High decision momentum</div>
      <p class="pi-muted">Converts interest into clear next steps. Creates urgency and ownership faster.</p>
      <div style="font-family:'Cormorant Garamond',serif;font-size:52px;color:#e8a832;font-weight:700;">78%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pi-card-solid">
      <div class="pi-kicker">Marcus</div>
      <div class="pi-title">Strong discovery, slower commitment</div>
      <p class="pi-muted">Builds trust and gets positive buyer feedback, but deals may stay warm without movement.</p>
      <div style="font-family:'Cormorant Garamond',serif;font-size:52px;color:#e8a832;font-weight:700;">41%</div>
    </div>
    """, unsafe_allow_html=True)


section_header(
    "report",
    "What you receive",
    "A validation report built to support a better coaching conversation.",
    "The participant receives an individual report that translates assessment answers into a sales behavior map. It is written for real-world use by the participant, manager, or HR partner.",
)

rows = [
    ("Natural Sales Pattern", "A plain-language summary of how this person creates revenue, what environment fits best, and what should be validated in real deals.", "Executive Summary"),
    ("Sales Cycle Translation", "How the person’s pattern may appear across discovery, positioning, urgency, follow-through, and expansion.", "Revenue Process"),
    ("Strengths & High-Effort Zones", "What feels natural, what costs more energy, and where structure or role design may improve consistency.", "Coaching Insight"),
    ("Environment Fit", "Where this person is more likely to perform well and which environments should be evaluated carefully.", "Role Alignment"),
    ("Validation Questions", "Structured feedback questions for the participant and, optionally, their manager or HR partner.", "Pilot Feedback"),
]

for name, desc, tag in rows:
    st.markdown(f"""
    <div class="pi-row">
      <div style="display:grid;grid-template-columns:210px 1fr 170px;gap:18px;align-items:center;">
        <div class="pi-title" style="margin-bottom:0;">{name}</div>
        <div class="pi-muted">{desc}</div>
        <div><span class="pi-pill">{tag}</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="pi-section" style="margin-top:2rem;">
  <div class="pi-kicker">Sample preview</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pi-section" style="margin-top:2rem;">
  <div class="pi-kicker">Sample preview</div>
  <div class="pi-lead">
    Below is an example of the individual Sales Architecture Report participants receive after completing the assessment.
  </div>
</div>
""", unsafe_allow_html=True)

render_html_file(SAMPLE_REPORT_PATH, height=760)

section_header(
    "process",
    "How it works",
    "Simple pilot process",
    "The goal is not to prove the framework is perfect. The goal is to learn what is accurate, useful, confusing, or wrong.",
)

col1, col2, col3, col4 = st.columns(4)
steps = [
    ("01", "Take the assessment", "The participant answers structured questions about real sales behavior and work patterns."),
    ("02", "Receive the report", "A pilot Sales Architecture Report is generated and shared for review."),
    ("03", "Reflect on accuracy", "The participant reviews what feels accurate, useful, unclear, or wrong."),
    ("04", "Share feedback", "Feedback is used to validate the framework and improve the product before launch."),
]

for col, (num, title, body) in zip([col1, col2, col3, col4], steps):
    with col:
        st.markdown(f"""
        <div class="pi-card">
          <div class="pi-step-num">{num}</div>
          <div class="pi-title">{title}</div>
          <div class="pi-muted">{body}</div>
        </div>
        """, unsafe_allow_html=True)


section_header(
    "methodology",
    "Methodology architecture",
    "A simple business layer over a deeper diagnostic system.",
    "For clients, we keep the language practical: revenue behavior, sales cycle patterns, coaching signals, and role fit. The deeper methodology stays behind the scenes until needed.",
)

col1, col2, col3 = st.columns(3)
cards = [
    ("Layer 1", "Business language", "Revenue behavior, sales cycle patterns, coaching signals, role fit."),
    ("Layer 2", "Behavioral drivers", "Underlying patterns that explain how people create trust, urgency, clarity, structure, and momentum."),
    ("Layer 3", "Diagnostic interpretation", "Whether a pattern appears naturally, with support, or as a high-effort behavior under pressure."),
]

for col, (k, title, body) in zip([col1, col2, col3], cards):
    with col:
        st.markdown(f"""
        <div class="pi-card">
          <div class="pi-kicker">{k}</div>
          <div class="pi-title">{title}</div>
          <div class="pi-muted">{body}</div>
        </div>
        """, unsafe_allow_html=True)


section_header(
    "team",
    "Why you can trust the process",
    "Built from HR diagnostics, learning design, and enterprise sales experience.",
    "Potential Intelligence™ is being developed at the intersection of human behavior, revenue execution, HR diagnostics, and real-world sales practice.",
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="pi-card-solid">
      <div class="pi-title">Asselya Zhanybek</div>
      <p><strong style="color:#e8a832;">HR, talent diagnostics, learning systems, and workforce intelligence</strong></p>
      <p class="pi-muted">15+ years across HR consulting, corporate learning, assessment tools, and workforce development.</p>
      <p class="pi-muted">Asselya is building Potential Intelligence™ as a practical framework for understanding how people actually perform — especially in roles where behavior, trust, pressure, and execution all matter.</p>
      <p class="pi-muted">Based in San Diego. Currently validating the first version with real participants and feedback.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pi-card-solid">
      <div class="pi-title">Nurlan Zhanybek</div>
      <p><strong style="color:#e8a832;">Enterprise sales validation advisor</strong></p>
      <p class="pi-muted">15+ years in enterprise sales and global technology companies, including Microsoft and Pearson.</p>
      <p class="pi-muted">Nurlan helps pressure-test the framework against real sales behavior, sales cycles, buyer conversations, and the realities of quota-driven environments.</p>
      <p class="pi-muted">This helps keep the product grounded in how enterprise sales actually works — not only how assessments describe people.</p>
    </div>
    """, unsafe_allow_html=True)


section_header("faq", "FAQ", "Common questions")

faq = [
    ("Is this a personality test?", "No. The report is designed to map revenue behavior patterns: how a person reads buyers, creates value, moves deals, and responds to different sales environments."),
    ("Is this a performance evaluation?", "No. This is a validation-stage report. It should not be used to judge, rank, hire, fire, or penalize participants."),
    ("What if a participant disagrees with their report?", "That is useful feedback. The validation goal is not to convince anyone. It is to learn. Disagreement helps improve the questions, scoring, language, and interpretation."),
    ("Can a manager see the report?", "Only with the participant’s agreement. The pilot works best when the report is discussed as a coaching and reflection tool, not as a judgment tool."),
]

for q, a in faq:
    st.markdown(f"""
    <div class="pi-row">
      <div class="pi-title">{q}</div>
      <div class="pi-muted">{a}</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown(f"""
<div class="pi-final">
  <div class="pi-kicker">Join the validation pilot</div>
  <h2>Take the assessment and help shape the next version.</h2>
  <p class="pi-muted" style="max-width:720px;margin:0 auto;">
    You will receive a pilot Sales Architecture Report and be asked to share honest feedback about what feels accurate, useful, confusing, or wrong.
  </p>
  <div class="pi-btn-row" style="justify-content:center;">
    <a class="pi-btn pi-btn-primary" href="{ASSESSMENT_URL}" target="_blank">Take the assessment — free</a>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="pi-footer">
  <strong>Potential Intelligence™</strong> · Sales Architecture Pilot · Validation Stage<br>
  Revenue Behavior Mapping · Individual Reports · Sales & HR Research Version<br>
  This pilot is for methodology validation and should not be used as a final performance evaluation.
</div>
""", unsafe_allow_html=True)