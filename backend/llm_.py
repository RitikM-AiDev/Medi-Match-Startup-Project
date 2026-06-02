from langchain_openai import ChatOpenAI
import os
from langgraph.graph.message import Annotated,TypedDict,add_messages
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("BASE")
    
)

class memory(TypedDict):
    history : list
    file_path : str
    hospitals : list
    best_hospital : str
    gmap_link : str
    forward_msg : str

