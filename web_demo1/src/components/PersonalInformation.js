import React, { Component } from 'react';
import { Statistic, Row, Col, Button } from 'antd';

class PersonalInformation extends Component{
    constructor(props) {
        super(props);

    }


render()
{
    return(
    <Row gutter={16}>
        <Col span={12}>
            <Statistic title="积分" value={112893} />
        </Col>
        <Col span={12}>
            <Statistic title="用户余额 (CNY)" value={112893} precision={2} />
            <Button style={{ marginTop: 16 }} type="primary">Recharge</Button>
        </Col>
    </Row>
    )
}
}

export default PersonalInformation;