from brain_of_the_doctor import encode_image,analyze_imaege_with_querry
from voice_of_the_patient import record_audio,transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts
import gradio as gr
import os

system_prompt = """
            You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please
"""

def process_input(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        stt_model='whisper-large-v3',
        audio_filepath=audio_filepath,
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
    )
    if image_filepath:
        doctor_analysis = analyze_imaege_with_querry(
            query=system_prompt + speech_to_text_output,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encode_image=encode_image(image_filepath)
        )
    else:
        doctor_analysis = "No image provided for analysis."
    voice_of_doctor_output = text_to_speech_with_gtts(doctor_analysis, "final.mp3")
    return speech_to_text_output, doctor_analysis, "final.mp3"

iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3")
    ],
    title="AI Doctor with Vision and Voice"
)
iface.launch(debug=True)