# Define an event and a reminder
# event -> summary, description, start, end

from pydantic import BaseModel, Field
from typing import Optional, Sequence
from dotenv import load_dotenv
load_dotenv()

from langchain.chains.openai_functions import (
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


class Event(BaseModel):
    """Identifying information about an event"""

    summary: str = Field(..., description="Title of the event")
    description: Optional[str] = Field(..., description="Brief description of the event")
    start: str = Field(..., description="HH:MM format for event start", examples=["17:00", "17:30", "18:00", "18:30", "19:00", "19:30"])
    end: str = Field(..., description="HH:MM format for event end", examples=["17:00", "17:30", "18:00", "18:30", "19:00", "19:30"])

class Events(BaseModel):
    """A list of events"""

    events: Sequence[Event] = Field(..., description="A list of events in the text")

class ExtractEvents:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a world class algorithm for extracting information about multiple events mentioned by a user."),
                ("human", "Use the given format to extract event details from the following input. Assume reasonable start and end times wherever user has not provided them: {input}"),
                ("human", "Tip: Make sure to answer in the correct format"),
            ]
        )

        self.chain = create_structured_output_chain(Events, self.llm, self.prompt, verbose=True)

    def extract(self, text):
        events = self.chain.run(text)
        return events

if __name__ == "__main__":
    test_msg = """I want to have milk and cereal for breakfast. I'll cook rice for lunch. I'll order salad for dinner. I need to finish the MLLD assignment tomorrow which will take a couple of hours. Will also play basketball with John. Wanted to read my book for an hour before sleeping at 12."""
    e = ExtractEvents()
    print(e.extract(test_msg))