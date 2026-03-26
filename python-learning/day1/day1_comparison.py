def char_frequency(text:str) -> dict[str,int]:
  char_count: dict[str,int]={}

  for char in text:
    char_count[char] = char_count.get(char,0)+1

  return char_count



def main() -> None:
  name="Maple"
  age=26
  print(f"{name} is {age} years old.")

  arr = ['a','b','c']
  arr_upper = []
  for x in arr: 
    arr_upper.append(x.upper())
  print(arr_upper)

  num_arr = [1,2,3]
  num_add_ten = []
  for x in num_arr:
    num_add_ten.append(x+10)
  print(num_add_ten)

  text = "fastapi"
  print(f"text={text}, freq={char_frequency(text)}")

  num1 = 100
  num1_flag = num1 % 2 == 0 # True if num1 % 2 == 0 else False
  print(f"{num1} is {num1_flag}")


if __name__ == "__main__":
  main()


"""
定义变量 name="maple"、age=26，打印 name is 26 years old。
把 JS 数组 ["a","b","c"] 映射成大写列表。
给列表 [1,2,3] 每个元素加 10。
统计字符串 "fastapi" 每个字符出现次数（dict）。
判断一个数字是否偶数，返回 True/False。
写函数：输入年份，判断闰年。
写函数：返回列表第二大“不同值”。
用列表推导式取 [1..20] 里的偶数。
用字典推导式生成 {1:1,2:4,...,5:25}。
遍历字典并打印 key=value。
模拟 JS filter：从列表中过滤出长度大于 3 的字符串。
模拟 JS reduce：求列表总和。
写 try/except：处理字符串转整数失败。
读取一个 json 字符串并取字段值。
写类 User，包含 name 和 say_hi() 方法。
写继承：Admin(User)，新增 role 字段。
写函数默认参数：greet(name="world")。
写可变参数函数：sum_all(*nums)。
写一个简单模块文件并在另一个文件中 import 调用。
写一个小 CLI：输入名字后输出欢迎语，输入 q 退出
"""