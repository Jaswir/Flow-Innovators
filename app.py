# import streamlit as st
# import langflow_output

# st.title("Question and Answer App")

# st.write("Ask a question and get an answer:")

# question = st.text_input("Your question:")

# if st.button("Get Answer"):
#     if question:
#         answer = langflow_output.getResponseFromLangFlow(question)
#         st.write(answer)
#     else:
#         st.write("Please enter a question.")


# This code adds custom REST api handler at runtime to a running Streamlit app
from tornado.web import Application, RequestHandler
from tornado.routing import Rule, PathMatches
import gc
import streamlit as st

@st.cache_resource()
def setup_api_handler(uri, handler):
    print("Setup Tornado. Should be called only once")

    # Get instance of Tornado
    tornado_app = next(o for o in gc.get_referrers(Application) if o.__class__ is Application)

    # Setup custom handler
    tornado_app.wildcard_router.rules.insert(0, Rule(PathMatches(uri), handler))
    
# === Usage ======
class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello'})

# This setup will be run only once
setup_api_handler('/api/hello', HelloHandler)