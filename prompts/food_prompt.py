def build_food_prompt(destination: str):

    return f"""
Recommend authentic local food in {destination}.

Return ONLY JSON.

[
 {{
   "dish":"",
   "description":""
 }}
]
"""