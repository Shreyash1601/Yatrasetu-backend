def build_hidden_prompt(destination: str):

    return f"""
Suggest five hidden gems in {destination}, India.

Return ONLY JSON.

Format:

[
    {{
        "name":"",
        "why_visit":""
    }}
]
"""