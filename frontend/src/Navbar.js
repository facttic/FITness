import React from 'react'
import {Link} from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="nav-wrapper teal">
      <div className="container">
        <a className="brand-logo">FITness</a>
        <ul className="right">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/technology/">Technology</Link></li>
          <li><Link to="/oportunity/">Oportunity</Link></li>
          <li><Link to="/cCandidate/">Candidate</Link></li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar