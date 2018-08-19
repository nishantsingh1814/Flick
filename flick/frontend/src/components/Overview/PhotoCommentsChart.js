import React, {Component} from "react";
import { Redirect} from 'react-router-dom';
import {PieChart} from 'react-easy-chart';
import '../../css/overview.css';

class PhotoCommentsChart extends Component{
  constructor(props){
    super(props)
    this.state={redirect:false}
    this.chartData = this.getChartData(this.props.data);
  }
  getChartData= (data) =>{
    const chartData = [];
    for(var i = 0; i < data.length-1; i++){
      let test = {};
      test.key = data[i].photo_id;
      test.value = data[i].comments_count;
      chartData.push(test);
    }
    let test = {}
    test.key = 'other';
    test.value = data[data.length-1].comments_count;
    chartData.push(test)
    return chartData;
  }

  render(){
    if (this.state.redirect) {
      return <Redirect push to={`/photo/${this.state.photoId}`} />;
    }
    return(
      <div id="top-photos-chart">
        <PieChart
          labels
          size={250}
          data ={this.chartData}
          clickHandler={(d) => d.data.key!=='other'?this.setState({redirect: true, photoId:d.data.key}):this.state={redirect:false}}
        />
        <h3>Top 9 photos with most Comments</h3>
      </div>
    )
  }
}

export default PhotoCommentsChart;
