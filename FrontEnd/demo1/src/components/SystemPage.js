import React, { Component } from 'react';
import { Layout, Menu, Icon,Avatar } from 'antd';
import routes, {routes2} from "../routes";
import {BrowserRouter as Router,Route,Link}from "react-router-dom"
import {close_regaction, quit_action} from "../redux/actions/reg_action";
import {connect} from "react-redux";
import {Redirect }from "react-router-dom"
import "../css/SysPage.css"

const { Header, Sider, Content } = Layout;
class SystemPage extends Component{
    constructor(props) {
        super(props);

    }
    state = {
        collapsed: false,
    };

    toggle = () => {
        this.setState({
            collapsed: !this.state.collapsed,
        });
    }
    render() {
        if (!this.props.loginflag)
        {
            return<Redirect to={"/"}/>
        }
        return(<div>
            <Layout style={{height:"100%",minHeight:"720px",background: "rgb(32,96,79)"}}>
                <Sider
                    trigger={null}
                    collapsible
                    collapsed={this.state.collapsed}
                    style={{background: "rgb(32,96,79)",height:"100%"}}
                >
                    <div className="logo" />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']} style={{background: "rgb(32,96,79)"}}>
                        <Avatar shape="square" size={64} icon="user" style={{display:"inline-block",margin:"10px"}}/>
                        <br/>

                        <p style={{padding:"10px"}}>{`${this.props.username}你好`}</p>
                        <a onClick={this.props.quit}>注销登录</a>
                        <div style={{margin:"10%",padding:"10%"}}></div>
                        <Menu.Item key="1" >
                            <Link to={"/system/"}>
                            <Icon type="home"/>
                            <span >首页</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="2">
                            <Link to={"/system/personalinformation"}>
                            <Icon type="user" />
                            <span>个人信息</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="3">
                            <Link to={"/system/star"}>
                            <Icon type="star" />
                            <span>我的收藏</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="4" >
                            <Link to={"/system/account"}>
                            <Icon type="wallet" />
                            <span>我的账户</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="5" >
                            <Link to={"/system/resources"}>
                                <Icon type="read" />
                                <span>已购资源</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="6"disabled={!this.props.is_expert} title={ this.props.is_expert? "": "此功能只向专家用户开放"}>
                            <Link to={"/system/account"}>
                                <Icon type="solution" />
                                <span>个人门户</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="7" >
                            <Link to={"/system/shopcar"}>
                                <Icon type="shopping-cart" />
                                <span>购物车</span>
                            </Link>
                        </Menu.Item>
                    </Menu>
                </Sider>
                <Layout>
                    <Header style={{ background: '#ffffff', padding: 0 }}>
                        <Icon
                            className="trigger"
                            type={this.state.collapsed ? 'menu-unfold' : 'menu-fold'}
                            onClick={this.toggle}
                        />
                    </Header>
                    <Content style={{
                        margin: '24px 16px', padding: 24, background: '#fff', minHeight: 280
                    }}
                    >
                        {
                            routes2.map((route,key)=>{
                        if(route.exact){
                            return <Route key={key} exact path={route.path} component={route.component} />
                        }
                        else {
                            return <Route key={key}  path={route.path} component={route.component} />
                        }
                        })
                        }
                    </Content>
                </Layout>
            </Layout>

        </div>)
    }

}


function mapStateToProps(state)
{
    return{
        loginflag:state.login.loginflag,
        username:state.login.username,
        is_expert:state.login.is_expert
    }
}

function mapDispatchToProps(dispatch){
    return{

        quit:()=>{dispatch(quit_action)},

    }
}
SystemPage=connect(mapStateToProps,mapDispatchToProps)(SystemPage)
export default SystemPage;