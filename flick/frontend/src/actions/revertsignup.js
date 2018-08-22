import * as actionTypes from '../actionTypes';

export function revertsignup(){
  return (dispatch) => {
    dispatch({
      type:  actionTypes.REVERT_SIGN_UP
    })
  }
}
