'''
current status:
- input via text first
- then proceed by clicking via buttons, seamlessly goes on
- cannot randomize # of options properly,
- can only null-ify a ran num of buttons

workflow:
- enter theme input via textbox
- make buttons visible, textbox invisible
- enter options input via buttons
- buttons.onclick triggers smth like the respond (chatbot) function
'''

import gradio as gr
import random

def respond(message, chat_history):
    text = "The length of our chat is {}".format(len(chat_history))

    if len(chat_history) > 0:
        text = "ASDFGHJKL"
    bot_message = text
    chat_history.append((message, bot_message))
    return chat_history, gr.Textbox.update(visible=False)

# user clicked on a button, chatbot output text should be based on that, and change button info
def respondButton(chat_history, buttonA, buttonB, buttonC, buttonD, buttonE):
    # buttonA will be the button pressed, if it is null return from func unchanged
    if buttonA == "null":
        return chat_history, buttonA, buttonB, buttonC, buttonD, buttonE
    
    bot_message = "You chose button: {}".format(buttonA)
    chat_history.append((buttonA, bot_message))

    # easily update optionData via backend
    optionData = ["OptionA", "OptionB", "OptionC", "OptionD", "OptionE"]
    
    # null-ification
    n = random.randint(0,3)
    for x in range(n):
        optionData[x] = "null"
    buttonA = optionData[0]
    buttonB = optionData[1]
    buttonC = optionData[2]
    buttonD = optionData[3]
    buttonE = optionData[4]

    return chat_history, buttonA, buttonB, buttonC, buttonD, buttonE

with gr.Blocks() as demo:
    with gr.Column():
        chatbot = gr.Chatbot()
        theme = gr.Textbox(visible=True, label="Theme")
        with gr.Row():
            button1 = gr.Button(visible=True, value="Option1")
            button2 = gr.Button(visible=True, value="Option2")
            button3 = gr.Button(visible=True, value="Option3")
            button4 = gr.Button(visible=True, value="Option4")
            button5 = gr.Button(visible=True, value="Option5")
            buttons = [button1, button2, button3, button4, button5]

    clear = gr.ClearButton([chatbot])

    theme.submit(respond, [theme, chatbot], [chatbot, theme])
    
    # this sol won't work...
    # can't input type list into .click method 
    '''
    for button in buttons:
        otherButtons = [x for x in buttons if x != button]
        button.click(respondButton, [chatbot, button, otherButtons], [chatbot])
    '''

    # for each button click, first input passed is the button that was clicked on
    button1.click(respondButton, 
        # inputs 
        [chatbot, button1, button2, button3, button4, button5], 
        # outputs
        [chatbot, button1, button2, button3, button4, button5])
    
    button2.click(respondButton, 
        # inputs 
        [chatbot, button2, button1, button3, button4, button5], 
        # outputs
        [chatbot, button2, button1, button3, button4, button5])
    
    button3.click(respondButton, 
        # inputs 
        [chatbot, button3, button1, button2, button4, button5], 
        # outputs
        [chatbot, button3, button1, button2, button4, button5])
    
    button4.click(respondButton, 
        # inputs 
        [chatbot, button4, button1, button2, button3, button5], 
        # outputs
        [chatbot, button4, button1, button2, button3, button5])
    
    button5.click(respondButton, 
        # inputs 
        [chatbot, button5, button1, button2, button3, button4], 
        # outputs
        [chatbot, button5, button1, button2, button3, button4])

    demo.launch()