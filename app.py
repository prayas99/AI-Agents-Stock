import gradio as gr
from data_fetcher import get_last_week_data
from summarizer import set_api_key, summarize_stock

def run_summary(ticker, api_key):
    set_api_key(api_key)
    df = get_last_week_data(ticker)
    summary = summarize_stock(ticker, df)
    return summary

app = gr.Interface(
    fn=run_summary,
    inputs=[
        gr.Textbox(label="Enter Stock Ticker (e.g. AAPL)", placeholder="AAPL"),
        gr.Textbox(label="OpenAI API Key", type="password")
    ],
    outputs="text",
    title="📊 Stock Trend Summarizer",
    description="Enter a stock ticker to get a 7-day LLM-based price summary."
)

if __name__ == "__main__":
    app.launch()
