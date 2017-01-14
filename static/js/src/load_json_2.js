$(function() {
	var seriesOptions = [],
		yAxisOptions = [],
		seriesCounter = 0,
		names = ['KPI_1'];
	
	var path = "50CA3DFB510CC5A8F28B48D1BF2A5702/MQL4/Files/json/";
	$.each(names, function(i, name) {
	
		$.getJSON(path+ name.toLowerCase() +'.json',	function(result) {
			
			var data = result;

	

			// As we're loading the data asynchronously, we don't know what order it will arrive. So
			// we keep a counter and create the chart when all the data is loaded.
			seriesCounter++;

			if (seriesCounter == names.length) {
			
				//document.getElementById("data1").innerHTML='<h1>'+result.avg_profit*100+'%</h1>'
				//document.getElementById("data2").innerHTML='<h1>'+result.avg_profit_week*100+'%</h1>'
				//document.getElementById("data3").innerHTML='<div class="progress"><div class="progress-bar progress-bar-success" style="width:'+result.success*100+'%"><span >'+result.success*100+'%</span></div><div class="progress-bar progress-bar-warning progress-bar-striped" style="width: '+(1-result.success)*100+'%"><span >'+(1-result.success)*100+'%</span></div></div><div class="progress"><div class="progress-bar progress-bar-success" style="width:'+result.success_profit*100+'%"><span>'+result.success_profit*100+'%</span></div><div class="progress-bar progress-bar-warning progress-bar-striped" style="width:'+(1-result.success_profit)*100+'%"><span >'+(1-result.success_profit)*100+'%</span></div></div>'
				document.getElementById("data2_1").innerHTML='<h1>'+result.jingzhibili.toFixed(2)+'%</h1>'
				document.getElementById("data2_2").innerHTML='<h1>'+result.ordertotal+'</h1>'
				document.getElementById("data2_3").innerHTML='<h1>'+result.lotscount+'</h1>'
//"                <a href="#" class="list-group-item list-group-item-success">日常生活支出<span class="badge">11500</span><span class="badge">11500</span></a>
 //               <a href="#" class="list-group-item list-group-item-info">电费余额  <span class="badge">532.5</span></a>
    //            <a href="#" class="list-group-item list-group-item-warning">水费和煤气费余额   <span class="badge">99</span></a>
  //              <a href="#" class="list-group-item list-group-item-danger">固定购物账户余额  <span class="badge">1934.5</span></a>
      //          <a href="#" class="list-group-item list-group-item-dark">物业费待缴纳日期  <span class="badge">2016-1-3</span></a>"



			}
		});
	});

});	