import {FETCH_WEATHER} from '../actions/index';

export default function(state= [], action){
    //console.log("Action received:" , action);
    switch(action.type){
        case FETCH_WEATHER:
            // never mutate data in state 
            //rather make a new array
            return  [action.payload.data , ...state]; // concat data 
    }
    return state;
}
