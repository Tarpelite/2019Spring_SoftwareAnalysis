import {createStore,compose,applyMiddleware} from "redux"
import thunk from "redux-thunk"
import regreducer from "../reducers/reg_reducer";
import rootReducer from "../reducers/rootReducer";

export const store=createStore(rootReducer,
    compose(
        applyMiddleware(...[thunk]), // 需要使用的中间件数组
        window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    ))
