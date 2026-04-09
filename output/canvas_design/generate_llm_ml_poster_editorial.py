from PIL import Image, ImageDraw, ImageFont
import os


W, H = 1080, 1440
OUT = "/Users/maple/Documents/AI-project/AI-Systematicity/output/canvas_design/llm_ml_poster_editorial.png"

BG = "#F3F2EE"
TEXT = "#222222"
TEXT_MUTED = "#66605A"
ACCENT = "#B7682C"
PINK = "#F4E8E7"
NUM = "#6B7FC5"


def font(size: int):
    candidates = [
        "/Users/maple/Library/Fonts/SourceHanSansCN-Normal.otf",
        "/System/Library/Fonts/PingFang.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    raise FileNotFoundError("No suitable font found")


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

title_font = font(64)
title_font_2 = font(58)
section_font = font(27)
section_num_font = font(23)
body_font = font(22)
formula_font = font(46)
formula_small_font = font(34)

left = 56


def measure(text: str, current_font):
    box = draw.textbbox((0, 0), text, font=current_font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(text: str, current_font, max_width: int):
    lines = []
    current = ""
    for char in text:
        trial = current + char
        if measure(trial, current_font)[0] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_paragraph(text: str, x: int, y: int, max_width: int, fill: str = TEXT, gap: int = 8):
    lines = wrap_text(text, body_font, max_width)
    _, line_h = measure("测试A", body_font)
    for line in lines:
        draw.text((x, y), line, font=body_font, fill=fill)
        y += line_h + gap
    return y


def draw_section_bar(x: int, y: int, width: int, number: int, title: str):
    height = 34
    draw.rounded_rectangle((x, y, x + width, y + height), radius=7, fill=PINK)
    draw.text((x + 10, y + 4), f"{number}.", font=section_num_font, fill=NUM)
    draw.text((x + 52, y + 4), title, font=section_font, fill=TEXT)
    return y + height + 14


# Masthead
title_y = 72
draw.text((left, title_y), "大模型", font=title_font, fill=ACCENT)
draw.text((left + 6, title_y + 74), "机器学习", font=title_font_2, fill=TEXT)

# Q5 top lead
q5_x = left
q5_y = 206
q5_width = 910
y = draw_section_bar(q5_x, q5_y, q5_width, 5, "什么是梯度下降法?")
y = draw_paragraph(
    "梯度下降是沿损失函数负梯度方向迭代更新模型参数，使损失函数逐步最小化的优化算法。",
    q5_x,
    y,
    760,
)
y += 18
formula = "θ = θ - η · ∇J(θ)"
fw, fh = measure(formula, formula_font)
draw.text((q5_x + 330, y), formula, font=formula_font, fill=TEXT)
y += fh + 18
y = draw_paragraph(
    "其中 θ 是模型参数，η 是学习率，∇J(θ) 是损失函数的梯度。",
    q5_x,
    y,
    720,
    fill=TEXT_MUTED,
)

# Q6 dominant center block
q6_x = left
q6_y = 510
q6_width = 860
y = draw_section_bar(q6_x, q6_y, q6_width, 6, "反向传播是如何工作的？（以梯度下降法为例）")
steps = [
    "先通过前向传播计算网络输出与损失值",
    "再利用链式法则将误差从输出层反向传递到各层，求出每一层权重和偏置的梯度",
    "最后依据梯度下降法，沿梯度反方向更新权重与偏置",
    "重复以上过程，不断迭代减小损失，直至模型收敛",
]
_, line_h = measure("测试A", body_font)
for index, step in enumerate(steps, start=1):
    draw.text((q6_x, y), f"{index}.", font=section_num_font, fill=NUM)
    lines = wrap_text(step, body_font, 760)
    for line_index, line in enumerate(lines):
        draw.text((q6_x + 30, y + line_index * (line_h + 8)), line, font=body_font, fill=TEXT)
    y += len(lines) * (line_h + 8) + 10

# Q7 lower closing block
q7_x = left
q7_y = 860
q7_width = 790
y = draw_section_bar(q7_x, q7_y, q7_width, 7, "什么是逻辑回归？它是分类还是回归算法?")
y = draw_paragraph(
    "逻辑回归是将特征线性组合后，把结果通过 Sigmoid 激活函数映射到 0 到 1 得到类别概率，是用于二分类的监督学习算法，属于分类算法。",
    q7_x,
    y,
    760,
)
y += 18
formula2 = "hθ(x) = 1 / (1 + e^(-θ^T x))"
fw2, fh2 = measure(formula2, formula_font)
draw.text((q7_x + 260, y), formula2, font=formula_font, fill=TEXT)
y += fh2 + 16
y = draw_paragraph(
    "式中 hθ(x) 为样本为正类的概率，θ^T x 是特征线性加权，以 0.5 为概率阈值划分二分类结果，具体分类规则如下：",
    q7_x,
    y,
    760,
    fill=TEXT_MUTED,
)
y += 10
rule1 = "y = {1,  hθ(x) ≥ 0.5"
rule2 = "    {0,  hθ(x) < 0.5"
for rule in (rule1, rule2):
    rw, rh = measure(rule, formula_small_font)
    draw.text((q7_x + 350, y), rule, font=formula_small_font, fill=TEXT)
    y += rh + 2
y += 10
draw_paragraph(
    "式中 y 为样本的最终分类结果，1 代表正类，0 代表负类。",
    q7_x,
    y,
    760,
)

img.save(OUT, "PNG")
print(OUT)
