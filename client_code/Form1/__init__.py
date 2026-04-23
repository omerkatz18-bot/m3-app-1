from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    client_msg = self.text_box_1.text
    print(f"Client message: {client_msg}")  # לוג להצגת ההודעה שהתקבלה
    result = anvil.server.call('server_says_hello', client_msg)
    print(f"Received from server: {result}")  # לוג להצגת התוצאה מהשרת
    self.text_box_2.text = result

  @handle("file_loader_1", "change")
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:  # Ensure that a file has been uploaded
      uploaded_image = self.file_loader_1.file
      self.image_loaded.source = uploaded_image

      # בדיקה אם הפונקציה `predict_image` קיימת בשרת
      print("Calling predict_image with uploaded image")  # לוג לבדיקת קריאה לפונקציה
      result = anvil.server.call('predict_image', uploaded_image)
      print(f"Received prediction result: {result}")  # לוג להצגת התוצאה מהפונקציה
      self.prediction_text_box.text = result

      
