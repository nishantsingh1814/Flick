import * as actionTypes from '../../actionTypes';

export function signup(username, password){
  var formData  = new FormData();
  formData.append('user_name', username)
  formData.append('password', password)
  return (dispatch) => {

      fetch('/signup/', {
       method: 'post',
       body:formData
     }).then(response => {
       if (response.status !== 200) {
         dispatch({
             type:  actionTypes.SIGN_UP_FAILED ,
         })
       }
       return response.json();
     })
     .then(
       data =>{
         if(data.status==200){
           dispatch({
             type:  actionTypes.SIGN_UP_SUCCESS ,
             payload: data
           })
         }else{
           dispatch({
               type:  actionTypes.SIGN_UP_FAILED ,
           })
         }
       }
     );
    }
}
