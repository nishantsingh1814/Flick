import React, { PropTypes, Component } from 'react';

import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import { signout } from '../../actions/signout';
import { Redirect} from 'react-router-dom';

class Header extends Component{
  constructor(props){
    super(props)
  }

  signOut(){
      this.props.signout()
  }
  render(){
    if (!this.props.loggedIn) {
        return <Redirect to={'/'}/>
    }else{
      return(
        <header className="header">
          <div className="g-row">
            <div className="g-col">
              <h1 className="header__title">Flick</h1>

              <ul className="header__actions">
                 <li><button className="btn" onClick={this.signOut.bind(this)}>Sign out</button></li>
              </ul>
            </div>
          </div>
        </header>
      )
    }
  }
}
function mapDispatchToProps(dispatch) {
    return bindActionCreators({signout}, dispatch);
}

function mapStateToProps(state) {
    return {
        loggedIn: state.login.logged_in
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Header);
