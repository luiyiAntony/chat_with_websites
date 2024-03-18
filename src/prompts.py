from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

prompt = "May the {subject} be with you"

chat_message_prompt = ChatMessagePromptTemplate.from_template(role="Jedi", template=prompt)

#print(chat_message_prompt.format(subject="force"))


human_prompt = "Summarize our conversation so far in {word_count} words."
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)

#print(chat_prompt)

from langchain_core.messages import AIMessage, HumanMessage

human_message = HumanMessage(content="What is the best way to learn programming?")
ai_message = AIMessage(
    content="""\
        1. Choose a programming language: Decide on a programming language that you want to learn.

        2. Start with the basics: Familiarize yourself with the basic programming concepts such as variables, data types and control structures.

        3. Practice, practice, practice: The best way to learn programming is through hands-on experience\
    """
)

result = chat_prompt.format_prompt(
    conversation=[human_message, ai_message], word_count="10"
).to_messages()

print(result)



