"""Hand-coded, transparent, light/dark adaptive SVGs for the Kaifi1199 profile README.
Content mirrors kaifbuilds.vercel.app (Kaifi1199/portfolio data.ts). Run: python3 gen4.py
Fonts: subset woff2 of Instrument Serif, JetBrains Mono, Inter Tight in /tmp/f4 (pyftsubset from ~/.fonts)."""
import base64, html, os
from PIL import ImageFont

F = "/tmp/f4"; TTF = os.path.expanduser("~/.fonts")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)
O = "#FF4A1C"
W = 900
EASE = 'calcMode="spline" keySplines="0.16 1 0.3 1"'

def ff(file, fam, style="normal"):
    b = base64.b64encode(open(f"{F}/{file}.woff2", "rb").read()).decode()
    return f"@font-face{{font-family:'{fam}';font-style:{style};src:url(data:font/woff2;base64,{b}) format('woff2')}}"
FACES = {"serif": ff("serif", "IS"), "serifi": ff("serifi", "IS", "italic"), "mono": ff("mono", "JBM"), "sans": ff("sans", "IT")}

BASE = f"""
:root{{--ink:#1F2328;--mute:#656D76;--line:#D0D7DE}}
@media (prefers-color-scheme:dark){{:root{{--ink:#E6EDF3;--mute:#8D96A0;--line:#30363D}}}}
.ink{{fill:var(--ink)}}.mute{{fill:var(--mute)}}.o{{fill:{O}}}
.serif{{font-family:'IS',Georgia,serif}}.it{{font-style:italic}}
.mono{{font-family:'JBM',ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase}}
.sans{{font-family:'IT','Inter',system-ui,sans-serif}}
.hair{{stroke:var(--line);stroke-width:1}}
.up{{animation:up 1.1s cubic-bezier(.16,1,.3,1) both}}
.fade{{animation:fade 1s ease both}}
.draw{{stroke-dasharray:{W};stroke-dashoffset:{W};animation:draw 1.6s cubic-bezier(.65,0,.35,1) forwards}}
.spin{{transform-box:fill-box;transform-origin:center;animation:spin 14s linear infinite}}
.nudge{{animation:nudge 2.4s ease-in-out infinite}}
@keyframes up{{from{{transform:translateY(110%)}}to{{transform:none}}}}
@keyframes fade{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes nudge{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(4px,-4px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;stroke-dashoffset:0!important}}}}
"""

def svg(name, h, body, faces=("serif", "serifi", "mono", "sans"), extra=""):
    css = "".join(FACES[f] for f in faces) + BASE + extra
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" fill="none">'
         f'<style>{css}</style>{body}</svg>')
    open(f"{OUT}/{name}.svg", "w").write(s)

def e(t): return html.escape(t, quote=False)
def d(s): return f'style="animation-delay:{s}s"'
STAR = "M50 0c3 30 20 47 50 50-30 3-47 20-50 50-3-30-20-47-50-50C30 47 47 30 50 0Z"
def star(x, y, size, cls="o spin", delay=0):
    k = size / 100
    return f'<g transform="translate({x},{y}) scale({k})"><path class="{cls}" {d(delay)} d="{STAR}"/></g>'

def width(text, font, size):
    return ImageFont.truetype(f"{TTF}/{font}", size).getlength(text)

def mask(i, x, y, w, h):
    return f'<clipPath id="m{i}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'

# ---------------- hero ----------------
def hero():
    b = ['<defs>' + mask(1, 0, 40, W, 132) + mask(2, 0, 160, W, 140) + '</defs>']
    b.append(f'<text class="mono mute fade" x="0" y="20" font-size="11">(Portfolio — 2026)</text>')
    b.append(f'<g class="fade" {d(.2)}><circle cx="{W-214}" cy="16" r="3.5" class="o"/>'
             f'<circle cx="{W-214}" cy="16" r="3.5" stroke="{O}" stroke-width="1.4">'
             f'<animate attributeName="r" values="3.5;8" dur="1.8s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/></circle>'
             f'<text class="mono ink" x="{W}" y="20" font-size="11" text-anchor="end">Open to full-time roles</text></g>')
    b.append(f'<g clip-path="url(#m1)"><text class="serif ink up" x="-6" y="158" font-size="150" letter-spacing="-5">Muhammad</text></g>')
    kw = width("Kaif", "InstrumentSerif-Italic.ttf", 150) - 10
    b.append(f'<g clip-path="url(#m2)"><text class="serif it o up" {d(.12)} x="-6" y="284" font-size="150" letter-spacing="-5">Kaif</text></g>')
    b.append(f'<g class="fade" {d(.5)}>' + star(kw + 22, 200, 72) + '</g>')
    rx = W
    b.append(f'<g class="fade" {d(.7)}><text class="mono ink" x="{rx}" y="236" font-size="12" text-anchor="end">Full Stack AI Engineer</text>'
             f'<text class="mono mute" x="{rx}" y="258" font-size="12" text-anchor="end">Faisalabad, Pakistan</text></g>')
    b.append(f'<line class="hair draw" {d(.3)} x1="0" y1="312" x2="{W}" y2="312"/>')
    svg("hero", 318, "".join(b))

