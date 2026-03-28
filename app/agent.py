class SummarizerAgent:
    def __init__(self, model, tool):
        self.model = model
        self.tool = tool

    def run(self, input_text: str) -> str:
        if len(input_text.strip()) < 20:
            return "Input too short to summarize."

        return self.tool.run(input_text)