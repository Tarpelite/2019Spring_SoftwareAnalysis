import React, { Component } from 'react';
import { Input,Carousel,Card, Col, Row } from 'antd';
import "../css/Home.css"
import {connect} from "react-redux";
import SearchPage from "./SearchResult";

class Home extends Component{
    constructor(props) {
        super(props);
        this.props.init();
    }

search=(value)=>{
    console.log(value);
    //非空检查
    if(value!="")
    this.props.dis_res(value)
    else console.log("搜索框的输入不能为空")
}
    render() {
        if (this.props.dissearch_flag)
        {
            return(<div>
                <SearchPage/>
                <p>搜索结果</p>

            </div>)
        }
        return(<div style={{/*background: '#ECECEC'*/}}>


                <h2>资源检索</h2>
            <Input.Search
                placeholder="这里是搜索测试，请输入你想获取几条数据，必须是数字"
                enterButton="Search"
                size="large"
                onSearch={value => this.search(value)}
                style={{width:'80%'}}
            />
            <h2>资讯推荐</h2>
            <Carousel autoplay>
                <div className={"zhenjing"}><h3>1震惊！99.99%的人都不知道的死法！</h3></div>
                <div className={"zhenjing2"}><h3>2深度揭秘！美国总统看到后都惊呆了！</h3></div>
                <div className={"zhenjing3"}><h3>3全世界80万人疯传的机器学习算法</h3></div>
                <div><h3>4不敢相信！动态调控元件在微生物学中竟有这种应用</h3></div>
            </Carousel>
            <br/>
            <div style={{  padding: '30px' }}>
                <Row gutter={16}>
                    <Col span={12}>
                        <Card title="学术动态" bordered={false}>

                            <a ref={""}>震惊！99.99%的人都不知道的死法！</a>
                        </Card>
                    </Col>
                    {/*<Col span={8}>
                        <Card title="Card title" bordered={false}>Card content</Card>
                    </Col>*/}
                    <Col span={12}>
                        <Card title="热搜排名" bordered={false}>Card content</Card>
                    </Col>
                </Row>
            </div>
        </div>
        )
    }
}

function mapStateToProps(state)
{
    return{
        dissearch_flag:state.search.dis_flag,
    }
}

function mapDispatchToProps(dispatch){
    return{

        dis_res:(keyword)=>{dispatch({type:"search",keyword:keyword})},
init:()=>{dispatch({type:"search_init"})}
    }
}
Home=connect(mapStateToProps,mapDispatchToProps)(Home)
export default  Home;