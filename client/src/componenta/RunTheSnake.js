import { saveUser } from "./user";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import { savePoint, saveAllPoint } from "./point";
export default function RunTheSnake() {
  const [flag, setflag] = useState(0);
  const nav = useNavigate();
  const [massage, setMessage] = useState("Not Found");

  useEffect(() => {
    if (flag == 1) {
      checkInServer();
      setflag(0);
    }
  }, [flag]);
  async function checkInServer(event) {
    try {
      const response = await axios.post("http://localhost:5000/MoveRobut");
      savePoint(response.data);
      saveAllPoint(response.data);
      console.log("yes");
    } catch (error) {
      setMessage(error.response.data);
      console.log("no");
    }
  }
  //   nav();
  const handleClick = () => {
    // Use a separate function for button click
    setflag(1);
  };
  return (
    <div class="px-4 py-5 my-5 text-center">
      <h1 class="display-5 fw-bold text-body-emphasis">Ran the snake</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">
          snake לחץ להפעלת ה 
        </p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <button
            type="submit"
            onClick={handleClick}
            class="btn btn-primary btn-lg px-4 gap-3"
            style={{ backgroundColor: "darkseagreen", border: "black" }}

          >
            Click to activate
          </button>
        </div>
      </div>
    </div>
  );
}
