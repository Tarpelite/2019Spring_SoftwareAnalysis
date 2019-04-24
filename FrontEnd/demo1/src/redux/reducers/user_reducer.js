const user_reducer=(state={username:"",usertype:0},action)=>{
    switch (action.type) {
        case "user_login":return{...state,loginflag:true}
        case "user_quit":return{...state,loginflag:false}
        default: return state
    }
}
export default user_reducer