from PIL import Image, ImageDraw, ImageFont
import os


W, H = 1080, 1440
OUT = "/Users/maple/Documents/AI-project/AI-Systematicity/output/canvas_design/llm_ml_poster_refined.png"

BG = "#F2F3F1"
TEXT = "#2A2A2A"
TEXT_MUTED = "#575757"
ACCENT = "#B6672B"
PINK = "#F7ECEC"
NUM = "#6E85D6"


def font(size: int):
    candidates = [
        "/Users/maple/Library/Fonts/SourceHanSansCN-Normal.otf",
        "/System/Library/Fonts/PingFang.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    raise FileNotFoundError("No suitable font found")


IMG = Image.new("RGB", (W, H), BG)
DRAW = ImageDraw.Draw(IMG)

TITLE_FONT = font(56)
BAR_FONT = font(27)
BAR_NUM_FONT = font(24)
BODY_FONT = font(23)
STEP_NUM_FONT = font(22)
FORMULA_FONT = font(40)
RULE_FONT = font(33)

LEFT = 46
RIGHT = 46
CONTENT_W = W - LEFT - RIGHT


def measure(text: str, current_font):
    box = DRAW.textbbox((0, 0), text, font=current_font)
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


def draw_paragraph(text: str, x: int, y: int, current_font, fill: str, max_width: int, gap: int = 8):
    lines = wrap_text(text, current_font, max_width)
    _, line_h = measure("测试A", current_font)
    for line in lines:
        DRAW.text((x, y), line, font=current_font, fill=fill)
        y += line_h + gap
    return y


def draw_question_bar(number: int, text: str, y: int):
    height = 34
    DRAW.rounded_rectangle(
        (LEFT, y, LEFT + CONTENT_W, y + height),
        radius=7,
        fill=PINK,
    )
    DRAW.text((LEFT + 12, y + 3), f"{number}.", font=BAR_NUM_FONT, fill=NUM)
    DRAW.text((LEFT + 56, y + 3), text, font=BAR_FONT, fill=TEXT)
    return y + height + 16


title_y = 56
DRAW.text((LEFT, title_y), "大模型", font=TITLE_FONT, fill=ACCENT)
title_x = DRAW.textbbox((LEFT, title_y), "大模型", font=TITLE_FONT)[2] + 5
DRAW.text((title_x, title_y), "-机器学习", font=TITLE_FONT, fill=TEXT)

y = 176
y = draw_question_bar(5, "什么是梯度下降法?", y)
y = draw_paragraph(
    "梯度下降是沿损失函数负梯度方向迭代更新模型参数，使损失函数逐步最小化的优化算法。",
    LEFT,
    y,
    BODY_FONT,
    TEXT,
    900,
)
y += 14
formula = "θ = θ - η · ∇J(θ)"
fw, fh = measure(formula, FORMULA_FONT)
DRAW.text(((W - fw) // 2, y), formula, font=FORMULA_FONT, fill=TEXT)
y += fh + 18
y = draw_paragraph(
    "其中 θ 是模型参数，η 是学习率，∇J(θ) 是损失函数的梯度。",
    LEFT,
    y,
    BODY_FONT,
    TEXT_MUTED,
    900,
)
y += 26

y = draw_question_bar(6, "反向传播是如何工作的？（以梯度下降法为例）", y)
steps = [
    "先通过前向传播计算网络输出与损失值",
    "再利用链式法则将误差从输出层反向传递到各层，求出每一层权重和偏置的梯度",
    "最后依据梯度下降法，沿梯度反方向更新权重与偏置",
    "重复以上过程，不断迭代减小损失，直至模型收敛",
]
for index, step in enumerate(steps, start=1):
    DRAW.text((LEFT, y), f"{index}.", font=STEP_NUM_FONT, fill=NUM)
    lines = wrap_text(step, BODY_FONT, 870)
    _, line_h = measure("测试A", BODY_FONT)
    for line_index, line in enumerate(lines):
        DRAW.text((LEFT + 34, y + line_index * (line_h + 7)), line, font=BODY_FONT, fill=TEXT)
    y += len(lines) * (line_h + 7) + 7

y += 16
y = draw_question_bar(7, "什么是逻辑回归？它是分类还是回归算法?", y)
y = draw_paragraph(
    "逻辑回归是将特征线性组合后，把结果通过 Sigmoid 激活函数映射到 0 到 1 得到类别概率，是用于二分类的监督学习算法，属于分类算法。",
    LEFT,
    y,
    BODY_FONT,
    TEXT,
    900,
)
y += 14
formula2 = "hθ(x) = 1 / (1 + e^(-θ^T x))"
fw2, fh2 = measure(formula2, FORMULA_FONT)
DRAW.text(((W - fw2) // 2, y), formula2, font=FORMULA_FONT, fill=TEXT)
y += fh2 + 18
y = draw_paragraph(
    "式中 hθ(x) 为样本为正类的概率，θ^T x 是特征线性加权，以 0.5 为概率阈值划分二分类结果，具体分类规则如下：",
    LEFT,
    y,
    BODY_FONT,
    TEXT_MUTED,
    900,
)
y += 12
rule_1 = "y = {1,  hθ(x) ≥ 0.5"
rule_2 = "    {0,  hθ(x) < 0.5"
for rule in (rule_1, rule_2):
    rw, rh = measure(rule, RULE_FONT)
    DRAW.text(((W - rw) // 2, y), rule, font=RULE_FONT, fill=TEXT)
    y += rh + 2
y += 10
draw_paragraph(
    "式中 y 为样本的最终分类结果，1 代表正类，0 代表负类。",
    LEFT,
    y,
    BODY_FONT,
    TEXT,
    CONTENT_W,
)

IMG.save(OUT, "PNG")
print(OUT)
