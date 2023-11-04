import streamlit as st
import random

st.set_page_config(page_title="Story", page_icon="🧩")
st.title("Interactive Storytelling Experience")

sub_container = st.empty()
sub = sub_container.subheader("Begin by entering a starting point for your story")
st.caption("make it your very own.")

if 'init_prompt' not in st.session_state:
    st.session_state.init_prompt = ""

if 'story' not in st.session_state:
    st.session_state.story = "Once upon a time there was..."

if 'lastClick' not in st.session_state:
    st.session_state.lastClick = -1

if 'buttonLen' not in st.session_state:
    st.session_state.buttonLen = random.randint(2, 4)

prompt_container = st.empty()
prompt = prompt_container.text_input('init story prompt', value= st.session_state.init_prompt, label_visibility="collapsed", placeholder='write me a story about...')

col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
cols = [col1, col2, col3, col4, col5]

with col1:
    button = st.button("0")
if 'buttons' not in st.session_state:
    st.session_state.buttons = [button] * 5

# buttons = -1,0,1,2,3

for i in range(st.session_state.buttonLen-1):
    with cols[i+1]:
        st.session_state.buttons[i+1] = st.button(str(i+1))

if prompt != "" and st.session_state.lastClick == -1:
    # prompt gets printed TWICE in storybox instead of ONCE
    prompt_container.empty()
    st.session_state.init_prompt = ""
    st.info(prompt)
    st.session_state.story = st.session_state.story + (f" {prompt}")
    sub = sub_container.subheader("Continue your story by choosing from the options below")

# storyBox = st.text_area("storybox", value=st.session_state.story, disabled=False)
# ADD HERE
storyBox = st.write(st.session_state.story)

st.write(f"buttons: {st.session_state.buttons}")

# 0,1,2,3,4
for i in range(5):
    st.write(f"current button: {st.session_state.buttons[i]}")
    if st.session_state.buttons[i]:
        if i != st.session_state.lastClick:
            st.session_state.buttons[i] = False
        st.session_state.lastClick = i
        st.session_state.buttonLen = random.randint(2, 5)
        st.session_state.story = st.session_state.story + (f"\n \nYou have chosen option: {i}")
        # adds to textbox a click late,
        # and ofc if ncurr> nlast and click on button[n-1], that one won't show up AT ALL.
        break  

st.write(f"{st.session_state.lastClick} last clicked")
