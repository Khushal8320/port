import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Khushal Patel · Data Scientist",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

/* ── Reset & Root ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --cream:    #F5F2EC;
  --ink:      #0F0E0C;
  --charcoal: #1E1D1B;
  --forest:   #1A3D2E;
  --sage:     #3B6E52;
  --mint:     #6FBFA0;
  --gold:     #C9A84C;
  --warm:     #E8E0D0;
  --border:   #D4CCBC;
  --muted:    #7A7468;
}

/* ── Streamlit chrome hide ── */
#MainMenu, footer, header { visibility: hidden; }
.stAppDeployButton { display: none; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stDecoration"] { display: none; }

/* ── App shell ── */
.stApp {
  background: var(--cream) !important;
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
}

.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* ── Hero ── */
.hero {
  background: var(--forest);
  background-image:
    radial-gradient(ellipse 80% 60% at 70% 50%, rgba(107,191,160,0.18) 0%, transparent 70%),
    radial-gradient(ellipse 40% 80% at 10% 80%, rgba(201,168,76,0.10) 0%, transparent 60%);
  color: var(--cream);
  padding: 96px 72px 80px;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 340px; height: 340px;
  border: 1.5px solid rgba(111,191,160,0.25);
  border-radius: 50%;
  pointer-events: none;
}

.hero::after {
  content: '';
  position: absolute;
  bottom: -80px; left: 50px;
  width: 220px; height: 220px;
  border: 1px solid rgba(201,168,76,0.20);
  border-radius: 50%;
  pointer-events: none;
}

.hero-tag {
  display: inline-block;
  background: rgba(111,191,160,0.18);
  border: 1px solid rgba(111,191,160,0.45);
  color: var(--mint);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  text-transform: uppercase;
  padding: 6px 16px;
  border-radius: 2px;
  margin-bottom: 28px;
}

.hero-name {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(52px, 7vw, 88px);
  line-height: 1.02;
  letter-spacing: -1.5px;
  margin-bottom: 8px;
}

.hero-name span {
  color: var(--mint);
}

.hero-title {
  font-size: 18px;
  font-weight: 300;
  color: rgba(245,242,236,0.65);
  margin-bottom: 32px;
  letter-spacing: 0.5px;
}

.hero-desc {
  max-width: 540px;
  font-size: 15.5px;
  line-height: 1.75;
  color: rgba(245,242,236,0.80);
  margin-bottom: 44px;
}

.hero-contacts {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 48px;
}

.hero-contact-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: rgba(245,242,236,0.70);
  text-decoration: none;
}

.hero-contact-item:hover {
  color: var(--mint);
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--gold);
  color: var(--charcoal);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 14px 32px;
  border-radius: 2px;
  text-decoration: none;
  transition: all 0.2s ease;
  margin-right: 16px;
}

.hero-cta:hover {
  background: #d4b358;
}

.hero-cta-ghost {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  border: 1px solid rgba(245,242,236,0.35);
  color: rgba(245,242,236,0.85);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 14px 32px;
  border-radius: 2px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.hero-cta-ghost:hover {
  border-color: var(--mint);
  color: var(--mint);
}

/* ── Stats strip ── */
.stats-strip {
  background: var(--charcoal);
  display: flex;
  justify-content: center;
  align-items: stretch;
  flex-wrap: wrap;
}

.stat-cell {
  padding: 36px 56px;
  text-align: center;
  border-right: 1px solid rgba(255,255,255,0.06);
  flex: 1;
  min-width: 150px;
}

.stat-cell:last-child { border-right: none; }

.stat-num {
  font-family: 'DM Serif Display', serif;
  font-size: 38px;
  color: var(--mint);
  display: block;
  line-height: 1;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.40);
}

/* ── Sections ── */
.section {
  padding: 88px 72px;
}

.section-alt {
  background: var(--warm);
}

.section-dark {
  background: var(--charcoal);
  color: var(--cream);
}

.section-header {
  display: flex;
  align-items: baseline;
  gap: 20px;
  margin-bottom: 56px;
}

.section-num {
  font-family: 'DM Serif Display', serif;
  font-style: italic;
  font-size: 13px;
  color: var(--mint);
  letter-spacing: 1px;
  min-width: 28px;
}

.section-title {
  font-family: 'DM Serif Display', serif;
  font-size: 42px;
  line-height: 1.1;
  letter-spacing: -0.5px;
}

