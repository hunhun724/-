from prompt_builder import PromptBuilder
from llm_invoker import LLMInvoker
from instruction_parser import InstructionParser
from atomic_instruction_set import AtomicInstructionSet


class InstructionDecomposerSystem:
    """
    系统调度模块
    """

    def __init__(self, llm_client):
        self.prompt_builder = PromptBuilder()
        self.llm_invoker = LLMInvoker(llm_client)
        self.parser = InstructionParser()

    def decompose(self, instruction: str) -> AtomicInstructionSet:
        prompt = self.prompt_builder.build_prompt(instruction)
        llm_output = self.llm_invoker.invoke(prompt)
        parsed = self.parser.parse(llm_output)
        return AtomicInstructionSet(parsed)
