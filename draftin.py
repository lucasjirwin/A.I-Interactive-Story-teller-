import streamlit as st
from backend import Storyteller

# IMAGE BUTTONS
# st.markdown(
#             "###### [![this is an image link](https://picsum.photos/200)](https://github.com/openai/openai-node)"
#         )

#```````````````````````````````````````````````````````````````````
# Quickstart
# from st_clickable_images import clickable_images

# if 'steps' not in st.session_state:st.session_state.steps = 50
# st.slider('steps: *number of diffusion steps to run*', 10, 150, value=st.session_state.steps, key="steps")

# if "clicked" not in st.session_state: st.session_state.clicked = -1
# if "thetext" not in st.session_state: st.session_state.thetext = ""
# if "images" not in st.session_state: st.session_state.images = [
#         "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
#         "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
#         "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
#         "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
#         "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700"
#         # "https://picsum.photos/300",
#         # "https://picsum.photos/300",
#         # "https://picsum.photos/300",
#         # "https://picsum.photos/300"
#     ]

# def add():
#     st.session_state.images.append("https://picsum.photos/300")

# st.text_area("init", placeholder="YOMAMA", value=st.session_state.thetext)
# st.button('add', on_click=add)

# st.session_state.clicked = clickable_images(
#     st.session_state.images,
#     titles=[f"Image #{str(i)}" for i in range(8)]
#     ,div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"}
#     ,img_style={"margin": "5px", "height": "200px"},
# )

# # st.markdown(f"Image #{st.session_state.clicked} clicked" if st.session_state.clicked > -1 else "No image clicked")
# st.markdown(f"last clicked: {st.session_state.clicked}" if st.session_state.clicked > -1 else "No image clicked")

# if st.session_state.clicked > -1:
#     st.write(f"HEYYOOO last clicked: {st.session_state.clicked}")
#     st.session_state.thetext = "PINK SKIES MY GUY" + st.session_state.images[st.session_state.clicked]
    # del st.session_state.images[st.session_state.clicked]

# ```````````````````````````````````````````````````````````````````
## RELOAD PAGE

# from streamlit_js_eval import streamlit_js_eval
# streamlit_js_eval(js_expressions="parent.window.location.reload()")

# ```````````````````````````````````````````````````````````````````

# captions = list(range(200,500,100))
# img_items = [f"https://dummyimage.com/400x{w}/d4c9d4/3740bd.jpg&text=IMG_{w}" for w in captions]

# for img in img_items:
#     c1,mid,c3 = st.columns([2,1,3])
#     c1.image(img)
#     title = c3.text_input('Comments',key=img+"title")
#     if c3.button('Save Me', key=img+"save"):
#         c1.write(title)

# ##```````````````````````````````````````````````````````````````````
# import random

# if 'images' not in st.session_state:
#     st.session_state.images = []
#     # which gets updated dynamically

# if 'story' not in st.session_state:
#     st.session_state.story = []

# if 'page' not in st.session_state: 
#     st.session_state.book = {
#         "story": "Sample story",
#         "images": ["image1.jpg", "image2.jpg", "image3.jpg"]
#     }

# # Iterate over the key-value pairs
# for key, value in book.items():
#     if key == "story":
#         print("story:", value)
#     elif key == "images":
#         print("Images:", value)


# if 'samples' not in st.session_state:
#     st.session_state.samples = 1

# def add():
#     for _ in range(st.session_state.samples):
#         st.session_state.images.append("https://picsum.photos/200")
#         st.session_state.story.append(f"asdfghj asdfghj qwertyu asdfgh {len(st.session_state.images)}")

# st.slider('samples: *how many images to generate at each step*', 1,10, value=st.session_state.samples, key="samples")
# st.button("add", on_click=add)

# # rendering
# # for i in range (len(st.session_state.images)):
# col1,col2 = st.columns(2)
# # img_cols = st.columns(10)
# with col1:
#     st.write(st.session_state.story)
# with col2:
#     # if st.session_state.samples>1:
#     #     for i in range (st.session_state.samples):
#     #         with img_cols[i]:
#     #             st.image(st.session_state.images[i])
#     # else:    
#     #     st.image(st.session_state.images[i])
#     streamlit_imagegrid(urls=st.session_state.images, height=1000, key=f"grid {random.randint(0,100)}")
# st.divider()

# ##```````````````````````````````````````````````````````````````````

# import requests

# st.title('Image grid test')
# # zoom_val = st.sidebar.slider('Zoom',40,240)

# urls = [
#         # { "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/81/07/83/1000_F_281078312_PcISs3yKL9r70nCqvDkgOR17UBGIw97C.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/81/07/83/1000_F_281078312_PcISs3yKL9r70nCqvDkgOR17UBGIw97C.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/81/07/83/1000_F_281078312_PcISs3yKL9r70nCqvDkgOR17UBGIw97C.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"},
#         # { "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"},
#         { "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"}
#       ]

# # return_value = 
# streamlit_imagegrid(urls=urls, height=1000)

# if return_value is not None:
#     response = requests.get(return_value)
#     st.sidebar.markdown('<img src={} width=240px></img>'.format(return_value),unsafe_allow_html=True)


