import React, { Component } from 'react';
import { Card, Icon, Avatar } from 'antd';
import {quit_action} from "../redux/actions/reg_action";
import {connect} from "react-redux";

class PersonalInformation extends Component{
    constructor(props) {
        super(props);

    }


render()
{
    const { Meta } = Card;
    return(
        <Card
            style={{ width:"80%" ,margin:"auto"}}
            /*cover={<img alt="example" src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png" />}*/
            /*cover={<img alt="example" src="https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2897408807,1190668089&fm=27&gp=0.jpg" />}*/
            actions={[<a onClick={()=>alert("你将编辑个人资料")}> <Icon type="edit" /> 编辑</a>]}
        >
            <Meta
                avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
                title={`${this.props.username}的个人信息`}
                description="This is the description"
            />
            <hr/>
            <h2>学术动态</h2>
            <a ref={""}>震惊！99.99%的人都不知道的死法！</a><Icon type="star" />
        </Card>
    )
}
}


function mapStateToProps(state)
{
    return{
        username:state.login.username,
    }
}

function mapDispatchToProps(dispatch){
    return{

        quit:()=>{dispatch(quit_action)},

    }
}
PersonalInformation=connect(mapStateToProps,mapDispatchToProps)(PersonalInformation)
export default PersonalInformation;