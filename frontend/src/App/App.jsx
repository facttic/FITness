import React from 'react';
import { Route, Router, Switch, Link } from 'react-router-dom';
import { history } from '@/_helpers';
import { HomePage } from '@/HomePage';
import { TechnologyPage } from '@/TechnologyPage';
import { CandidatePage } from '@/CandidatePage';
import { CooperativePage } from '@/CooperativePage';
import { OpportunityPage } from '@/OpportunityPage';

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
                <Link to="/cooperative" className="nav-item nav-link">Cooperativas</Link>
                <Link to="/opportunity" className="nav-item nav-link">Oportunidades</Link>
                <Link to="/candidate" className="nav-item nav-link">Perfiles</Link>
                <Link to="/technology" className="nav-item nav-link">Tecnologias</Link>
                {/* <a onClick={this.logout} className="nav-item nav-link">Logout</a> */}
            </div>
          </nav>
        </div>
        <Switch>
          <Route exact path='/' component={HomePage}/>
          <Route path='/cooperative' component={CooperativePage}/>
          <Route path='/opportunity' component={OpportunityPage}/>
          <Route path='/candidate' component={CandidatePage}/>
          <Route path='/technology' component={TechnologyPage}/>
        </Switch>
      </Router>
    );
  }
}

export {App};
