"""生成背诵范文配图：chart.png（带考点标注的折线图）、essay_card.png（分色范文卡）、structure.png（四段结构提纲）。
运行：python3 make_figures.py   输出到 ../img/
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["font.family"] = ["Hiragino Sans GB", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

# ---------------------------------------------------------------- 数据
years = [2000, 2003, 2006, 2009, 2012, 2015, 2018]
data = {
    "Thailand": [10, 11, 14, 14, 22, 30, 38],
    "Egypt":    [5, 6, 9, 12, 11, 9, 11],
    "Vietnam":  [2, 2.5, 3.5, 4, 7, 8, 15],
}
colors = {"Thailand": "#1f77b4", "Egypt": "#e07b00", "Vietnam": "#2a9d4b"}

# ---------------------------------------------------------------- 图 1：折线图 + 考点
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=160)
for name, ys in data.items():
    ax.plot(years, ys, marker="o", lw=2.8, ms=7, color=colors[name], label=name, zorder=3)
    for x, y in zip(years, ys):
        ax.annotate(f"{y:g}", (x, y), textcoords="offset points", xytext=(0, 9),
                    ha="center", fontsize=9.5, color=colors[name], fontweight="bold")

ax.set_title("International tourist arrivals in Thailand, Egypt and Vietnam, 2000–2018",
             fontsize=15, fontweight="bold", pad=16)
ax.set_ylabel("Arrivals (millions)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 44)
ax.grid(axis="y", alpha=0.3)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper left", fontsize=11, frameon=False)

def badge(x, y, num, text, dx, dy, color, ha="left"):
    """编号圆圈 + 考点说明，箭头指向数据点"""
    ax.annotate(
        f"{num}", xy=(x, y), xytext=(x + dx, y + dy),
        fontsize=11, fontweight="bold", color="white", ha="center", va="center",
        bbox=dict(boxstyle="circle,pad=0.3", fc=color, ec=color),
        arrowprops=dict(arrowstyle="-", color=color, lw=1.3, alpha=0.8), zorder=5)
    ax.text(x + dx + (0.55 if ha == "left" else -0.55), y + dy, text, fontsize=9.6,
            color=color, ha=ha, va="center", zorder=5,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=color, alpha=0.95))

badge(2000, 10, "①", "起点对比：Thailand ≈ 2× Egypt, 5× Vietnam\ntwice as many as / five times the figure for", 0.8, 12, "#444444")
badge(2009, 14, "②", "2009 后加速上升\ngrew modestly … then accelerated sharply", -1.2, 14, colors["Thailand"], ha="left")
badge(2009, 12, "③", "顶点 peak\nrose steadily to a peak of 12 million", -0.6, 6, colors["Egypt"], ha="right")
badge(2015, 9, "④", "低点 low\ndeclined to a low of 9 million", -1.0, -5, colors["Egypt"], ha="left")
badge(2006, 3.5, "⑤", "2009 前 <4m，之后陡升\nremained below 4 million … before climbing steeply", 3.3, -2.3, colors["Vietnam"], ha="left")
badge(2018, 15, "⑥", "2018 反超 Egypt\nhad been overtaken by Vietnam", -2.6, 6.5, colors["Vietnam"], ha="left")

fig.tight_layout()
fig.text(0.99, 0.01, "数据为教学用近似值", fontsize=8.5, color="grey", ha="right", va="bottom")
fig.savefig(os.path.join(OUT, "chart.png"))
plt.close(fig)

# ---------------------------------------------------------------- 图 2：分色范文卡（PIL）
# 样式：n 普通 | v 趋势动词/名词(红) | d 数据+介词(蓝) | c 连接/对比(绿) | p 改写/Overview信号词(紫)
STYLE_COLOR = {"n": (40, 40, 40), "v": (200, 30, 30), "d": (20, 90, 200),
               "c": (20, 140, 70), "p": (130, 40, 170)}
LEGEND = [("v", "趋势动词 / 名词"), ("d", "数据 + 介词"), ("c", "连接 / 对比"), ("p", "题目改写 / 总览信号词")]

essay = [
    ("P1  Introduction  改写题目", [
        ("The line graph ", "n"), ("compares the number of", "p"), (" international tourists ", "n"),
        ("visiting", "p"), (" Thailand, Egypt and Vietnam ", "n"), ("over an 18-year period from 2000 to 2018", "p"), (".", "n")]),
    ("P2  Overview  两句，不写数字", [
        ("Overall,", "p"), (" Thailand attracted ", "n"), ("by far the most", "c"), (" visitors ", "n"),
        ("throughout the period", "d"), (" and saw ", "n"), ("the largest growth", "v"), (", ", "n"), ("while", "c"),
        (" Vietnam experienced ", "n"), ("the most rapid rise", "v"), (" in proportional terms. Egypt was ", "n"),
        ("the only country whose", "c"), (" figures ", "n"), ("fluctuated", "v"), (", and ", "n"),
        ("by the end of the period", "d"), (" it ", "n"), ("had been overtaken by", "v"), (" Vietnam.", "n")]),
    ("P3  Body 1  Thailand + Vietnam（相似模式）", [
        ("In 2000", "d"), (", Thailand received ", "n"), ("around 10 million", "d"), (" tourists, ", "n"),
        ("roughly twice as many as", "c"), (" Egypt ", "n"), ("(5 million)", "d"), (" and ", "n"),
        ("five times the figure for", "c"), (" Vietnam ", "n"), ("(2 million)", "d"), (". Thai arrivals ", "n"),
        ("grew modestly", "v"), (" to 14 million by 2009", "d"), (", and then ", "n"), ("accelerated sharply", "v"),
        (", ", "n"), ("reaching", "v"), (" 38 million in 2018", "d"), (". Vietnam ", "n"),
        ("followed a similar pattern on a smaller scale", "c"), (": numbers ", "n"), ("remained below", "v"),
        (" 4 million until 2009", "d"), (" ", "n"), ("before climbing steeply", "v"), (" to 15 million in 2018", "d"), (".", "n")]),
    ("P4  Body 2  Egypt（不同模式）", [
        ("Egypt, ", "n"), ("by contrast", "c"), (", ", "n"), ("followed a very different trajectory", "c"),
        (". Visitor numbers ", "n"), ("rose steadily", "v"), (" from 5 million ", "d"), ("to a peak of", "v"),
        (" 12 million in 2009", "d"), (", but then ", "n"), ("declined", "v"), (" to ", "d"), ("a low of", "v"),
        (" 9 million in 2015", "d"), (". ", "n"), ("Although", "c"), (" there was ", "n"), ("a partial recovery", "v"),
        (" to 11 million in 2018", "d"), (", this was ", "n"), ("still below", "c"), (" the figure recorded ", "n"),
        ("nine years earlier", "d"), (", and ", "n"), ("4 million lower than that of", "c"), (" Vietnam.", "n")]),
]

FONT_DIR = "/System/Library/Fonts/Supplemental/"
f_reg = ImageFont.truetype(FONT_DIR + "Arial Unicode.ttf", 30)
f_bold = ImageFont.truetype(FONT_DIR + "Arial Bold.ttf", 30)
f_label = ImageFont.truetype(FONT_DIR + "Arial Unicode.ttf", 24)
f_title = ImageFont.truetype(FONT_DIR + "Arial Unicode.ttf", 38)

W, PAD, LINE_H, MAXW = 1900, 70, 46, 1900 - 2 * 70

def tokens(segments):
    """按空格切词，空格本身也是 token（用普通字体测宽），保证分色词前后空格不丢"""
    import re
    out = []
    for text, st in segments:
        for p in re.split(r"(\s+)", text):
            if p:
                out.append((p, st))
    return out

def layout(segments):
    lines, cur, x = [], [], 0
    for word, st in tokens(segments):
        is_space = word.isspace()
        font = f_reg if (st == "n" or is_space) else f_bold
        w = font.getlength(word)
        if x + w > MAXW and cur and not is_space:
            while cur and cur[-1][0].isspace():
                cur.pop()
            lines.append(cur); cur, x = [], 0
        if is_space and not cur:
            continue
        cur.append((word, st, font)); x += w
    if cur:
        lines.append(cur)
    return lines

paras = [(label, layout(seg)) for label, seg in essay]
H = PAD + 70 + 60 + sum(40 + len(ls) * LINE_H + 30 for _, ls in paras) + PAD
img = Image.new("RGB", (W, H), (253, 251, 246))
d = ImageDraw.Draw(img)
y = PAD
d.text((PAD, y), "Task 1 背诵范文 · 分色标注卡（199 words）", font=f_title, fill=(30, 30, 30)); y += 70
x = PAD
for st, name in LEGEND:
    d.rectangle([x, y + 6, x + 26, y + 32], fill=STYLE_COLOR[st]); x += 36
    d.text((x, y), name, font=f_label, fill=(60, 60, 60)); x += f_label.getlength(name) + 48
y += 60
for label, lines in paras:
    d.text((PAD, y), label, font=f_label, fill=(120, 120, 120)); y += 40
    for ln in lines:
        x = PAD
        for word, st, font in ln:
            d.text((x, y + 34), word, font=font, fill=STYLE_COLOR[st], anchor="ls"); x += font.getlength(word)
        y += LINE_H
    y += 30
img.save(os.path.join(OUT, "essay_card.png"))

# ---------------------------------------------------------------- 图 3：四段结构提纲
fig, ax = plt.subplots(figsize=(13, 8.6), dpi=160)
ax.set_xlim(0, 13); ax.set_ylim(0, 8.6); ax.axis("off")
blocks = [
    ("P1  Introduction · 1 句", "#8e44ad",
     "改写题目：图表类型 + compares + 内容 + 地点 + 时间段\n起句：The line graph compares the number of …\n考点：不抄题；percentage→proportion / shows→compares / between…and→over a period from…to…"),
    ("P2  Overview · 2 句", "#2980b9",
     "句 1：谁最多 + 谁增长最快（by far the most / the largest growth / while …）\n句 2：谁是例外（the only country whose … fluctuated）+ 结尾状态（had been overtaken by）\n考点：不写具体数字；用 the most / the only / by the end of the period 概括"),
    ("P3  Body 1 · 4 句 · 相似的两条线", "#1f77b4",
     "① 起点 + 倍数对比：twice as many as / five times the figure for\n② 先缓后急：grew modestly to … by …, and then accelerated sharply, reaching …\n③ 另一条线同模式：followed a similar pattern on a smaller scale\n④ remained below … until …, before climbing steeply to …"),
    ("P4  Body 2 · 3 句 · 不同的一条线", "#e07b00",
     "① 转折开头：X, by contrast, followed a very different trajectory\n② 升到顶再降到底：rose steadily … to a peak of … but then declined to a low of …\n③ 让步 + 两重比较：Although … a partial recovery …, this was still below … and lower than that of …"),
]
y0 = 8.3
for title, col, body in blocks:
    h = 0.62 + 0.36 * (body.count("\n") + 1)
    ax.add_patch(FancyBboxPatch((0.3, y0 - h), 12.4, h - 0.12, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=col, ec="none", alpha=0.10))
    ax.add_patch(FancyBboxPatch((0.3, y0 - h), 0.18, h - 0.12, boxstyle="square,pad=0", fc=col, ec="none"))
    ax.text(0.7, y0 - 0.32, title, fontsize=13.5, fontweight="bold", color=col, va="top")
    ax.text(0.7, y0 - 0.68, body, fontsize=10.3, color="#333333", va="top", linespacing=1.55)
    y0 -= h + 0.08
ax.text(6.5, 8.5, "背诵提纲：先背结构，再背每段的「骨架句式」，最后填数据", fontsize=12.5,
        ha="center", va="bottom", color="#222222", fontweight="bold")
fig.savefig(os.path.join(OUT, "structure.png"), bbox_inches="tight")
plt.close(fig)
print("ok:", os.listdir(OUT))
