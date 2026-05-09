
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
METHODOLOGY_PATH = Path("methodology/indices_framework.md")

PAGES = {
    "home": "Home",
    "assessment": "Take Assessment",
    "report": "Sample Report",
    "methodology": "Methodology",
    "cases": "Case Studies",
    "about": "About",
}

if "page" not in st.session_state:
    st.session_state.page = "home"

# Query param support
try:
    qp = st.query_params
    if "page" in qp and qp["page"] in PAGES:
        st.session_state.page = qp["page"]
except Exception:
    pass

def set_page(page_key: str):
    st.session_state.page = page_key
    try:
        st.query_params["page"] = page_key
    except Exception:
        pass


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Outfit:wght@300;400;500;600;700;800&display=swap');

:root{
--ink:#0d0f15;
--ink2:#171a26;
--panel:#1e2130;
--gold:#c07d20;
--gold2:#e8a832;
--cream:#f8f4ee;
--soft:#f4f1eb;
--line:rgba(255,255,255,.10);
--muted:rgba(255,255,255,.58);
--muted2:rgba(255,255,255,.38);
}

html, body, [class*="css"] {
  font-family:'Outfit', sans-serif;
}

html, body, .stApp {
  background:#0d0f15 !important;
  color:white !important;
}

.stApp {
  background:
    radial-gradient(circle at 80% -10%, rgba(232,168,50,.10), transparent 38%),
    radial-gradient(circle at 0% 100%, rgba(192,125,32,.05), transparent 34%),
    #0d0f15 !important;
}

/* Hide Streamlit chrome */
[data-testid="stSidebar"] { display:none !important; }
[data-testid="collapsedControl"] { display:none !important; }
#MainMenu { visibility:hidden; }
footer { visibility:hidden; }
header[data-testid="stHeader"] {
  background: transparent !important;
  height: 0rem !important;
}

/* Main container */
.block-container {
  padding-top: 0rem !important;
  padding-bottom: 4rem;
  max-width: 1180px;
}

/* Typography */
h1,h2,h3 {
  font-family:'Cormorant Garamond', serif !important;
  letter-spacing:-.02em;
  color:white !important;
}

h1 {
  font-size:4.4rem !important;
  line-height:.98 !important;
  font-weight:700 !important;
}

h2 {
  font-size:2.8rem !important;
  line-height:1.08 !important;
  font-weight:700 !important;
}

p, li {
  font-size:1rem;
  line-height:1.7;
}

/* Top nav */
.pi-topbar {
  position: sticky;
  top: 0;
  z-index: 999;
  margin: 0 -999px 2rem -999px;
  padding: 0 999px;
  background: rgba(13,15,21,.86);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255,255,255,.08);
}

.pi-topbar-inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 18px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.pi-brand {
  font-family:'Cormorant Garamond', serif;
  color:white;
  font-size: 27px;
  font-weight: 700;
  line-height: .9;
  letter-spacing: -.02em;
  white-space: nowrap;
}

.pi-brand span {
  color:#e8a832;
}

.pi-brand-sub {
  font-family:'Outfit', sans-serif;
  font-size: 9px;
  letter-spacing: 2.6px;
  text-transform: uppercase;
  color: rgba(255,255,255,.35);
  margin-top: 6px;
}

.pi-nav {
  display:flex;
  align-items:center;
  justify-content:flex-end;
  gap: 8px;
  flex-wrap: wrap;
}

.pi-nav a {
  color: rgba(255,255,255,.64) !important;
  text-decoration: none !important;
  font-size: 12px;
  font-weight: 600;
  padding: 8px 11px;
  border-radius: 3px;
  transition: .16s ease;
}

.pi-nav a:hover {
  color:#e8a832 !important;
  background: rgba(232,168,50,.07);
}

.pi-nav a.active {
  color:#1e2130 !important;
  background:#e8a832;
  font-weight:800;
}

.pi-nav a.cta {
  color:#1e2130 !important;
  background:#e8a832;
  font-weight:800;
  letter-spacing:.6px;
  text-transform:uppercase;
  margin-left:4px;
}