##```````````````````````````````````````````````````````````````````

# from streamlit_imagegrid import streamlit_imagegrid
# import random

# images = [
#         {
#           "width": 1000,
#           "height": 666,
#           "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"
#         },
#         {
#           "width": 1000,
#           "height": 422,
#           "src": "https://as2.ftcdn.net/jpg/02/81/07/83/1000_F_281078312_PcISs3yKL9r70nCqvDkgOR17UBGIw97C.jpg"
#         },
#         {
#           "width": 1000,
#           "height": 666,
#           "src": "https://as2.ftcdn.net/jpg/02/96/35/64/1000_F_296356423_f6IEidPVRWzaqj2MJQ2VLJJTYGRAtY4P.jpg"
#         }
#       ]

# from st_clickable_images import clickable_images

# images = ["https://picsum.photos/300"] * 10

# if 'chapters' not in st.session_state:
#     st.session_state.chapters = [
#         {"story": "Once upon a time there was a...", "images": images},
#         {"story": "So he jumped! And he fell, squaeoering..", "images": images}
#     ]

# if 'samples' not in st.session_state:
#     st.session_state.samples = 1

# def new_chap():
#     # st.write("Button action")
#     images = []
#     for _ in range(st.session_state.samples):
#         # st.write("Loop action")
#         images.append("https://picsum.photos/512")
#     st.session_state.chapters.append({"story": "3 WEEKS LATER... He fell in love.", "images": images})
#     # st.write(st.session_state.chapters)
    
# st.slider('samples: *how many images to generate at each step*', 1,10, value=st.session_state.samples, key="samples")
# st.button('chapter', on_click=new_chap)
# count=0

# for index, chapter in enumerate(st.session_state.chapters):
#     cols = st.columns(2)
#     story = chapter["story"]
#     images = chapter["images"]
#     count +=1
    
#     # with cols[0]:
#     st.write(story) 
#     # with cols[1]:
#         # st.image(images, output_format="auto")
#     clickable_images(
#             images,
#             div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
#             img_style={"margin": "1px", "height": "150px"}
#             ,key=count
#         )
#         # return_value=
#         # streamlit_imagegrid(urls=images, height=300, key=count)
#         # maybe height can be h_w*2+100 so it's sortaaa dynamic... BUG: why is the img size capped??

# # ##```````````````````````````````````````````````````````````````````
# # import streamlit as st
# from streamlit_imagegrid import streamlit_imagegrid
# import requests
# from PIL import Image
# from io import BytesIO

# st.title('Image grid test')
# zoom_val = st.sidebar.slider('Zoom',40,240)

# urls = [
#         {
#           "width": 1000,
#           "height": 666,
#           "src": "https://as2.ftcdn.net/jpg/02/25/53/52/1000_F_225535263_n14yO9cXk18X90qQYxBf5Vcf00uOtAhW.jpg"
#         },
#         {
#           "width": 1000,
#           "height": 422,
#           "src": "https://as2.ftcdn.net/jpg/02/81/07/83/1000_F_281078312_PcISs3yKL9r70nCqvDkgOR17UBGIw97C.jpg"
#         },
#         {
#           "width": 1000,
#           "height": 666,
#           "src": "https://as2.ftcdn.net/jpg/02/96/35/64/1000_F_296356423_f6IEidPVRWzaqj2MJQ2VLJJTYGRAtY4P.jpg"
#         }
#       ]

# for i in range(5):
#     cols=st.columns(2)
#     with cols[0]:   
#         '''HIIIII'''
#     with cols[1]:
#         return_value= streamlit_imagegrid(urls=urls,zoom=zoom_val,height=1000, key="grid")

# if return_value is not None:
#     response = requests.get(return_value)
#     st.sidebar.markdown('<img src={} width=240px></img>'.format(return_value),unsafe_allow_html=True)
# ##```````````````````````````````````````````````````````````````````

# if 'chapters' not in st.session_state: st.session_state.chapters = [{"story": "Ashskslas sfghjk shjaksakl", "images": ["https://picsum.photos/512"]},{"story": "Qwerwetyui wtyquio tyqwuio", "images": ["https://picsum.photos/512"]}]

# for index, chapter in enumerate(st.session_state.chapters):
#     story = chapter["story"]
#     images = chapter["images"]
    
#     st.write(story) 
#     cols = st.columns(3)
#     st.divider()
#     count = 0
#     for i, image in enumerate(images):
#         with cols[count]:
#             count+=1
#             if count == 3:
#                 count = 0
#             st.image(images[i])      

# def submit():
#     st.session_state.chapters.append({"story": "THE STORY IS CHANGED.", "images": ["https://picsum.photos/512"]})

# st.text_input('', placeholder="Caption", on_change=submit)

# prompt = st.chat_input("Say something", on_submit=submit, disabled=True)
   

# ##```````````````````````````````````````````````````````````````````

# Usage:
storyteller = Storyteller()
output = storyteller.run_chain("Write me a story about a Venetian general in Cyprus")
st.write(output)
