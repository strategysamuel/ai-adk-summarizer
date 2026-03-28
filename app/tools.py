class SummarizeTool:
    def __init__(self, client):
        self.client = client

    def run(self, input_text: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this in 3-4 lines:\n\n{input_text}"
        )
        return response.text