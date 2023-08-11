class Instruction:
    """Instruction part of a prompt"""


class Context:
    """Context part of a prompt"""


class InputData:
    """Input data"""


class OutputIndicator:
    """"""


class Task:
    def get_format_text(self):
        pass

    def get_guide_text(self):
        pass

    def parse_output(self, output: str):
        pass


class Generator(Task):
    """Points to be generated"""
    task_format = "## {}\n{}\n"
    guide_format = "## {}: {}\n"

    def __init__(self, name: str, output_format: str, output_guide: str, required_context: dict = None):
        self.name = name
        self.required_context = {} if not required_context else required_context
        self.output_format = output_format
        self.output_guide = output_guide

    def get_format_text(self):
        return self.task_format.format(self.name, self.output_format)

    def get_guide_text(self):
        return self.guide_format.format(self.name, self.output_guide)

    def parse_output(self, output: str):
        pass


class Prompt:
    prompt_context = "# Context\n{}\n"
    prompt_format = "# Format example\n\n---\n{}---\n\n"
    prompt_instruction = "#----\n{}\n"

    def __init__(self,
                 instruction: str,
                 context: str,
                 input_data: InputData = None,
                 indicator: OutputIndicator = None):
        self.instruction = instruction
        self.context = context
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_formats(self):
        formats = [task.get_format_text() for task in self.tasks]
        formats = "\n".join([part for part in formats if part])
        return formats

    def get_guides(self):
        guides = [task.get_guide_text() for task in self.tasks]
        guides = "\n".join([part for part in guides if part])
        return guides

    def get_prompt(self):
        prompt = self.prompt_context.format(self.context)
        prompt += self.prompt_format.format(self.get_formats())
        prompt += self.prompt_instruction.format(self.instruction)
        prompt += self.get_guides()

        return prompt

