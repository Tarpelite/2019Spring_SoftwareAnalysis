const login_reducer=(state={loginflag:false},action)=>{
    switch (action.type) {
        case "login":return{...state,loginflag:true}
        case "quit":return{...state,loginflag:false}
        default: return state
    }
}
export default login_reducer