# ---------------- statement ----------------
def statement():
    text = ("I build web products with a model somewhere inside them, and I care just as much "
            "about the front end people actually touch.")
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if width(t, "InstrumentSerif-Regular.ttf", 38) > W - 40: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    b = []
    for i, l in enumerate(lines):
        b.append(f'<text class="serif ink fade" {d(.15*i)} x="0" y="{44+i*48}" font-size="38">{e(l)}</text>')
    svg("statement", 60 + 48 * (len(lines) - 1) + 10, "".join(b), ("serif",))

# ---------------- section label ----------------
def label(name, num, title, aside):
    b = [f'<text class="mono o fade" x="0" y="44" font-size="12">({num})</text>',
         f'<text class="serif it ink fade" {d(.1)} x="52" y="48" font-size="44" letter-spacing="-1">{e(title)}</text>',
         f'<text class="mono mute fade" {d(.25)} x="{W}" y="44" font-size="11" text-anchor="end">{e(aside)}</text>',
         f'<line class="hair draw" x1="0" y1="66" x2="{W}" y2="66"/>']
    svg(name, 70, "".join(b), ("serifi", "mono"))

# ---------------- project row ----------------
def row(name, no, title, kind, year, line, delay=0, arrow=True):
    b = [f'<text class="mono o fade" {d(delay)} x="0" y="44" font-size="12">{no}</text>',
         f'<text class="serif ink fade" {d(delay+.08)} x="52" y="52" font-size="48" letter-spacing="-1">{e(title)}</text>',
         f'<text class="mono mute fade" {d(delay+.16)} x="{W-34}" y="40" font-size="11" text-anchor="end">{e(kind)}</text>',
         f'<text class="mono mute fade" {d(delay+.2)} x="{W-34}" y="58" font-size="11" text-anchor="end">{e(year)}</text>',
         f'<text class="sans mute fade" {d(delay+.24)} x="54" y="90" font-size="16">{e(line)}</text>',
         f'<g class="nudge"><text class="sans o" x="{W}" y="50" font-size="22" text-anchor="end">↗</text></g>' if arrow else '',
         f'<line class="hair draw" {d(delay+.1)} x1="0" y1="116" x2="{W}" y2="116"/>']
    svg(name, 120, "".join(b), ("serif", "mono", "sans"))

# ---------------- experience ----------------
def experience():
    rows = [("CodeCelix", "AI Automation Engineer", "Aug 2025 – Nov 2025",
             "Recruitment automation: resume parsing, semantic job matching, proposal generation."),
            ("CosmiCode", "AI & ML Engineer", "2025",
             "Image captioning, music genre classification, an SVD movie recommender, segmentation.")]
    b = []
    for i, (c, r, w, l) in enumerate(rows):
        y = i * 104
        b += [f'<text class="serif ink fade" {d(i*.15)} x="0" y="{y+44}" font-size="40" letter-spacing="-1">{e(c)}</text>',
              f'<text class="sans ink fade" {d(i*.15+.1)} x="300" y="{y+34}" font-size="17" font-weight="600">{e(r)}</text>',
              f'<text class="sans mute fade" {d(i*.15+.15)} x="300" y="{y+60}" font-size="15">{e(l)}</text>',
              f'<text class="mono o fade" {d(i*.15+.2)} x="{W}" y="{y+34}" font-size="11" text-anchor="end">{e(w)}</text>',
              f'<line class="hair draw" {d(i*.15)} x1="0" y1="{y+90}" x2="{W}" y2="{y+90}"/>']
    svg("experience", 200, "".join(b))

