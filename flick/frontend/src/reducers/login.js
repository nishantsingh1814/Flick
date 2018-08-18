import * as actionTypes from '../actionTypes';

export default function (state = {}, action) {
    switch (action.type) {
        case actionTypes.LOGIN_SUCCESS:
            return {
                ...state, 'logged_in': true
            };
        case actionTypes.LOGIN_FAILED:
            return {
                ...state, 'logged_in': false
            };
        case actionTypes.SIGN_OUT:
            return {
                ...state, 'logged_in': false
            };
        default:
            return state;
    }
}
