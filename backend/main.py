from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fastapi.middleware.cors import CORSMiddleware

class VideoAnalysis(BaseModel):
    youtube_url: HttpUrl

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/analyse_video/")
def analyze_video(video: VideoAnalysis):
#    from langchain_community.document_loaders import YoutubeLoader
#    from langchain_text_splitters import RecursiveCharacterTextSplitter

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

