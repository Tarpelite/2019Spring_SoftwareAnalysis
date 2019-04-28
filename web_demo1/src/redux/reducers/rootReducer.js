import {combineReducers}from "redux"
import regreducer from "./reg_reducer";
import login_reducer from "./login_reducer";
const rootReducer=combineReducers({
    reg:regreducer,
    login:login_reducer
})
export default rootReducer