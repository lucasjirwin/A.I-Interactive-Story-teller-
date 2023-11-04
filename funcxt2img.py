import os
import requests
import base64
import streamlit as st
import random
from backend import Storyteller

storyteller = Storyteller()
# story_txt = ""
# INITIALIZING SESSION STATE VARIABLES
if 'prompt' not in st.session_state: st.session_state.prompt = ""
if 'img_prompt' not in st.session_state: st.session_state.img_prompt = ""
if "style" not in st.session_state: st.session_state.style = "Basic art"
if "styles" not in st.session_state: st.session_state.styles = ["Studio Ghibli", "Watercolor", "Academicism", "Pop-art", "Anime"]
if 'user_input' not in st.session_state: st.session_state.user_input = ""
if 'last_clicked' not in st.session_state: st.session_state.last_clicked = -1
if 'end' not in st.session_state: st.session_state.end = False
if 'init' not in st.session_state: st.session_state.init = True
if "disabled" not in st.session_state: st.session_state.disabled = True
if "init_disabled" not in st.session_state: st.session_state.init_disabled = True
if 'header' not in st.session_state: st.session_state.header = "Begin by choosing an art style for your story"
if 'expanded' not in st.session_state: st.session_state.expanded = False
if 'story_txt' not in st.session_state: st.session_state.story_txt = ""  # Initializing as an empty string
if 'options' not in st.session_state: st.session_state.options = [] 

# CHAPTERS
if 'chapters' not in st.session_state: st.session_state.chapters = []
if 'image_num' not in st.session_state: st.session_state.image_num = 0

if 'samples' not in st.session_state: st.session_state.samples = 1
if 'height_width' not in st.session_state: st.session_state.height_width = 512
if 'steps' not in st.session_state: st.session_state.steps = 50
if 'cfg_scale' not in st.session_state: st.session_state.cfg_scale = 7
if 'clips' not in st.session_state: st.session_state.clips = ["NONE", "FAST_BLUE", "FAST_GREEN", "SIMPLE", "SLOW", "SLOWER", "SLOWEST"]
if 'clip_guidance_preset' not in st.session_state: st.session_state.clip_guidance_preset = 'NONE'

if 'img_to_edit' not in st.session_state: st.session_state.img_to_edit = -1
if 'chapter_to_edit' not in st.session_state: st.session_state.chapter_to_edit = -1
if 'to_edit' not in st.session_state: st.session_state.to_edit = False

# the art style should be the first input by the user
def update_style(btn):
    st.session_state.style = st.session_state.styles[btn]
    st.session_state.styles = []
    st.session_state.init_disabled = False
    st.session_state.header = "Enter a starting point for your story"

# if the user has clicked on the 'edit' button associated with an img, expand the edit image prompt section
# and paste the selected image's prompt into the text_area, the user must then click recreate.
def edit_prompt(prompt, chapter_index, img_index):
    st.session_state.expanded = True
    st.session_state.chapter_to_edit = chapter_index
    st.session_state.img_to_edit = img_index

    # st.session_state.prompt = prompt
    st.session_state.img_prompt = prompt

    st.session_state.disabled = False
    st.session_state.to_edit = True

# recreates the selected image (via edit_prompt) by first popping its data from the given chapter, 
# and calling gen_img at the specific chapter and img index to correctly place the new img
def recreate(prompt, chapter_index):
    st.session_state.expanded = False
    img_index = st.session_state.img_to_edit

    chapter = st.session_state.chapters[chapter_index]
    
    chapter["images"].pop(img_index)
    chapter["filenames"].pop(img_index)
    chapter["captions"].pop(img_index)

    generate_images(api_key, prompt, st.session_state.style, st.session_state.samples, output_directory, chapter_index, img_index)
    
    # reset
    st.session_state.disabled = True
    # st.session_state.prompt = ""

# option #N buttons to continue story, update last_clicked info and just generate img (atp in time the story is 'generated' within gen_img as well)
def on_button_click(button, prompt):
    # global story_txt
    st.session_state.last_clicked = button
    if st.session_state.end:
        return
    
    # if st.session_state.chapters == []:
    #     print('generate!')
    #     story_txt = generate_images(api_key, prompt, st.session_state.style, st.session_state.samples, output_directory)
    # else: 
    #     # print(prompt)
    print('continue!')
    st.session_state.story_txt = continue_story(api_key, prompt, st.session_state.style, st.session_state.samples, output_directory)
    # print(story_txt)

## API-less img gen
# def generate_images(api_key, text_prompt, style, num, output_directory, chapter_index= len(st.session_state.chapters)+1, img_index=len(st.session_state.chapters)+1):
#     filenames = []
#     captions = []
#     images = []

#     if st.session_state.to_edit:
#         num=1

#     # API-LESS IMG GEN
#     for _ in range(num):
#         url = f"https://picsum.photos/512"

#         os.makedirs(output_directory, exist_ok=True)
#         file_path = os.path.join(output_directory, f"{text_prompt[:100]}{st.session_state.image_num}.png") #BUG: NEEDS REPLACEMENT
        
