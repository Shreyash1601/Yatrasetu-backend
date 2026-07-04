def build_story_prompt(place: str, style: str):

    return f"""
Tell an immersive story about {place}.

Narration style:
{style}

Keep it engaging, factual and under 400 words.
"""