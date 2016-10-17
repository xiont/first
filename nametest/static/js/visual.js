// JavaScript Document
//画布大小、
var width = 600;
var height = 340;
//var svg = d3.select("body")
//			.append("svg")
//			.attr("width",width)
//			.attr("height",height);
			
			
var svg = d3.select("body")
			.select(".content")
			.select("p")
			.append("svg")
			.attr("width",width)
			.attr("height",height);
//x的比例尺
var xScale=d3.scale.linear()
	.domain([0,12])
	.range([0,500]);
var yScale=d3.scale.linear()
	.domain([0,0])
	.range([0,300]);
//定义x轴
var xAxis = d3.svg.axis()
	.scale(xScale)
	.orient("bottom");
//定义y 轴
var yAxis = d3.svg.axis()
	.scale(yScale)
	.orient("left");
//添加x轴
svg.append("g")
  .attr("class","axis")
  .attr("transform","translate(50,90)")
  .call(xAxis); 
svg.append("g")
  .attr("class","axis")
  .attr("transform","translate(50,190)")
  .call(xAxis); 
 svg.append("g")
  .attr("class","axis")
  .attr("transform","translate(50,290)")
  .call(xAxis); 
  
        
//添加y轴
svg.append("g")
  .attr("class","axis")
  .attr("transform","translate(50,40)")
  .call(yAxis);
  
//csv处理  
//var dataset2=[];
//var data2time=[];
//d3.csv("test.csv",function(error,data){
//	 for(var i=0;i<data.length;i++)
 //     {
   //         dataset2.push(parseFloat(data[i].data2));
  //          data2time.push(parseFloat(data[i].time2));
   //   }
   // });

  
//var dataset1=[25,57.3,78.4,66.3,99,12,13];
//var dataset2=[34,67.3,38.4,86.3,29,99];
//var dataset3=[98,17.3,43.6,36.3,95.3,62];
//var data1time=[1,3,4,7,9,11,12];
//var data2time=[2,3,4,5,9,11];
//var data3time=[1,5,7,8,9,10];

//控制颜色
//var index = [1, 2, 3, 4, 5];
//var color = ["red", "blue", "green", "yellow", "black"];
//var ordinal = d3.scale.ordinal()
        //.domain(index)
        //.range(color);
//颜色渐变控制
var a = d3.rgb(220,220,220);    //红色  
var b = d3.rgb(0,0,220);    //绿色  
   
var compute = d3.interpolate(a,b);
var ordinal = d3.scale.linear()
		.domain([0,100])
		.range([0,1]);  

//var circle1 = svg.append("circle")
  //      .attr("cx", 100)
    //    .attr("cy", 100)
      //  .attr("r", 45)
        //.style("fill","green");

//在1秒（1000毫秒）内将圆心坐标由100变为300
//circle1.transition()
 //   .duration(1000)
 //   .attr("cx", 300);

  
var circle1 = svg.selectAll(".MyCircle")
			.data(dataset1)
			.enter()
			.append("circle")
			.attr("class","MyCircle")
			.attr("cx",  function(d,i){
			return data1time[i]*(500/12)+50})
            .attr("cy", 90)
            .attr("r", 5)
			.transition()
			.duration(2000)
    		.ease("linear")
   			.attr("cx", function(d,i){
			return data1time[i]*(500/12)+50})
			.attr("cy", 90)
   		    .style("fill",function(d,i){return compute(ordinal(dataset1[i]))})
    		.attr("r", function(d,i)
			{return dataset1[i]/2});
			
var circle2 = svg.selectAll(".MyCircle2")
			.data(dataset2)
			.enter()
			.append("circle")
			.attr("class","MyCircle2")
			.attr("cx", function(d,i){
			return data2time[i]*(500/12)+50})
            .attr("cy", 190)
            .attr("r", 5)
			.transition()
			.duration(3000)
    		.ease("linear")
   			.attr("cx", function(d,i){
			return data2time[i]*(500/12)+50})
			.attr("cy", 190)
   		    .style("fill",function(d,i){return compute(ordinal(dataset2[i]))})
    		.attr("r", function(d,i)
			{return dataset2[i]/2});
			
var circle3 = svg.selectAll(".MyCircle3")
			.data(dataset3)
			.enter()
			.append("circle")
			.attr("class","MyCircle3")
			.attr("cx", function(d,i){
			return data3time[i]*(500/12)+50})
            .attr("cy", 290)
            .attr("r", 5)
			.transition()
			.duration(4000)
    		.ease("linear")
   			.attr("cx", function(d,i){
			return data3time[i]*(500/12)+50})
			.attr("cy", 290)
   		    .style("fill",function(d,i){return compute(ordinal(dataset3[i]))})
    		.attr("r", function(d,i)
			{return dataset3[i]/2});


//与第一个圆一样，省略部分代码

//在2秒（2000毫秒）内将圆心坐标由100变为300
//将颜色从绿色变为红色
//将半径从45变成25
//过渡方式采用bounce（在终点处弹跳几次

//添加文字
   var text1 =svg
        .append("text")
        .attr("class","MyText")
        .attr("transform","translate(10,57)")
        .attr("x", 1)
        .attr("y",10)
        .attr("dx",10)
        .attr("dy",30)
        .text("团队1");
	var text2 =svg
        .append("text")
        .attr("class","MyText")
        .attr("transform","translate(10,157)")
        .attr("x", 1)
        .attr("y",10)
        .attr("dx",10)
        .attr("dy",30)
        .text("团队2");
		
	var text3 =svg
        .append("text")
        .attr("class","MyText")
        .attr("transform","translate(10,257)")
        .attr("x", 1)
        .attr("y",10)
        .attr("dx",10)
        .attr("dy",30)
        .text("团队3");
	var text =svg
        .append("text")
        .attr("class","MyText2")
        .attr("transform","translate(280,0)")
        .attr("x", 1)
        .attr("y",30)
        .attr("dx",10)
        .attr("dy",0)
        .text("团队行为可视化摸型");