.section-dark .section-title { color: var(--cream); }

.section-line {
  flex: 1;
  height: 1px;
  background: var(--border);
  margin-left: 24px;
  align-self: center;
}

.section-dark .section-line { background: rgba(255,255,255,0.10); }

/* ── About ── */
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: start;
}

.about-text {
  font-size: 16px;
  line-height: 1.85;
  color: #3A3830;
}

.about-text p { margin-bottom: 20px; }

.about-values {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.value-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 24px 0;
  border-bottom: 1px solid var(--border);
}

.value-item:last-child { border-bottom: none; }

.value-icon {
  width: 40px;
  height: 40px;
  background: var(--forest);
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  margin-top: 2px;
}

.value-label {
  font-weight: 600;
  font-size: 14px;
  color: var(--forest);
  margin-bottom: 4px;
}

.value-desc {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.6;
}

/* ── Skills ── */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
}

.skill-card {
  background: white;
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 32px;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}

.skill-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 3px; height: 100%;
  background: var(--sage);
}

.skill-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.08);
}

.skill-category {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--sage);
  margin-bottom: 16px;
}

.skill-name {
  font-family: 'DM Serif Display', serif;
  font-size: 22px;
  color: var(--ink);
  margin-bottom: 20px;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.skill-tag {
  background: var(--cream);
  border: 1px solid var(--border);
  font-size: 12px;
  font-weight: 500;
  color: var(--charcoal);
  padding: 4px 12px;
  border-radius: 2px;
}

/* ── Projects ── */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}

.project-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 4px;
  padding: 36px;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  background: rgba(255,255,255,0.07);
  border-color: rgba(111,191,160,0.35);
  transform: translateY(-2px);
}

.project-card-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 18px;
}

.project-num {
  font-family: 'DM Serif Display', serif;
  font-style: italic;
  font-size: 48px;
  color: rgba(111,191,160,0.18);
  line-height: 1;
  flex-shrink: 0;
}

.project-icon {
  font-size: 30px;
  line-height: 1;
}

.project-name {
  font-family: 'DM Serif Display', serif;
  font-size: 23px;
  color: var(--cream);
  margin-bottom: 14px;
  line-height: 1.25;
}

.project-desc {
  font-size: 14px;
  line-height: 1.8;
  color: rgba(245,242,236,0.62);
  margin-bottom: 24px;
  flex: 1;
}

.project-metrics {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}

.metric-badge {
  background: rgba(111,191,160,0.15);
  border: 1px solid rgba(111,191,160,0.30);
  color: var(--mint);
  font-size: 12px;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 2px;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.project-tag {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.10);
  color: rgba(245,242,236,0.45);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 1px;
  padding: 4px 10px;
  border-radius: 2px;
  text-transform: uppercase;
}

/* ── Experience ── */
.exp-timeline {
  border-left: 2px solid var(--border);
  padding-left: 36px;
}

.exp-item {
  padding-bottom: 48px;
}

.exp-item:last-child { padding-bottom: 0; }

.exp-period {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--sage);
  margin-bottom: 8px;
}

.exp-period::before {
  content: '';
  display: inline-block;
  width: 10px; height: 10px;
  background: var(--sage);
  border-radius: 50%;
  border: 2px solid var(--cream);
  box-shadow: 0 0 0 2px var(--sage);
  flex-shrink: 0;
  margin-left: -42px;
  margin-right: 6px;
}

.exp-role {
  font-family: 'DM Serif Display', serif;
  font-size: 26px;
  color: var(--ink);
  margin-bottom: 4px;
}

.exp-company {
  font-size: 14px;
  color: var(--muted);
  margin-bottom: 20px;
  font-style: italic;
}

.exp-points {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.exp-points li {
  font-size: 15px;
  line-height: 1.65;
  color: #3A3830;
  display: flex;
  gap: 12px;
}

.exp-points li::before {
  content: '—';
  color: var(--mint);
  flex-shrink: 0;
  font-weight: 300;
}

/* ── Education ── */
.edu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.edu-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 4px;
  padding: 32px;
  position: relative;
  overflow: hidden;
}

.edu-card::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--mint), var(--gold));
}

.edu-degree {
  font-family: 'DM Serif Display', serif;
  font-size: 20px;
  color: var(--cream);
  margin-bottom: 10px;
  line-height: 1.3;
}

.edu-school {
  font-size: 13px;
  color: var(--mint);
  margin-bottom: 6px;
  font-weight: 500;
}

