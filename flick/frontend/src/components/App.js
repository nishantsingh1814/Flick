import React, {Component} from "react";
import ReactDOM from "react-dom";
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Group from '../components/Group/Group';

import Gallery from '../components/Gallery/Gallery';



class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <Switch>

            <Route exact path="/" component={Group}/>
            <Route exact path="/gallery/:id" component={Gallery}/>

        </Switch>
      </BrowserRouter>
    );
  }
}
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
