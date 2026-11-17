"""生成 07_拓展练习 的全部配图，输出到 ../img/
运行：python3 make_figures.py

method.png        解题五步流程（20 分钟时间分配）
trend_shapes.png  趋势形状 × 词汇（看图选词）
prepositions.png  数据介词图解 from / to / by / of / at
caseN.png         练习题原图（考试风格，不带提示）
caseN_key.png     同一张图 + 考点编号标注（解题思路里用）
所有数据为教学用近似值。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["font.family"] = ["Hiragino Sans GB", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

C = ["#1f77b4", "#e07b00", "#2a9d4b", "#c0392b", "#8e44ad"]
GREY = "#444444"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight")
    plt.close(fig)


# ============================================================ 1. 解题五步
def method():
    steps = [
        ("① 读题", "2 分钟", "#8e44ad",
         "圈出：图表类型 / 对象\n单位 / 地点 / 时间段\n\n过去？现在？预测？\n→ 定时态"),
        ("② 读图找特征", "3 分钟", "#2980b9",
         "总体趋势（升 / 降 / 稳）\n最高 & 最低\n变化最大的\n交叉、反超、例外\n→ 2 个写进 Overview"),
        ("③ 分组定提纲", "2 分钟", "#1f77b4",
         "按时间：有明确转折点\n按趋势：多条线\n按类别：类别少、线长\n→ Body 1 / Body 2\n各 3–4 句"),
        ("④ 写", "11 分钟", "#e07b00",
         "P1 改写题目 1 句\nP2 Overview 2 句不写数\nP3 / P4 数据句\n每句：趋势+数据+时间\n160–190 词"),
        ("⑤ 检查", "2 分钟", "#2a9d4b",
         "对照错题集自查清单\n• of owned ✗\n• 名词前用形容词\n• in + 年份\n• from/to/by/of/at"),
    ]
    fig, ax = plt.subplots(figsize=(15.5, 4.4), dpi=160)
    ax.set_xlim(0, 15.5); ax.set_ylim(1.4, 5.6); ax.axis("off")
    w, gap, x = 2.6, 0.48, 0.2
    for i, (title, t, col, body) in enumerate(steps):
        ax.add_patch(FancyBboxPatch((x, 1.5), w, 3.1, boxstyle="round,pad=0.02,rounding_size=0.18",
                                    fc=col, ec="none", alpha=0.10))
        ax.add_patch(FancyBboxPatch((x, 3.85), w, 0.75, boxstyle="round,pad=0.02,rounding_size=0.18",
                                    fc=col, ec="none"))
        ax.text(x + w / 2, 4.22, title, color="white", fontsize=14, fontweight="bold", ha="center", va="center")
        ax.text(x + w / 2, 3.5, t, color=col, fontsize=12, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.18, 3.15, body, color="#333333", fontsize=10.5, va="top", linespacing=1.6)
        if i < len(steps) - 1:
            ax.add_patch(FancyArrowPatch((x + w + 0.04, 3.0), (x + w + gap - 0.04, 3.0),
                                         arrowstyle="-|>", mutation_scale=20, color="#999999", lw=2))
        x += w + gap
    ax.text(7.75, 5.15, "Task 1 动态图 · 20 分钟解题流程", fontsize=16, fontweight="bold", ha="center", color="#222222")
    save(fig, "method.png")


# ============================================================ 2. 趋势形状 × 词汇
def trend_shapes():
    import numpy as np
    x = np.linspace(0, 10, 50)
    shapes = [
        ("稳步上升", x * 0.6 + 2, "rise / increase / climb steadily\na steady / gradual rise"),
        ("急剧上升", np.where(x < 6, 2 + x * 0.1, 2.6 + (x - 6) ** 2 * 0.35), "soar / rocket / surge\na dramatic / sharp rise"),
        ("小幅下降", 6 - x * 0.12, "fall / dip / decrease slightly\na slight / modest fall"),
        ("暴跌", np.where(x < 5, 7.5, np.maximum(7.5 - (x - 5) * 1.3, 1.2)), "plummet / plunge / collapse\na sharp / dramatic fall"),
        ("保持不变", 4 + 0 * x, "remain stable / unchanged\nstay constant at …\nlevel off（升后变平）"),
        ("波动", 4 + 1.2 * np.sin(x * 1.6), "fluctuate (between … and …)\nwild / slight fluctuations"),
        ("到顶后回落", 7 - 0.12 * (x - 5.5) ** 2, "peak at / reach a peak of …\nthen fall back to …"),
        ("跌到底后回升", 2 + 0.11 * (x - 4.5) ** 2, "hit a low of / bottom out at …\nrecover / pick up to …"),
        ("交叉反超", None, "overtake / exceed / surpass\nconverge（持平）/ the gap narrows"),
    ]
    fig, axes = plt.subplots(3, 3, figsize=(14, 11), dpi=160)
    for ax, (title, y, words) in zip(axes.flat, shapes):
        if y is None:
            ax.plot(x, 2 + x * 0.55, color=C[0], lw=3)
            ax.plot(x, 6.5 - x * 0.25, color=C[1], lw=3)
            ax.plot([5.3], [5.2], "o", ms=12, mfc="none", mec=C[3], mew=2.5)
        else:
            ax.plot(x, y, color=C[0], lw=3)
        ax.set_ylim(0, 9.5); ax.set_xlim(-0.3, 10.3)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.set_title(title, fontsize=14, fontweight="bold", color=GREY, pad=8)
        ax.text(0.5, -0.06, words, transform=ax.transAxes, ha="center", va="top",
                fontsize=10.8, color=C[3], linespacing=1.5)
    fig.suptitle("看形状选词：动词（上）/ 形容词 + 名词（下）", fontsize=17, fontweight="bold", y=0.995)
    fig.tight_layout(h_pad=5.2)
    save(fig, "trend_shapes.png")


# ============================================================ 3. 数据介词图解
def prepositions():
    fig, ax = plt.subplots(figsize=(13, 6.4), dpi=160)
    yrs = [1918, 1971, 2001, 2011]
    vals = [23, 50, 69, 64]
    ax.plot(yrs, vals, marker="o", lw=3, ms=9, color=C[0], zorder=3)
    ax.set_ylim(0, 95); ax.set_xlim(1905, 2040)
    ax.set_xticks(yrs); ax.set_ylabel("Home ownership (%)", fontsize=11)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", alpha=0.25)

    def note(xy, xytext, text, col):
        ax.annotate(text, xy=xy, xytext=xytext, fontsize=11.5, color=col, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=col, lw=1.5),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.5))

    note((1918, 23), (1918, 48), "起点 from\nrose from 23% …", C[2])
    note((1971, 50), (1950, 72), "终点 to\n… to 50%", C[2])
    ax.annotate("", xy=(1985, 50), xytext=(1985, 23),
                arrowprops=dict(arrowstyle="<->", color=C[1], lw=2))
    ax.plot([1918, 1985], [23, 23], ls=":", color=C[1]); ax.plot([1971, 1985], [50, 50], ls=":", color=C[1])
    ax.text(1987, 36.5, "变化量 27 percentage points\n动词后 by：rose by 27 points\n名词后 of：a rise of 27 points in …",
            fontsize=11.5, color=C[1], va="center",
            bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=C[1], lw=1.5))
    note((2001, 69), (1996, 86), "停在某值 at\npeaked at 69% in 2001", C[3])
    note((2011, 64), (2027, 80), "终点 to\nfell back to 64%", C[2])
    ax.text(1906, 8, "年份前一律 in：in 1918 / in 2001　　百分比相减说 percentage points，不说 %",
            fontsize=11, color=GREY)
    ax.set_title("数字前用什么介词？先问：起点 / 终点 / 变化量 / 停在某值", fontsize=15, fontweight="bold", pad=14)
    save(fig, "prepositions.png")


# ============================================================ 4. 练习题图
def badge(ax, xy, xytext, num, text, col, ha="left"):
    ax.annotate(num, xy=xy, xytext=xytext, fontsize=11, fontweight="bold", color="white",
                ha="center", va="center", bbox=dict(boxstyle="circle,pad=0.3", fc=col, ec=col),
                arrowprops=dict(arrowstyle="-", color=col, lw=1.3), zorder=6)
    off = 0.012 if ha == "left" else -0.012
    ax.annotate(text, xy=xytext, xycoords="data", xytext=(off * 1000, 0), textcoords="offset points",
                fontsize=9.8, color=col, ha=ha, va="center", zorder=6,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=col, alpha=0.95))


def style(ax, title, ylabel):
    ax.set_title(title, fontsize=13.5, fontweight="bold", pad=14)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.grid(axis="y", alpha=0.3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def bars(ax, cats, series, colors, width=0.38, labels=True):
    n = len(series)
    for i, (name, ys) in enumerate(series.items()):
        xs = [k + (i - (n - 1) / 2) * width for k in range(len(cats))]
        b = ax.bar(xs, ys, width=width * 0.95, color=colors[i], label=name, zorder=3)
        if labels:
            ax.bar_label(b, fmt="%g", fontsize=8.5, padding=2, color=colors[i])
    ax.set_xticks(range(len(cats))); ax.set_xticklabels(cats)


def lines(ax, xs, series, colors, labels=True, dashed_from=None):
    for i, (name, ys) in enumerate(series.items()):
        if dashed_from is None:
            ax.plot(xs, ys, marker="o", lw=2.6, ms=6, color=colors[i], label=name, zorder=3)
        else:
            k = xs.index(dashed_from)
            ax.plot(xs[:k + 1], ys[:k + 1], marker="o", lw=2.6, ms=6, color=colors[i], label=name, zorder=3)
            ax.plot(xs[k:], ys[k:], marker="o", lw=2.6, ms=6, color=colors[i], ls="--", mfc="white", zorder=3)
        if labels:
            for x, y in zip(xs, ys):
                ax.annotate(f"{y:g}", (x, y), textcoords="offset points", xytext=(0, 8),
                            ha="center", fontsize=8.5, color=colors[i])


def case1(key):
    cats = ["1950", "1960", "1970", "1980", "1990", "2000", "2010", "2020"]
    s = {"Urban": [18, 24, 31, 40, 48, 55, 63, 71], "Rural": [82, 76, 69, 60, 52, 45, 37, 29]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    bars(ax, cats, s, [C[0], C[2]])
    style(ax, "Percentage of the population living in urban and rural areas, Country X, 1950–2020", "% of population")
    ax.set_ylim(0, 100); ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5))
    if key:
        badge(ax, (0, 82), (1.2, 94), "①", "起点：农村占绝对多数 82 vs 18", GREY)
        badge(ax, (4.5, 50), (3.0, 72), "②", "1990–2000 之间交叉（不在整年份）\nsome time between 1990 and 2000", C[3])
        badge(ax, (7, 71), (5.6, 88), "③", "终点：城市 71 ≈ 农村 29 的 2.5 倍", C[0])
        badge(ax, (3.2, 40), (1.6, 47), "④", "镜像：一升一降，每 10 年约 7 个点", C[2])
    save(fig, f"case1{'_key' if key else ''}.png")


def case2(key):
    xs = [2010, 2012, 2014, 2016, 2018, 2020]
    s = {"Art Museum": [420, 450, 390, 410, 430, 440],
         "Science Museum": [180, 210, 290, 380, 460, 520],
         "History Museum": [260, 250, 240, 230, 225, 220]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    lines(ax, xs, s, C[:3])
    style(ax, "Number of visits to three museums in a European city, 2010–2020", "Visits (thousands)")
    ax.set_xticks(xs); ax.set_ylim(0, 600); ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5))
    if key:
        badge(ax, (2012, 450), (2011, 560), "①", "Art：在 390–450 之间波动，整体稳定", C[0])
        badge(ax, (2017, 420), (2012.4, 130), "②", "2016–2018 Science 反超 Art\novertook … shortly after 2016", C[3])
        badge(ax, (2020, 520), (2018.4, 580), "③", "Science 涨近 3 倍：180 → 520", C[1], ha="right")
        badge(ax, (2020, 220), (2018.6, 130), "④", "History 缓慢下降 260 → 220", C[2], ha="right")
    save(fig, f"case2{'_key' if key else ''}.png")


def case3(key):
    xs = [2015, 2020, 2025, 2030, 2035]
    s = {"Country A": [20, 50, 85, 95, 98], "Country B": [2, 10, 20, 45, 70], "Country C": [1, 2, 5, 18, 40]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    lines(ax, xs, s, [C[0], C[1], C[2]], dashed_from=2025)
    ax.axvspan(2025, 2035.6, color="#eeeeee", zorder=0)
    ax.text(2030, 3, "projected 预测", ha="center", fontsize=10, color="grey")
    style(ax, "Electric cars as a percentage of new car sales in three countries, 2015–2035", "% of new car sales")
    ax.set_xticks(xs); ax.set_ylim(0, 110); ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5))
    if key:
        badge(ax, (2025, 85), (2021, 100), "①", "实线 = 已发生 → 过去时 / 现在完成时", C[0], ha="right")
        badge(ax, (2035, 98), (2032.5, 80), "②", "A 预计趋平 level off at ~98%", C[0], ha="right")
        badge(ax, (2032, 57), (2026.5, 62), "③", "B 未来涨最快 20 → 70\nis expected to more than triple", C[1], ha="right")
        badge(ax, (2035, 40), (2031, 26), "④", "C 仍落后 will still lag behind", C[2], ha="right")
    save(fig, f"case3{'_key' if key else ''}.png")


def table_fig(name, title, header, rows, highlight=None):
    fig, ax = plt.subplots(figsize=(10, 0.7 + 0.55 * (len(rows) + 1)), dpi=150)
    ax.axis("off")
    t = ax.table(cellText=rows, colLabels=header, loc="center", cellLoc="center")
    t.auto_set_font_size(False); t.set_fontsize(12); t.scale(1, 2.0)
    for (r, c), cell in t.get_celld().items():
        cell.set_edgecolor("#bbbbbb")
        if r == 0:
            cell.set_facecolor("#1f77b4"); cell.set_text_props(color="white", fontweight="bold")
        elif c == 0:
            cell.set_text_props(fontweight="bold")
        if highlight and (r, c) in highlight:
            cell.set_facecolor(highlight[(r, c)])
    ax.set_title(title, fontsize=13.5, fontweight="bold", pad=10)
    save(fig, name)


def case4(key):
    header = ["Mode of transport", "2000", "2010", "2020"]
    rows = [["Bus", "120", "105", "80"], ["Metro", "60", "110", "165"],
            ["Bicycle", "10", "18", "45"], ["Taxi", "30", "32", "28"]]
    hl = None
    if key:
        hl = {(1, 1): "#fde2e2", (1, 3): "#fde2e2", (2, 1): "#dff3e4", (2, 2): "#fff3c4", (1, 2): "#fff3c4",
              (2, 3): "#dff3e4", (3, 1): "#e3ecfa", (3, 3): "#e3ecfa", (4, 1): "#eeeeee", (4, 2): "#eeeeee",
              (4, 3): "#eeeeee"}
    table_fig(f"case4{'_key' if key else ''}.png",
              "Number of journeys made by four modes of transport in a city (millions)" +
              ("\n红 = Bus 下降　绿 = Metro 大涨　黄 = 2010 反超　蓝 = 自行车涨幅最大（×4.5）　灰 = Taxi 基本不变" if key else ""),
              header, rows, hl)


def case5(key):
    cats = ["Housing", "Food", "Transport", "Leisure"]
    s = {"1980": [20, 28, 14, 10], "2000": [26, 20, 16, 15], "2020": [32, 15, 15, 19]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    bars(ax, cats, s, ["#9ecae1", "#4292c6", "#08519c"], width=0.27)
    style(ax, "Percentage of household income spent on four categories in a country, 1980–2020", "% of household income")
    ax.set_ylim(0, 40); ax.legend(frameon=False, loc="upper right", ncol=3)
    if key:
        badge(ax, (0.27, 32), (0.9, 37), "①", "Housing 稳步上升 20 → 32，成最大项", C[3])
        badge(ax, (1 - 0.27, 28), (1.6, 31), "②", "Food 1980 最大，2000 被 Housing 取代\n降 13 percentage points", C[1])
        badge(ax, (2, 16), (2.2, 24), "③", "Transport 基本稳定 14–16", GREY)
        badge(ax, (3.27, 19), (2.9, 33), "④", "Leisure 近翻倍 10 → 19", C[2])
    save(fig, f"case5{'_key' if key else ''}.png")


def case6(key):
    xs = [0, 3, 6, 9, 12, 15, 18, 21, 24]
    lab = ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00", "24:00"]
    s = {"Winter day": [30, 26, 32, 40, 38, 37, 45, 38, 31], "Summer day": [24, 20, 22, 30, 34, 36, 33, 28, 25]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    lines(ax, xs, s, [C[0], C[3]])
    style(ax, "Electricity demand in a country on a typical winter day and summer day", "Demand (gigawatts)")
    ax.set_xticks(xs); ax.set_xticklabels(lab); ax.set_ylim(0, 55); ax.legend(frameon=False, loc="upper left")
    if key:
        badge(ax, (3, 26), (4.5, 12), "①", "两条线最低都在凌晨 3 点\nat 3 am / in the early hours", GREY)
        badge(ax, (18, 45), (19.5, 51), "②", "冬季顶点：at 6 pm, 45 GW", C[0])
        badge(ax, (15, 36), (12.5, 49), "③", "夏季顶点：at 3 pm, 36 GW\n两线最接近", C[3], ha="right")
        badge(ax, (10.5, 39), (6.5, 47), "④", "冬季上午后平稳 remained fairly stable", C[0], ha="right")
    save(fig, f"case6{'_key' if key else ''}.png")


def case7():
    m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    s = {"2015": [20, 22, 35, 50, 62, 80, 110, 115, 70, 55, 25, 40],
         "2025": [35, 38, 50, 72, 85, 105, 140, 150, 95, 80, 40, 70]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    lines(ax, list(range(12)), s, [C[4], C[1]])
    style(ax, "Monthly visitors to a theme park, 2015 and 2025", "Visitors (thousands)")
    ax.set_xticks(range(12)); ax.set_xticklabels(m); ax.set_ylim(0, 170); ax.legend(frameon=False, loc="upper left")
    save(fig, "case7.png")


def case8():
    xs = [2000, 2005, 2010, 2015, 2020, 2025]
    s = {"Newspapers (print)": [72, 65, 52, 38, 24, 15], "Television": [80, 78, 74, 68, 60, 55],
         "Online sources": [8, 20, 41, 62, 78, 86], "Radio": [35, 33, 30, 28, 27, 25]}
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=150)
    lines(ax, xs, s, [C[0], C[1], C[2], C[4]])
    style(ax, "Percentage of adults in a country using each source for news, 2000–2025", "% of adults")
    ax.set_xticks(xs); ax.set_ylim(0, 100); ax.legend(frameon=False, loc="center left", bbox_to_anchor=(1, 0.5))
    save(fig, "case8.png")


if __name__ == "__main__":
    method(); trend_shapes(); prepositions()
    for k in (False, True):
        case1(k); case2(k); case3(k); case4(k); case5(k); case6(k)
    case7(); case8()
    print("ok:", sorted(os.listdir(OUT)))
