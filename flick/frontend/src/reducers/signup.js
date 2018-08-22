import * as actionTypes from '../../actionTypes';

export default function (state = {}, action) {
    switch (action.type) {
        case actionTypes.SIGN_UP_FAILED:
            return {
                ...state, 'data': action.payload,
                'signedup':false
            };
        case actionTypes.SIGN_UP_SUCCESS:
            return {
              ...state, 'data': action.payload,
              'signedup':true
            };
        case actionTypes.REVERT_SIGN_UP:
            return {
              ...state, 'data': action.payload,
              'signedup':false
            };
        default:
            return state;
    }
}