/* Components */
.pi-hero {
  background: #1e2130;
  color: white;
  border: 1px solid rgba(255,255,255,.10);
  border-radius: 8px;
  padding: 4.4rem 4rem;
  position: relative;
  overflow: hidden;
  margin-bottom: 2.2rem;
  box-shadow: 0 40px 120px rgba(0,0,0,.32);
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

.pi-hero:after {
  content:'';
  position:absolute;
  left:-240px;
  bottom:-280px;
  width:560px;
  height:560px;
  border-radius:50%;
  border:1px solid rgba(232,168,50,.06);
}

.pi-hero * {
  position:relative;
  z-index:1;
}

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

.pi-gold { color:#e8a832; }

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
  font-family:'Cormorant Garamond', serif;
  font-size:2.75rem;
  line-height:1.08;
  font-weight:700;
  color:white;
  letter-spacing:-.02em;
  margin-bottom:.8rem;
}

.pi-lead {
  font-size:1.08rem;
  color:rgba(255,255,255,.58);
  line-height:1.72;
  max-width:860px;
  margin-bottom:2rem;
}

.pi-card {
  background:rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.10);
  border-radius:6px;
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
  font-family:'Cormorant Garamond', serif;
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
  background:rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.10);
  border-radius:5px;
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
  font-family:'Cormorant Garamond', serif;
  font-size:2.7rem;
  font-weight:700;
  color:#e8a832;
  line-height:1;
  margin-bottom:.75rem;
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

/* Streamlit widgets */
.stTabs [data-baseweb="tab-list"] {
  gap: 8px;
}

.stTabs [data-baseweb="tab"] {
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.10);
  border-radius: 3px;
  color: rgba(255,255,255,.70);
}

.stTabs [aria-selected="true"] {
  background: rgba(232,168,50,.14) !important;
  color: #e8a832 !important;
}

.streamlit-expanderHeader {
  color:white !important;
  font-weight:800;
}

div[data-testid="stExpander"] {
  background: rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.10);
  border-radius:6px;
}

/* responsive */
@media(max-width:900px) {
  h1 { font-size:3rem!important; }
  .pi-hero { padding:2.4rem 1.8rem; }
  .pi-section-title { font-size:2.2rem; }
  .pi-topbar-inner { flex-direction:column; align-items:flex-start; }
  .pi-nav { justify-content:flex-start; }
}
</style>
""", unsafe_allow_html=True)


def nav():
    current = st.session_state.page
    links = ""
    for key, label in PAGES.items():
        active = "active" if key == current else ""
        links += f'<a class="{active}" href="?page={key}">{label}</a>'
    links += f'<a class="cta" href="{ASSESSMENT_URL}" target="_blank">Take Assessment</a>'

    st.markdown(f"""
    <div class="pi-topbar">
      <div class="pi-topbar-inner">
        <div>
          <div class="pi-brand">Potential <span>Intelligence™</span></div>
          <div class="pi-brand-sub">Validation Hub</div>
        </div>
        <div class="pi-nav">{links}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def section_header(kicker, title, lead=None):
    st.markdown(f"""
    <div class="pi-section">
      <div class="pi-kicker">{kicker}</div>
      <div class="pi-section-title">{title}</div>
      {f'<div class="pi-lead">{lead}</div>' if lead else ''}
    </div>
    """, unsafe_allow_html=True)


def cta_buttons():
    st.markdown(f"""
    <div class="pi-btn-row">
      <a class="pi-btn pi-btn-primary" href="{ASSESSMENT_URL}" target="_blank">Take the assessment — free</a>
      <a class="pi-btn pi-btn-secondary" href="?page=report">View sample report</a>
    </div>
    """, unsafe_allow_html=True)


def render_html_file(path: Path, height=760):
    if path.exists():
        components.html(path.read_text(encoding="utf-8"), height=height, scrolling=True)
    else:
        st.warning(f"File not found: `{path}`")
        st.info("Add your HTML report to this path or update app.py.")


def render_markdown_file(path: Path):
    if path.exists():
        st.markdown(path.read_text(encoding="utf-8"))
    else:
        st.info(f"Add methodology file here: `{path}`")


def home():
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
        <a class="pi-btn pi-btn-secondary" href="?page=report">See what you receive</a>
      </div>
      <div class="pi-note">Validation pilot for Sales Leaders, HR Partners, founders, and revenue teams. This is validation, not evaluation.</div>
    </div>
    """, unsafe_allow_html=True)

    section_header(
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

    cta_buttons()


def assessment():
    section_header(
        "Take assessment",
        "Complete the Potential Intelligence™ Sales Architecture Assessment.",
        "This form is part of the validation pilot. You will receive a pilot report and may be asked to share feedback on what feels accurate, useful, confusing, or wrong.",
    )
    st.markdown(f"""
    <div class="pi-card-solid">
      <div class="pi-kicker">Pilot assessment</div>
      <div class="pi-title">Start the assessment in Tally</div>
      <p class="pi-muted">The assessment opens in a new tab. After submission, your answers can be used to generate the individual validation report.</p>
      <div class="pi-btn-row">
        <a class="pi-btn pi-btn-primary" href="{ASSESSMENT_URL}" target="_blank">Open assessment</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Embedded form")
    components.iframe(ASSESSMENT_URL, height=760, scrolling=True)


