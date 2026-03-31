"""Day 2 exercises scaffold.
第2天练习脚手架

Run:
  python3 python-learning/day2/day2_exercises.py
"""


def exception_demos() -> None:
    """异常处理演示函数

    演示 Python 异常处理的基本语法：
    - try: 尝试执行的代码块
    - except: 捕获特定类型的异常
    - else: 当没有异常时执行的代码块
    - finally: 无论是否有异常都会执行的代码块
    """
    print("=== Exception Demo ===")
    # 定义测试用例列表，每个元素是一个元组 (被除数, 除数)
    cases = [(10, 2), (5, 0), ("a", 1)]

    # 遍历每个测试用例
    for a, b in cases:
        try:
            # 尝试执行除法运算
            result = a / b
        except ZeroDivisionError:
            # 捕获除零错误：当除数为0时触发
            print(f"{a}/{b} -> divide by zero")
        except TypeError:
            # 捕获类型错误：当操作数类型不支持除法运算时触发
            print(f"{a}/{b} -> type error")
        else:
            # 当没有异常发生时执行：打印正常结果
            print(f"{a}/{b} -> {result}")
        finally:
            # 无论是否有异常都会执行（这里用 pass 占位）
            pass


def exception_demo2() -> None:
    """异常处理演示函数2

    演示字符串转换为整数后的异常处理
    """
    print("=== Exception Demo2 ===")
    # 定义测试用例列表，第一个元素是字符串形式的数字
    cases = [("10", 2), ("5", 0), ("a", 1)]

    for a, b in cases:
        try:
            # int(a) 将字符串转换为整数，然后进行除法运算
            result = int(a) / b
        except TypeError:
            # 捕获类型错误（在这个例子中不会触发，因为 int() 会处理字符串）
            print(f"{a}/{b} -> type error")
        except ZeroDivisionError:
            # 捕获除零错误
            print(f"{a}/{b} -> divide by zero")
        else:
            # 正常情况：打印结果
            print(f"{a}/{b} -> {result}")
        finally:
            # 无论是否有异常都会执行
            pass


def comprehension_demos() -> None:
    """推导式演示函数

    演示 Python 的列表推导式和字典推导式语法
    """
    print("\n=== Comprehension Demo ===")

    # 定义数字列表
    nums = [1, 2, 3, 4, 5, 6]

    # 列表推导式：计算每个数字的平方
    # 语法：[表达式 for 变量 in 可迭代对象]
    squares = [x * x for x in nums]

    # 列表推导式 + 条件过滤：只保留偶数
    # 语法：[表达式 for 变量 in 可迭代对象 if 条件]
    evens = [x for x in nums if x % 2 == 0]

    # 列表推导式 + 条件表达式：为每个数字添加标签
    # 语法：[值1 if 条件 else 值2 for 变量 in 可迭代对象]
    labels = ["even" if x % 2 == 0 else "odd" for x in nums]

    # 字典推导式：创建数字到平方的映射
    # 语法：{键表达式: 值表达式 for 变量 in 可迭代对象}
    square_map = {x: x * x for x in range(1, 6)}

    # 第二组演示数据
    num2 = [1, 2, 3, 4, 5, 6]
    squares2 = [x * x for x in num2]
    labels2 = ["even" if x % 2 == 0 else "odd" for x in num2]
    square_map2 = {x: x * x for x in range(1, 6)}

    # 打印结果
    print(f"squares={squares}")
    print(f"evens={evens}")
    print(f"labels={labels}")
    print(f"square_map={square_map}")

    print(f"squares2={squares2}")
    print(f"labels2={labels2}")
    print(f"square_map2={square_map2}")


