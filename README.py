import os

def generate_markdown(path, level=0, exclude_list=None):
    """
    递归遍历文件夹并生成Markdown内容：
    - 文件夹使用 <details> 和 <summary> 实现折叠。
    - 每深入一层，增加空格数量来缩进，而不是增加 '-' 的数量。
    - 文件夹和文件的层级通过空格缩进对齐。
    - 排除功能：如果路径包含排除词，则跳过该路径。
    """
    if exclude_list is None:
        exclude_list = []

    markdown = ""
    indent = "  " * level  # 每深入一层，增加两个空格的缩进
    bullet = "- "  # 文件和文件夹的前缀始终为 "- "，层级通过空格缩进体现

    try:
        items = sorted(os.listdir(path))  # 获取当前文件夹中的所有内容
    except PermissionError:
        print(f"无法访问文件夹：{path}")
        return ""

    for item in items:
        item_path = os.path.join(path, item)

        # 检查路径是否包含排除词
        if any(exclude in item_path for exclude in exclude_list):
            continue  # 如果包含排除词，则跳过

        if os.path.isdir(item_path):  # 如果是文件夹
            markdown += f"{indent}{bullet}<details>\n"
            markdown += f"{indent}  <summary>{item}/</summary>\n\n"
            markdown += generate_markdown(item_path, level + 1, exclude_list)  # 递归处理子文件夹
            markdown += f"{indent}</details>\n\n"
        else:  # 如果是文件
            markdown += f"{indent}{bullet}{item}\n"

    return markdown


if __name__ == "__main__":
    # 获取脚本所在路径
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("正在生成Markdown内容...")

    # 定义排除词列表
    exclude_list = [".git", "exclude_word2", "exclude_folder"]

    # 生成Markdown内容
    markdown_content = generate_markdown(script_path, exclude_list=exclude_list)

    # 输出到文件
    output_file = os.path.join(script_path, "file_structure.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown内容已生成并保存到：{output_file}")
