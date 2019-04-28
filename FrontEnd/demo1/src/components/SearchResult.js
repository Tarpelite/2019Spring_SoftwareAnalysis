import React, { Component } from 'react';
import {Input,List,Skeleton,Avatar,Icon} from "antd";
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
        /*axios.get(`https://randomuser.me/api/?results=${keyword}&inc=name,gender,email,nat&noinfo`)
            .then( (response) =>{
                console.log(response);
                this.props.set_res(response.data.results,keyword)
            })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
                // always executed
            });*/
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
                    <List.Item actions={[<a>购买</a>, <Icon type={"star"}/>]}>
                        <Skeleton avatar title={false} loading={item.loading} active>
                            <List.Item.Meta
                                /*avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}*/
                                title={<a href={item.url}>{item.title}</a>}
                                description={<div><p>作者：</p> <a href={item.url} target="_Blank">{item.authors}</a></div>}
                            />
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