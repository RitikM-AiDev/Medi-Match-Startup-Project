from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import Annotated,TypedDict,add_messages
from langgraph.prebuilt import ToolNode
from langchain.messages import HumanMessage,SystemMessage
from llm_ import llm,memory

def forward_msg_generator(state : memory):
   messages = [
      SystemMessage(
        content=f"""
You are an assistant helping healthcare professionals.

Generate a brief clinical summary for a doctor based on the provided medical condition and keywords.

Requirements:
- 20-50 words.
- Focus on clinically relevant information.
- Mention critical symptoms, risks, and potential complications.
- Use professional medical language.
- Prioritize information useful in emergency or urgent care situations.
- Do not provide treatment recommendations.
- Do not add information that is not medically associated with the condition.
- Return only the summary.
"""
    ),
    HumanMessage(
       content=f"""Condition: {title},  Keywords: {keywords}"""
    )
    
]