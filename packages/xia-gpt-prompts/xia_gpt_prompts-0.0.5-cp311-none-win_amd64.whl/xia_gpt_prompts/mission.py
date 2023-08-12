import logging
import os
import sys
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from jinja2.utils import concat
from xia_gpt_prompts.task import Task, Produce
from xia_gpt_prompts.goal import Goal, KnowledgeNode


class Mission:
    @classmethod
    def get_jinja_env(cls, resource_type: str):
        package_dir = os.path.dirname(os.path.abspath(sys.modules[cls.__module__].__file__))
        task_template_dir = os.path.join(package_dir, "templates", resource_type)
        return Environment(
            loader=FileSystemLoader(searchpath=task_template_dir),
            trim_blocks=True,
            keep_trailing_newline=True
        )

    def __init__(self, goal, mission_type: str, contexts: list = None):
        """Mission is consisted of several tasks

        Args:
            goal: The virtual holder of what we are working for
            mission_type: Mission type
            contexts: All necessary information for the mission
        """
        self.goal = goal
        self.env = self.get_jinja_env("missions")
        self.mission_type = mission_type
        self.contexts = contexts if contexts else []
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_context(self):
        context_list = []
        for context_key in self.contexts:
            context_content = KnowledgeNode.load(key=context_key)
            context_item = {
                "title": ' '.join([word.capitalize() for word in context_key.split("_")]),
                "content": context_content.value
            }
            context_list.append(context_item)
        return context_list

    def get_formats(self):
        formats = [{"title": task.title, "content": task.format} for task in self.tasks if task.format]
        return formats

    def get_guides(self):
        guides = [{"title": task.title, "content": task.guide} for task in self.tasks if task.guide]
        return guides

    def get_prompt(self, actor_role: str):
        """Get prompt for GPT call

        Args:
            actor_role: Description of action's profile

        Returns:
            prompts as string
        """
        try:
            template = self.env.get_template(self.mission_type + ".prompt")
        except TemplateNotFound:
            return None
        prompt = template.render(
            contexts=self.get_context(),
            formats=self.get_formats(),
            guides=self.get_guides(),
            actor_role=actor_role
        )
        return prompt

    async def run(self, gpt_agent, actor_role: str):
        prompt = self.get_prompt(actor_role)
        result, job_status = await gpt_agent.chat_complete_stream("", prompt)
        for task in self.tasks:
            if isinstance(task, Produce):
                node = KnowledgeNode(key=task.name,
                                     value_type=task.output_type,
                                     value_format=str(task.output_format),
                                     value=task.parse_output(result)).save()
                self.goal.knowledge_map.add_node(node)
