import React, { Component, PropTypes } from 'react';
import '../../css/login.css';
import { Link } from 'react-router-dom';


class LoginForm extends Component {


  constructor(props, context) {
    super(props, context);

    this.state = {user : {}};
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
    const login = this.state.user.email.trim();
    const password = this.state.user.password.trim();

  }

  render() {
    return (
      <div id="root">

        <main className="main">
          <div className="container">
            <div id="login">
              <form className="login-form">
                <span className="icon fa fa-user">

                </span>
                <input className= "field-input" type="text" placeholder="Username" name="username" required />
                <span className="icon fa fa-lock">

                </span>
                <input className ="field-input"type="password" placeholder="Password" name="password" required />
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

export default LoginForm;
