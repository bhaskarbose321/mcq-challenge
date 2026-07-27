import gradio as gr
from inference import predict

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=4, label="Question"),
    outputs=gr.Textbox(label="Predicted Answer"),
    title="Smart MCQ Solver (BiLSTM)"
)

demo.launch()
