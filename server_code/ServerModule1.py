import anvil.server
import anvil._threaded_server

class DummyTracer:
  def start_as_current_span(self, name):
    from contextlib import contextmanager
    @contextmanager
    def dummy(): yield
    return dummy()

# Replace the tracer function with our dummy
anvil._threaded_server.ensure_anvil_tracer = lambda: DummyTracer()
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
def button_1_click(self, **event_args):
  """This method is called when the button is clicked"""
  client_msg = self.text_box_1.text
  result = anvil.server.call('server_says_hello', client_msg)
  self.text_box_2.text = result

