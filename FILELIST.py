import os

def generate_file_paths(path, whitelist=None, relative_to=None):
    """
    递归遍历文件夹并生成文件的纯路径列表。
    只有路径中包含白名单中的任意字符串时，才会被包含。
    参数：
    - path: 起始路径
    - whitelist: 白名单列表，路径中必须包含这些字符串之一
    - relative_to: 生成相对路径的基准路径
    """
    if whitelist is None:
        whitelist = []  # 默认为空列表

    if relative_to is None:
        relative_to = path  # 默认基准路径为起始路径

    file_paths = []  # 用于存储文件的纯路径

    try:
        items = sorted(os.listdir(path))  # 获取当前文件夹中的所有内容
    except PermissionError:
        print(f"无法访问文件夹：{path}")
        return []

    for item in items:
        item_path = os.path.join(path, item)

        # 获取相对于基准路径的纯路径，并使用正斜杠
        relative_path = os.path.relpath(item_path, start=relative_to).replace("\\", "/")

        if os.path.isdir(item_path):  # 如果是文件夹
            # 递归处理子文件夹
            file_paths.extend(generate_file_paths(item_path, whitelist, relative_to))
        elif os.path.isfile(item_path):  # 如果是文件
            # 检查路径是否包含白名单中的任意字符串
            if any(whitelist_item in relative_path for whitelist_item in whitelist):
                file_paths.append(relative_path)  # 添加文件路径

    return file_paths


if __name__ == "__main__":
    # 获取脚本所在路径
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("正在生成文件路径列表...")

    # 定义白名单列表
    whitelist = ["m4a"]  # 路径中必须包含这些字符串之一

    # 生成文件路径列表
    file_paths = generate_file_paths(script_path, whitelist=whitelist)

    # 输出到文件
    output_file = os.path.join(script_path, "FILELIST.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for path in file_paths:
            f.write(path + "\n")

    print(f"文件路径列表已生成并保存到：{output_file}")
