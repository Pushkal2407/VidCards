from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

class VideoAnalysis(BaseModel):
    youtube_url: HttpUrl

app = FastAPI()

@app.post("/analyze_video/")
def analyze_video(video: VideoAnalysis):
   from langchain_community.document_loaders import YoutubeLoader
   from langchain_text_splitters import RecursiveCharacterTextSplitter

   loader = YoutubeLoader.from_youtube_url(str(video.youtube_url),add_video_info=True)
   docs=loader.load()
   print(f"On load:{type(docs)}")
   text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
   result = text_splitter.split_documents(docs)

   print(f"Result:{result}")
   author=result[0].metadata['author']
   length = result[0].metadata['length']
   title = result[0].metadata['title']
   total_size=len(result)

   return {"author":author,"length":length,"title":title,"total_size":total_size}

