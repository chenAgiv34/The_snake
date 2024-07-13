import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";
import img from "../images/img.png";
import './SignIn.css'
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import { saveUser } from "./user";
import { Link, Outlet } from "react-router-dom";
export default function SignIn() {
  const [flag, setflag] = useState("Not Found");
  const [massage, setMessage] = useState("Not Found");
  const [mail, setMail] = useState("");
  const [password, setpassword] = useState("");
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
        nav("../../Enter");
      }
    } catch (error) {
      setMessage(error.response.data);
    }
  }
  return (
    <main className="form-signin w-100 m-auto" 
    >
    <form
style={{marginTop: '200px'}}
        onSubmit={(event) => {
          event.preventDefault();
          setflag(1);
        }}
      >      
        <img src={img} alt="img" />
        {/* <h1 className="h3 mb-3 fw-normal" style={{fontSize: 'xxx-large'}} >sign in</h1> */}
        <div className="form-floating">
          <input
            type="email"
            className="form-control"
            id="floatingInput"
            placeholder="name@example.com"
            style={{backgroundColor: "rgb(230, 243, 230)",border: "black"}}

            onInput={(e) => {
              setMail(e.target.value);
            }}
          />
          <label htmlFor="floatingInput">Email address</label>
        </div>
        <div className="form-floating">
          <input
            type="password"
            className="form-control"
            id="floatingPassword"
            placeholder="Password"
            style={{backgroundColor: "rgb(230, 243, 230)",}}
            onInput={(e) => {
              setpassword(e.target.value);
            }}
          />
          <label htmlFor="floatingPassword">Password</label>
        </div>
        {/* <Link class="btn btn-primary w-100 py-2" to={"../Enter"}>Sign in</Link> */}

        <button className="btn btn-primary w-100 py-2" type="submit"style={{backgroundColor: "darkseagreen",border: "black"}}
>
          Sign in
        </button>
      </form>
      <Outlet />

    </main>
  );
}
