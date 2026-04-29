import os
from pathlib import Path
from datetime import datetime
from openpyxl import Workbook
from CriaObjetos import CriaObjetos, extrair_texto
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from threading import Timer

class MonitorDePasta(FileSystemEventHandler):

    def __init__(self, wait_time=2.0):
        super().__init__()
        self.wait_time = wait_time  
        self.timer = None
        self.last_event_time = []

    def _handle_event(self):

            time.sleep(0.75)
            
            os.chdir(os.path.dirname(os.path.realpath(__file__)))
            directory = 'Pdfs'
            files = os.listdir(directory)

            wb = Workbook()

            for file in files:
                
                if file.lower().endswith('.pdf'): 
                    pdf_texto = extrair_texto(directory + '/' + file)
                    nota = CriaObjetos(pdf_texto)
                    nota.adicionarExcel(wb)
                    del nota

            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            filesProject = os.listdir()

            if filesProject.__contains__('Planilhas Preechidas'):
                print('Essa pasta já existe')
            else:
                os.mkdir('Planilhas Preechidas')

            os.chdir('Planilhas Preechidas')
            wb.save('Planilha preenchida '+ now +'.xlsx')

            self.last_event_time = []

    def on_created(self, event):
        
        if event.is_directory:
            return

        caminho_do_arquivo = event.src_path
        print(f"Opa, arquivo novo detectado: {caminho_do_arquivo}") 

        self.last_event_time.append(caminho_do_arquivo)

        if  self.timer is not None:
            self.timer.cancel()

        self.timer = Timer(self.wait_time, self._handle_event)
        self.timer.start()


local = (os.path.dirname(os.path.realpath(__file__)) + "/" + "Pdfs")
pasta_alvo = local


event_handler = MonitorDePasta(wait_time=2.0)
observer = Observer()
observer.schedule(event_handler, pasta_alvo, recursive=False)
observer.start()

print(f"Monitorando a pasta: {pasta_alvo}")

try:

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
