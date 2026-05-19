import subprocess
import time
import uvicorn
import os
from threading import Thread


def iniciar_servidor():

    uvicorn.run("server.app.main:app",host="localhost",port=8000,reload=False)


if __name__ == "__main__":

    servidor = Thread(target=iniciar_servidor,daemon=True)
    servidor.start()

    time.sleep(2)
    subprocess.run(["python", "client/main.py"])

    print("Fechando aplicação.") #caso seja selecionado o sair ("0")do menu do client/main.py
    os._exit(0)