import React, { Component } from "react";
import ProductService from "../services/product.service";

import { withRouter } from '../common/with-router';

class Product extends Component {
    constructor(props) {
        super(props);

        this.state = {
            product: {},
        };
    }

    componentDidMount() {

        ProductService.getProduct(this.props.router.params.id).then(
            response => {
                this.setState({
                    product: response.data
                });
            },
        );
    }

    render() {
        return (
            <div className="container">
                <h3>Title: {this.state.product.title}</h3>
                <p>Price: {this.state.product.price}</p>
                <p>Description: {this.state.product.description}</p>
            </div >
        );
    }
}

export default withRouter(Product);
