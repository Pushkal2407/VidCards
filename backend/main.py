from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware
from services.genai import YoutubeVideoProcessor

class VideoAnalysis(BaseModel):
    youtube_url: HttpUrl

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/analyse_video/")
def analyze_video(video: VideoAnalysis):
#    from langchain_community.document_loaders import YoutubeLoader
#    from langchain_text_splitters import RecursiveCharacterTextSplitter
    processor=YoutubeVideoProcessor()
    result=processor.retrieve_youtube_documents(str(video.youtube_url))

   

    return {"result" : result}

