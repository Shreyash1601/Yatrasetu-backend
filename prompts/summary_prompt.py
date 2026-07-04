def build_summary_prompt(destination, days, budget, interests):

    return f"""
You are an expert cultural travel planner.

Generate an engaging travel summary for the following trip.

Destination: {destination}

Duration: {days} days

Budget: ₹{budget}

Interests:
{", ".join(interests)}

Requirements:

- Maximum 120 words
- Explain why this itinerary suits the traveller
- Mention cultural experiences
- Mention hidden gems
- Mention authentic local experiences
- Mention heritage
- Make it sound exciting

Return plain text only.
"""