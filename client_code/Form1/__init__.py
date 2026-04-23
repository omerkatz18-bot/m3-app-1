from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  @handle("file_loader_1", "change")
  def file_loader_1_change(self, file, **event_args):
    if file:
      self.image_loaded.source = file
      self.prediction_text_box.text = "מזהה את הנחש..."

      # קריאה לקולאב
      result = anvil.server.call('predict_image', file)
      self.prediction_text_box.text = result

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    client_msg = self.text_box_1.text
    result = anvil.server.call('server_says_hello', client_msg)
    self.text_box_2.text = result