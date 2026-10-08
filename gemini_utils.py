import os
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    USE_AI = True
except:
    USE_AI = False

def get_home_recommendations(budget, room_type):
    if USE_AI:
        try:
            prompt = f"For {room_type} with budget {budget} rupees, give 3 home decor products from Amazon/IKEA with price"
            res = model.generate_content(prompt)
            return res.text
        except: pass
    return f"""
    **Home Planner for {room_type} - Budget Rs.{budget}:**
    1. IKEA LACK Table - Rs.{int(budget)*0.3} (Amazon)
    2. Philips Ceiling Light - Rs.{int(budget)*0.2} (Flipkart)
    3. Wall Decor Set - Rs.{int(budget)*0.15} (IKEA)
    """

def get_party_recommendations(budget, guests, event_type):
    if USE_AI:
        try:
            prompt = f"Party plan for {event_type}, {guests} guests, budget {budget}, give catering, decor, venue from Swiggy/Zomato/OYO"
            res = model.generate_content(prompt)
            return res.text
        except: pass
    per_head = int(budget)//int(guests) if int(guests)>0 else int(budget)
    return f"""
    **{event_type} Party - {guests} Guests - Rs.{budget}:**
    Catering (Swiggy): Rs.{int(budget)*0.5} (Rs.{per_head} per head)
    Decoration: Rs.{int(budget)*0.3}
    Venue (OYO): Rs.{int(budget)*0.2}
    """

def get_jewelry_recommendations(budget, occasion, style):
    if USE_AI:
        try:
            prompt = f"Jewelry for {occasion}, style {style}, budget {budget}, from Amazon/Flipkart"
            res = model.generate_content(prompt)
            return res.text
        except: pass
    return f"""
    **Jewelry for {occasion} - Rs.{budget}:**
    1. {style} Necklace - Rs.{int(budget)*0.5} (Amazon)
    2. Matching Earrings - Rs.{int(budget)*0.3} (Flipkart)
    3. Bangle Set - Rs.{int(budget)*0.2}
    """