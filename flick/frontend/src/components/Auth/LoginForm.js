import React, { Component, PropTypes } from 'react';
import '../../css/login.css';
import { Link } from 'react-router-dom';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import { login } from '../../actions/login';
import { Redirect} from 'react-router-dom';
import { revertsignup } from '../../actions/revertsignup';

class LoginForm extends Component {


  constructor(props) {
    super(props);
    this.props.revertsignup();
    this.state = {user : {"username":"","password":""}};
    this.onSubmit = this.onSubmit.bind(this);
  }

  clearInput() {
    this.setState({user : {}});
  }

  handleChange(propertyName, event) {
      const user = this.state.user;
      user[propertyName] = event.target.value;
      this.setState({user: user });
  }

  onSubmit(event) {
    event.preventDefault();
    const login = this.state.user.username.trim();
    const password = this.state.user.password.trim();
    this.props.login(login, password);
  }

  render() {
    if (this.props.loggedIn) {
        return <Redirect to={'/group'}/>
    } else {
    return (

          <div id="root">

            <main className="main">
              <div className="container">
                <div id="login">
                  <form className="login-form" onSubmit={this.onSubmit}>
                    <span className="icon fa fa-user">

                    </span>
                    <input className= "field-input"
                      autoFocus
                      maxLength="25"
                      onChange={this.handleChange.bind(this, 'username')}
                      placeholder="Username"
                      type="Username"
                      value={this.state.user.username}
                      required
                      />
                    <span className="icon fa fa-lock">

                    </span>
                    <input className ="field-input" autoComplete="off"
                      maxLength="25"
                      onChange={this.handleChange.bind(this, 'password')}
                      placeholder="Password"
                      type="password"
                      value={this.state.user.password}
                      required
                       />
                    <input id="submit" type="submit" value="Log in" />
                  </form>
                  <Link to="/signup">Sign Up</Link>
                </div>
              </div>
            </main>
          </div>
        );
      }
  }
}
function mapDispatchToProps(dispatch) {
    return bindActionCreators({login, revertsignup}, dispatch);
}

function mapStateToProps(state) {
    return {
        loggedIn: state.login.logged_in
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginForm);
