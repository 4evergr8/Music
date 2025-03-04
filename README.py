import os

def generate_markdown(path, level=0):
    """
    递归遍历文件夹并生成Markdown列表，文件夹用折叠表示，层级用'>'符号表示缩进。
    每个文件和文件夹独立一行，子文件夹也用'>'符号表示层级。
    :param path: 当前遍历的文件夹路径
    :param level: 当前层级（用于缩进）
    :return: Markdown格式的字符串
    """
    markdown = ""
    indent = ">" * level  # 使用'>'表示层级缩进

    try:
        items = sorted(os.listdir(path))  # 获取当前文件夹中的所有内容
    except PermissionError:
        print(f"无法访问文件夹：{path}")
        return ""

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):  # 如果是文件夹
            markdown += f"{indent} <details>\n"
            markdown += f"{indent} <summary>{item}</summary>\n\n"
            markdown += generate_markdown(item_path, level + 1)  # 递归处理子文件夹
            markdown += f"{indent} </details>\n\n"
        else:  # 如果是文件
            markdown += f"{indent} {item}  \n\n"

    return markdown


if __name__ == "__main__":
    # 获取脚本所在路径
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("正在生成Markdown内容...")

    # 生成Markdown内容
    markdown_content = generate_markdown(script_path)

    # 输出到文件
    output_file = os.path.join(script_path, "README.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown内容已生成并保存到：{output_file}")
