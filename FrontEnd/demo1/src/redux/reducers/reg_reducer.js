import regaction from "../actions/reg_action";

const regreducer = ( state={regflag:false},action) => {
    switch(action.type) {
        case "reg":
            return{
                ...state,
            regflag: true
            }
        case "close_reg":
            return{
                ...state,
                regflag: false
            }
        default:return state
    }
    // if(action=={type:"reg"})
    //     return{
    //         ...state,
    //         regflag: true
    //     }
    // else return state
}
export default regreducer