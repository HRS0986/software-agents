from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class SoftwareCrew:
	"""SoftwareCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def business_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['business_analyst'],
			verbose=True
		)

	@agent
	def software_architect(self) -> Agent:
		return Agent(
			config=self.agents_config['software_architect'],
			verbose=True
		)

	@agent
	def ai_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_expert'],
			verbose=True
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			verbose=True
		)

	@agent
	def cost_estimator(self) -> Agent:
		return Agent(
			config=self.agents_config['cost_estimator'],
			verbose=True
		)

	@agent
	def markdown_formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['markdown_formatter'],
			verbose=True
		)

	@task
	def gather_requirements(self) -> Task:
		return Task(
			config=self.tasks_config['gather_requirements'],
		)

	@task
	def create_software_architecture(self) -> Task:
		return Task(
			config=self.tasks_config['create_software_architecture'],
		)

	@task
	def create_cost_estimation(self) -> Task:
		return Task(
			config=self.tasks_config['create_cost_estimation'],
		)

	@task
	def design_ai_solution(self) -> Task:
		return Task(
			config=self.tasks_config['design_ai_solution'],
		)

	@task
	def create_project_proposal(self) -> Task:
		return Task(
			config=self.tasks_config['create_project_proposal'],
		)

	@task
	def format_proposal(self) -> Task:
		return Task(
			config=self.tasks_config['format_proposal']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SoftwareCrew crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
