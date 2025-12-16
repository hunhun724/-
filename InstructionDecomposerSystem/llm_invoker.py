class DummyLLMClient:
    """
    模拟大语言模型客户端
    用于替代真实 API，保证系统独立性
    """
    def generate(self, prompt: str) -> str:
        return """1. top book → notebook
2. bottom book → red"""


class LLMInvoker:
    """
    大模型调用模块
    """
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def invoke(self, prompt: str) -> str:
        return self.llm_client.generate(prompt)
