from llm_invoker import DummyLLMClient
from decomposer_system import InstructionDecomposerSystem


def main():
    llm_client = DummyLLMClient()
    system = InstructionDecomposerSystem(llm_client)

    instruction = "Replace the top book with a notebook and turn the bottom book red"
    result = system.decompose(instruction)

    for idx, item in enumerate(result.to_list(), 1):
        print(f"{idx}. {item['object']} -> {item['edit']}")


if __name__ == "__main__":
    main()
