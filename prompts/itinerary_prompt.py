def build_itinerary_prompt(destination, days, budget, interests):

    return f"""
Generate a {days}-day itinerary for {destination}, India.

Budget: {budget if budget else "Flexible"}

Interests:
{", ".join(interests) if interests else "General Tourism"}

Return ONLY valid JSON.

Format:

{{
"title":"",
"days":[
{{
"day":1,
"activities":[
{{
"time":"",
"title":"",
"description":""
}}
]
}}
]
}}
"""