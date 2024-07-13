import { Link, Outlet } from "react-router-dom";
import img from "../images/img1.png";

export function Enter() {
  return (
    <div className="container">
    <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">

      <div className="col-md-3 mb-2 mb-md-0" >
        <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
        <img src={img} alt="img" />
        </a>
      </div>
      <div className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0" >
      <Link className="nav-link px-2" style={{color: "darkseagreen" , fontSize: "large"}} to={"./RunTheSnake"}>Run the snake</Link>
      <Link className="nav-link px-2" style={{color: "darkseagreen" , fontSize: "large"}} to={"./TheMapView"}>The map view</Link>
      <Link className="nav-link px-2" style={{color: "darkseagreen" , fontSize: "large"}} to={"./UserManual"}>User manual</Link>

      </div>

      <div className="col-md-3 text-end">
      <Link className= 'btn btn-primary' style={{backgroundColor: "darkseagreen",border: "black"}} to={"../SignIn"}>Output</Link>
      </div>
    </header>
    <Outlet />
  </div>  );
}