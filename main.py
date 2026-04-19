from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MeetingPrepAgents

def main():
    load_dotenv()  # Load environment variables from .env file

    print("Welcome to the Meeting Preparation Crew")
    print("---------------------------------")
    meeting_participants = input("What are the emails of the participants (other than you) in the meeting? (separate with commas): ")
    meeting_context = input("What is the context of the meeting?")
    meeting_objectives = input("What are the objectives of this meeting?") 

    tasks = MeetingPrepTasks()
    agents = MeetingPrepAgents()    

    # Create agents
    research_agent = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    meeting_strategy_agent = agents.meeting_strategy_agent()

    # Create tasks
    research_task = tasks.research_task(research_agent, meeting_participants, meeting_context)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent, meeting_participants, meeting_context)
    meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent, meeting_context, meeting_objectives)
    summrize_and_briefing_task = tasks.summrize_and_briefing_task(meeting_strategy_agent, meeting_context, meeting_objectives)  

    meeting_strategy_task.context = [research_task, industry_analysis_task]
    summrize_and_briefing_task.context = [research_task, industry_analysis_task, meeting_strategy_task]

    crew = Crew(
        agents=
        [
            research_agent,
            industry_analysis_agent,
            meeting_strategy_agent
        ],
        tasks=[
            research_task,
            industry_analysis_task,
            meeting_strategy_task,
            summrize_and_briefing_task
        ],
        processes="sequential" # default is sequential, you can also set it to "parallel" if you want the agents to work on their tasks at the same time
         
    )

    results = crew.kickoff()


if __name__ == "__main__":
    main()