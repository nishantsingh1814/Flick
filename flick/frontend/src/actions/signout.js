import * as actionTypes from '../actionTypes';

export function signout(){
  return (dispatch) => {
    dispatch({
      type:  actionTypes.SIGN_OUT
    })
  }
}
