import axios from "axios";

const API_URL = "http://localhost:5000";

export const sendMessage = async (symptoms) => {
  return await axios.post(`${API_URL}/chat`, { symptoms });
};

export const bookAppointment = async (start_time, end_time) => {
  return await axios.post(`${API_URL}/book_appointment`, { start_time, end_time });
};
