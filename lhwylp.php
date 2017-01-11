<html lang="zh-CN" >
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<head>
  <script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>

   <!--  <script type="text/javascript" src="js/src/1.js"></script>-->
    <script type="text/javascript" src="js/src/load_json.js"></script>

    <script type="text/javascript" src="js/bootstrap.min.js"></script>

<link rel="stylesheet" href="css/bootstrap.min.css">
<header class="main-header" style="background-image: url(title.jpg);background-size:100%;height:300px">

        <div class="container">
            <div class="row" >

                <div class="col-sm-12" >

                    <div class='row'>
                    	<!-- start logo -->
                   
      				</div>
                </div>
            </div>
        </div>
        
    </header>
<body>

	<nav class="navbar navbar-inverse navbar-static-top">


<div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">

    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">

        <li class="active"><a href="lhwylp.html">KPI日报文件下载</a></li>
 
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->

</nav>



<div class="container-fluid">
<div class="row" >
<div class="col-sm-12" >

<div class="panel panel-default">
  <div class="panel-heading">计算结果下载1
</div>
  <div class="panel-body">
   
<div class="list-group"  id="target1">

  

  </div>
   
</div>
<div class="panel-footer" id='target2'><button type="button" class="btn btn-success" id="submit" onclick=setTimeout("window.location.reload()",1000);>重新计算全部</button>&nbsp;<button type="button" class="btn btn-success" id="submit" >重新计算当日增量</button></div>
</div>


 </div>
</div>
</div>
</body>
</html>


<script type="text/javascript"> 

    $("#submit").click(function(){

            $.ajax({url: 'test2.php', 
            type: 'GET',
            dataType: 'html', 

 
            });  
            return false;

        });
      
</script>
