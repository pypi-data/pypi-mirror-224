import logging
import os
import sys
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from jinja2.utils import concat


class Task:
    @classmethod
    def get_jinja_env(cls, resource_type: str):
        package_dir = os.path.dirname(os.path.abspath(sys.modules[cls.__module__].__file__))
        task_template_dir = os.path.join(package_dir, "templates", resource_type)
        return Environment(
            loader=FileSystemLoader(searchpath=task_template_dir),
            trim_blocks=True,
            keep_trailing_newline=True
        )

    def __init__(self, name: str, required_context: dict = None, **kwargs):
        self.env = self.get_jinja_env("tasks")
        self.name = name
        self.title = ' '.join([word.capitalize() for word in name.split("_")])
        # self.output_format = kwargs.get("output_format")

    def get_block(self, item_type: str, params: dict = None):
        params = {} if not params else params
        try:
            template = self.env.get_template(self.name + ".prompt")
        except TemplateNotFound:
            return None
        context = template.new_context(params)
        if item_type not in template.blocks:
            return None
        content = concat(template.blocks[item_type](context))
        return content

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

    def __init__(self, name: str, required_context: dict = None, **kwargs):
        super().__init__(name=name)
        self.name = name
        self.required_context = {} if not required_context else required_context
        self.format = kwargs.get("format", self.get_block("format"))
        self.guide = kwargs.get("format", self.get_block("guide"))

    def get_format_text(self):
        return self.task_format.format(self.title, self.format)

    def get_guide_text(self):
        return self.guide_format.format(self.title, self.guide)

    def parse_output(self, output: str):
        pass
