from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre:List[str]#one movie can belong to multiple genres
    director: Optional[str]
    cast: List[str]#list of main characters
    rating: Optional[float]
    awards: Optional[List[str]]#list of awards or nominations
    plot_summary: str
parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system',"""
    Extract movie information from the given movie description and provide the output in a structured format.
     {format_instructions}
     """),
    ('human',"{movie_description}")
])


def extract_movie_information(movie_description):
    model = ChatMistralAI(
        model="mistral-small-2603",
        temperature=0.3
    )

    chain = prompt | model | parser

    response = chain.invoke({
        "movie_description": movie_description,
        "format_instructions": parser.get_format_instructions()
    })

    return response