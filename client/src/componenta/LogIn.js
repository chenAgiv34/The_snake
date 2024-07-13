import { UserList } from "../data/db";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import { getAllUser } from "./user";
import { saveUser } from "./user";
export default function LogIn() {
  let id = "";
  const [flag, setflag] = useState("Not Found");
  const [massage, setMessage] = useState("Not Found");
  const [mail, setMail] = useState("");
  const [password, setpassword] = useState("");
  const userList = [...UserList];
  const nav = useNavigate();

  useEffect(() => {
    if (flag == 1) {
      checkLogInInServer();
      setflag(0);
    }
  }, [flag]);
  //async, await=זה אומר שהפונקציה אסינכרונית,פונקציה שמחכה ולא ממשיכה בקוד עד שלא קיבלת תשובה מהשורה הזו
  async function checkLogInInServer(event) {
    const objectToServer = {
      email: mail,
      password: password,
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/login",
        objectToServer
      );
      console.log(response);
      if (response.data == "Not Found") setMessage(response.data);
      else {
        saveUser(response.data);
        // const axios = require('axios');
        checkInServer()
        async function checkInServer(event) {
          try {
            const response = await axios.post(
              "http://localhost:5000/MoveRobut",
            );
            savePoint(response.data);
            console.log('yes')

          } catch (error) {
            setMessage(error.response.data);
            console.log('no')
          }
        }
        nav("../../UserExist/robot");
      }
    } catch (error) {
      setMessage(error.response.data);
    }
  }

  return (
    <div className="LogIn">
      <h1 className="h1">Log In</h1>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          setflag(1);
        }}
      >
        <br></br>
        <label className="label">email:</label>
        <br />
        <input
          className="input"
          type="email"
          onInput={(e) => {
            setMail(e.target.value);
          }}
        />

        <br></br>

        <label>password:</label>
        <br />
        <input
          type="password"
          onInput={(e) => {
            setpassword(e.target.value);
          }}
        />
        <br />
        <br />
        <input type="submit" value="connection"></input>
        <p>you dont have an account? click here👇</p>
        <input
          type="button"
          value="Sign Up"
          onClick={() => {
            nav("../SignUp");
          }}
        ></input>
      </form>
    </div>
  );
}
export function savePoint(arr) {
  localStorage.setItem("arrPoint",JSON.stringify(arr));
}


