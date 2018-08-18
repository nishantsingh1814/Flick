import React, {Component} from "react";
import ReactDOM from "react-dom";
import {Provider} from 'react-redux';
import {BrowserRouter, Switch, Route, Redirect,} from 'react-router-dom';
import Group from '../components/Group/Group';
import LoginForm from './Auth/LoginForm';
import SignUpForm from './Auth/SignUpForm';

import Gallery from '../components/Gallery/Gallery';
import Photo from '../components/Photo/Photo';
import Overview from '../components/Overview/Overview';


import configureStore from '../store';

import HeaderLayout from "../layouts/header";
import PublicLayout from "../layouts/public";



const HeaderRoute = ({component: Component, ...rest}) => {
    return (
        <Route
            {...rest}
            render={matchProps => (
                <HeaderLayout>
                    <Component {...matchProps} />
                </HeaderLayout>
            )}
        />
    );
};

const PublicLayoutRoute = ({component: Component, ...rest}) => {
    return (
        <Route
            {...rest}
            render={matchProps => (
                <PublicLayout>
                    <Component {...matchProps} />
                </PublicLayout>
            )}
        />
    );
};

class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <Switch>
            <Route exact path="/">
                <Redirect to="/login"/>
            </Route>
            <HeaderRoute exact path="/group" component={Group}/>
            <HeaderRoute exact path="/photo/:id" component={Photo}/>
            <HeaderRoute exact path="/overview" component={Overview}/>
            <PublicLayoutRoute exact path="/login" component={LoginForm}/>
            <HeaderRoute exact path="/gallery/:id" component={Gallery}/>
            <PublicLayoutRoute exact path="/signup" component={SignUpForm}/>

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
