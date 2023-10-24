import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './styles.css';
import logo from '../../logo.svg';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <div className="navbar">
      <div style={{display: 'flex', alignItems: 'center'}}>
        <div className="hamburger" onClick={toggleMenu}>
          <div className={`bar ${isMenuOpen ? 'open' : ''}`}></div>
          <div className={`bar ${isMenuOpen ? 'open' : ''}`}></div>
          <div className={`bar ${isMenuOpen ? 'open' : ''}`}></div>
        </div>
        <div className={`menu ${isMenuOpen ? 'open' : ''}`}>
          <a href="/page1" style={{color: "#00585E"}}>Vendas</a>
          <a href="/page2" style={{color: "#00585E"}}>Comissões</a>
        </div>
        <Link to="/"><img src={logo} alt='Logo'/></Link>
      </div>
      <div style={{ flex: 1, textAlign: 'center' }}>
        <h1 style={{color: '#00585E'}}>Vendas</h1>
      </div>
    </div>
  );
};

export default Navbar;