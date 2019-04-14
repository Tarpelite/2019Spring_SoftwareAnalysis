import React, { Component } from 'react';
import {Button, Col, Row, Statistic} from "antd";

class MyAccount extends Component{
    constructor(props) {
        super(props);

    }

    render() {
        return(<div>
<p>我的账户</p>
            <Row gutter={16}>
                <Col span={12}>
                    <Statistic title="积分" value={112893} />
                </Col>
                <Col span={12}>
                    <Statistic title="用户余额 (CNY)" value={112893} precision={2} />
                    <Button style={{ marginTop: 16 }} type="primary">Recharge</Button>
                </Col>
            </Row>
        </div>)
    }

}

export default MyAccount;