import React from 'react';
import { Route, HashRouter as Router, Routes, BrowserRouter } from "react-router-dom";
import MainPage from './pages/Main.tsx';
import SignInPage from './pages/SignIn.tsx';
import ProfilerPage from './pages/Profiler.tsx';

export interface IApplicationProps { }

const Application: React.FunctionComponent<IApplicationProps> = (props) => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<SignInPage />} />
        <Route path="/main" element={<MainPage />} />
        <Route path="/signup" element={<ProfilerPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Application;