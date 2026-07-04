def build_event_prompt(destination: str):

    return f"""
List famous cultural events and festivals associated with {destination}.

If no live event information is available, mention recurring annual events.

Return ONLY JSON.

[
 {{
   "event":"",
   "description":""
 }}
]
"""