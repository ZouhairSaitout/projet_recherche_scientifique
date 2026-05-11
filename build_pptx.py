"""Build the 16-slide presentation as presentation.pptx."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

NAVY = RGBColor(0x0B, 0x2F, 0x5C)
ACCENT = RGBColor(0xC0, 0x39, 0x2B)
GRAY = RGBColor(0x55, 0x55, 0x55)
LIGHT = RGBColor(0xF4, 0xF4, 0xF4)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def add_band(slide, color=NAVY, height=Inches(0.6)):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, height)
    bar.fill.solid(); bar.fill.fore_color.rgb = color
    bar.line.fill.background()
    return bar


def add_text(slide, left, top, width, height, text, size=18,
             bold=False, color=None, align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.05)
    if isinstance(text, str):
        text = [text]
    for i, line in enumerate(text):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = line
        r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
        if color is not None:
            r.font.color.rgb = color
    return tb


def add_bullets(slide, left, top, width, height, items, size=18, color=None):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame; tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(6)
        if isinstance(item, tuple):
            level, txt = item
        else:
            level, txt = 0, item
        prefix = "  " * level + ("• " if level == 0 else "– ")
        r = p.add_run(); r.text = prefix + txt
        r.font.size = Pt(size)
        if color is not None:
            r.font.color.rgb = color
    return tb


def title_slide(slide, title, subtitle=None, page=None):
    add_band(slide, NAVY, Inches(0.55))
    if page:
        add_text(slide, Inches(12.5), Inches(0.12), Inches(0.7), Inches(0.3),
                 page, size=12, color=RGBColor(0xFF, 0xFF, 0xFF), align=PP_ALIGN.RIGHT)
    add_text(slide, Inches(0.5), Inches(0.08), Inches(11.5), Inches(0.45),
             title, size=22, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
    if subtitle:
        add_text(slide, Inches(0.5), Inches(0.7), Inches(12), Inches(0.4),
                 subtitle, size=14, italic=True, color=GRAY)


def footer(slide, who, page):
    add_text(slide, Inches(0.4), Inches(7.1), Inches(8), Inches(0.3),
             f"{who}", size=10, color=GRAY)
    add_text(slide, Inches(12.3), Inches(7.1), Inches(0.8), Inches(0.3),
             f"{page} / 16", size=10, color=GRAY, align=PP_ALIGN.RIGHT)


# =====================================================================
# SLIDE 1 — Title
# =====================================================================
s = prs.slides.add_slide(BLANK)
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
bar.fill.solid(); bar.fill.fore_color.rgb = NAVY
bar.line.fill.background()

add_text(s, Inches(0.8), Inches(2.0), Inches(11.7), Inches(2),
         ["Profondeur des réseaux de neurones :",
          "peut-on caractériser les fonctions qui la nécessitent ?"],
         size=32, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
add_text(s, Inches(0.8), Inches(4.4), Inches(11.7), Inches(0.5),
         "Initiation à la recherche scientifique — Polytech Nice Sophia, MAM3",
         size=18, italic=True, color=RGBColor(0xCC, 0xD6, 0xE6))
add_text(s, Inches(0.8), Inches(5.6), Inches(11.7), Inches(0.5),
         "Zouhair Saitout  ·  Thibaud Crotta  ·  Romain Ben",
         size=20, color=RGBColor(0xFF, 0xFF, 0xFF))
add_text(s, Inches(0.8), Inches(6.4), Inches(11.7), Inches(0.4),
         "Mai 2026", size=14, italic=True, color=RGBColor(0xCC, 0xD6, 0xE6))

# =====================================================================
# SLIDE 2 — Pourquoi la profondeur ?
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Pourquoi la profondeur ?",
            "Un facteur empiriquement décisif des réseaux modernes")
add_bullets(s, Inches(0.7), Inches(1.4), Inches(12), Inches(4),
            ["Les architectures modernes les plus performantes sont profondes :",
             (1, "GPT-4 : ~96 couches de transformers"),
             (1, "ResNet-152 : 152 couches convolutives"),
             (1, "AlphaFold : blocs profonds pour la prédiction de structures"),
             "Intuition : chaque couche apprend une abstraction de plus haut niveau",
             "Mais : est-ce une nécessité théorique, ou juste une heuristique qui marche ?"],
            size=20)
# emphasis box
box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(5.8), Inches(12), Inches(0.95))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r = p.add_run()
r.text = "Tension centrale :  pratique (profondeur essentielle)  vs.  théorie (1 couche suffit)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
footer(s, "Romain Ben — Introduction", 2)

# =====================================================================
# SLIDE 3 — Théorème d'approximation universelle
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Le théorème d'approximation universelle",
            "Un réseau peu profond suffit... en théorie")

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(1.5), Inches(12), Inches(2.2))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1.5)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Théorème (Cybenko, 1989)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(8)
r = p2.add_run()
r.text = ("Pour toute fonction continue f sur [0,1]^d et tout ε > 0, "
          "il existe un réseau à UNE SEULE couche cachée (sigmoïde) "
          "tel que  ‖ f − f_N ‖∞  <  ε.")
r.font.size = Pt(18); r.font.italic = True

add_bullets(s, Inches(0.7), Inches(4.1), Inches(12), Inches(2.5),
            ["Extension : Hornik (1991) — valable pour toute activation non polynomiale",
             "Synthèse complète : Pinkus (1999), théorie de l'approximation MLP",
             "Conséquence : la profondeur n'est pas nécessaire pour l'expressivité",
             "MAIS : ce théorème ne dit rien sur la valeur de N (nombre de neurones)"],
            size=20)
footer(s, "Romain Ben — Introduction", 3)

# =====================================================================
# SLIDE 4 — Coût caché en neurones
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Le coût caché en neurones",
            "Combien de neurones faut-il vraiment ?")

# Barron box
box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(1.4), Inches(12), Inches(2.0))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Borne de Barron (1993)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = ("Pour f de spectre de Fourier intégrable (C_f < ∞) :"
          "    erreur quadratique  ≤  C_f² / N")
r.font.size = Pt(18)
p3 = tf.add_paragraph(); p3.space_before = Pt(4)
r = p3.add_run(); r.text = "→ borne indépendante de la dimension d, mais classe restreinte."
r.font.size = Pt(16); r.font.italic = True; r.font.color.rgb = ACCENT

add_bullets(s, Inches(0.7), Inches(3.7), Inches(12), Inches(2.5),
            ["Pour des fonctions plus générales : N peut être exponentiel en d ou en 1/ε",
             "Intuition : une fonction qui oscille k fois → ∼ k neurones par oscillation en shallow",
             (1, "Un réseau profond compose les oscillations → 2^k morceaux avec k couches"),
             "Le coût caché du théorème de Cybenko : la largeur peut exploser"],
            size=20)
footer(s, "Romain Ben — Introduction", 4)

# =====================================================================
# SLIDE 5 — Problématique
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "La question de recherche")

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(1.0), Inches(2.3), Inches(11.3), Inches(3.0))
box.fill.solid(); box.fill.fore_color.rgb = NAVY
box.line.fill.background()
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.4); tf.margin_top = Inches(0.4)
p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r = p.add_run()
r.text = ("Peut-on caractériser mathématiquement la classe des fonctions "
          "pour lesquelles la profondeur d'un réseau de neurones est "
          "strictement nécessaire ?")
r.font.size = Pt(24); r.font.bold = True
r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER; p2.space_before = Pt(20)
r = p2.add_run()
r.text = ("c'est-à-dire celles dont l'approximation par un réseau peu profond "
          "requiert un nombre de neurones exponentiellement plus grand")
r.font.size = Pt(18); r.font.italic = True
r.font.color.rgb = RGBColor(0xCC, 0xD6, 0xE6)

add_text(s, Inches(0.7), Inches(6.0), Inches(12), Inches(0.5),
         "→ Zouhair pose le cadre formel, puis présente les premiers résultats de séparation.",
         size=16, italic=True, color=GRAY, align=PP_ALIGN.CENTER)
footer(s, "Romain Ben — Introduction", 5)

# =====================================================================
# SLIDE 6 — Définition formelle
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Formalisme : définition d'un réseau",
            "Réseau feedforward")

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(1.4), Inches(12), Inches(1.7))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Définition (réseau de profondeur L)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = "h⁽⁰⁾ = x ,    h⁽ˡ⁾ = σ ( W⁽ˡ⁾ h⁽ˡ⁻¹⁾ + b⁽ˡ⁾ )    pour 1 ≤ l ≤ L ,    f_θ(x) = h⁽ᴸ⁾"
r.font.size = Pt(20); r.font.bold = True
p3 = tf.add_paragraph(); p3.space_before = Pt(4)
r = p3.add_run(); r.text = "avec W⁽ˡ⁾ ∈ ℝ^{n_l × n_{l-1}} ,  b⁽ˡ⁾ ∈ ℝ^{n_l}"
r.font.size = Pt(15); r.font.italic = True

add_bullets(s, Inches(0.7), Inches(3.4), Inches(12), Inches(3.2),
            ["Profondeur L : nombre de couches",
             "Largeur : max_l n_l (nombre maximal de neurones par couche)",
             "Activations :",
             (1, "Sigmoïde σ(t) = 1/(1+e⁻ᵗ)  —  théorie classique (Cybenko, Hornik)"),
             (1, "ReLU σ(t) = max(0, t)  —  réseau linéaire par morceaux, résultats modernes")],
            size=20)
footer(s, "Zouhair Saitout — Formalisme", 6)

# =====================================================================
# SLIDE 7 — Approximation et complexité
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Formalisme : approximation et complexité",
            "Coût en neurones d'une ε-approximation")

add_bullets(s, Inches(0.7), Inches(1.4), Inches(12), Inches(1.8),
            ["ε-approximation : trouver f_N tel que  ‖ f − f_N ‖ < ε  (norme ∞ ou L²)"],
            size=20)

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(2.5), Inches(12), Inches(1.7))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Quantité centrale"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = ("N(ε, f, L)  =  nombre minimal de neurones pour approcher f à précision ε "
          "avec un réseau de profondeur ≤ L.")
r.font.size = Pt(18)

box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                           Inches(0.7), Inches(4.6), Inches(12), Inches(1.8))
box2.fill.solid(); box2.fill.fore_color.rgb = NAVY
box2.line.fill.background()
tf = box2.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.2)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Séparation par profondeur (formellement)"
r.font.size = Pt(18); r.font.bold = True
r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p2 = tf.add_paragraph(); p2.space_before = Pt(8)
r = p2.add_run()
r.text = "∃ f :    N(ε, f, L_petit)  ≥  exp(d) · N(ε, f, L_grand)"
r.font.size = Pt(20); r.font.bold = True
r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p3 = tf.add_paragraph(); p3.space_before = Pt(4)
r = p3.add_run(); r.text = "→ prouver de telles bornes inférieures est tout l'enjeu de la théorie."
r.font.size = Pt(14); r.font.italic = True
r.font.color.rgb = RGBColor(0xCC, 0xD6, 0xE6)
footer(s, "Zouhair Saitout — Formalisme", 7)

# =====================================================================
# SLIDE 8 — Telgarsky
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Telgarsky (2016) : fonctions zigzag",
            "Première séparation exponentielle prouvée")

add_bullets(s, Inches(0.7), Inches(1.4), Inches(12), Inches(1.5),
            ["Construction : dent de scie  t(x) = 2 |x − 1/2|  sur [0,1]",
             (1, "Itération : t_k = t ∘ t ∘ ··· ∘ t  (k fois)  →  t_k a 2^k morceaux linéaires")],
            size=20)

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(3.0), Inches(12), Inches(2.4))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1.5)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Théorème (Telgarsky, 2016)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = "• Un réseau ReLU de profondeur k et largeur O(1) représente t_k exactement."
r.font.size = Pt(18)
p3 = tf.add_paragraph(); p3.space_before = Pt(4)
r = p3.add_run()
r.text = ("• Tout réseau ReLU de profondeur ≤ k/2 qui approche t_k à précision 1/2 "
          "doit avoir au moins  2^{k/6}  neurones.")
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = ACCENT

add_bullets(s, Inches(0.7), Inches(5.7), Inches(12), Inches(1.2),
            ["Idée de preuve : chaque couche ReLU au plus DOUBLE le nombre de morceaux linéaires"],
            size=18)
footer(s, "Zouhair Saitout — Séparations", 8)

# =====================================================================
# SLIDE 9 — Illustration zigzag
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Illustration : itérations de la dent de scie",
            "L'analogie fractale : doublement à chaque couche")

# Draw 4 zigzag plots
import math
def zigzag(slide, left, top, width, height, k, label):
    # frame
    f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    f.fill.solid(); f.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    f.line.color.rgb = GRAY; f.line.width = Pt(0.75)
    # label
    add_text(slide, left, top + height + Emu(50000), width, Inches(0.35),
             label, size=14, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    # compute polyline of t_k on [0,1] sampled
    n_segments = 2 ** k
    pts = []
    pad = Inches(0.15)
    plot_w = width - 2 * pad; plot_h = height - 2 * pad
    for i in range(n_segments + 1):
        x = i / n_segments
        # y = t_k(x): triangle wave with 2^k oscillations
        # value: peak/valley pattern
        y = 1.0 if (i % 2 == 1) else 0.0
        if i == 0 or i == n_segments:
            y = 0.0
        pts.append((x, y))
    # build connectors
    prev = None
    for (x, y) in pts:
        px = left + pad + Emu(int(x * plot_w))
        py = top + pad + Emu(int((1 - y) * plot_h))
        if prev is not None:
            line = slide.shapes.add_connector(1, prev[0], prev[1], px, py)
            line.line.color.rgb = ACCENT; line.line.width = Pt(1.5)
        prev = (px, py)

zigzag(s, Inches(0.6), Inches(1.6), Inches(2.8), Inches(2.0), 1, "t₁ — 2 morceaux")
zigzag(s, Inches(3.7), Inches(1.6), Inches(2.8), Inches(2.0), 2, "t₂ — 4 morceaux")
zigzag(s, Inches(6.8), Inches(1.6), Inches(2.8), Inches(2.0), 3, "t₃ — 8 morceaux")
zigzag(s, Inches(9.9), Inches(1.6), Inches(2.8), Inches(2.0), 5, "t₅ — 32 morceaux")

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(4.7), Inches(12), Inches(2.0))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.2)
p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r = p.add_run()
r.text = ("Réseau profond : k couches → 2^k morceaux par composition")
r.font.size = Pt(20); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER; p2.space_before = Pt(8)
r = p2.add_run()
r.text = ("Réseau peu profond : il faut 2^k neurones séparés pour les générer un par un")
r.font.size = Pt(20); r.font.bold = True; r.font.color.rgb = ACCENT
footer(s, "Zouhair Saitout — Séparations", 9)

# =====================================================================
# SLIDE 10 — Montufar
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Montufar et al. (2014) : régions linéaires",
            "Géométrie de l'expressivité d'un réseau ReLU")

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(1.4), Inches(12), Inches(1.6))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = NAVY; box.line.width = Pt(1)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Théorème (Montufar et al., 2014)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = "Un réseau ReLU à L couches, largeur n, dimension d, a au plus  Θ( (n/d)^{d(L−1)} · n^d )  régions linéaires."
r.font.size = Pt(17); r.font.bold = True

# table
add_text(s, Inches(0.7), Inches(3.3), Inches(12), Inches(0.4),
         "À nombre total de paramètres fixé (n · L = const) :",
         size=18, bold=True, color=NAVY)

# Build table
tbl = s.shapes.add_table(3, 2, Inches(2.5), Inches(3.9), Inches(8.3), Inches(1.8)).table
tbl.cell(0, 0).text = "Paramètre qui croît"
tbl.cell(0, 1).text = "Croissance du nb de régions"
tbl.cell(1, 0).text = "Profondeur L"
tbl.cell(1, 1).text = "EXPONENTIELLE"
tbl.cell(2, 0).text = "Largeur n"
tbl.cell(2, 1).text = "Polynomiale"
for r in range(3):
    for c in range(2):
        cell = tbl.cell(r, c)
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.size = Pt(16)
                if r == 0:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                if r == 1 and c == 1:
                    run.font.bold = True
                    run.font.color.rgb = ACCENT

add_text(s, Inches(0.7), Inches(6.0), Inches(12), Inches(0.6),
         "→ La profondeur est exponentiellement plus efficace que la largeur "
         "pour générer de la complexité géométrique.",
         size=18, italic=True, color=NAVY, align=PP_ALIGN.CENTER)
footer(s, "Zouhair Saitout — Séparations", 10)

# =====================================================================
# SLIDE 11 — Eldan & Shamir
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Eldan & Shamir (2016) : fonctions radiales",
            "Séparer 2 vs 3 couches — le résultat le plus surprenant")

add_bullets(s, Inches(0.7), Inches(1.4), Inches(12), Inches(1.0),
            ["Construction : f : ℝ^d → ℝ  radiale (dépend uniquement de ‖x‖), "
             "fortement oscillante en ‖x‖"],
            size=18)

# Table
add_text(s, Inches(0.7), Inches(2.7), Inches(12), Inches(0.4),
         "Théorème (Eldan & Shamir, 2016)",
         size=18, bold=True, color=NAVY)
tbl = s.shapes.add_table(3, 2, Inches(2.0), Inches(3.2), Inches(9.3), Inches(1.7)).table
tbl.cell(0, 0).text = "Profondeur"
tbl.cell(0, 1).text = "Largeur nécessaire pour approcher f"
tbl.cell(1, 0).text = "3 couches ReLU"
tbl.cell(1, 1).text = "poly(d)"
tbl.cell(2, 0).text = "2 couches ReLU"
tbl.cell(2, 1).text = "≥ exp( Ω(d) )"
for r in range(3):
    for c in range(2):
        cell = tbl.cell(r, c)
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.size = Pt(16)
                if r == 0:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                if r == 2 and c == 1:
                    run.font.bold = True
                    run.font.color.rgb = ACCENT

add_bullets(s, Inches(0.7), Inches(5.3), Inches(12), Inches(1.7),
            ["Séparation EXPONENTIELLE entre profondeur 2 et profondeur 3, en dimension d",
             "Preuve : analyse fine du spectre de Fourier en coordonnées radiales",
             (1, "La 3ᵉ couche permet de \"reconcentrer\" l'oscillation, infaisable en 2 couches sans coût exponentiel")],
            size=17)
footer(s, "Thibaud Crotta — Séparations & caractérisation", 11)

# =====================================================================
# SLIDE 12 — Daniely + Safran-Shamir
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Daniely (2017)  &  Safran–Shamir (2017)",
            "Séparation algébrique  ·  trade-off largeur–profondeur")

# Two columns
col_w = Inches(5.9)
left1, left2 = Inches(0.5), Inches(6.9)
top = Inches(1.4)

box1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left1, top, col_w, Inches(5.4))
box1.fill.solid(); box1.fill.fore_color.rgb = LIGHT
box1.line.color.rgb = NAVY; box1.line.width = Pt(1)
tf = box1.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Daniely (COLT 2017)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
for line in [
    "",
    "Un réseau ReLU à 2 couches à poids polynomialement bornés",
    "ne peut pas approcher f",
    "si f est loin (en L²) d'un polynôme de bas degré",
    "sur S^{d−1} × S^{d−1}.",
    "",
    "→ condition SUFFISANTE de non-approximation",
    "    par les réseaux peu profonds.",
]:
    pp = tf.add_paragraph()
    rr = pp.add_run(); rr.text = line; rr.font.size = Pt(15)

box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left2, top, col_w, Inches(5.4))
box2.fill.solid(); box2.fill.fore_color.rgb = LIGHT
box2.line.color.rgb = NAVY; box2.line.width = Pt(1)
tf = box2.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Safran & Shamir (ICML 2017)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
for line in [
    "",
    "Pour des fonctions naturelles, ex. f(x) = ‖x‖₂ :",
    "",
    "À précision fixée,",
    "    diminuer L d'un facteur multiplicatif",
    "    → augmente N d'un facteur EXPONENTIEL.",
    "",
    "→ quantification du trade-off profondeur–largeur.",
]:
    pp = tf.add_paragraph()
    rr = pp.add_run(); rr.text = line; rr.font.size = Pt(15)
footer(s, "Thibaud Crotta — Séparations & caractérisation", 12)

# =====================================================================
# SLIDE 13 — Raghu + Diakonikolas
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Raghu et al. (2017)  &  Diakonikolas et al. (2022)",
            "Mesure géométrique  ·  caractérisation spectrale")

box1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                           Inches(0.7), Inches(1.4), Inches(12), Inches(1.7))
box1.fill.solid(); box1.fill.fore_color.rgb = LIGHT
box1.line.color.rgb = NAVY; box1.line.width = Pt(1)
tf = box1.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Raghu et al. (ICML 2017) — longueur de trajectoire"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph(); p2.space_before = Pt(6)
r = p2.add_run()
r.text = ("Métrique : longueur ℓ(L) de l'image, par le réseau, d'une courbe simple. "
          "ℓ(L) croît exponentiellement avec L. → le réseau profond \"plie\" l'espace.")
r.font.size = Pt(16)

box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                           Inches(0.7), Inches(3.3), Inches(12), Inches(3.4))
box2.fill.solid(); box2.fill.fore_color.rgb = NAVY
box2.line.fill.background()
tf = box2.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.2)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Diakonikolas et al. (JMLR 2022) — caractérisation Fourier sphérique"
r.font.size = Pt(18); r.font.bold = True
r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p2 = tf.add_paragraph(); p2.space_before = Pt(10)
r = p2.add_run()
r.text = "Sur la sphère S^{d−1} :"
r.font.size = Pt(16); r.font.italic = True
r.font.color.rgb = RGBColor(0xCC, 0xD6, 0xE6)
p3 = tf.add_paragraph(); p3.space_before = Pt(8)
r = p3.add_run()
r.text = "f efficacement approchable par 1 couche cachée de taille poly(d)"
r.font.size = Pt(17); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p4 = tf.add_paragraph(); p4.space_before = Pt(2); p4.alignment = PP_ALIGN.CENTER
r = p4.add_run(); r.text = "⇔"
r.font.size = Pt(20); r.font.bold = True
r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p5 = tf.add_paragraph(); p5.space_before = Pt(2)
r = p5.add_run()
r.text = ("son spectre de Fourier sphérique est concentré sur des harmoniques "
          "de degré ≤ O(polylog d)")
r.font.size = Pt(17); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
p6 = tf.add_paragraph(); p6.space_before = Pt(8)
r = p6.add_run()
r.text = "→ SEULE caractérisation nécessaire ET suffisante connue, mais uniquement sur la sphère."
r.font.size = Pt(15); r.font.italic = True
r.font.color.rgb = RGBColor(0xCC, 0xD6, 0xE6)
footer(s, "Thibaud Crotta — Séparations & caractérisation", 13)

# =====================================================================
# SLIDE 14 — Vardi
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Vardi et al. (2020) : barrières formelles",
            "Pourquoi une caractérisation générale est-elle si difficile ?")

add_bullets(s, Inches(0.7), Inches(1.4), Inches(12), Inches(1.5),
            ["Toutes les preuves actuelles de séparation supposent (souvent implicitement) :",
             (1, "‖W^{(l)}‖∞ , ‖b^{(l)}‖∞  ≤  poly(d)")],
            size=18)

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                          Inches(0.7), Inches(3.0), Inches(12), Inches(2.2))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT
box.line.color.rgb = ACCENT; box.line.width = Pt(1.5)
tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Résultat (Vardi, Yehudai, Shamir — NeurIPS 2020)"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = ACCENT
p2 = tf.add_paragraph(); p2.space_before = Pt(8)
r = p2.add_run()
r.text = "Si on autorise des poids exponentiellement grands :"
r.font.size = Pt(17)
p3 = tf.add_paragraph(); p3.space_before = Pt(4)
r = p3.add_run()
r.text = "•  tout réseau profond peut être simulé EXACTEMENT par un réseau peu profond"
r.font.size = Pt(17)
p4 = tf.add_paragraph(); p4.space_before = Pt(2)
r = p4.add_run()
r.text = "•  toutes les séparations connues (Telgarsky, Eldan–Shamir...) S'EFFONDRENT"
r.font.size = Pt(17); r.font.bold = True

add_bullets(s, Inches(0.7), Inches(5.4), Inches(12), Inches(1.6),
            ["Conséquence : toute caractérisation future devra",
             (1, "spécifier le régime de poids considéré"),
             (1, "s'appuyer sur des arguments valides quand cette contrainte est relachée")],
            size=17)
footer(s, "Thibaud Crotta — Séparations & caractérisation", 14)

# =====================================================================
# SLIDE 15 — Conclusion
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Bilan et questions ouvertes",
            "Ce qui est établi  ·  ce qui reste ouvert")

# Two columns
col_w = Inches(5.9)
left1, left2 = Inches(0.5), Inches(6.9)
top = Inches(1.4)
hh = Inches(5.4)

# Left: ce qui est établi
box1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left1, top, col_w, hh)
box1.fill.solid(); box1.fill.fore_color.rgb = RGBColor(0xE8, 0xF1, 0xE8)
box1.line.color.rgb = RGBColor(0x2E, 0x7D, 0x32); box1.line.width = Pt(1.5)
tf = box1.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Ce qui est établi"
r.font.size = Pt(18); r.font.bold = True
r.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)
for line in [
    "",
    "Séparations exponentielles prouvées :",
    "  •  Fonctions zigzag (Telgarsky, 2016)",
    "  •  Fonctions radiales (Eldan–Shamir, 2016)",
    "  •  Spectre sphérique haute fréquence",
    "       (Diakonikolas et al., 2022)",
    "",
    "Nb de régions linéaires :",
    "  exponentiel en la profondeur",
    "  (Montufar et al., 2014)",
]:
    pp = tf.add_paragraph()
    rr = pp.add_run(); rr.text = line; rr.font.size = Pt(15)

# Right: ce qui reste ouvert
box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left2, top, col_w, hh)
box2.fill.solid(); box2.fill.fore_color.rgb = RGBColor(0xFD, 0xEC, 0xEA)
box2.line.color.rgb = ACCENT; box2.line.width = Pt(1.5)
tf = box2.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.15)
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Ce qui reste ouvert"
r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = ACCENT
for line in [
    "",
    "Aucune caractérisation nécessaire ET",
    "suffisante de portée générale",
    "",
    "Les preuves ne tiennent que si les poids",
    "sont bornés (Vardi et al., 2020)",
    "",
    "Extension au-delà de la sphère : ouverte",
    "",
    "Lien formel avec la complexité booléenne",
    "(NC¹ vs AC⁰) : à explorer",
]:
    pp = tf.add_paragraph()
    rr = pp.add_run(); rr.text = line; rr.font.size = Pt(15)
footer(s, "Romain Ben — Conclusion", 15)

# =====================================================================
# SLIDE 16 — Bibliographie
# =====================================================================
s = prs.slides.add_slide(BLANK)
title_slide(s, "Références principales", "13 articles")

refs = [
    ("Cybenko",            1989, "Math. Control Signals Syst.", "Approximation universelle (sigmoïde)"),
    ("Hornik",             1991, "Neural Networks",             "Activations non polynomiales"),
    ("Barron",             1993, "IEEE Trans. Inf. Theory",     "Borne quantitative (Fourier)"),
    ("Pinkus",             1999, "Acta Numerica",               "Synthèse théorie MLP"),
    ("Montufar et al.",    2014, "NeurIPS",                     "Régions linéaires et profondeur"),
    ("Eldan & Shamir",     2016, "COLT",                        "Radiales, séparation 2 vs 3 couches"),
    ("Telgarsky",          2016, "COLT",                        "Zigzag, séparation exponentielle"),
    ("Raghu et al.",       2017, "ICML",                        "Longueur de trajectoire"),
    ("Daniely",            2017, "COLT",                        "Séparation via polynômes bas degré"),
    ("Safran & Shamir",    2017, "ICML",                        "Trade-offs profondeur–largeur"),
    ("Yarotsky",           2017, "Neural Networks",             "Bornes d'erreur ReLU profond"),
    ("Vardi et al.",       2020, "NeurIPS",                     "Barrières formelles aux preuves"),
    ("Diakonikolas et al.",2022, "JMLR",                        "Caract. Fourier sphérique"),
]
tbl = s.shapes.add_table(len(refs) + 1, 4,
                          Inches(0.4), Inches(1.4),
                          Inches(12.5), Inches(5.3)).table
headers = ["Auteurs", "Année", "Conf./Journal", "Contribution"]
for c, h in enumerate(headers):
    cell = tbl.cell(0, c); cell.text = h
    for para in cell.text_frame.paragraphs:
        for run in para.runs:
            run.font.size = Pt(13); run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
for i, (auth, yr, ven, contrib) in enumerate(refs, start=1):
    for c, val in enumerate([auth, str(yr), ven, contrib]):
        cell = tbl.cell(i, c); cell.text = val
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.size = Pt(11)

add_text(s, Inches(0.4), Inches(7.1), Inches(8), Inches(0.3),
         "PDFs disponibles dans biblio/ — Merci pour votre attention !",
         size=12, italic=True, color=GRAY)
add_text(s, Inches(12.3), Inches(7.1), Inches(0.8), Inches(0.3),
         "16 / 16", size=10, color=GRAY, align=PP_ALIGN.RIGHT)

prs.save("slides/presentation.pptx")
print("OK")
