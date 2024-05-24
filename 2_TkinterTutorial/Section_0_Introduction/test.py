import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_path = filedialog.askopenfilename()
    # 在这里可以添加你处理文件的代码，比如打印文件路径
    print("文件路径:", file_path)

# 创建主窗口
root = tk.Tk()
root.title("文件上传")

# 创建一个标签用于显示文件路径（可选）
file_label = tk.Label(root, text="文件路径:")
file_label.pack()

# 创建一个上传文件按钮
upload_button = tk.Button(root, text="上传文件", command=upload_file)
upload_button.pack()

# 运行主循环
root.mainloop()
