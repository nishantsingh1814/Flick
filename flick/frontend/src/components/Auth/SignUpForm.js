import React, { Component, PropTypes } from 'react';
import '../../css/login.css';
import { Link } from 'react-router-dom';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import { signup } from '../../actions/signup';
import { revertsignup } from '../../actions/revertsignup';
import { Redirect} from 'react-router-dom';

class SignUpForm extends Component {


  constructor(props, context) {
    super(props, context);

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
    this.props.signup(login, password);
  }

  render() {
    if(this.props.signedup){
      return <Redirect to={'/login'}/>
    }else{
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
                  <input id="sign_up" type="submit" value="Sign Up" />
                </form>
                <Link to="/login">Login</Link>
              </div>
            </div>
          </main>
        </div>
      );
    }
  }
}
function mapDispatchToProps(dispatch) {
    return bindActionCreators({signup}, dispatch);
}

function mapStateToProps(state) {
    return {
        signedup: state.signup.signedup
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(SignUpForm);
