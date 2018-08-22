import * as actionTypes from '../../actionTypes';

export function signout(){
  return (dispatch) => {
    localStorage.removeItem('Token');
    localStorage.removeItem('Username')
    dispatch({
      type:  actionTypes.SIGN_OUT
    })
  }
}
