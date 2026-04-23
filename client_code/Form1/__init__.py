from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # אתחול הרכיבים של המסך
    self.init_components(**properties)

  @handle("file_loader_1", "change")
  def file_loader_1_change(self, file, **event_args):
    """פונקציה שרצה ברגע שמעלים תמונה"""
    if file:
      # 1. הצגת התמונה שבחרת על המסך
      self.image_loaded.source = file

      # 2. עדכון טקסט זמני כדי שתראה שהאתר בתהליך
      self.prediction_text_box.text = "מזהה... נא להמתין"

      try:
        # 3. שליחת התמונה לקולאב וקבלת התוצאה למשתנה result
        result = anvil.server.call('predict_image', file)

        # 4. הצגת התוצאה הסופית בתיבת הטקסט
        self.prediction_text_box.text = result

      except Exception as e:
        # אם יש שגיאה (למשל הקולאב לא מחובר), היא תופיע כאן
        self.prediction_text_box.text = f"שגיאה בחיבור: {str(e)}"

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """פונקציה לבדיקת הודעת טקסט רגילה"""
    client_msg = self.text_box_1.text
    try:
      result = anvil.server.call('server_says_hello', client_msg)
      self.text_box_2.text = result
    except:
      self.text_box_2.text = "השרת לא מגיב לבדיקת טקסט"