#         response = requests.get(url)
#         response.raise_for_status()

#         with open(file_path, "wb") as file:
#             file.write(response.content)
    
#         filenames.insert(img_index, file_path)
#         captions.insert(img_index, text_prompt + f" {random.randint(0,100)} These are my index details. {chapter_index}: {img_index}")
#         images.insert(img_index, file_path)
#         st.session_state.image_num +=1

#     if st.session_state.to_edit:
#         st.session_state.chapters[chapter_index]["images"].insert(img_index, images[0])
#         st.session_state.chapters[chapter_index]["captions"].insert(img_index, captions[0])
#         st.session_state.chapters[chapter_index]["filenames"].insert(img_index, filenames[0])
#         st.session_state.to_edit = False
#     else:
#         story_txt = storyteller.run_chain("Write me a story about..." + text_prompt)
#         chapter = {"story": story_txt, "images": images, "captions": captions, "filenames": filenames}
#         # chapter = {"story": text_prompt +f"{st.session_state.image_num}", "images": images, "captions": captions, "filenames": filenames}
#         st.session_state.chapters.insert(chapter_index, chapter)

# UNCOMMENT ME~~~~~~~~~~
# API-ful img gen- uses Stable Diffusion v1.5



##################
def continue_story(api_key, text_prompt, style, num, output_directory, chapter_index= len(st.session_state.chapters)+1, img_index=len(st.session_state.chapters)+1):
    # global story_txt 
    filenames = []
    captions = []
    images = []
    if st.session_state.to_edit:
        num = 1
    else:
        num = st.session_state.samples

    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    engine_id = "stable-diffusion-v1-5"

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text_prompt + f", in the art style of {style}"
                }
            ],
            # the hyper params are 'fetched' from the session state variables as they're also customizable via the hyper params section at the bottom
            "cfg_scale": st.session_state.cfg_scale,
            "clip_guidance_preset": st.session_state.clip_guidance_preset,
            "height": st.session_state.height_width,
            "width": st.session_state.height_width,
            "samples": num,
            "steps": st.session_state.steps,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for _, image in enumerate(data["artifacts"]):
        # the filepath's name structure is very important, do NOT change without changing all other references as well
        file_path = os.path.join(output_directory, f"{prompt[:100]}{st.session_state.image_num}.png")
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))

        filenames.insert(img_index, file_path)
        captions.insert(img_index, text_prompt + f", in the art style of {style}")
        images.insert(img_index, file_path)
        st.session_state.image_num +=1
  
    if st.session_state.to_edit:
        # INSERTING the img data at the correct place if the current image being created is a 'recreation'
        st.session_state.chapters[chapter_index]["images"].insert(img_index, images[0])
        st.session_state.chapters[chapter_index]["captions"].insert(img_index, captions[0])
        st.session_state.chapters[chapter_index]["filenames"].insert(img_index, filenames[0])
        st.session_state.to_edit = False
    else:
        story_txt = storyteller.run_chain(text_prompt)
        # print(story_txt)
        # print("[]")
        chapter = {"story": story_txt.split("Option 1.")[0], "images": images, "captions": captions, "filenames": filenames}
        # chapter = {"story": text_prompt +f"{st.session_state.image_num}", "images": images, "captions": captions, "filenames": filenames}
        st.session_state.chapters.insert(chapter_index, chapter)
        return story_txt
#####################
def generate_images(api_key, text_prompt, style, num, output_directory, chapter_index= len(st.session_state.chapters)+1, img_index=len(st.session_state.chapters)+1):
    # global story_txt 
    filenames = []
    captions = []
    images = []
    if st.session_state.to_edit:
        num = 1
    else:
        num = st.session_state.samples

    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    engine_id = "stable-diffusion-v1-5"

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text_prompt + f", in the art style of {style}"
                }
            ],
            # the hyper params are 'fetched' from the session state variables as they're also customizable via the hyper params section at the bottom
            "cfg_scale": st.session_state.cfg_scale,
            "clip_guidance_preset": st.session_state.clip_guidance_preset,
            "height": st.session_state.height_width,
            "width": st.session_state.height_width,
            "samples": num,
            "steps": st.session_state.steps,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for _, image in enumerate(data["artifacts"]):
        # the filepath's name structure is very important, do NOT change without changing all other references as well
        file_path = os.path.join(output_directory, f"{prompt[:100]}{st.session_state.image_num}.png")
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))

        filenames.insert(img_index, file_path)
        captions.insert(img_index, text_prompt + f", in the art style of {style}")
        images.insert(img_index, file_path)
        st.session_state.image_num +=1

    if st.session_state.to_edit:
        # INSERTING the img data at the correct place if the current image being created is a 'recreation'
        st.session_state.chapters[chapter_index]["images"].insert(img_index, images[0])
        st.session_state.chapters[chapter_index]["captions"].insert(img_index, captions[0])
        st.session_state.chapters[chapter_index]["filenames"].insert(img_index, filenames[0])
        st.session_state.to_edit = False
    else:
        story_txt = storyteller.run_chain("Write me a story about..." + text_prompt)
        chapter = {"story": story_txt.split("Option 1.")[0], "images": images, "captions": captions, "filenames": filenames}
        # chapter = {"story": text_prompt +f"{st.session_state.image_num}", "images": images, "captions": captions, "filenames": filenames}
        st.session_state.chapters.insert(chapter_index, chapter)
        return story_txt
