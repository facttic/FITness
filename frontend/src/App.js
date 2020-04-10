import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <Switch>
            <Route exact path='/' component={Home}/>
            <Route path='/oportunity' component={Oportunity}/>
            <Route path='/candidate' component={Candidate}/>
            <Route path='/technology' component={Technology}/>
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

function Home() {
  return (
    <div className="container">
      <h2>Bienvenidxs a FITness!</h2>
      <p>Esta es una aplicación para cargar oportunidades de trabajo para el FIT.</p>
    </div>
  );
}
function Candidate() {
  return (
    <div className="container">
      <h2>Candidate!</h2>
    </div>
  );
}
function Technology() {
  return (
    <div className="container">
      <h2>Technology!</h2>
    </div>
  );
}
function Oportunity() {
  return (
    <div className="container">
      <h2>Oportunity!</h2>
    </div>
  );
}

export default App;
