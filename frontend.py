'''
current status:
- input via text first (can only enter a single letter as it is rn)
- then proceed by clicking via buttons, seamlessly goes on
- textbox remains visible at the bottom tho

workflow:
- enter theme via textbox
- make buttons visible
- enter text input via buttons
- preferably, hide textbox from user while
  using it to converse w/ the chatbot

* radio/buttons onclick functionality?
* calling respond from optionSubmit to simulate
  buttons triggering the chatbot discussion
'''

import gradio as gr

def optionSubmit(choice, chat_history):
    chat_history.append((choice, "You chose: {}".format(choice)))
    options = ["option1", "option2", "option3", "option4", "option5"]
    # progress the options and fill the chatbot with radio choice
    return gr.Radio.update(choices=options, value=None), chat_history

def themeSubmit(message, chat_history):
    text = "The length of our chat is {}".format(len(chat_history))
    # if we wanna do something specific after the 1st user input
    # maybe instead of "start" api call it would be "continue"
    if len(chat_history) > 0:
        text = "ASDFGHJKL"
    bot_message = text
    chat_history.append((message, bot_message))
    return gr.Textbox.update(visible=False), chat_history, gr.Radio.update(visible=True)

with gr.Blocks() as demo:
    # list in radio will be updated via latest options from backend
    chatbot = gr.Chatbot()
    msg = gr.Textbox(visible=True, label="Theme")
    radio = gr.Radio(["option A", "option B", "option C", "option D", "option E"], visible=False, label="How would you like to proceed?")

    clear = gr.ClearButton([msg, chatbot])

    msg.submit(themeSubmit, [msg, chatbot], [msg, chatbot, radio])
    radio.input(fn=optionSubmit, inputs=[radio, chatbot], outputs=[radio, chatbot])

    demo.launch()