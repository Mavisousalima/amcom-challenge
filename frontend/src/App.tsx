import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import SalesTable from './components/SalesTable';
import NewSale from './components/NewSale';

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<SalesTable/>} />
        <Route path="/new-sale" element={<NewSale/>} />
      </Routes>
    </Router>
  );
}

export default App;
