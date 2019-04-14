import React, { Component } from 'react';
import { Layout, Menu, Icon,Avatar } from 'antd';
import routes from "../routes";
import {BrowserRouter as Router,Route,Link}from "react-router-dom"
import Home from "./Home";
import PersonalInformation from "./PersonalInformation";
import MyAccount from "./MyAccount";
import MyResources from "./MyResources";
import logo from '../image/logo.png';
import {close_regaction, quit_action} from "../redux/actions/reg_action";
import {connect} from "react-redux";
import {Redirect }from "react-router-dom"


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
                    style={{background: "rgb(32,96,79)"}}
                >
                    <div className="logo" />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']} style={{background: "rgb(32,96,79)"}}>
                        <Avatar shape="square" size={64} icon="user" style={{display:"inline-block",margin:"10px"}}/>
                        <br/>

                        <p style={{padding:"10px"}}>用户你好</p>
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
                            <Link to={"/system/resources"}>
                            <Icon type="upload" />
                            <span>我的收藏</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="4" >
                            <Link to={"/system/account"}>
                            <Icon type="user" />
                            <span>我的账户</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="5" >
                            <Link to={"/system/account"}>
                                <Icon type="user" />
                                <span>已购资源</span>
                            </Link>
                        </Menu.Item>

                        <Menu.Item key="6" >
                            <Link to={"/system/account"}>
                                <Icon type="user" />
                                <span>个人门户</span>
                            </Link>
                        </Menu.Item>
                        <Menu.Item key="7" >
                            <Link to={"/system/account"}>
                                <Icon type="user" />
                                <span>购物车</span>
                            </Link>
                        </Menu.Item>
                    </Menu>
                </Sider>
                <Layout>
                    <Header style={{ background: '#fff', padding: 0 }}>
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
                        Content
                        {/*<Router>*/}
                            <Route  exact path={"/system/"} component={Home} />
                            <Route  path={"/system/personalinformation"} component={PersonalInformation}/>
                            <Route path={"/system/account"} component={MyAccount} />
                            <Route path={"/system/resources"} component={MyResources} />
                        {/*</Router>*/}
                    </Content>
                </Layout>
            </Layout>

        </div>)
    }

}


function mapStateToProps(state)
{
    return{
        loginflag:state.login.loginflag
    }
}

function mapDispatchToProps(dispatch){
    return{

        quit:()=>{dispatch(quit_action)},

    }
}
SystemPage=connect(mapStateToProps,mapDispatchToProps)(SystemPage)
export default SystemPage;