from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel,Field
from typing import Literal,Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-Next",
    task="text-generation",
)

model = ChatHuggingFace(llm = llm)

class review(BaseModel):
    key_themes : list[str] = Field(description="Write down all the key themes from the given review")
    summary : str = Field(description="A brief summary of the review")
    sentiment : Literal["Possitive","Negative"] = Field(description="Return sentiment of the review either negative, positive")
    pros : Optional[list[str]] = Field(default=None,description="Write down all the pros inside a list")
    cons : Optional[list[str]] = Field(default=None,description="Write down all the cons inside a list")
    name : Optional[str] = Field(description="Write the name of the reviewer")

parser = PydanticOutputParser(pydantic_object=review)


rev = '''Samsung is a leading global brand known for its innovative technology and wide product range.
Its smartphones, especially the Galaxy series, offer strong performance, sleek design, and excellent displays.
Samsung also excels in home appliances and electronics with reliable and feature-rich products.
However, some devices can be expensive compared to competitors with similar specs.
Overall, Samsung is a trusted brand delivering quality, innovation, and versatility.
''' 

prompt = PromptTemplate.from_template(
    template = "Genarate the required data from the given review\n{text}\n{format_instruction}",
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

chain = prompt | model | parser

res = chain.invoke({'text':rev})
print(res.key_themes)

