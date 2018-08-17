import React, {Component} from "react";
import ReactDOM from "react-dom";
import {Provider} from 'react-redux';
import {BrowserRouter, Switch, Route, Redirect,} from 'react-router-dom';
import Group from '../components/Group/Group';
import LoginForm from './Auth/LoginForm';
import SignUpForm from './Auth/SignUpForm';

import Gallery from '../components/Gallery/Gallery';
import configureStore from '../store';

class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <Switch>
            <Route exact path="/">
                <Redirect to="/login"/>
            </Route>
            <Route exact path="/group" component={Group}/>
            <Route exact path="/login" component={LoginForm}/>
            <Route exact path="/gallery/:id" component={Gallery}/>
            <Route exact path="/signup" component={SignUpForm}/>

        </Switch>
      </BrowserRouter>
    );
  }
}
const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(
  <Provider store={configureStore()}>
    <App />
  </Provider>,
   wrapper
  ) : null;
