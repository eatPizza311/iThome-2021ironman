### Script for Ironman 2021
import os
import json
import requests
import SessionState
import streamlit as st
import tensorflow as tf
from utils import load_and_prep_image, classes_and_models, update_logger, predict_json

# Setup environment credentials (you'll need to change these)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ironman-327706-ba995652161d.json" # change for your GCP key
PROJECT = "ironman-327706" # change for your GCP project
REGION = "asia-east1" # change for your GCP region (where your model is hosted)

### Streamlit code (works as a straigtht-forward script) ###
st.title("歡迎來到 Iron bird 🦅")
st.header("看看你的照片是什麼鳥!?")

@st.cache # cache the function so predictions aren't always redone (Streamlit refreshes every click)
def make_prediction(image, model, class_names):
    """
    Takes an image and uses model (a trained TensorFlow model) to make a
    prediction.

    Returns:
     image (preproccessed)
     pred_class (prediction class from class_names)
     pred_conf (model confidence)
    """
    image = load_and_prep_image(image)
    # Turn tensors into int16 (saves a lot of space, ML Engine has a limit of 1.5MB per request)
    image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
    # image = tf.expand_dims(image, axis=0)
    preds = predict_json(project=PROJECT,
                         region=REGION,
                         model=model,
                         instances=image)
    pred_class = class_names[tf.argmax(preds[0])]
    pred_conf = tf.reduce_max(preds[0])
    return image, pred_class, pred_conf

# Pick the model version
choose_model = st.sidebar.selectbox(
    "選擇模型哦",
    ("Model 1 (10 種鳥類)", # original 10 classes
     "Model 2 (11 種鳥類)", # original 10 classes + ASIAN CRESTED IBIS
     "Model 3 (11 種鳥類 + 非鳥類)") # 11 classes (same as above) + NOT_BIRDS class
)

# Model choice logic
if choose_model == "Model 1 (10 種鳥類)":
    CLASSES = classes_and_models["model_1"]["classes"]
    MODEL = classes_and_models["model_1"]["model_name"]
elif choose_model == "Model 2 (11 種鳥類)":
    CLASSES = classes_and_models["model_2"]["classes"]
    MODEL = classes_and_models["model_2"]["model_name"]
else:
    CLASSES = classes_and_models["model_3"]["classes"]
    MODEL = classes_and_models["model_3"]["model_name"]

# Display info about model and classes
if st.checkbox("想看可辨識的鳥兒有哪些？"):
    st.write(f"你選擇的模型是 {MODEL}, 這裡是它可以辨別出來的鳥兒種類:\n", CLASSES)

# File uploader allows user to add their own image
uploaded_file = st.file_uploader(label="上傳鳥照吧...🤭",
                                 type=["png", "jpeg", "jpg"])

# Setup session state to remember state of app so refresh isn't always needed
# See: https://discuss.streamlit.io/t/the-button-inside-a-button-seems-to-reset-the-whole-app-why/1051/11 
session_state = SessionState.get(pred_button=False)

# Create logic for app flow
if not uploaded_file:
    st.warning("請給我一個圖片啦！！")
    st.stop()
else:
    session_state.uploaded_image = uploaded_file.read()
    st.image(session_state.uploaded_image, use_column_width=True)
    pred_button = st.button("開始預測！")

# Did the user press the 開始預測！ button?
if pred_button:
    session_state.pred_button = True 

# And if they did...
if session_state.pred_button:
    session_state.image, session_state.pred_class, session_state.pred_conf = make_prediction(session_state.uploaded_image, model=MODEL, class_names=CLASSES)
    st.write(f"Prediction: {session_state.pred_class}, \
               Confidence: {session_state.pred_conf:.3f}")

    # Create feedback mechanism (building a data flywheel)
    session_state.feedback = st.selectbox(
        "結果正確嗎？",
        ("幫個忙吧", "對！", "錯了！"))
    if session_state.feedback == "Select an option":
        pass
    elif session_state.feedback == "對！":
        st.write("謝謝您的回饋🙏")
        # Log prediction information to terminal (this could be stored in Big Query or something...)
        print(update_logger(image=session_state.image,
                            model_used=MODEL,
                            pred_class=session_state.pred_class,
                            pred_conf=session_state.pred_conf,
                            correct=True))
    elif session_state.feedback == "錯了！":
        session_state.correct_class = st.text_input("正確的類別是什麼呢？")
        if session_state.correct_class:
            st.write("謝啦！有你的協助能讓模型變得更好💪")
            # Log prediction information to terminal (this could be stored in Big Query or something...)
            print(update_logger(image=session_state.image,
                                model_used=MODEL,
                                pred_class=session_state.pred_class,
                                pred_conf=session_state.pred_conf,
                                correct=False,
                                user_label=session_state.correct_class))