def char_frequency(text: str) -> dict[str, int]:
    """统计字符串中每个字符的出现频率

    参数:
        text: 输入的字符串

    返回:
        字典，键为字符，值为该字符的出现次数

    示例:
        char_frequency("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # 初始化空字典，用于存储字符频率
    freq: dict[str, int] = {}

    # 遍历字符串中的每个字符
    for ch in text:
        # dict.get(key, default) 方法：
        # - 如果键存在，返回对应的值
        # - 如果键不存在，返回默认值（这里是0）
        # 然后将值加1，更新到字典中
        freq[ch] = freq.get(ch, 0) + 1

    return freq


def safe_divide(a: float, b: float):
    """安全除法函数

    参数:
        a: 被除数
        b: 除数

    返回:
        除法结果（成功时）或错误信息（除数为0时）

    特点:
        使用异常处理来避免程序崩溃，返回友好的错误信息
    """
    try:
        # 尝试执行除法运算
        return a / b
    except ZeroDivisionError:
        # 捕获除零错误，返回错误信息而不是抛出异常
        return "Error: divide by zero"


def normalize_scores(scores: list[float]) -> list[float]:
    """最小-最大归一化函数

    将分数值缩放到 [0, 1] 区间
    公式: x_norm = (x - min) / (max - min)

    参数:
        scores: 分数列表

    返回:
        归一化后的分数列表

    边界情况处理:
        1. 空列表：返回空列表
        2. 所有值相同：返回全0列表（避免除零错误）
    """
    # 检查输入列表是否为空
    if not scores:
        return []

    # 计算最小值和最大值
    min_v = min(scores)
    max_v = max(scores)

    # 处理所有值相同的情况（避免除零错误）
    if max_v == min_v:
        # 返回与原列表长度相同的全0列表
        # _ 是占位符，表示我们不关心循环变量的值
        return [0.0 for _ in scores]

    # 应用归一化公式：对每个分数进行归一化
    # 使用列表推导式生成结果列表
    return [(x - min_v) / (max_v - min_v) for x in scores]


def top_k(nums: list[int], k: int) -> list[int]:
    """获取前k个最大的唯一数字

    参数:
        nums: 数字列表
        k: 要获取的数量

    返回:
        前k个最大的唯一数字列表

    边界情况处理:
        1. k <= 0：返回空列表
        2. 唯一数字数量少于k：返回所有唯一数字
    """
    # 检查k是否有效
    if k <= 0:
        return []

    # 去重并排序
    # set(nums): 去除重复元素
    # sorted(..., reverse=True): 降序排列
    uniq = sorted(set(nums), reverse=True)

    # 切片操作：获取前k个元素
    # 如果uniq长度小于k，返回所有元素
    return uniq[:k]


def run_function_tests() -> None:
    """运行函数测试

    测试各个函数的功能，验证边界情况处理
    """
    print("\n=== Function Tests ===")

    # 测试 safe_divide 函数
    # 正常情况：10/2=5.0
    # 异常情况：10/0 返回错误信息
    print("safe_divide:", safe_divide(10, 2), safe_divide(10, 0))

    # 测试 normalize_scores 函数
    # 正常情况：[60, 70, 80] -> [0.0, 0.5, 1.0]
    # 边界情况：[5, 5, 5] -> [0.0, 0.0, 0.0]
    print(
        "normalize_scores:", normalize_scores([60, 70, 80]), normalize_scores([5, 5, 5])
    )

    # 测试 top_k 函数
    # 正常情况：[7, 2, 9, 9, 1], k=2 -> [9, 7]
    # 边界情况：[1, 1, 1], k=3 -> [1]（只有一个唯一值）
    print("top_k:", top_k([7, 2, 9, 9, 1], 2), top_k([1, 1, 1], 3))

    # 测试 char_frequency 函数
    # 统计 "fastapi" 中每个字符的出现频率
    print("char_frequency:", char_frequency("fastapi"))


if __name__ == "__main__":
    # 当文件作为主程序运行时，执行以下函数
    exception_demos()  # 运行异常处理演示
    comprehension_demos()  # 运行推导式演示
    run_function_tests()  # 运行函数测试
