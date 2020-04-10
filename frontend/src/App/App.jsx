import React from 'react';
import { Route, Router, Switch, Link } from 'react-router-dom';
import { history } from '@/_helpers';
import { HomePage } from '@/HomePage';
import { TechnologyPage } from '@/TechnologyPage';

class App extends React.Component {
  logout() {
    history.push('/login');
  }

  render() {
    return (
      <Router history={history}>
        <div>
          <nav className="navbar navbar-expand navbar-dark bg-dark">
            <div className="navbar-nav">
                <Link to="/"  className="nav-item nav-link">Home</Link>
                <Link to="/oportunity" className="nav-item nav-link">Oportunity</Link>
                <Link to="/candidate" className="nav-item nav-link">Candidate</Link>
                <Link to="/technology" className="nav-item nav-link">Technology</Link>
                <a onClick={this.logout} className="nav-item nav-link">Logout</a>
            </div>
          </nav>
        </div>
        <Switch>
          <Route exact path='/' component={HomePage}/>
          <Route path='/oportunity' component={OportunityPage}/>
          <Route path='/candidate' component={CandidatePage}/>
          <Route path='/technology' component={TechnologyPage}/>
        </Switch>
      </Router>
    );
  }
}


function OportunityPage() {
  return (
    <div className="container">
      <h2>Oportunity!</h2>
    </div>
  );
}

function CandidatePage() {
  return (
    <div className="container">
      <h2>Candidate!</h2>
    </div>
  );
}

export {App};
