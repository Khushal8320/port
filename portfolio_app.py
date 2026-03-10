import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Khushal Patel · Data Scientist",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default chrome
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.stAppDeployButton { display: none; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stDecoration"] { display: none; }
.stApp { background: #163529 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; display: block; }
</style>
""", unsafe_allow_html=True)

# Full portfolio via components.html — bypasses Streamlit's HTML sanitizer completely
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --cream: #F5F2EC; --ink: #0F0E0C; --charcoal: #1A1917;
  --forest: #163529; --sage: #2E6B4F; --mint: #5DBFA0;
  --gold: #C9A84C; --warm: #EDE8DF; --border: #D5CCBC; --muted: #7A7468;
}
html { scroll-behavior: smooth; }
body { font-family: 'DM Sans', sans-serif; background: var(--cream); color: var(--ink); margin: 0; overflow-x: hidden; }

/* NAV */
nav {
  background: rgba(22,53,41,0.99);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 60px; height: 64px;
  border-bottom: 1px solid rgba(93,191,160,0.15);
  position: sticky; top: 0; z-index: 100;
}
.nav-logo { font-family: 'DM Serif Display', serif; font-size: 20px; color: var(--cream); letter-spacing: -0.3px; }
.nav-logo span { color: var(--mint); }
.nav-links { display: flex; gap: 32px; list-style: none; }
.nav-links a { font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: rgba(245,242,236,0.55); text-decoration: none; transition: color 0.2s; }
.nav-links a:hover { color: var(--mint); }
.nav-cta { background: var(--gold) !important; color: var(--charcoal) !important; padding: 8px 20px; border-radius: 2px; }

/* HERO */
#hero {
  background: var(--forest);
  background-image: radial-gradient(ellipse 90% 70% at 75% 55%, rgba(93,191,160,0.16) 0%, transparent 65%), radial-gradient(ellipse 50% 90% at 5% 85%, rgba(201,168,76,0.12) 0%, transparent 55%);
  color: var(--cream); padding: 100px 80px 80px;
  position: relative; overflow: hidden;
}
.ring { position: absolute; border-radius: 50%; pointer-events: none; }
.r1 { width: 440px; height: 440px; top: -80px; right: -80px; border: 1px solid rgba(93,191,160,0.18); animation: spin 30s linear infinite; }
.r2 { width: 280px; height: 280px; top: 40px; right: 40px; border: 1px solid rgba(201,168,76,0.12); animation: spin 20s linear infinite reverse; }
.r3 { width: 200px; height: 200px; bottom: -60px; left: 80px; border: 1px solid rgba(93,191,160,0.10); }
@keyframes spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
.hero-content { max-width: 720px; position: relative; z-index: 2; }
.hero-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(93,191,160,0.15); border: 1px solid rgba(93,191,160,0.40); color: var(--mint); font-size: 11px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; padding: 7px 18px; border-radius: 2px; margin-bottom: 32px; }
.bdot { width: 6px; height: 6px; background: var(--mint); border-radius: 50%; animation: pulse 2s ease infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.4;transform:scale(0.6)} }
.hero-name { font-family: 'DM Serif Display', serif; font-size: clamp(56px,8vw,96px); line-height: 0.95; letter-spacing: -3px; color: var(--cream); margin-bottom: 14px; }
.hero-name .accent { color: var(--mint); }
.hero-title { font-size: 16px; font-weight: 300; letter-spacing: 1px; color: rgba(245,242,236,0.50); margin-bottom: 28px; }
.hero-desc { font-size: 15.5px; line-height: 1.8; color: rgba(245,242,236,0.75); max-width: 500px; margin-bottom: 40px; border-left: 2px solid var(--mint); padding-left: 20px; }
.hero-contacts { display: flex; flex-wrap: wrap; gap: 24px; margin-bottom: 40px; }
.hc { display: flex; align-items: center; gap: 8px; font-size: 13px; color: rgba(245,242,236,0.60); text-decoration: none; transition: color 0.2s; }
.hc:hover { color: var(--mint); }
.hero-actions { display: flex; gap: 14px; flex-wrap: wrap; }
.btn-gold { display: inline-flex; align-items: center; gap: 8px; background: var(--gold); color: var(--charcoal); font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; padding: 14px 32px; border-radius: 2px; text-decoration: none; transition: all 0.2s; }
.btn-gold:hover { background: #d4b358; transform: translateY(-1px); }
.btn-out { display: inline-flex; align-items: center; gap: 8px; border: 1px solid rgba(245,242,236,0.28); color: rgba(245,242,236,0.80); font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; padding: 14px 32px; border-radius: 2px; text-decoration: none; transition: all 0.2s; }
.btn-out:hover { border-color: var(--mint); color: var(--mint); }

/* STATS */
.stats { background: var(--charcoal); display: grid; grid-template-columns: repeat(5,1fr); }
.stat { padding: 40px 20px; text-align: center; border-right: 1px solid rgba(255,255,255,0.05); }
.stat:last-child { border-right: none; }
.snum { font-family: 'DM Serif Display', serif; font-size: 42px; color: var(--mint); display: block; line-height: 1; margin-bottom: 10px; }
.slbl { font-size: 10px; font-weight: 600; letter-spacing: 2.5px; text-transform: uppercase; color: rgba(255,255,255,0.32); line-height: 1.5; }

/* SECTIONS */
.sec { padding: 88px 80px; }
.sec-warm { background: var(--warm); }
.sec-dark { background: var(--charcoal); color: var(--cream); }
.sec-hd { display: flex; align-items: center; gap: 16px; margin-bottom: 56px; }
.sn { font-family: 'DM Serif Display', serif; font-style: italic; font-size: 14px; color: var(--mint); min-width: 24px; }
.st { font-family: 'DM Serif Display', serif; font-size: 44px; letter-spacing: -1px; white-space: nowrap; }
.sl { flex: 1; height: 1px; background: var(--border); }
.sec-dark .sl { background: rgba(255,255,255,0.08); }

/* ABOUT */
.about-g { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 64px; align-items: start; }
.atext { font-size: 15.5px; line-height: 1.9; color: #3A3830; }
.atext p { margin-bottom: 20px; }
.atext p:last-child { margin-bottom: 0; }
.hl { color: var(--sage); font-weight: 600; }
.vals { display: flex; flex-direction: column; }
.val { display: flex; align-items: flex-start; gap: 16px; padding: 20px 0; border-bottom: 1px solid var(--border); transition: padding-left 0.2s; }
.val:first-child { padding-top: 0; }
.val:last-child { border-bottom: none; }
.val:hover { padding-left: 6px; }
.vico { width: 42px; height: 42px; background: var(--forest); border-radius: 2px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
.vt { font-weight: 600; font-size: 13px; color: var(--forest); margin-bottom: 4px; }
.vd { font-size: 13px; color: var(--muted); line-height: 1.6; }

/* SKILLS */
.skills-g { display: grid; grid-template-columns: repeat(4,1fr); gap: 22px; }
.skcard { background: white; border: 1px solid var(--border); border-radius: 3px; padding: 28px; transition: all 0.25s; border-top: 3px solid var(--sage); }
.skcard:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.09); }
.skcat { font-size: 9px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--sage); margin-bottom: 12px; }
.skname { font-family: 'DM Serif Display', serif; font-size: 20px; color: var(--ink); margin-bottom: 18px; }
.tags { display: flex; flex-wrap: wrap; gap: 7px; }
.tag { background: var(--cream); border: 1px solid var(--border); font-size: 11px; font-weight: 500; color: var(--charcoal); padding: 4px 11px; border-radius: 2px; }

/* PROJECTS */
.proj-g { display: grid; grid-template-columns: repeat(3,1fr); gap: 22px; }
.pcard { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.09); border-radius: 3px; padding: 36px; display: flex; flex-direction: column; transition: all 0.25s; border-bottom: 2px solid transparent; }
.pcard:hover { background: rgba(255,255,255,0.08); border-bottom-color: var(--mint); transform: translateY(-3px); }
.ptop { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
.pico { font-size: 30px; line-height: 1; }
.pnum { font-family: 'DM Serif Display', serif; font-style: italic; font-size: 44px; color: rgba(93,191,160,0.18); line-height: 1; }
.pname { font-family: 'DM Serif Display', serif; font-size: 22px; color: var(--cream); margin-bottom: 12px; line-height: 1.3; }
.pdesc { font-size: 14px; line-height: 1.8; color: rgba(245,242,236,0.62); margin-bottom: 24px; flex: 1; }
.pmets { display: flex; flex-wrap: wrap; gap: 9px; margin-bottom: 20px; }
.met { background: rgba(93,191,160,0.14); border: 1px solid rgba(93,191,160,0.28); color: var(--mint); font-size: 12px; font-weight: 600; padding: 5px 12px; border-radius: 2px; }
.ptags { display: flex; flex-wrap: wrap; gap: 7px; }
.ptag { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); color: rgba(245,242,236,0.38); font-size: 10px; font-weight: 600; letter-spacing: 1.5px; padding: 4px 10px; border-radius: 2px; text-transform: uppercase; }

/* EXPERIENCE */
.exp-g { display: grid; grid-template-columns: 260px 1fr; gap: 72px; align-items: start; }
.exp-aside-lbl { font-size: 10px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--sage); margin-bottom: 16px; }
.exp-aside-t { font-family: 'DM Serif Display', serif; font-size: 30px; color: var(--ink); margin-bottom: 14px; line-height: 1.2; }
.exp-aside-d { font-size: 13.5px; line-height: 1.7; color: var(--muted); }
.timeline { border-left: 2px solid var(--border); padding-left: 32px; }
.exp-item { padding-bottom: 48px; }
.exp-item:last-child { padding-bottom: 0; }
.ep-wrap { display: flex; align-items: center; margin-bottom: 8px; margin-left: -40px; gap: 12px; }
.edot { width: 12px; height: 12px; background: var(--sage); border-radius: 50%; border: 2.5px solid var(--cream); box-shadow: 0 0 0 2.5px var(--sage); flex-shrink: 0; }
.eperiod { font-size: 10px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; color: var(--sage); }
.erole { font-family: 'DM Serif Display', serif; font-size: 28px; color: var(--ink); margin-bottom: 4px; }
.ecomp { font-size: 13px; color: var(--muted); margin-bottom: 20px; font-style: italic; }
.epoints { list-style: none; display: flex; flex-direction: column; gap: 12px; }
.epoints li { font-size: 14.5px; line-height: 1.7; color: #3A3830; display: flex; gap: 12px; align-items: flex-start; }
.epoints li::before { content: '→'; color: var(--mint); flex-shrink: 0; font-size: 13px; margin-top: 3px; }
.echips { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 22px; }
.echip { background: var(--warm); border: 1px solid var(--border); font-size: 11px; font-weight: 600; color: var(--forest); padding: 5px 13px; border-radius: 2px; }

/* EDUCATION */
.edu-g { display: grid; grid-template-columns: repeat(3,1fr); gap: 22px; }
.ecard { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 3px; padding: 34px; transition: all 0.25s; border-bottom: 2px solid transparent; }
.ecard:hover { background: rgba(255,255,255,0.08); border-bottom-color: var(--gold); transform: translateY(-3px); }
.eico { font-size: 28px; margin-bottom: 18px; display: block; }
.edeg { font-family: 'DM Serif Display', serif; font-size: 21px; color: var(--cream); margin-bottom: 12px; line-height: 1.3; }
.eschool { font-size: 13px; color: var(--mint); margin-bottom: 8px; font-weight: 500; }
.eloc { font-size: 12px; color: rgba(245,242,236,0.35); }

/* CONTACT */
.contact-g { display: grid; grid-template-columns: 1fr 1fr; gap: 72px; align-items: start; }
.chd { font-family: 'DM Serif Display', serif; font-size: 40px; line-height: 1.1; color: var(--ink); margin-bottom: 16px; letter-spacing: -1px; }
.chd span { color: var(--sage); }
.csub { font-size: 15px; line-height: 1.8; color: var(--muted); margin-bottom: 28px; }
.abadge { display: inline-flex; align-items: center; gap: 8px; background: white; border: 1px solid var(--border); padding: 10px 18px; border-radius: 2px; font-size: 13px; color: var(--muted); }
.gdot { width: 8px; height: 8px; background: #4CAF50; border-radius: 50%; animation: pulse 2s ease infinite; }
.clinks { display: flex; flex-direction: column; }
.clink { display: flex; align-items: center; gap: 16px; padding: 18px 0; border-bottom: 1px solid var(--border); text-decoration: none; color: var(--ink); transition: all 0.2s; }
.clink:last-child { border-bottom: none; }
.clink:hover { padding-left: 8px; color: var(--sage); }
.clink:hover .cion { background: var(--forest); }
.cion { width: 44px; height: 44px; background: var(--warm); border-radius: 2px; display: flex; align-items: center; justify-content: center; font-size: 19px; flex-shrink: 0; transition: background 0.2s; }
.clbl { font-size: 10px; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 2px; }
.cval { font-size: 14px; font-weight: 500; }

/* FOOTER */
footer { background: var(--ink); color: rgba(245,242,236,0.25); text-align: center; padding: 28px; font-size: 12px; letter-spacing: 1px; }
footer span { color: var(--mint); }

@media (max-width: 900px) {
  .about-g, .contact-g, .exp-g { grid-template-columns: 1fr; gap: 40px; }
  .skills-g, .proj-g, .edu-g { grid-template-columns: 1fr; }
  .stats { grid-template-columns: repeat(2,1fr); }
  nav { padding: 0 24px; }
  .nav-links { display: none; }
  .sec { padding: 64px 28px; }
  #hero { padding: 80px 28px 60px; }
}
</style>
</head>
<body>

<nav>
  <div class="nav-logo">KP<span>.</span></div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#education">Education</a></li>
    <li><a href="#contact" class="nav-cta">Hire Me</a></li>
  </ul>
</nav>

<section id="hero">
  <div class="ring r1"></div>
  <div class="ring r2"></div>
  <div class="ring r3"></div>
  <div class="hero-content">
    <div class="hero-badge"><div class="bdot"></div>&nbsp;Open to Opportunities</div>
    <div class="hero-name">Khushal<br><span class="accent">Patel</span></div>
    <div class="hero-title">Data Scientist &nbsp;·&nbsp; ML Engineer &nbsp;·&nbsp; Software Developer</div>
    <div class="hero-desc">Building intelligent, end-to-end analytical solutions — from raw data to deployed models. Passionate about energy systems, emissions reduction, and AI that drives real-world impact.</div>
    <div class="hero-contacts">
      <a class="hc" href="mailto:patelkhushal222@gmail.com">📧 patelkhushal222@gmail.com</a>
      <a class="hc" href="tel:+14033977009">📞 +1 (403) 397-7009</a>
      <span class="hc">📍 Calgary, Canada</span>
    </div>
    <div class="hero-actions">
      <a class="btn-gold" href="mailto:patelkhushal222@gmail.com">Get in Touch →</a>
      <a class="btn-out" href="https://github.com/Khushal8320" target="_blank">GitHub ↗</a>
      <a class="btn-out" href="https://www.linkedin.com/in/khushal-patel-215b20343" target="_blank">LinkedIn ↗</a>
    </div>
  </div>
</section>

<div class="stats">
  <div class="stat"><span class="snum">93%</span><div class="slbl">Critical Patient<br>Recall</div></div>
  <div class="stat"><span class="snum">~90%</span><div class="slbl">Housing Model<br>Accuracy</div></div>
  <div class="stat"><span class="snum">25%</span><div class="slbl">App Response<br>Improved</div></div>
  <div class="stat"><span class="snum">40%</span><div class="slbl">Triage Workload<br>Reduced</div></div>
  <div class="stat"><span class="snum">2+</span><div class="slbl">Years<br>Experience</div></div>
</div>

<section id="about" class="sec">
  <div class="sec-hd"><span class="sn">01</span><span class="st">About Me</span><span class="sl"></span></div>
  <div class="about-g">
    <div class="atext">
      <p>I'm a <span class="hl">Data Science and Machine Learning professional</span> based in Calgary, Canada, with a background spanning industrial analytics, healthcare AI, and full-stack software development. My work bridges rigorous statistical thinking with production-grade engineering.</p>
      <p>With dual post-graduate credentials in <span class="hl">Artificial Intelligence and Data Science</span> from SAIT, and hands-on software engineering experience in Agile teams, I approach problems with both depth and pragmatism.</p>
      <p>I'm particularly drawn to applications in <span class="hl">energy systems, emissions reduction, and industrial analytics</span> — domains where better data and smarter models can have lasting environmental and social impact.</p>
    </div>
    <div class="vals">
      <div class="val"><div class="vico">🎯</div><div><div class="vt">Impact-Driven</div><div class="vd">Every model serves a real decision. I measure success by value delivered, not just the metric achieved.</div></div></div>
      <div class="val"><div class="vico">🌿</div><div><div class="vt">Sustainability Focus</div><div class="vd">Deep interest in energy systems and emissions analytics — using data to accelerate the energy transition.</div></div></div>
      <div class="val"><div class="vico">🤝</div><div><div class="vt">Collaborative Builder</div><div class="vd">Experienced in Agile teams, communicating results clearly to both technical and non-technical stakeholders.</div></div></div>
      <div class="val"><div class="vico">📐</div><div><div class="vt">End-to-End Ownership</div><div class="vd">From data wrangling and EDA through model training, evaluation, and Streamlit deployment — I own the full pipeline.</div></div></div>
    </div>
  </div>
</section>

<section id="skills" class="sec sec-warm">
  <div class="sec-hd"><span class="sn">02</span><span class="st">Technical Skills</span><span class="sl"></span></div>
  <div class="skills-g">
    <div class="skcard"><div class="skcat">Core Languages</div><div class="skname">Programming</div><div class="tags"><span class="tag">Python</span><span class="tag">SQL</span><span class="tag">Ruby</span><span class="tag">JavaScript</span></div></div>
    <div class="skcard"><div class="skcat">Machine Learning & Data</div><div class="skname">ML & Analytics</div><div class="tags"><span class="tag">Scikit-learn</span><span class="tag">Pandas</span><span class="tag">NumPy</span><span class="tag">Feature Engineering</span><span class="tag">Model Evaluation</span><span class="tag">Classification</span></div></div>
    <div class="skcard"><div class="skcat">Frameworks & Tools</div><div class="skname">Development</div><div class="tags"><span class="tag">Ruby on Rails</span><span class="tag">React.js</span><span class="tag">Streamlit</span><span class="tag">Git / GitHub</span><span class="tag">REST APIs</span></div></div>
    <div class="skcard"><div class="skcat">Practices & Methods</div><div class="skname">Engineering</div><div class="tags"><span class="tag">Agile / Scrum</span><span class="tag">Code Review</span><span class="tag">EDA</span><span class="tag">Data Wrangling</span><span class="tag">Dashboard Design</span></div></div>
  </div>
</section>

<section id="projects" class="sec sec-dark">
  <div class="sec-hd"><span class="sn" style="color:var(--mint)">03</span><span class="st">Featured Projects</span><span class="sl"></span></div>
  <div class="proj-g">

    <div class="pcard">
      <div class="ptop"><span class="pico">🏥</span><span class="pnum">01</span></div>
      <div class="pname">Emergency Triage ML Application</div>
      <div class="pdesc">A machine learning–based triage system that prioritizes emergency patients using clinical features and symptom data. Built a real-time Streamlit dashboard providing severity classification and probability-based clinical recommendations for frontline decision support.</div>
      <div class="pmets"><span class="met">92% Critical Patient Recall</span><span class="met">40% Workload Reduction</span></div>
      <div class="ptags"><span class="ptag">Python</span><span class="ptag">Scikit-learn</span><span class="ptag">Streamlit</span><span class="ptag">Healthcare AI</span></div>
    </div>

    <div class="pcard">
      <div class="ptop"><span class="pico">🏠</span><span class="pnum">02</span></div>
      <div class="pname">Ames Housing Price Prediction</div>
      <div class="pdesc">End-to-end regression pipeline for predicting residential housing prices. Focused on advanced feature engineering and ensemble classification techniques to achieve high predictive accuracy across the full Ames dataset.</div>
      <div class="pmets"><span class="met">~90% Model Accuracy</span></div>
      <div class="ptags"><span class="ptag">Python</span><span class="ptag">Pandas</span><span class="ptag">Feature Engineering</span><span class="ptag">Regression</span></div>
    </div>

    <div class="pcard">
      <div class="ptop"><span class="pico">🛡️</span><span class="pnum">03</span></div>
      <div class="pname">E-Commerce Fraud Detection</div>
      <div class="pdesc">Supervised classification system to detect fraudulent e-commerce transactions. Carefully balanced precision and recall to minimize false positives while maintaining high detection sensitivity, reducing costly manual review overhead.</div>
      <div class="pmets"><span class="met">95% Precision</span><span class="met">30% Fewer False Positives</span></div>
      <div class="ptags"><span class="ptag">Python</span><span class="ptag">Scikit-learn</span><span class="ptag">Classification</span><span class="ptag">Fraud Analytics</span></div>
    </div>

  </div>
</section>

<section id="experience" class="sec">
  <div class="sec-hd"><span class="sn">04</span><span class="st">Experience</span><span class="sl"></span></div>
  <div class="exp-g">
    <div>
      <div class="exp-aside-lbl">Work History</div>
      <div class="exp-aside-t">Building things that matter</div>
      <div class="exp-aside-d">From production web apps to data pipelines — every role has sharpened my ability to deliver reliable, scalable solutions in team environments.</div>
    </div>
    <div class="timeline">
      <div class="exp-item">
        <div class="ep-wrap"><div class="edot"></div><div class="eperiod">July 2023 – October 2024</div></div>
        <div class="erole">Software Developer</div>
        <div class="ecomp">Bacancy Services Ltd. · India</div>
        <ul class="epoints">
          <li>Developed and maintained scalable web applications using Ruby on Rails and React.js within cross-functional Agile teams.</li>
          <li>Improved application response time by 25% through systematic optimization of backend logic and database queries.</li>
          <li>Delivered production features with zero critical defects by actively participating in code reviews and sprint planning.</li>
          <li>Implemented API integrations to bridge backend services with frontend functionality, enhancing overall application reliability.</li>
        </ul>
        <div class="echips"><span class="echip">Ruby on Rails</span><span class="echip">React.js</span><span class="echip">Agile</span><span class="echip">API Integration</span></div>
      </div>
    </div>
  </div>
</section>

<section id="education" class="sec sec-dark">
  <div class="sec-hd"><span class="sn" style="color:var(--mint)">05</span><span class="st">Education</span><span class="sl"></span></div>
  <div class="edu-g">
    <div class="ecard"><span class="eico">🤖</span><div class="edeg">Integrated Artificial Intelligence Post-Diploma</div><div class="eschool">Southern Alberta Institute of Technology</div><div class="eloc">📍 Calgary, Alberta, Canada</div></div>
    <div class="ecard"><span class="eico">📊</span><div class="edeg">Data Science Post-Graduate Certificate</div><div class="eschool">Southern Alberta Institute of Technology</div><div class="eloc">📍 Calgary, Alberta, Canada</div></div>
    <div class="ecard"><span class="eico">💻</span><div class="edeg">Bachelor of Information Technology</div><div class="eschool">Gujarat Technological University</div><div class="eloc">📍 Gujarat, India</div></div>
  </div>
</section>

<section id="contact" class="sec sec-warm">
  <div class="sec-hd"><span class="sn">06</span><span class="st">Let's Connect</span><span class="sl"></span></div>
  <div class="contact-g">
    <div>
      <div class="chd">Open to roles in <span>Data Science</span> & ML Engineering</div>
      <div class="csub">Whether you're building an analytics team, exploring AI-driven products, or need someone who can go from raw data to a deployed model — I'd love to hear from you. Currently based in Calgary, open to hybrid and remote opportunities across Canada.</div>
      <div class="abadge"><div class="gdot"></div>&nbsp;Available for new opportunities</div>
    </div>
    <div class="clinks">
      <a class="clink" href="mailto:patelkhushal222@gmail.com"><div class="cion">📧</div><div><div class="clbl">Email</div><div class="cval">patelkhushal222@gmail.com</div></div></a>
      <a class="clink" href="tel:+14033977009"><div class="cion">📞</div><div><div class="clbl">Phone</div><div class="cval">+1 (403) 397-7009</div></div></a>
      <a class="clink" href="https://www.linkedin.com/in/khushal-patel-215b20343" target="_blank"><div class="cion">💼</div><div><div class="clbl">LinkedIn</div><div class="cval">khushal-patel-215b20343</div></div></a>
      <a class="clink" href="https://github.com/Khushal8320" target="_blank"><div class="cion">🐙</div><div><div class="clbl">GitHub</div><div class="cval">Khushal8320</div></div></a>
    </div>
  </div>
</section>

<footer>Designed & built with ♥ &nbsp;·&nbsp; <span>Khushal Patel</span> © 2025 &nbsp;·&nbsp; Calgary, Canada</footer>

<script>
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector(a.getAttribute('href'))?.scrollIntoView({ behavior: 'smooth' });
    });
  });
</script>
</body>
</html>
""", height=5000, scrolling=True)
