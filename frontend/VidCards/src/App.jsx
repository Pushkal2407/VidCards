import React, {useState} from "react";
import axios from "axios";

function App() {
  const [youtubeLink, setYoutubeLink] = useState("");
  const [response, setResponse] = useState(null);

  const handleLinkChange = (event) => {
    setYoutubeLink(event.target.value);
  };

  const sendLink = async () => {
    try {
      const response = await axios.post("http://localhost:8000/analyse_video", {
        youtube_url: youtubeLink,
      });
      setResponse(response.data);
    } catch (error) {
      console.log(error);
    }
  };
  return (
      <div className="App">
        <h1>Video Analysis</h1>
        <input
          type="text"
          placeholder="Enter YouTube link"
          value={youtubeLink}
          onChange={handleLinkChange}
        />
        <button onClick={sendLink}>
        Generate Flashcards
        </button>
        {response && (
          <div>
            <h2>Response Data: </h2>
            <div>
              <h2> Response Data: </h2>
              <p>{JSON.stringify(response,null, 2)}
              </p>
            </div>
          </div>
         )}
       </div>
    )
  }
  export default App;