# ##
api_key = "sk-dPkkaTHM49rksWXxfuSFOB1IAejgWMN31Y6PlYO2hy5NkfWE" # insert API key
output_directory = "./out/"

## STREAMLIT WEBSITE RENDERING ----------------------
st.set_page_config(page_title="Story", page_icon="🧩")
st.title("Interactive Storytelling Experience")

sub_container = st.empty()
sub = sub_container.subheader(st.session_state.header)
st.caption("make it your very own.")

prompt = st.text_input(placeholder="write me a story about...", disabled=st.session_state.init_disabled, key="init_prompt", help="Begin your story here", label='initprompt', label_visibility="collapsed")

cols = st.columns(5)
text_col, img_col = st.columns(2)

if len(st.session_state.styles) > 0:
    for i in range(len(st.session_state.styles)):
        with cols[i]:
            st.button(st.session_state.styles[i], on_click=update_style, kwargs={"btn": i})

if prompt != "":
    st.session_state.init_disabled = True
    st.session_state.header = "Continue your story by choosing from the options below"
    st.divider()
    if st.session_state.init:
        st.session_state.init = False
        if st.session_state.last_clicked == -1:
            st.session_state.story_txt = generate_images(api_key, prompt, st.session_state.style, st.session_state.samples, output_directory)

### change ^ 
# story + image RENDERING on website
for index, chapter in enumerate(st.session_state.chapters):
    story = chapter["story"]
    images = chapter["images"]
    captions = chapter["captions"]
    
    st.write(story) 
    cols = st.columns(3)
    st.divider()
    count = 0
    for i, image in enumerate(images):
        with cols[count]:
            count+=1
            if count == 3:
                count = 0
            st.image(images[i], captions[i])
            st.button("Edit image", key=captions[i], on_click=edit_prompt, kwargs={"prompt": captions[i], "chapter_index": index, "img_index": i})
            # st.text_input("Edit image prompt", on_change=recreate, value=st.session_state.img_prompt, key="img_prompt", kwargs={"prompt": st.session_state.img_prompt, "chapter_index": st.session_state.chapter_to_edit})
            # st.write(st.session_state.img_prompt)
img_prompt = st.chat_input("click on the image you want to re-create and enter your new prompt here", on_submit=recreate, kwargs={"prompt": prompt, "chapter_index": st.session_state.chapter_to_edit})
# NOTE: can't set val disabled of chat_input to session_state.disabled bc of the incompatibility with the chatbot widget.
# BUG: clicking on edit image button first is necessary.

# Add in red space the regex options 
#     # BUG: pressing the edit button re-gens buttons, could be an issue... could also be solved once API is integrated
if prompt != "":
    print(st.session_state.story_txt) 
    print(type(st.session_state.story_txt))
    options = storyteller.split_options(st.session_state.story_txt)
    nbuttons = random.randint(2,5)
    cols = st.columns(5)
    # print(f"options: {options}")
    # print(f"story_txt: {story_txt}")
    for i in range(nbuttons): #nbuttons
        if st.session_state.end:
            break
        with cols[i]:
            st.button(f"Option #{i+1}: {options[i]}", on_click=on_button_click, kwargs={"button": i, "prompt": options[i]})
        st.divider()
    with st.expander("Edit Image Prompts", expanded=st.session_state.expanded):
        # prompt = st.text_area('Click on the image you want to re-create and enter your new prompt below', disabled=st.session_state.disabled, help="To achieve optimal results with Stable Diffusion, ensure adherence to recommended standards for prompting.", key="prompt")
        st.button("Re-create", on_click=recreate, kwargs={"prompt": prompt, "chapter_index": st.session_state.chapter_to_edit})

with st.expander("Edit Stable Diffusion Hyper-Parameters"):
    '''To see more details on the parameters below, refer to: https://api.stability.ai/docs#tag/v1generation/operation/textToImage'''
    st.slider('samples: *how many images to generate at each step*', 1,10, value=st.session_state.samples, key="samples")
    st.slider('height/width', 512, 1024, value=st.session_state.height_width, step=64, key="height_width")
    st.slider('steps: *number of diffusion steps to run*', 10, 150, value=st.session_state.steps, key="steps")
    st.slider('cfg_scale: *how strictly the diffusion process adheres to the prompt (higher values keep image closer to prompt)*', 0,35, value=st.session_state.cfg_scale, key="cfg_scale")
    st.radio('clip_guidance_preset', st.session_state.clips, key="clip_guidance_preset")
    st.write("You have chosen a consistent art style of: " + "'" + st.session_state.style + "'")
    '''*Stable Diffusion, v1-5, 2023*'''