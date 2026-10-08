from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<html><body style="font-family:Arial;padding:20px">
<h1>PocketSmart AI Working da! 🎉</h1>
<h3>🏠 Home Planner</h3>
Budget: <input id="b1" value="20000"> 
Room: <select id="r1"><option>Living Room</option><option>Bedroom</option></select>
<button onclick="alert('Home Plan for '+document.getElementById('r1').value+' Rs.'+document.getElementById('b1').value+' - IKEA Table, Philips Light from Amazon')">Generate</button>

<h3>🎉 Party Planner</h3>
Budget: <input id="b2" value="50000"> Guests: <input id="g" value="20">
<button onclick="alert('Party Plan Rs.'+document.getElementById('b2').value+' for '+document.getElementById('g').value+' guests - Swiggy catering, OYO venue')">Generate</button>

<h3>💍 Jewelry Planner</h3>
Budget: <input id="b3" value="30000">
<button onclick="alert('Jewelry Rs.'+document.getElementById('b3').value+' - Amazon/Flipkart Necklace set')">Generate</button>

<p style="color:green;margin-top:30px"><b>✅ Project Running Successfully da!</b></p>
</body></html>
    """