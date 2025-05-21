from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.exa import ExaTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_agent=Agent(
    name="web agent",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[
        DuckDuckGo(),
    ],
    instructions=[
        "Provide youtube links for the search movies"
    ],
    markdown=True,
)

movies_pal_agent=Agent(
    name="movies pal",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[
        ExaTools(),
    ],
    instructions=[
        "Use Exa to search for the movies.",
        "Provide results with the following details: movie title, genre, movies with good ratings, description, recommended viewing age, primary language,runtime, imdb rating and release date.",
        "Include trailers for movies similar to the recommendations and upcoming movies of the same genre or from related directors/actors.",
        "Give atleast 5 movie recommendations for each query",
        "Present the output in a well-structured markdown table for readability.",
        "Ensure all movie data is correct, especially for recent or upcoming releases.",
    ],
    markdown=True,
)

movies_team=Agent(
    team=[web_agent,movies_pal_agent],
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
        description=(
        "You are movie Pal, a movie recommendation agent that searches and scrapes movie websites to provide detailed recommendations, "
        "including ratings, genres, descriptions, trailers, and upcoming releases."
        "You only tell about movies and pop culture, do not tell anything except these"
    ),
    instructions=[
        "Present the output in a well-structured formate for readability.",
        
    ],
    markdown=True,

)

# movies_team.print_response(
#     "Suggest some movies to watch with a rating of 8 or above on rotten Tomatoes.For movie La La Land.",
#     stream=True,
# )