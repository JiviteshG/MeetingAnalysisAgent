from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
                Conduct comprehensive research on each of the individuals and companies
                involved in the upcoming meeting. Gather information on recent
                news, achievements, professional background, and any relevant business activities.
                
                Participants: {meeting_participants}
                Meeting Context: {meeting_context}"""  ),
            expected_output=dedent("""\
                A detailed report summarizing the key information about each participant and their respective companies, including:
                - Recent news and developments
                - Notable achievements
                - Professional background and expertise
                - Any relevant business activities or partnerships"""),
            agent=agent,
            async_execution=True
        )
    def industry_analysis_task(self, agent, meeting_participants,  meeting_context ):
        return Task(
            description=dedent(f"""\
                Analyse the current industry trends, challenges, and opportunities
                relevant to the meeting's context. Consider market reports, recent
                developments, and expert opinions to provide a comprehensive overview
                of the industry landscape.   
                               
                Participants: {meeting_participants}
                Meeting Context: {meeting_context}"""),
            expected_output=dedent("""\
                An insightful analysis report that identifies:"
                - Current major trends in the industry
                - Key challenges faced by the industry
                - Emerging opportunities"""),
            agent=agent,
            async_execution=True
        )
    def meeting_strategy_task(self, agent, meeting_context, meeting_objectives):
        return Task(
            description=dedent(f"""\
                Develop a talking, questions, and discussion angles 
                for the upcoming meeting based on the research and analysis conducted.
                
                Meeting Objectives: {meeting_objectives}
                Meeting Context: {meeting_context}"""),
            expected_output=dedent("""\
                Complete a report with a list of key talking points, strategic questions to 
                ask to help achieve the meeting objectives during the meeting."""),
            agent=agent,

        ) 
    def summrize_and_briefing_task(self, agent, meeting_context, meeting_objectives):
        return Task(
            description=dedent(f"""\
                Complete all the research findings, industry analysis, and strategic talking
                points into a concise, comprehensive briefing document for the meeting.
                Ensure the briefing is easy to digest and equips the meeting participants with all necsessary
                information and strategies.
                
                Meeting Context: {meeting_context}
                Meeting Objectives: {meeting_objectives}"""),
            expected_output=dedent("""\
                A well-structured briefing document that includes:
                - A section for participant bias
                - industry overview
                - talking points 
                - strategic recommendations"""),
            agent=agent
            )
    