.edu-location {
  font-size: 12px;
  color: rgba(245,242,236,0.40);
  letter-spacing: 1px;
}

/* ── Contact ── */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: start;
}

.contact-intro {
  font-family: 'DM Serif Display', serif;
  font-size: 36px;
  line-height: 1.2;
  margin-bottom: 24px;
  color: var(--ink);
  letter-spacing: -0.5px;
}

.contact-sub {
  font-size: 15px;
  line-height: 1.75;
  color: var(--muted);
  margin-bottom: 36px;
}

.contact-links {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 0;
  border-bottom: 1px solid var(--border);
  text-decoration: none;
  color: var(--ink);
  transition: all 0.2s;
}

.contact-link:last-child { border-bottom: none; }

.contact-link:hover { color: var(--sage); }
.contact-link:hover .contact-link-icon { background: var(--forest); color: var(--mint); }

.contact-link-icon {
  width: 42px; height: 42px;
  background: var(--warm);
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  transition: all 0.2s;
  flex-shrink: 0;
}

.contact-link-label { font-size: 11px; color: var(--muted); letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 2px; }
.contact-link-value { font-size: 15px; font-weight: 500; }

/* ── Footer ── */
.footer {
  background: var(--ink);
  color: rgba(245,242,236,0.35);
  text-align: center;
  padding: 28px;
  font-size: 13px;
  letter-spacing: 0.5px;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .hero { padding: 64px 28px 56px; }
  .section { padding: 64px 28px; }
  .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 40px; }
  .stat-cell { padding: 28px 24px; }
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div class="hero-tag">⚡ Available for Opportunities</div>
  <div class="hero-name">Khushal<br><span>Patel</span></div>
  <div class="hero-title">Data Scientist · Machine Learning Engineer · Software Developer</div>
  <div class="hero-desc">
    Building intelligent, end-to-end analytical solutions — from raw data to deployed models.
    Passionate about energy systems, emissions reduction, and AI that creates real-world impact.
  </div>
  <div class="hero-contacts">
    <a class="hero-contact-item" href="mailto:patelkhushal222@gmail.com">
      📧 patelkhushal222@gmail.com
    </a>
    <a class="hero-contact-item" href="tel:+14033977009">
      📞 +1 (403) 397-7009
    </a>
    <span class="hero-contact-item">📍 Calgary, Canada</span>
  </div>
  <a class="hero-cta" href="mailto:patelkhushal222@gmail.com">Get in Touch</a>
  <a class="hero-cta-ghost" href="https://github.com/Khushal8320" target="_blank">GitHub ↗</a>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# STATS STRIP
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="stats-strip">
  <div class="stat-cell"><span class="stat-num">93%</span><div class="stat-label">Patient Recall (Triage AI)</div></div>
  <div class="stat-cell"><span class="stat-num">90%</span><div class="stat-label">Model Accuracy (Housing)</div></div>
  <div class="stat-cell"><span class="stat-num">25%</span><div class="stat-label">App Response Time Improved</div></div>
  <div class="stat-cell"><span class="stat-num">40%</span><div class="stat-label">Triage Workload Reduced</div></div>
  <div class="stat-cell"><span class="stat-num">3+</span><div class="stat-label">Years Experience</div></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section">
  <div class="section-header">
    <span class="section-num">01</span>
    <span class="section-title">About Me</span>
    <span class="section-line"></span>
  </div>
  <div class="about-grid">
    <div class="about-text">
      <p>
        I'm a Data Science and Machine Learning professional based in Calgary, Canada, with a
        background spanning industrial analytics, healthcare AI, and full-stack software development.
        My work bridges rigorous statistical thinking with production-grade engineering — I care
        equally about the math behind a model and the system that puts it into practice.
      </p>
      <p>
        With dual post-graduate credentials in Artificial Intelligence and Data Science from SAIT,
        and hands-on software engineering experience in Agile teams, I approach problems with both
        depth and pragmatism.
      </p>
      <p>
        I'm particularly drawn to applications in energy systems, emissions reduction, and industrial
        analytics — domains where better data and smarter models can have lasting environmental and
        social impact.
      </p>
    </div>
    <div class="about-values">
      <div class="value-item">
        <div class="value-icon">🎯</div>
        <div>
          <div class="value-label">Impact-Driven</div>
          <div class="value-desc">Every model I build serves a real decision. I measure success by the value delivered, not just the metric achieved.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">🌿</div>
        <div>
          <div class="value-label">Sustainability Focus</div>
          <div class="value-desc">Deep interest in energy systems and emissions analytics — using data to accelerate the energy transition.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">🤝</div>
        <div>
          <div class="value-label">Collaborative Builder</div>
          <div class="value-desc">Experienced in Agile teams, code reviews, and communicating results clearly to both technical and non-technical stakeholders.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">📐</div>
        <div>
          <div class="value-label">End-to-End Ownership</div>
          <div class="value-desc">From data wrangling and EDA through model training, evaluation, and Streamlit deployment — I own the full pipeline.</div>
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-alt">
  <div class="section-header">
    <span class="section-num">02</span>
    <span class="section-title">Technical Skills</span>
    <span class="section-line"></span>
  </div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-category">Core Languages</div>
      <div class="skill-name">Programming</div>
      <div class="skill-tags">
        <span class="skill-tag">Python</span>
        <span class="skill-tag">SQL</span>
        <span class="skill-tag">Ruby</span>
        <span class="skill-tag">JavaScript</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-category">Machine Learning & Data</div>
      <div class="skill-name">ML & Analytics</div>
      <div class="skill-tags">
        <span class="skill-tag">Scikit-learn</span>
        <span class="skill-tag">Pandas</span>
        <span class="skill-tag">NumPy</span>
        <span class="skill-tag">Feature Engineering</span>
        <span class="skill-tag">Model Evaluation</span>
        <span class="skill-tag">Classification</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-category">Frameworks & Tools</div>
      <div class="skill-name">Development</div>
      <div class="skill-tags">
        <span class="skill-tag">Ruby on Rails</span>
        <span class="skill-tag">React.js</span>
        <span class="skill-tag">Streamlit</span>
        <span class="skill-tag">Git</span>
        <span class="skill-tag">GitHub</span>
        <span class="skill-tag">REST APIs</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-category">Practices & Methods</div>
      <div class="skill-name">Engineering</div>
      <div class="skill-tags">
        <span class="skill-tag">Agile / Scrum</span>
        <span class="skill-tag">Code Review</span>
        <span class="skill-tag">API Integration</span>
        <span class="skill-tag">EDA</span>
        <span class="skill-tag">Data Wrangling</span>
        <span class="skill-tag">Dashboard Design</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-dark">
  <div class="section-header">
    <span class="section-num" style="color:var(--mint)">03</span>
    <span class="section-title" style="color:var(--cream)">Featured Projects</span>
    <span class="section-line"></span>
  </div>
  <div class="projects-grid">

    <div class="project-card">
      <div class="project-card-top">
        <span class="project-icon">🏥</span>
        <span class="project-num">01</span>
      </div>
      <div class="project-name">Emergency Triage ML Application</div>
      <div class="project-desc">
        A machine learning–based triage system that prioritizes emergency patients using clinical
        features and symptom data. Built a real-time Streamlit dashboard providing severity
        classification and probability-based clinical recommendations for frontline decision support.
      </div>
      <div class="project-metrics">
        <span class="metric-badge">92% Critical Patient Recall</span>
        <span class="metric-badge">40% Workload Reduction</span>
      </div>
      <div class="project-tags">
        <span class="project-tag">Python</span>
        <span class="project-tag">Scikit-learn</span>
        <span class="project-tag">Streamlit</span>
        <span class="project-tag">Healthcare AI</span>
      </div>
    </div>

    <div class="project-card">
      <div class="project-card-top">
        <span class="project-icon">🏠</span>
        <span class="project-num">02</span>
      </div>
      <div class="project-name">Ames Housing Price Prediction</div>
      <div class="project-desc">
        End-to-end regression pipeline for predicting residential housing prices. Focused on advanced
        feature engineering and ensemble classification techniques to achieve high predictive accuracy
        across the Ames dataset.
      </div>
      <div class="project-metrics">
        <span class="metric-badge">~90% Model Accuracy</span>
      </div>
      <div class="project-tags">
        <span class="project-tag">Python</span>
        <span class="project-tag">Pandas</span>
        <span class="project-tag">Feature Engineering</span>
        <span class="project-tag">Regression</span>
      </div>
    </div>

    <div class="project-card">
      <div class="project-card-top">
        <span class="project-icon">🛡️</span>
        <span class="project-num">03</span>
      </div>
      <div class="project-name">E-Commerce Fraud Detection</div>
      <div class="project-desc">
        Supervised classification system to detect fraudulent e-commerce transactions. Carefully
        balanced precision and recall to minimize false positives while maintaining high fraud
        detection sensitivity, improving trust and reducing costly manual reviews.
      </div>
      <div class="project-metrics">
        <span class="metric-badge">95% Precision</span>
        <span class="metric-badge">30% Fewer False Positives</span>
      </div>
      <div class="project-tags">
        <span class="project-tag">Python</span>
        <span class="project-tag">Scikit-learn</span>
        <span class="project-tag">Classification</span>
        <span class="project-tag">Fraud Analytics</span>
      </div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section">
  <div class="section-header">
    <span class="section-num">04</span>
    <span class="section-title">Experience</span>
    <span class="section-line"></span>
  </div>
  <div class="exp-timeline">
    <div class="exp-item">
      <div class="exp-period">July 2023 – October 2024</div>
      <div class="exp-role">Software Developer</div>
      <div class="exp-company">Bacancy Services Ltd. · India</div>
      <ul class="exp-points">
        <li>Supported the development and maintenance of scalable web applications using Ruby on Rails and React.js within cross-functional Agile teams.</li>
        <li>Improved application response time by 25% through systematic optimization of backend logic and database queries.</li>
        <li>Delivered production features with zero critical defects by actively participating in code reviews and sprint planning processes.</li>
        <li>Implemented API integrations to bridge backend services with frontend functionality, enhancing overall application reliability.</li>
      </ul>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-dark">
  <div class="section-header">
    <span class="section-num" style="color:var(--mint)">05</span>
    <span class="section-title" style="color:var(--cream)">Education</span>
    <span class="section-line"></span>
  </div>
  <div class="edu-grid">
    <div class="edu-card">
      <div class="edu-degree">Integrated Artificial Intelligence Post-Diploma</div>
      <div class="edu-school">Southern Alberta Institute of Technology</div>
      <div class="edu-location">📍 Calgary, Alberta, Canada</div>
    </div>
    <div class="edu-card">
      <div class="edu-degree">Data Science Post-Graduate Certificate</div>
      <div class="edu-school">Southern Alberta Institute of Technology</div>
      <div class="edu-location">📍 Calgary, Alberta, Canada</div>
    </div>
    <div class="edu-card">
      <div class="edu-degree">Bachelor of Information Technology</div>
      <div class="edu-school">Gujarat Technological University</div>
      <div class="edu-location">📍 Gujarat, India</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-alt">
  <div class="section-header">
    <span class="section-num">06</span>
    <span class="section-title">Let's Connect</span>
    <span class="section-line"></span>
  </div>
  <div class="contact-grid">
    <div>
      <div class="contact-intro">Open to roles in Data Science & ML Engineering</div>
      <div class="contact-sub">
        Whether you're building an analytics team, exploring AI-driven products, or looking for
        someone who can go from raw data to a deployed model — I'd love to hear from you.
        Currently based in Calgary, open to hybrid and remote opportunities.
      </div>
    </div>
    <div class="contact-links">
      <a class="contact-link" href="mailto:patelkhushal222@gmail.com">
        <div class="contact-link-icon">📧</div>
        <div>
          <div class="contact-link-label">Email</div>
          <div class="contact-link-value">patelkhushal222@gmail.com</div>
        </div>
      </a>
      <a class="contact-link" href="tel:+14033977009">
        <div class="contact-link-icon">📞</div>
        <div>
          <div class="contact-link-label">Phone</div>
          <div class="contact-link-value">+1 (403) 397-7009</div>
        </div>
      </a>
      <a class="contact-link" href="https://www.linkedin.com/in/khushal-patel-215b20343" target="_blank">
        <div class="contact-link-icon">💼</div>
        <div>
          <div class="contact-link-label">LinkedIn</div>
          <div class="contact-link-value">khushal-patel-215b20343</div>
        </div>
      </a>
      <a class="contact-link" href="https://github.com/Khushal8320" target="_blank">
        <div class="contact-link-icon">🐙</div>
        <div>
          <div class="contact-link-label">GitHub</div>
          <div class="contact-link-value">Khushal8320</div>
        </div>
      </a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  Designed & built with Streamlit · Khushal Patel © 2025 · Calgary, Canada
</div>
""", unsafe_allow_html=True)
