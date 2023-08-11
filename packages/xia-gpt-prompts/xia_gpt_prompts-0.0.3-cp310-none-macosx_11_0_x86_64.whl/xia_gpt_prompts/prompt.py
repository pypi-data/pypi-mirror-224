from xia_gpt_prompts.task import Task


class Prompt:
    prompt_context = "# Context\n{}\n"
    prompt_format = "# Format example\n\n---\n{}---\n\n"
    prompt_instruction = "#----\n{}\n"

    def __init__(self,
                 instruction: str,
                 context: str):
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

