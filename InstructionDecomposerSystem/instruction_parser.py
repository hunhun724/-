import re

class InstructionParser:
    """
    指令解析模块
    将模型输出解析为结构化原子指令
    """

    def parse(self, llm_output: str):
        instructions = []
        pattern = r"\d+\.\s*(.+?)\s*→\s*(.+)"
        for line in llm_output.splitlines():
            match = re.match(pattern, line.strip())
            if match:
                obj, edit = match.groups()
                instructions.append({
                    "object": obj.strip(),
                    "edit": edit.strip()
                })
        return instructions
