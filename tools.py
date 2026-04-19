import os
import sys
from exa_py import Exa  
from langchain.agents import Tool ## unsed to import @tool decorator as CrewAI is built upon Langchain

class ExaSearchToolset:
    @tool
    def search(query: str):
        """
        Search for  a webpage based on the query."""
        return ExaSearchToolset._exa().search(f"{query}", use_autoprompt=True, num_results=3)   

    @tool
    def find_similar(url: str):
        """
        Search for websites similar to the URL.
        The url passed should be a URL returned by the search tool."""
        return ExaSearchToolset._exa().find_similar(f"{url}", num_results=3)

    @tool
    def get_contents(ids: str):
        """
        Get the contents of a webpage.
        The ids passed in as a list, a list of ids returned by the search"""

        # print(f"Ids  from  param:", ids)

        ids = eval(ids) 
        # print(f"Eval Ids:", ids)
        contents = str(ExaSearchToolset._exa().get_contents(ids))
        # print(f"Contents:", contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [
            ExaSearchToolset.search, 
            ExaSearchToolset.find_similar, 
            ExaSearchToolset.get_contents
        ]
    def _exa():
        return Exa(api_key=os.environ.get("EXA_API_KEY"))