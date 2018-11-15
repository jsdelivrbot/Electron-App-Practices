import React, {Component} from 'react';
import {connect} from 'react-redux';
import {fetchWeather} from '../actions/index'
import { bindActionCreators } from 'redux';

class SearchBar extends Component{
    constructor(props){
        super(props);

        this.state = {term : ''}
    }
    onInputChange(event){
        this.setState({term:event.target.value});
       // console.log(event.target.value);
    }
    onFormSubmit(event){
        event.preventDefault();

        //we need to go and fetch weather data

        this.props.fetchWeather(this.state.term);
        this.setState({term:""});

    }
    render(){
       return (
        <form className="input-group" onSubmit={this.onFormSubmit.bind(this)}>
            <input 
            placeholder="get a five-day forecast in your favorite cities" 
            className="form-control"
            value={this.state.term}
            onChange={this.onInputChange.bind(this)}
            />
            <span className="input-group-btn">
                <button type="submit" className="btn btn-secondary" >Submit</button>
            </span>
        </form>);
    }
}

function mapDispatchToProps(dispatch){
    return bindActionCreators({fetchWeather}, dispatch);
}

export default connect(null, mapDispatchToProps)(SearchBar);