const shopcar_reducer = ( state={data:[],selectedRowKeys:[]},action) => {
    switch(action.type) {
        case "get_shopcar"://从服务器将购物车全部覆盖本地数据的操作，需要把selectrowkey一起删掉
        {
            let newdata = [];
            for (let i = 0; i < 20; i++) {
                newdata.push({
                    key: i,
                    name: `资源 ${i}`,
                    type:"论文",
                    author: `作者. ${i}`,
                    url:"https://www.jianshu.com/p/9cc2f7696300?from=timeline&isappinstalled=0",
                    author_url:"http://space.bilibili.com/123938419/"
                });
            }
            return{
                ...state,
                data: newdata,
                selectedRowKeys:[]
            }
        }
        case "multidelete_shopcar":
        {
            let newdata=state.star_data.filter(item => state.selectedRowKeys.indexOf(item.key)=== -1);
            return{
                ...state,
                star_data:newdata,
                selectedRowKeys: []
            }
        }
        case "delete_shopcar":
        {
            let newdata=state.star_data.filter(item => item.key!==action.itemkey);
            return{
                ...state,
                star_data:newdata,
                selectedRowKeys:[]
            }
        }
        case "set_shopcar_selectedRowKeys":
        {
            return{
                ...state,
                selectedRowKeys:action.selectedRowKeys
            }
        }
        default:return state
    }

}

export default shopcar_reducer