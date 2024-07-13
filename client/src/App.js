import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import MoveRobut from './componenta/MoveRobut';
import UserManual from './componenta/UserManual.js';
import RunTheSnake from './componenta/RunTheSnake.js';
import TheMapView from './componenta/TheMapView.js';
import SignIn from './componenta/SignIn';
import Not_fount from './componenta/Not_fount';
import { Enter } from './componenta/Enter';
import Home from './componenta/Home.js';
import ImageGallery from './componenta/ImageGallery';
import { ImageProvider } from './componenta/ImageContext.js';

function App() {
  return (
    <ImageProvider>
      <Routes>
        <Route index element={<Navigate to="./SignIn" />} />
        <Route path="Enter" element={<Enter />}>
          <Route path="UserManual" element={<UserManual />} />
          <Route index element={<Home />} />
          <Route path="RunTheSnake" element={<RunTheSnake />} />
          <Route path="TheMapView" element={<TheMapView />} />
          <Route path="ImageGallery" element={<ImageGallery />} />
        </Route>
        <Route path="SignIn" element={<SignIn />} />
        <Route path="*" element={<Not_fount />} />
      </Routes>
    </ImageProvider>
  );
}

export default App;
