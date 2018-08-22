import * as actionTypes from '../../actionTypes';

export function login(username, password){
  var formData  = new FormData();
  formData.append('user_name', username)
  formData.append('password', password)
  return (dispatch) => {

      fetch('/login/', {
       method: 'post',
       body:formData
     }).then(response => {
       if (response.status !== 200) {
         dispatch({
             type:  actionTypes.LOGIN_FAILED ,
         })
       }
       return response.json();
     })
     .then(
       data =>{
         if(data.status==200){
             localStorage.setItem("Username",username)
             localStorage.setItem("Token",data.token)
             dispatch({
               type:  actionTypes.LOGIN_SUCCESS ,
               payload: data,
             })
         }
     }
     );
    }
}
