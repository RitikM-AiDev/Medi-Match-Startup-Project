from langchain_core.messages import SystemMessage, HumanMessage
from llm_ import llm


def hospital_analysis(patient_condition: str, hospitals: list):
    messages = [
        SystemMessage(
            content="""
You are an AI Healthcare Decision Support Assistant.

Your task is to analyze multiple hospitals and recommend the most suitable hospital.

Consider:
- Medical specialty relevance
- Hospital rating
- Emergency services
- ICU availability
- Doctor expertise
- Distance from patient
- Patient reviews
- Bed availability
- Diagnostic facilities
- Cost effectiveness

Output Format:

1. Hospital Ranking (Best to Worst)

2. Detailed Analysis for Each Hospital
   - Strengths
   - Weaknesses
   - Suitability Score (0-100)

3. Final Recommendation
   - Recommended Hospital
   - Reasoning

4. Risk Factors
   - Missing facilities
   - Long distance
   - Poor reviews
   - Specialty mismatch

Be objective and explain the decision.
"""
        ),
        HumanMessage(
            content=f"""
Patient Condition:
{patient_condition}

Hospital Data:
{hospitals}
"""
        )
    ]

    response = llm.invoke(messages)
    return response.content