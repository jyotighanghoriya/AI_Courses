import yaml
import os
from smolagents import GradioUI, CodeAgent, OpenAIModel

# Get current directory path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from AI_Courses.AlfredAgentCodingAgent.tools.suggest_menu import SimpleTool as SuggestMenu
from AI_Courses.AlfredAgentCodingAgent.tools.final_answer import FinalAnswerTool as FinalAnswer



model = OpenAIModel(
model_id='qwen2:7b',
)

suggest_menu = SuggestMenu()
final_answer = FinalAnswer()


with open(os.path.join(CURRENT_DIR, "prompts.yaml"), 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[suggest_menu],
    managed_agents=[],
    max_steps=5,
    verbosity_level=1,
    planning_interval=None,
    name=None,
    description=None,
    executor_type='local',
    executor_kwargs={},
    max_print_outputs_length=None,
    prompt_templates=prompt_templates
)
if __name__ == "__main__":
    GradioUI(agent).launch()
