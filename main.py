import uvicorn
import os

if __name__ == '__main__':
  if not os.path.exists("images"):
    os.makedirs("images")
  uvicorn.run("app.app:app", host="0.0.0.0", port=4000, reload=True)
