from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain import FewShotPromptTemplate
import re

class Storyteller:
    def __init__(self):
        self.chain = self.launch_chain()

    def launch_chain(self):
        EXAMPLES = [
            {
                "input": " Write me a story about a crazy psychopath singer in Brooklyn ",
                "answer": "Once upon a time, in the bustling streets of Brooklyn, there lived a crazy psychopath female singer named Mary. She was known for her hauntingly beautiful voice and her erratic behavior. One day, as she was walking down the street she saw a group of people gathered around a street performer. What does she do next? Option 1. She joins in and starts singing with the street performer. Option 2. She becomes jealous of the street performer's attention and attacks him. Option 3. She ignores the street performer and continues on her way. Option 4. She watches the street performer from a distance, intrigued by his talent. Option 5. She approaches the street performer and offers to collaborate with him. "
            },
            {
                "input": "Option 3: Marco gets the advice of a local wise man.",
                "answer": "Marco seeks the advice of a local wise man who is known for his knowledge of the island's history and culture. The wise man invites him into his home and they sit down to talk. What does the wise man tell him? Option 1. The wise man tells Marco about the island's ancient legends and myths. Option 2. The wise man shares stories of the island's past rulers and their accomplishments. Option 3. The wise man advises him on how to navigate the island's complex social hierarchy."
            }
            ,{
                "input": "Write a story about an Egyptian Pharaoh in hiding from his enemies.",
                "answer": " Once upon a time, in the depths of ancient Egypt, lived a powerful Pharaoh named Akhenaten.  He had many enemies, eager to seize his throne and overtake the kingdom. In order to stay safe and protect his people, Akhenaten had to hide from his enemies and find somewhere safe to stay. Where does he go? Option 1. He seeks refuge in a nearby temple. Option 2. He heads to the desert and builds a secret underground sanctuary. Option 3. He takes shelter in a forgotten tomb in the heart of the Valley of the Kings.  Option 4. He goes to a fortress in the east, on the banks of the Red Sea.  Option 5. He disguises himself as a peasant and lives amongst the common folk."
            },
               {
        "input": "Write me a story about a brave knight in a medieval kingdom.",
        "answer": "Once upon a time, in the medieval kingdom of Camelot, there lived a brave knight named Sir Arthur. He was known for his valor and chivalry. One day, the king summoned him to a grand quest. What does Sir Arthur do next? Option 1. He accepts the king's quest without hesitation. Option 2. He hesitates but eventually agrees to embark on the quest. Option 3. He respectfully declines the king's request and explains his reasons."
    },
    {
        "input": "Tell me a story about a curious scientist conducting experiments in a lab.",
        "answer": "In the bustling city of NeoTech, there worked a curious scientist named Dr. Emily. She was passionate about pushing the boundaries of science. One day, as she was conducting experiments in her lab, something extraordinary happened. What does Dr. Emily discover? Option 1. She creates a groundbreaking invention that changes the world. Option 2. Her experiment goes wrong, leading to unexpected consequences. Option 3. She stumbles upon a hidden formula that unlocks new possibilities."
    } ]

        EXAMPLE_TEMPLATE = """
        User: {input}
        AI: {answer}
        """

        PREFIX = """Act as an interactive storyteller. \
        You act as the narrator and present me with options of \
        how to continue the story. Present me a random number \
        of Options between 2 to 5 every time you produce an output. \
        After beginning the story, you will be provided an option \
        on how to continue the story. When this is done you should \
        continue the story and then provide a random number of Options \
        between 2 to 5 again. Continue this and do not end the story unless \
        you are specifically told to. Make sure you give your characters names\
        The following are examples of inputs \
        and outputs. The conversation history is {history}
        """

        SUFFIX = """
        User: {input}
        AI: """

        example_prompt = PromptTemplate(
            input_variables=["input", "answer"],
            template=EXAMPLE_TEMPLATE
        )
        few_shot_prompt_template = FewShotPromptTemplate(
            examples=EXAMPLES,
            example_prompt=example_prompt,
            prefix=PREFIX,
            suffix=SUFFIX,
            input_variables=["input", "history"],
            example_separator="\n\n"
        )

        llm = OpenAI(temperature=1.0, openai_api_key="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")
        memory = ConversationBufferMemory()

        chain = ConversationChain(
            llm=llm,
            verbose=False,
            memory=memory,
            prompt=few_shot_prompt_template
        )
        return chain

    def run_chain(self, input):
        return self.chain.run(input)
    
    def split_options(self, output):
        options = re.split(r"Option \d+\.", output)[1:]
        options = [option.strip() for option in options]

        return options


# Usage:
# storyteller = Storyteller()
# output = storyteller.run_chain("Write me a story about a Venetian general in Cyprus")
# print(output)
