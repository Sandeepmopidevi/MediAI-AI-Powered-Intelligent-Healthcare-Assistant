import React from "react";
import { bookAppointment } from "../api";
import "./Chatbot.css";

function Appointment() {
  const handleBookAppointment = async () => {
    const response = await bookAppointment("2025-02-20T10:00:00", "2025-02-20T10:30:00");
    alert(response.data.message);
  };

  return (
    <div className="appointment-container">
      <h2>Book an Appointment</h2>
      <button onClick={handleBookAppointment}>Book Appointment</button>
    </div>
  );
}

export default Appointment;