# ---------------- toolkit ----------------
def toolkit():
    groups = [("Languages", "Python, TypeScript, JavaScript, SQL"),
              ("Front end", "Next.js, React, Tailwind CSS, Framer Motion, GSAP, Streamlit"),
              ("Back end", "FastAPI, REST APIs, Firebase, MongoDB, Mongoose, Clerk"),
              ("AI / ML", "LLM integration, NLP, Computer vision, Deep learning, n8n"),
              ("Libraries", "TensorFlow, scikit-learn, spaCy, Pandas, NumPy"),
              ("Ship it", "Git, GitHub, Vercel, Railway, Flutter")]
    b = []; ys = []
    for i, (g, items) in enumerate(groups):
        y = 34 + i * 46; ys.append(y)
        b.append(f'<text class="mono mute fade" {d(i*.08)} x="22" y="{y}" font-size="11">{e(g)}</text>')
        x = 190; parts = []
        for j, it in enumerate(items.split(", ")):
            if j: parts.append(f'<tspan class="o"> / </tspan>')
            parts.append(f'<tspan>{e(it)}</tspan>')
        b.append(f'<text class="sans ink fade" {d(i*.08+.05)} x="{x}" y="{y}" font-size="17">{"".join(parts)}</text>')
        b.append(f'<line class="hair" x1="0" y1="{y+16}" x2="{W}" y2="{y+16}"/>')
    vals = ";".join(str(y - 4) for y in ys + ys[::-1][1:])
    b.append(f'<circle cx="6" cy="{ys[0]-4}" r="4" class="o"><animate attributeName="cy" values="{vals}" dur="9s" repeatCount="indefinite"/></circle>')
    svg("toolkit", ys[-1] + 22, "".join(b), ("mono", "sans"))

# ---------------- contact ----------------
def contact():
    b = ['<defs>' + mask(3, 0, 20, W, 110) + mask(4, 0, 116, W, 120) + '</defs>',
         f'<text class="mono o fade" x="0" y="14" font-size="12">(06) Contact</text>',
         f'<g clip-path="url(#m3)"><text class="serif ink up" x="-4" y="118" font-size="110" letter-spacing="-4">Let’s build</text></g>',
         f'<g clip-path="url(#m4)"><text class="serif it o up" {d(.12)} x="-4" y="222" font-size="110" letter-spacing="-4">something.</text></g>',
         f'<g class="fade" {d(.5)}>' + star(W - 64, 150, 60) + '</g>',
         f'<text class="sans mute fade" {d(.4)} x="0" y="270" font-size="16">Hiring for a full-stack or AI engineering role, or have a product that needs a model wired in properly?</text>',
         f'<text class="sans mute fade" {d(.5)} x="0" y="294" font-size="16">Email is the fastest way to reach me.</text>']
    svg("contact", 306, "".join(b))

def button(name, lab, w=290):
    b = [f'<rect x="1" y="1" width="{w-2}" height="54" rx="27" stroke="{O}" stroke-width="1.5"/>',
         f'<text class="mono ink" x="28" y="33" font-size="12">{e(lab)}</text>',
         f'<g class="nudge"><text class="sans o" x="{w-28}" y="35" font-size="20" text-anchor="end">→</text></g>']
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="56" viewBox="0 0 {w} 56" fill="none">'
         f'<style>{FACES["mono"]}{FACES["sans"]}{BASE}</style>{"".join(b)}</svg>')
    open(f"{OUT}/{name}.svg", "w").write(s)

if __name__ == "__main__":
    for f in os.listdir(OUT): os.remove(os.path.join(OUT, f))
    hero(); statement()
    label("s1", "01", "Selected work", "4 projects, 2025 – 26")
    row("p1", "01", "AasaanLearn", "Final year project · AI", "2025 – 26 · 1st position",
        "Reading, listening and visual-story tools for students who learn differently.")
    row("p2", "02", "NextGen Tech", "Full-stack platform", "2025",
        "A company site with a working back office: blog, contact inbox, user management.", .1)
    row("p3", "03", "Habiti", "Mobile app · Flutter", "2026",
        "A small, friendly habit tracker with streaks and a 9 am nudge.", .2)
    row("p4", "04", "Resume Screener", "NLP tool", "2025",
        "Reads resumes, pulls out skills and experience, predicts the job domain.", .3, arrow=False)
    label("s2", "02", "Where I’ve worked", "Internships, 2025"); experience()
    label("s3", "03", "Tools I reach for", "From the resume, not a wishlist"); toolkit()
    contact()
    button("b-email", "2004mkaif@gmail.com"); button("b-linkedin", "LinkedIn"); button("b-portfolio", "Portfolio")
    print(sorted(os.listdir(OUT)))
