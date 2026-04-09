# Day 4 Notes - venv + pip + 包结构

## 今日目标
- 理解为什么要使用虚拟环境（venv）
- 掌握 `pip install / freeze / requirements.txt` 的基本流程
- 理解 Python 包结构与导入路径

注释：
- `venv` 的核心价值是“项目隔离”，避免全局包版本互相污染。
- 可以把它类比成 Node 项目里每个项目独立的 `node_modules` + `package-lock` 环境边界。
- 包结构不是语法题，而是“让导入可预测、让代码可维护”的工程题。

## 关键命令
- `python3 -m venv python-learning/.venv`
- `source python-learning/.venv/bin/activate`
- `python -m pip install -U pip`
- `python -m pip install -r requirements.txt`
- `python -m pip freeze > requirements.txt`

注释：
- `python3 -m venv ...`：创建虚拟环境目录（相当于生成该项目的隔离 Python 运行空间）。
- `source .../activate`：激活后，`python`/`pip` 会指向该 venv 里的解释器和工具。
- `python -m pip ...`：比直接 `pip ...` 更稳，确保“哪个 python 就用哪个 pip”。
- `pip install -r requirements.txt`：按依赖清单安装，适合团队协作和部署复现。
- `pip freeze > requirements.txt`：把当前环境已安装包导出成清单。
- 常见坑：`freeze` 往往会导出很多“间接依赖”，正式项目建议配合依赖管理策略精简。

## 代码产出
- `python-learning/day4/day4_packages.py`
- `python-learning/day4/day4_project/`（包结构演示）
- `python-learning/day4/day4_exercises.py`

注释：
- `day4_packages.py`：偏“概念与工具函数”，展示环境信息和 requirements 解析。
- `day4_project/`：偏“真实包结构”，练习 `__init__.py`、分层与导入。
- `day4_exercises.py`：偏“统一入口”，一次运行验证当天所有知识点。

## 我今天真正弄懂的点
- `sys.prefix != sys.base_prefix` 可以判断当前解释器是否运行在 venv
- `from package.module import x` 的前提是目录被识别为包（通常要有 `__init__.py`）
- `requirements.txt` 本质是依赖规格清单，不等于“当前机器所有包”

注释：
- `sys.prefix`：当前解释器环境路径；`sys.base_prefix`：基础解释器路径。
- 两者不同，通常意味着你在虚拟环境里运行。
- `__init__.py` 的作用是告诉 Python“这个目录可作为包处理”（现代 Python 有命名空间包，但学习阶段保留它最清晰）。
- `requirements.txt` 更像“安装输入”，不是“项目唯一真相”；生产里可能还会有 `constraints` 或锁定文件策略。

## 卡点与解决
- 卡点：相对导入和直接运行文件时的路径差异
- 解决：把执行入口放在包外层（`day4_exercises.py`），包内部用相对导入

注释：
- 直接运行包内模块时，`__name__` 和模块上下文不同，容易触发导入错误。
- 稳妥做法：在包外设置统一入口，包内坚持相对导入或一致的绝对导入策略。
- 心智对照：类似前端项目里“统一从入口文件启动”，避免脚本被单独跑时上下文不一致。

## 下一步
- Day 5: 文件 IO + JSON

注释：
- 建议 Day 5 延续今天结构：`models/helpers + exercises + notes + run.log`。
- 重点提前准备三个场景：读取配置、写入日志、JSON 序列化/反序列化边界处理。
