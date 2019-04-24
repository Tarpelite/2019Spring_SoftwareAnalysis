import React, { Component } from 'react';
import './App.css';
import {BrowserRouter as Router,Route,Link}from "react-router-dom"
import {routes} from "./routes";


class App extends Component {
  render() {
    return (
      <div className="App" >
        <Router>
          {
            routes.map((route,key)=>
            {
              if (route.exact)
              {
                return <Route key={key} exact path={route.path} component={route.component}/>
              }else {
                return <Route key={key} path={route.path} component={route.component}/>
              }
            })
          }
        </Router>
      </div>
    );
  }
}

export default App;
