class AtomicInstructionSet:
    """
    原子指令管理模块
    """

    def __init__(self, instructions):
        self.instructions = instructions

    def __len__(self):
        return len(self.instructions)

    def get(self, index):
        return self.instructions[index]

    def to_list(self):
        return self.instructions
