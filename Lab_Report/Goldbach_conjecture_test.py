from graphviz import Digraph

# 创建流程图
dot = Digraph(comment='Goldbach Conjecture')

# 开始
dot.node('A', '开始', shape='ellipse')

# 输入 N
dot.node('B', '输入 N', shape='parallelogram')

# 检查 N 是否在范围内且为偶数
dot.node('C', '检查 N 是否在范围内\n且为偶数 (N % 2 == 0)', shape='diamond')

# 输出 "Invalid input" 并结束
dot.node('D', '输出 "Invalid input"\n并结束', shape='parallelogram')

# 初始化 p 从 2 开始
dot.node('E', '初始化 p 从 2 开始', shape='rectangle')

# 检查 p 是否 <= N // 2
dot.node('F', '检查 p 是否 <= N // 2', shape='diamond')

# 结束
dot.node('G', '结束', shape='ellipse')

# 计算 q = N - p
dot.node('H', '计算 q = N - p', shape='rectangle')

# 检查 p 和 q 是否均为素数
dot.node('I', '检查 p 和 q 是否均为素数', shape='diamond')

# 增加 p 并返回步骤 5
dot.node('J', '增加 p 并返回步骤 5', shape='rectangle')

# 输出 "N = p + q" 并结束
dot.node('K', '输出 "N = p + q"\n并结束', shape='parallelogram')

# 定义连接
dot.edges(['AB', 'BC'])
dot.edge('C', 'D', label='否')
dot.edge('C', 'E', label='是')
dot.edge('E', 'F')
dot.edge('F', 'G', label='否')
dot.edge('F', 'H', label='是')
dot.edge('H', 'I')
dot.edge('I', 'K', label='是')
dot.edge('I', 'J', label='否')
dot.edge('J', 'F')

# 显示流程图
dot.render('/mnt/data/goldbach_conjecture_flowchart', format='png', cleanup=False)
