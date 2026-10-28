"""v3 editorial design: paper, ink, one signal orange, embedded real type, varied motion."""
import os, base64, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")
FONTS = "/tmp/fonts"
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    os.remove(os.path.join(OUT, f))

PAPER, INK, ORANGE, MUTED, RULE, PAPER2 = "#F1ECE2", "#151412", "#FF4A1C", "#7B7468", "#D6CEBF", "#E8E1D3"

def font(name, fam, style="normal"):
    b = base64.b64encode(open(f"{FONTS}/{name}.woff2", "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-style:{style};src:url(data:font/woff2;base64,{b}) format('woff2');}}"

def fonts(*which):
    m = {"serif": ("serif", "IS", "normal"), "serifi": ("serif-i", "IS", "italic"), "mono": ("mono", "JB", "normal"),
         "sans": ("sans", "IT", "normal"), "sansb": ("sans-b", "ITB", "normal")}
    return "".join(font(*m[w]) for w in which)

BASE_CSS = """
.s{font-family:'IS',Georgia,serif}.si{font-family:'IS',Georgia,serif;font-style:italic}
.m{font-family:'JB',Consolas,monospace;letter-spacing:.08em}.t{font-family:'IT',Helvetica,Arial,sans-serif}.tb{font-family:'ITB',Helvetica,Arial,sans-serif}
.rise{animation:rise 1.1s cubic-bezier(.2,.8,.2,1) both}
@keyframes rise{from{transform:translateY(110%)}to{transform:none}}
.fade{animation:fade 1s ease both}@keyframes fade{from{opacity:0}to{opacity:1}}
.draw{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 1.6s cubic-bezier(.6,0,.2,1) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.spin{transform-box:fill-box;transform-origin:center;animation:spin 22s linear infinite}
.spinr{transform-box:fill-box;transform-origin:center;animation:spin 9s linear infinite reverse}
@keyframes spin{to{transform:rotate(360deg)}}
"""

def grain(i="g"):
    return f'<filter id="{i}"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0"/></filter>'

def asterisk(cx, cy, r, fill, cls=""):
    arms = "".join(f'<rect x="{cx - r*0.14}" y="{cy - r}" width="{r*0.28}" height="{2*r}" rx="{r*0.1}" transform="rotate({a} {cx} {cy})"/>' for a in (0, 60, 120))
    return f'<g class="{cls}" fill="{fill}">{arms}</g>'

def svg(w, h, css, body, defs="", rx=22, bg=PAPER, border=True):
    b = f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="{rx}" fill="none" stroke="{INK}" stroke-opacity=".14"/>' if border else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><style>{css}{BASE_CSS}</style>{grain()}<clipPath id="card"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath>{defs}</defs>
<g clip-path="url(#card)"><rect width="{w}" height="{h}" fill="{bg}"/>{body}<rect width="{w}" height="{h}" filter="url(#g)"/></g>{b}
</svg>'''

def save(n, s):
    open(os.path.join(OUT, n), "w").write(s)

def esc(t): return html.escape(t, quote=False)

# ------------------------------------------------------------------ HERO
def hero():
    W, H = 1200, 590
    css = fonts("serif", "serifi", "mono", "sans")
    items = ["AI AGENTS", "AGENTIC WORKFLOWS", "LLM APPS", "N8N AUTOMATION", "MACHINE LEARNING", "PRODUCT DESIGN"]
    # marquee: build one run, duplicate
    run, x = "", 0
    for it in items:
        run += f'<text x="{x}" y="38" class="m" font-size="17" fill="{INK}">{it}</text>'
        x += len(it) * 11.6 + 34
        run += asterisk(x - 17, 32, 8, INK)
        x += 20
    seg = x
    marquee = f'<g><g style="animation:mq 26s linear infinite">{run}<g transform="translate({seg},0)">{run}</g><g transform="translate({2*seg},0)">{run}</g></g></g>'
    badge_txt = "AI ENGINEER  \u2022  AGENTIC WORKFLOWS  \u2022  AUTOMATION  \u2022  "
    body = f'''
  <text x="56" y="62" class="m fade" font-size="13" fill="{INK}">KAIFI1199 / INDEX</text>
  <text x="{W/2}" y="62" text-anchor="middle" class="m fade" font-size="13" fill="{MUTED}">FAISALABAD, PK  31.42\u00b0N 73.08\u00b0E</text>
  <text x="{W-56}" y="62" text-anchor="end" class="m fade" font-size="13" fill="{INK}">EST. 2023</text>
  <line x1="56" y1="84" x2="{W-56}" y2="84" stroke="{INK}" stroke-width="1.2" class="draw"/>

  <svg x="0" y="96" width="{W}" height="190" overflow="hidden"><g class="rise" style="animation-delay:.15s">
    <text x="48" y="168" class="s" font-size="196" letter-spacing="-6" fill="{INK}">Muhammad</text></g></svg>
  <svg x="0" y="276" width="{W}" height="190" overflow="hidden"><g class="rise" style="animation-delay:.35s">
    <text x="50" y="164" class="si" font-size="196" letter-spacing="-5" fill="{INK}">Kaif<tspan fill="{ORANGE}">.</tspan></text></g></svg>

  <g class="fade" style="animation-delay:1s">
    <text x="520" y="368" class="m" font-size="13" fill="{ORANGE}">(ROLE)</text>
    <text x="520" y="400" class="t" font-size="23" fill="{INK}">AI engineer building agents and</text>
    <text x="520" y="430" class="t" font-size="23" fill="{INK}">automations that do real work, end</text>
    <text x="520" y="460" class="t" font-size="23" fill="{INK}">to end, from model to interface.</text>
  </g>

  <g transform="translate(1000,215)">
    <path id="circ" d="M 0,-92 a 92,92 0 1,1 -0.1,0" fill="none"/>
    <g class="spin"><circle r="118" fill="none"/><text class="m" font-size="15.2" fill="{INK}" letter-spacing="3"><textPath href="#circ" textLength="572" lengthAdjust="spacing">{badge_txt}</textPath></text></g>
    <circle r="62" fill="{ORANGE}"/>
    {asterisk(0, 0, 30, PAPER, "spinr")}
  </g>

  <g transform="translate(0,{H-64})">
    <rect width="{W}" height="64" fill="{ORANGE}"/>
    <svg width="{W}" height="64">{marquee}</svg>
  </g>
'''
    css += f"@keyframes mq{{to{{transform:translateX(-{seg}px)}}}}"
    save("hero.svg", svg(W, H, css, body))

# ------------------------------------------------------------------ ABOUT
def about():
    W, H = 1200, 540
    css = fonts("serif", "serifi", "mono", "sans")
    lines = [("I design and build ", ""), ("intelligent systems:", "i"), ("agents that read, decide and act,", ""), ("so people get their time back.", "")]
    stmt = ""
    for i, (t, st) in enumerate(lines):
        y = 150 + i * 62
        cls = "si" if st else "s"
        fill = ORANGE if st else INK
        stmt += f'<svg x="0" y="{y-56}" width="640" height="72" overflow="hidden"><g class="rise" style="animation-delay:{.2+i*.14:.2f}s"><text x="56" y="56" class="{cls}" font-size="56" letter-spacing="-1.2" fill="{fill}">{esc(t)}</text></g></svg>'
    rows = [("ROLE", "AI Engineer"), ("STUDIED", "BS Artificial Intelligence, NTU"), ("EXPERIENCE", "AI Engineer Intern, CosmiCode"),
            ("", "ML & NLP Intern, Elevvo Pathways"), ("BASED", "Faisalabad, Pakistan"), ("NEXT", "Master\u2019s in Germany")]
    spec, y = "", 120
    for i, (k, v) in enumerate(rows):
        d = .5 + i * .12
        if k:
            spec += f'<line x1="700" y1="{y-30}" x2="{W-56}" y2="{y-30}" stroke="{INK}" stroke-opacity=".25" class="draw" style="animation-delay:{d:.2f}s"/>'
        spec += f'<g class="fade" style="animation-delay:{d+.3:.2f}s"><text x="700" y="{y}" class="m" font-size="12" fill="{MUTED}">{k}</text><text x="850" y="{y}" class="t" font-size="19" fill="{INK}">{esc(v)}</text></g>'
        y += 46 if k == "EXPERIENCE" else 62
    if True:
        spec += f'<line x1="700" y1="{y-30}" x2="{W-56}" y2="{y-30}" stroke="{INK}" stroke-opacity=".25" class="draw" style="animation-delay:1.3s"/>'
    # live status ticker with pulsing dot
    status = f'''<g transform="translate(56,{H-74})" class="fade" style="animation-delay:1.2s">
      <rect width="452" height="40" rx="20" fill="none" stroke="{INK}" stroke-opacity=".3"/>
      <circle cx="22" cy="20" r="5" fill="{ORANGE}"/><circle cx="22" cy="20" r="5" fill="none" stroke="{ORANGE}"><animate attributeName="r" values="5;14" dur="1.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/></circle>
      <text x="42" y="25" class="m" font-size="13" fill="{INK}">CURRENTLY: SHIPPING AI AGENTS + AUTOMATIONS</text></g>'''
    body = f'''<text x="56" y="62" class="m" font-size="13" fill="{ORANGE}">(01)</text><text x="104" y="62" class="m" font-size="13" fill="{INK}">ABOUT</text>
    {stmt}{spec}{status}'''
    save("about.svg", svg(W, H, css, body))

# ------------------------------------------------------------------ SECTION LABEL
def label(fname, num, title, right):
    W, H = 1200, 150
    css = fonts("serif", "serifi", "mono")
    body = f'''<text x="56" y="52" class="m" font-size="13" fill="{ORANGE}">({num})</text>
    <svg x="0" y="46" width="900" height="100" overflow="hidden"><g class="rise"><text x="52" y="82" class="s" font-size="68" letter-spacing="-1.5" fill="{INK}">{title}</text></g></svg>
    <text x="{W-56}" y="126" text-anchor="end" class="m fade" font-size="13" fill="{MUTED}">{right}</text>'''
    save(fname, svg(W, H, css, body, rx=22))

# ------------------------------------------------------------------ PROJECT ROW
def row(fname, n, title, desc, tags, year, delay=0):
    W, H = 1200, 150
    css = fonts("serif", "mono", "sans")
    tagx, tg = 720, ""
    for t in tags:
        w = len(t) * 9.4 + 26
        tg += f'<g transform="translate({tagx},88)"><rect width="{w}" height="30" rx="15" fill="none" stroke="{INK}" stroke-opacity=".35"/><text x="{w/2}" y="20" text-anchor="middle" class="m" font-size="11.5" fill="{INK}">{t}</text></g>'
        tagx += w + 8
    body = f'''
  <g class="fade" style="animation-delay:{delay+.55:.2f}s">
    <text x="56" y="62" class="m" font-size="14" fill="{ORANGE}">{n}</text>
    <text x="110" y="84" class="s" font-size="58" letter-spacing="-1.4" fill="{INK}">{esc(title)}</text>
    <text x="112" y="120" class="t" font-size="18" fill="{MUTED}">{esc(desc)}</text>
    <text x="720" y="62" class="m" font-size="13" fill="{MUTED}">{year}</text>
    {tg}
    <g transform="translate({W-110},45)">
      <circle cx="30" cy="30" r="30" fill="{INK}"/>
      <g style="animation:nudge 2.4s ease-in-out infinite"><path d="M21 39 L39 21 M25 21 H39 V35" stroke="{PAPER}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
    </g>
  </g>
  <rect width="{W}" height="{H}" fill="{ORANGE}" style="transform-origin:0 0;animation:wipe 1.1s cubic-bezier(.7,0,.2,1) {delay:.2f}s both"/>'''
    css += """@keyframes wipe{0%{transform:scaleX(0);transform-origin:0 0}48%{transform:scaleX(1);transform-origin:0 0}52%{transform:scaleX(1);transform-origin:100% 0}100%{transform:scaleX(0);transform-origin:100% 0}}
@keyframes nudge{0%,60%,100%{transform:translate(0,0)}30%{transform:translate(3px,-3px)}}"""
    save(fname, svg(W, H, css, body, rx=18))

# ------------------------------------------------------------------ TOOLKIT
def toolkit():
    W, H = 1200, 470
    css = fonts("serif", "serifi", "mono", "sans")
    cols = [("LANGUAGES", ["Python", "TypeScript", "JavaScript", "C++", "Dart"]),
            ("AI / ML", ["TensorFlow", "Keras", "scikit-learn", "OpenCV", "LLM APIs"]),
            ("BUILD", ["Next.js", "FastAPI", "Flask", "Flutter", "Firebase"]),
            ("AUTOMATE + DESIGN", ["n8n", "Agentic workflows", "Figma", "Framer", "Vercel"])]
    body = f'<text x="56" y="62" class="m" font-size="13" fill="{ORANGE}">(03)</text><text x="104" y="62" class="m" font-size="13" fill="{INK}">TOOLKIT</text>'
    body += f'<svg x="0" y="70" width="{W}" height="90" overflow="hidden"><g class="rise"><text x="52" y="72" class="s" font-size="64" letter-spacing="-1.5" fill="{INK}">The <tspan class="si" fill="{ORANGE}">stack</tspan> I reach for.</text></g></svg>'
    cw = (W - 112) / 4
    k = 0
    pos = []
    for ci, (h, its) in enumerate(cols):
        x = 56 + ci * cw
        body += f'<line x1="{x}" y1="200" x2="{x + cw - 24}" y2="200" stroke="{INK}" stroke-width="1.2" class="draw" style="animation-delay:{.2+ci*.15:.2f}s"/>'
        body += f'<text x="{x}" y="230" class="m fade" font-size="12" fill="{MUTED}" style="animation-delay:{.4+ci*.15:.2f}s">{h}</text>'
        for ii, it in enumerate(its):
            y = 280 + ii * 40
            body += f'<text x="{x}" y="{y}" class="t fade" font-size="22" fill="{INK}" style="animation-delay:{.6+k*.06:.2f}s">{esc(it)}</text>'
            pos.append((x - 14, y - 8)); k += 1
    # roving highlighter dot that hops through every item
    n = len(pos)
    kt = ";".join(f"{i/n:.4f}" for i in range(n)) + ";1"
    xs = ";".join(str(round(p[0], 1)) for p in pos) + f";{round(pos[0][0],1)}"
    ys = ";".join(str(p[1]) for p in pos) + f";{pos[0][1]}"
    body += f'<circle r="4.5" fill="{ORANGE}"><animate attributeName="cx" values="{xs}" keyTimes="{kt}" calcMode="discrete" dur="{n*0.6}s" repeatCount="indefinite"/><animate attributeName="cy" values="{ys}" keyTimes="{kt}" calcMode="discrete" dur="{n*0.6}s" repeatCount="indefinite"/></circle>'
    save("toolkit.svg", svg(W, H, css, body))

# ------------------------------------------------------------------ CONTACT BUTTONS
def button(fname, lab, sub, dark=False):
    W, H = 390, 120
    css = fonts("serif", "mono")
    bg, fg = (INK, PAPER) if dark else (PAPER, INK)
    body = f'''<text x="30" y="44" class="m" font-size="12" fill="{ORANGE}">{sub}</text>
    <text x="28" y="94" class="s" font-size="44" letter-spacing="-.8" fill="{fg}">{lab}</text>
    <g transform="translate({W-78},48)" style="animation:slide 2.2s ease-in-out infinite"><path d="M0 16 H40 M26 2 L40 16 L26 30" stroke="{fg}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'''
    css += "@keyframes slide{0%,100%{transform:translate(312px,48px)}50%{transform:translate(320px,48px)}}"
    save(fname, svg(W, H, css, body, rx=18, bg=bg))

# ------------------------------------------------------------------ FOOTER
def footer():
    W, H = 1200, 420
    css = fonts("serif", "serifi", "mono")
    body = f'''<text x="56" y="62" class="m" font-size="13" fill="{ORANGE}">(05)</text><text x="104" y="62" class="m" font-size="13" fill="{PAPER}" opacity=".7">CONTACT</text>
    <svg x="0" y="80" width="{W}" height="150" overflow="hidden"><g class="rise"><text x="50" y="128" class="s" font-size="136" letter-spacing="-4" fill="{PAPER}">Let\u2019s build</text></g></svg>
    <svg x="0" y="214" width="{W}" height="150" overflow="hidden"><g class="rise" style="animation-delay:.2s"><text x="50" y="122" class="si" font-size="136" letter-spacing="-4" fill="{ORANGE}">something that thinks.</text></g></svg>
    <line x1="56" y1="370" x2="{W-56}" y2="370" stroke="{PAPER}" stroke-opacity=".3" class="draw" style="animation-delay:.6s"/>
    <text x="56" y="398" class="m" font-size="12" fill="{PAPER}" opacity=".6">\u00a9 2026 MUHAMMAD KAIF</text>
    <text x="{W-56}" y="398" text-anchor="end" class="m" font-size="12" fill="{PAPER}" opacity=".6">DESIGNED IN FAISALABAD</text>
    <g transform="translate(1060,110)">{asterisk(0,0,34,ORANGE,"spinr")}</g>'''
    save("footer.svg", svg(W, H, css, body, bg=INK))

hero(); about(); toolkit(); footer()
label("label-work.svg", "02", "Selected work", "06 PROJECTS / 2025\u20132026")
label("label-activity.svg", "04", "Activity", "LIVE FROM GITHUB")
P = [("p1.svg", "01", "AasaanLearn", "AI-powered learning platform, my final year project.", ["NEXT.JS", "FASTAPI", "OPENAI"], "2026"),
     ("p2.svg", "02", "Habiti", "Habit-tracking mobile application.", ["FLUTTER", "DART"], "2026"),
     ("p3.svg", "03", "Image Captioner", "Deep learning model that writes captions for images.", ["TENSORFLOW", "KERAS"], "2025"),
     ("p4.svg", "04", "Stock Predictor", "Python web app that forecasts stock prices.", ["PYTHON", "ML"], "2025"),
     ("p5.svg", "05", "Genre Classifier", "Classifies songs into genres from audio features.", ["SCIKIT-LEARN", "AUDIO"], "2025"),
     ("p6.svg", "06", "SVD Recommender", "Movie recommendations via matrix factorisation.", ["SVD", "PANDAS"], "2025")]
for i, p in enumerate(P):
    row(*p, delay=i * 0.12)
button("b-portfolio.svg", "Portfolio", "(WEB)", dark=True)
button("b-linkedin.svg", "LinkedIn", "(SOCIAL)")
button("b-email.svg", "Email", "(SAY HI)")
print("ok", sorted(os.listdir(OUT)))
