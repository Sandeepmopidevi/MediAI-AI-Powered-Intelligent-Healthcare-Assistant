import React, { useState } from "react";
import { sendMessage } from "../api";
import "./Chatbot.css";

function Chatbot() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [listening, setListening] = useState(false);

  const handleSendMessage = async () => {
    if (!message.trim()) return;

    const symptomsArray = message.split(",").map(symptom => symptom.trim().toLowerCase());
    const res = await sendMessage(symptomsArray);
    setResponse(res.data.response);
  };

  const startListening = () => {
    setListening(true);
    const recognition = new window.webkitSpeechRecognition();
    recognition.onresult = (event) => {
      setMessage(event.results[0][0].transcript);
    };
    recognition.start();
  };

  return (
    <div className="chat-container">
      <h2>AI-Powered Healthcare Assistant</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter symptoms (e.g., fever, cough)..."
      />
      <br />
      <button onClick={handleSendMessage}>Check Symptoms</button>
      <button onClick={startListening}>{listening ? "Listening..." : "Voice Input"}</button>
      {response && <div className="response-box">{response}</div>}
    </div>
  );
}

export default Chatbot;
