import youtube_transcript_api
from transformers import pipeline

# 1. Transcript Extraction
def get_transcript(video_id):
    transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([entry['text'] for entry in transcript])
    return text

# 2. Summarization
summarizer = pipeline("summarization", model="t5-small")

# 3. Main Function
def summarize_video(video_id):
    transcript = get_transcript(video_id)
    summary = summarizer(transcript, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    return summary


video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL
video_id = video_url.split("watch?v=")[1]
summary = summarize_video(video_id)

print(summary)
