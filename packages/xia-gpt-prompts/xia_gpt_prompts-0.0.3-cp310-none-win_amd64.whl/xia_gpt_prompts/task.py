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
