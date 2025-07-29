from pyngrok import ngrok
import nest_asyncio
import uvicorn
import threading

nest_asyncio.apply()
public_url = ngrok.connect(8000)
print("Public URL:", public_url.public_url + "/docs")

def run():
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

threading.Thread(target=run).start()
