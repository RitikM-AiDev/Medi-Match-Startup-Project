from pydantic import BaseModel
from fastapi import FastAPI
from langchain_core.messages import SystemMessage, HumanMessage
from llm_ import llm

app = FastAPI()



def forward_msg_generator(title: str, description: str):
    messages = [
        SystemMessage(
            content="""
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
            content=f"""
Condition: {title}
Keywords: {description}
"""
        )
    ]

    response = llm.invoke(messages) 
    return response.content


