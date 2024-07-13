import { useEffect, useState } from "react";
import { getPoint } from "./point.js";
import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { ImageContext } from '../componenta/ImageContext.js';
import './components.css'
export default function TheMapView() {
  const [flag, setflag] = useState(1);

  useEffect(() => {
    if (flag) {
      drowInCanvas(pointsWalls, pointsMines, pointsAbducted, pointsTerrorists, pointsArrNumImg);
      setflag(0);
    }
  }, []);
  const navigate = useNavigate();
  const { setImageUrls } = useContext(ImageContext);
  const handleButtonClick = (arr) => {
    const newImageUrls = []
    for(let i = 0; i< arr.length;i++){
      const imageName = arr[i][0]; // Assuming arr is a defined array and i is an index
      const imagePath = `${process.env.PUBLIC_URL}/face/${imageName}.jpg`;
      
      let parameter = 'x: ' + arr[i][1][0] + ' y: ' + arr[i][1][1]
      newImageUrls.push({ url: imagePath, parameter: parameter })
    }
   

    setImageUrls(newImageUrls);
    navigate('/Enter/ImageGallery');
  };


  let data = getPoint();
  let pointsWalls = data[0];
  let pointsMines = data[1];
  let pointsAbducted = data[2];
  let pointsTerrorists = data[3];
  let pointsArrNumImg = data[4];
  
  return (
    <div className="canvas">
      <canvas
        height={600}
        width={1500}
        id="myCanvas"
        onLoad={() =>drowInCanvas(pointsWalls, pointsMines, pointsAbducted, pointsTerrorists, pointsArrNumImg)}
      ></canvas>
      <p id="text"></p>
      <div class="d-flex gap-2 justify-content-center py-5">
        <button onClick={() => updateTextarea(data[2], "Abducted", 'green')} class="badge bg-success-subtle border border-success-subtle text-success-emphasis rounded-pill">Abducted</button>
        <button onClick={() => updateTextarea(data[3], "Terrorists", 'red')} class="badge bg-danger-subtle border border-danger-subtle text-danger-emphasis rounded-pill">Terrorists</button>
        <button onClick={() => updateTextarea(data[1], "Mines", 'yellow')} class="badge bg-warning-subtle border border-warning-subtle text-warning-emphasis rounded-pill">Mines</button>
        <button onClick={() => handleButtonClick(data[4])} class="badge bg-primary-subtle border border-primary-subtle text-primary-emphasis rounded-pill">img</button>

    </div>
    </div>
  );
}

function updateTextarea(arr, text, color) {
  // document.getElementById('text').target.style.border = "solid, red, 2px;";
  if(arr.length)
    document.getElementById('text').innerText = arr.join('\n');
  else{
    document.getElementById('text').innerText = "No " + text + " were found";
  }
  // document.getElementById('text').style.border = `2px solid ${color}`;


}


function drowInCanvas(pointsWalls, pointsMines, pointsAbducted, pointsTerrorists,pointsArrNumImg ) {
  let c = document.getElementById("myCanvas");
  let ctx = c.getContext("2d");
  const pageWidth = 700;
  const pageHeight = 400;
  drowWall(pointsWalls, ctx, pageWidth, pageHeight);
  drowMines(pointsMines, ctx,pageWidth, pageHeight);
  drowAbducted(pointsAbducted, ctx, pageWidth, pageHeight);
  drowTerrorists(pointsTerrorists, ctx, pageWidth, pageHeight);
  return;
}

function drowWall(pointsWalls, ctx, pageWidth, pageHeight) {
  const a = 1;

  ctx.beginPath();
  for (let i = 0; i < pointsWalls.length; i += 2) {
    ctx.moveTo(
      pointsWalls[i][0] * a + pageWidth,
      pointsWalls[i][1] * a + pageHeight
    );
    ctx.lineTo(
      pointsWalls[i + 1][0] * a + pageWidth,
      pointsWalls[i + 1][1] * a + pageHeight
    );
    ctx.stroke();
  }
  ctx.closePath();
}

function drowMines(pointsMines, ctx, pageWidth, pageHeight) {
  for (let i = 0; i < pointsMines.length; i++) {
    ctx.fillStyle = "yellow";
    // Start drawing the red dot
    ctx.beginPath();
    ctx.arc(
      pointsMines[i][0] + pageWidth,
      pointsMines[i][1] + pageHeight,
      1.5,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }
  ctx.closePath();
}

function drowAbducted(pointsAbducted, ctx, pageWidth, pageHeight) {
  for (let i = 0; i < pointsAbducted.length; i++) {
    ctx.fillStyle = "green";
    // Start drawing the red dot
    ctx.beginPath();
    ctx.arc(
      pointsAbducted[i][0][0] + pageWidth,
      pointsAbducted[i][0][1] + pageHeight,
      1.5,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }
  ctx.closePath();
}
function drowTerrorists(pointsTerrorists, ctx, pageWidth, pageHeight) {
  for (let i = 0; i < pointsTerrorists.length; i++) {
    ctx.fillStyle = "red";
    // Start drawing the red dot
    ctx.beginPath();
    ctx.arc(
      pointsTerrorists[i][0] + pageWidth,
      pointsTerrorists[i][1] + pageHeight,
      1.5,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }
  ctx.closePath();
}

