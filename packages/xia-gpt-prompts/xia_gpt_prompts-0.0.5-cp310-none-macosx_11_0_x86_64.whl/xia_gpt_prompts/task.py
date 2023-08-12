import json
import os
import sys
import re
import ast
import logging
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
        self.required_context = {} if not required_context else required_context
        self.output_type = "text"  # could be 'python', 'code', etc..
        self.output_format = str  # could be str or List

    def get_block_content(self, item_type: str, params: dict = None):
        params = {} if not params else params
        try:
            template = self.env.get_template(self.name + ".prompt")
        except TemplateNotFound:
            return ""
        context = template.new_context(params)
        if item_type not in template.blocks:
            return ""
        content = concat(template.blocks[item_type](context))
        return content

    def parse_output(self, output: str):
        pass


class Produce(Task):
    @classmethod
    def parse_format(cls, value: str, default_type, default_format):
        if not value:
            return default_type, default_format
        lines = [ln.strip() for ln in value.split("\n")]
        if lines[0].startswith("```"):
            if not lines[0][3:]:  # Case 1: Pure code with unknown code type
                return "code", str
            elif lines[0][3:] != "python":  # Case 2: Code with predefined code type
                return lines[0][3:], str
            if lines[1].startswith("["):  # Case 3: List in python code type
                return "text", list
            return "python", str
        return default_type, default_format

    @classmethod
    def extract_code(cls, code_type: str, output_text: str):
        pattern = rf'```{code_type}.*?\s+(.*?)```'
        match = re.search(pattern, output_text, re.DOTALL)
        return match.group(1) if match else None

    @classmethod
    def extract_list(cls, output_text: str):
        pattern = r'\s*(.*=.*)?(\[.*\])'
        match = re.search(pattern, output_text, re.DOTALL)
        if match:
            tasks_list_str = match.group(2)
            list_value = ast.literal_eval(tasks_list_str)
        else:
            list_value = output_text.split("\n")
        return json.dumps(list_value, ensure_ascii=False)

    def parse_output(self, output_text: str):
        """Extract the related data from output text

        Args:
            output_text: Output of GPT Engine

        Returns:
            Result if format is correct. None if format is not good
        """
        # Step 1: Get the content for the given produce task
        blocks = output_text.split("##")
        for block in blocks:
            lines = block.split("\n")
            if lines and self.title.lower() in lines[0].strip().lower():
                texts, codes = "", ""
                # Step 2: Get the correct output
                if self.output_type != "text" or self.output_format != str:
                    code_type = "" if self.output_type == "code" else self.output_type
                    code_type = "python" if self.output_format != str else code_type
                    codes = self.extract_code(code_type, "\n".join(lines[1:]))
                # Step 3: Generating output
                if self.output_type == "text" and self.output_format == str:  # Simple text output
                    return "\n".join(lines[1:])
                if codes and self.output_type != "text":  # Program code output
                    return codes
                if codes and self.output_format == list:  # List output
                    return self.extract_list(codes)

    """Points to be generated"""
    def __init__(self, name: str, required_context: dict = None, **kwargs):
        super().__init__(name=name, required_context=required_context, **kwargs)
        self.format = kwargs.get("format", self.get_block_content("format")).strip()
        self.guide = kwargs.get("format", self.get_block_content("guide")).strip()
        self.output_type, self.output_format = self.parse_format(self.format, self.output_type, self.output_format)
