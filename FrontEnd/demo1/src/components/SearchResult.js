import React, { Component } from 'react';
import {Input, List, Skeleton, Avatar, Icon, Tag} from "antd";
import {connect} from "react-redux";
import axios from "axios"

const count = 3;

class SearchPage extends Component{

    search=(keyword)=>{
        this.props.loading();
        axios.get(`Http://127.0.0.1:8000/search/${this.props.user_id}`, {
            params: {
                keywords: keyword
            }})
    .then( (response) =>{
            console.log(response);
            this.props.set_res(response.data,keyword)
        })
            .catch(function (error) {
                console.log(error);
            })

    }
    //收藏方法
    star=(resource_id)=>{
        /*this.props.loading();*/
        axios.post(`Http://127.0.0.1:8000/star/${this.props.user_id}/`, {
                user_ID:this.props.user_id,
                resource_ID:resource_id
        })
            .then( (response) =>{
                console.log(response);

            })
            .catch(function (error) {
                console.log(error);
            })
    }
    componentDidMount() {
        this.search(this.props.keyword)
    }
    render() {
        return(<div>
            <Icon type="close" className={"close"} onClick={this.props.quit_search}  />
            <p>搜索框</p>
            <Input.Search
                placeholder="input search text"
                enterButton="Search"
                size="large"
                defaultValue={this.props.keyword}
                onSearch={value => {console.log(value);this.search(value)}}
                style={{width:'100%'}}
            />
            <h2>搜索结果</h2>
            <List
                className="demo-loadmore-list"
                /*bordered={true}*/
                /*loading={initLoading}*/
                itemLayout="horizontal"
                /*loadMore={loadMore}*/
                dataSource={this.props.result_list}
                renderItem={item => (
                    <List.Item actions={[<a>加入购物车</a>,
                        <a onClick={()=>{console.log(item);this.star(item.resource_ID)}}>{item.is_star?<Icon type={"star"}theme={"filled"} />:<Icon type={"star"} />}</a>]}>
                        <Skeleton avatar title={false} loading={item.loading} active>
                            <p>{item.rank}</p>
                            <List.Item.Meta
                                /*avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}*/
                                title={<a href={item.url}>{item.title}</a>}
                                description={<div> <p>{`简介：${item.intro}`}</p></div>}
                            />
                            <a href={item.url} target="_Blank" style={{margin:"10px",padding:"10px"}}>{item.authors}</a>
                            <Tag color={'geekblue'} >文章类型</Tag>
                            <div><p>价格：{item.price}</p></div>

                        </Skeleton>
                    </List.Item>
                )}
            />
            <button onClick={()=>this.search(3)}>获取3条后台get的数据</button>
        </div>)
    }

}

function mapStateToProps(state)
{
    return{
        dissearch_flag:state.search.dis_flag,
        result_list:state.search.search_result_list,
        keyword:state.search.keyword,
        user_id:state.login.user_id
    }
}

function mapDispatchToProps(dispatch){
    return{

        dis_res:()=>{dispatch({type:"search"})},
        init:()=>{dispatch({type:"search_init"})},
        set_res:(list,keyword)=>{dispatch({type:"search_load",list:list,keyword:keyword})},
        quit_search:()=>{dispatch({type:"quit_search"})},
        loading:()=>{dispatch({type:"search_loading"})}
    }
}
SearchPage=connect(mapStateToProps,mapDispatchToProps)(SearchPage)
export default SearchPage;