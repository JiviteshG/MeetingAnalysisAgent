from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset

class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            name="Research Specialist",
            goal="Conduct through research on people and companies involved in the meeting",
            tools=[ExaSearchToolset.tools()],
            backstory=dedent("""\
                As a Research Specialist, your mission is to  uncover detailed information
                about the individuals and entities participating in the meeting. Your insights
                will lay the groundwork for a strategic meeting preparation."""),
                verbose=True
        )
    def industry_analysis_agent(self):
        return Agent(
            name="Industry Analyst",
            goal="Analyse the current industry trends, challenges, and opportunities relevant to the meeting's context",
            tools=[ExaSearchToolset.tools()],
            backstory=dedent("""\
                As an Industry Analyst, your mission is to identify key trends, challenges, and opportunities that 
                could be leveraged during the meeting for strategic advantage."""),
                verbose=True
        )
    def meeting_strategy_agent(self):
        return Agent(
            role="Meeting Strategy Advisor",
            goal="Develop talking points, questions, and strategic angles for the meeting"
            tools=[],
            backstory=dedent("""\
                As a Meeting Strategy Advisor, your mission wii guide the development of
                talking points, insightful questions, and strategic angles
                to ensure the meeting objectives are achieved."""),
            verbose=True
            )
    def summary_and_briefing_agent(self):
        return Agent(
            role="Briefing Coordinator",
            goal="Compile all gathered information into a concise, informative briefing document",
            tools=[],
            backstory=dedent("""\
                As a Briefing Coordinator, your role is to consolidate the research,
                analysis, and strategic insights."""),
            verbose=True
        )