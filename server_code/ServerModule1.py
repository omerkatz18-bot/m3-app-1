import anvil.server

@handle("file_loader_1", "change")
def file_loader_1_change(self, file, **event_args):
  if file:  # Ensure that a file has been uploaded
    uploaded_image = self.file_loader_1.file
    self.image_loaded.source = uploaded_image
    result = anvil.server.call('predict_image', uploaded_image)
    self.prediction_text_box.text = result
    
def button_1_click(self, **event_args):
  """This method is called when the button is clicked"""
  client_msg = self.text_box_1.text
  result = anvil.server.call('server_says_hello', client_msg)
  self.text_box_2.text = result

