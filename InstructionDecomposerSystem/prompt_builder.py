class PromptBuilder:
    """
    提示构建模块
    用于生成结构化 Prompt，引导大语言模型进行指令拆分
    """

    def build_prompt(self, instruction: str) -> str:
        prompt = f"""
You are an expert in decomposing composite image editing instructions.

Task:
Decompose a single composite editing instruction into a sequence of
logically coherent atomic instructions.

Rules:
- Do NOT add any new edits.
- Do NOT remove any edits.
- Do NOT merge multiple edits into one.
- Preserve the original transformation intent exactly.

Input format:
A single sentence describing multiple edits.

Output format:
A numbered list where each item represents one atomic object-attribute edit:
<object> → <new attribute or object>

Examples:
Input: Change the red ball to blue and the yellow cube to green.
Output:
1. red ball → blue
2. yellow cube → green

Now decompose the following instruction:
{instruction}
"""
        return prompt.strip()
