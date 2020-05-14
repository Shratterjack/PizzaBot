import dialogflow_v2 as dialogflow
import os

class Chat:
    def __init__(self,sessionId):
        self.sessionId = sessionId
        self.project_id = os.environ['PROJECT_ID']
        self.client = dialogflow.SessionsClient()


    def detect_intent_text(self,text,language_code='en-US'):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation."""

        session = self.client.session_path(self.project_id, self.sessionId)

        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = self.client.detect_intent(session=session, query_input=query_input)

        return response.query_result.fulfillment_text
    
