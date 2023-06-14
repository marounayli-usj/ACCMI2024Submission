import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from './Home';
import WebTestsComponent from './WebTests';

function App() {


  return (
    <Router>
      <div>
        <Routes>
        <Route exact path="/" element={<Home/>}/>
        <Route exact path="/tests" element={<WebTestsComponent/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
