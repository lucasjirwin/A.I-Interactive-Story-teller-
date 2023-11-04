import gradio as gr

def optionSubmit(choice, story):
    text = story + "\n" + "You chose option {}, ASDFGH SGSAHJKNLMS SHHSAKLNS ASG SHAHJKSJA".format(choice)
    options = ["option1", "option2", "option3", "option4", "option5"]
    # progress the options and fill the chatbot with radio choice
    return gr.Radio.update(choices=options, value=None), gr.Textbox.update(value=text), gr.Image.update(value="https://picsum.photos/50")

def themeSubmit(theme):
    text = "The theme of your story is {}".format(theme)
    # if we wanna do something specific after the 1st user input
    # maybe instead of "start" api call it would be "continue"
    return gr.Textbox.update(visible=False), gr.Textbox.update(visible=True, value=text, container=True), gr.Radio.update(visible=True), gr.Image.update(visible=True)

with gr.Blocks() as demo:
    theme = gr.Textbox(label="Enter your theme", visible=True, placeholder="comedy, horror, melodrama...")
    with gr.Column():
        with gr.Row():
            story = gr.Textbox(label="your story...", visible=False, interactive=False)
            image = gr.Image(value="https://picsum.photos/50", visible=False)
        radio = gr.Radio(["option A", "option B", "option C", "option D", "option E"], visible=False, label="How would you like to proceed?")

    theme.submit(themeSubmit, [theme], [theme, story, radio, image])
    radio.input(fn=optionSubmit, inputs=[radio, story], outputs=[radio, story, image])

    demo.launch()