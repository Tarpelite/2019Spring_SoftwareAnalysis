import {combineReducers}from "redux"
import regreducer from "./reg_reducer";
import login_reducer from "./login_reducer";
import star_reducer from "./star_reducer";
import search_reducer from "./search_reducer";
const rootReducer=combineReducers({
    reg:regreducer,
    login:login_reducer,
    star:star_reducer,
    search:search_reducer
})
export default rootReducer