def sample_report():
    section_header(
        "Sample report",
        "Sales Architecture Validation Report",
        "Use this page to show participants and leaders what they receive after the assessment.",
    )
    tabs = st.tabs(["Sample Report", "Nurlan Case", "How to use this page"])
    with tabs[0]:
        render_html_file(SAMPLE_REPORT_PATH, height=820)
    with tabs[1]:
        render_html_file(NURLAN_REPORT_PATH, height=820)
    with tabs[2]:
        st.markdown("""
        **Recommended setup**

        - Put your general sample report here: `reports/sample_report.html`
        - Put Nurlan's validation case here: `reports/nurlan_report.html`
        - Use this page during calls when someone asks: “What will I receive?”
        """)


def methodology():
    section_header(
        "Methodology architecture",
        "How the framework works — without overwhelming the client.",
        "This page explains just enough to create trust: business indices, behavioral drivers, diagnostic layers, and validation logic.",
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

    st.markdown("## Revenue Behavior Mapping")
    st.markdown("Potential Intelligence™ is being developed to explain **why sellers create revenue differently**.")
    with st.expander("Business indices / scoring framework"):
        render_markdown_file(METHODOLOGY_PATH)
    with st.expander("Validation principles"):
        st.markdown("""
        - This is validation, not evaluation.
        - Disagreement is valuable data.
        - Reports should not be used as hiring or performance decisions by themselves.
        - The primary goal is to create better coaching conversations.
        - Scores should be interpreted as natural vs high-effort behavior, not good vs bad.
        """)


def cases():
    section_header(
        "Case studies",
        "Build the evidence base one real case at a time.",
        "This page will become your product moat: real participants, real patterns, real feedback, and eventually real performance correlations.",
    )
    st.markdown("""
    <div class="pi-card">
      <div class="pi-kicker">Case 001</div>
      <div class="pi-title">Nurlan Zhanybek · Enterprise Sales Profile</div>
      <div class="pi-muted">
        First validation case. Enterprise sales background, global technology and education companies,
        with a pattern oriented around clarity, structured discovery, and consultative trust.
      </div>
      <span class="pi-pill">Validation case</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Report preview")
    render_html_file(NURLAN_REPORT_PATH, height=760)
    st.markdown("### What to collect for every case")
    st.markdown("""
    - Role and sales motion
    - Years in sales
    - Deal type: SMB / Mid-market / Enterprise
    - Inbound vs outbound
    - Participant feedback
    - Manager feedback if available
    - Real sales metrics if available
    - What felt accurate / inaccurate
    - Coaching implication
    """)


def about():
    section_header(
        "About the builders",
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

    section_header("Pilot ethics", "This is validation — not evaluation.")
    col1, col2, col3 = st.columns(3)
    ethics = [
        ("Not a finished claim", "The goal is not to prove the framework is perfect. The goal is to learn what is accurate, useful, confusing, or wrong."),
        ("Disagreement is data", "If a participant disagrees with their report, that is exactly what we need to know."),
        ("No judgment use", "No report should be used as a hiring or performance decision by itself."),
    ]
    for col, (title, body) in zip([col1, col2, col3], ethics):
        with col:
            st.markdown(f"""
            <div class="pi-card">
              <div class="pi-title">{title}</div>
              <div class="pi-muted">{body}</div>
            </div>
            """, unsafe_allow_html=True)
    cta_buttons()


nav()

page = st.session_state.page
if page == "home":
    home()
elif page == "assessment":
    assessment()
elif page == "report":
    sample_report()
elif page == "methodology":
    methodology()
elif page == "cases":
    cases()
elif page == "about":
    about()

st.markdown("""
<div class="pi-footer">
  <strong>Potential Intelligence™</strong> · Sales Architecture Pilot · Validation Stage<br>
  Revenue Behavior Mapping · Individual Reports · Sales & HR Research Version<br>
  This pilot is for methodology validation and should not be used as a final performance evaluation.
</div>
""", unsafe_allow_html=True)
