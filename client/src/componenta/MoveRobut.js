import axios from "axios";
import { User } from "./user";
import { useNavigate } from "react-router-dom";
import { getAllUser } from "./user";
import { saveUser } from "./user";
import { useEffect, useState } from "react";

export default function MoveRobut() {
  const [flag, setflag] = useState(1);
  useEffect(() => {
    if (flag) {
      drowInCanvas(pointsArray, weaponArray);
      setflag(0);
    }
  }, []);
  let data = getPoint();
  let pointsArray = data[0];
  let weaponArray = data[1];

  // let pointsArray =   [ { x: 15, y: 25 },
  // { x: 48, y: 220 },
  // { x: 70, y: 90 },
  // { x: 15, y: 160 },
  // { x: 35, y: 340 }]
  // let pointsArray = [
  //   [80, 0],
  //   [80, 100],
  //   [20, 0],
  //   [20, 100],
  // ];
  // let weaponArray = [
  //   { x: 15, y: 25 },
  //   { x: 48, y: 220 },
  //   { x: 70, y: 90 },
  //   { x: 15, y: 160 },
  //   { x: 35, y: 340 },
  // ];

  return (
    <div className="canvas">
      <canvas
        height={730}
        width={1102}
        id="myCanvas"
        onLoad={() => drowInCanvas(pointsArray)}
      ></canvas>
      {/* <input type="button" value='לחץ לתצוגה' onClick={() => drowInCanvas(pointsArray, weaponArray)} readOnly /> */}
    </div>
  );
}

function drowInCanvas(pointsArray, weaponArray) {
  console.log(getPoint());

  // const pageWidth = 551;
  const pageWidth = 400;

  const pageHeight = 0;
  const a = 1;
  let c = document.getElementById("myCanvas");
  let ctx = c.getContext("2d");
  ctx.beginPath();
  for (let i = 0; i < pointsArray.length; i += 2) {
    ctx.moveTo(
      pointsArray[i][0] * a + pageWidth,
      pointsArray[i][1] * a + pageHeight
    );
    ctx.lineTo(
      pointsArray[i + 1][0] * a + pageWidth,
      pointsArray[i + 1][1] * a + pageHeight
    );
    ctx.stroke();
  
  }
;
  ctx.closePath();

  for (let i = 0; i < weaponArray.length; i++) {
    ctx.fillStyle = "red";

    // Start drawing the red dot
    ctx.beginPath();
    ctx.arc(
      weaponArray[i][0] + pageWidth,
      weaponArray[i][1]  + pageHeight,
      2,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }
  ctx.closePath();
  return;
}
export function getPoint() {
  let arr = localStorage.getItem("arrPoint");
  return JSON.parse(arr);
}
