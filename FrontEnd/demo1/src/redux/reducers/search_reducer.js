
const search_reducer = ( state={dis_flag:false,search_result_list:[],keyword:""},action) => {
    switch(action.type) {
        case "search":
            return{
                ...state,
                dis_flag: true,
                keyword: action.keyword
            }
        case "search_init":return{
            ...state,
            dis_flag:false
        }
        case "search_load":{
            state.search_result_list.pop();
            return{
            ...state,
                search_result_list: action.list,
                keyword:action.keyword
        }}
        case "quit_search":return{
            ...state,
            dis_flag:false,
            search_result_list:[]
        }
        case "search_loading":{
            let temp_data=[]
            temp_data.push({loading:true,name:{}})
            return{
                ...state,
                search_result_list:state.search_result_list.concat(temp_data)
            }
        }
        default:return state
    }

}
export default search_reducer