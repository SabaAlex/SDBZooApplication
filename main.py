from ui import AnimalUI
from service import AnimalService

service = AnimalService()
ui = AnimalUI(service)

ui.run()
