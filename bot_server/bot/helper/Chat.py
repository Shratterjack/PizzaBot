import dialogflow_v2 as dialogflow


class Chat:
    def __init__(self,sessionId):
        self.sessionId = sessionId
        self.project_id = 'elated-pathway-270514'
        self.client = dialogflow.SessionsClient()


    def detect_intent_text(self,text,language_code='en-US'):
        """Returns the result of detect intent with texts as inputs.

        Using the same `session_id` between requests allows continuation
        of the conversation."""

        session = self.client.session_path(self.project_id, self.sessionId)

        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = self.client.detect_intent(session=session, query_input=query_input)

        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name, response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
        return response.query_result.fulfillment_text
    
