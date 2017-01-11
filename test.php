<html lang="zh-CN" >
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<head>
  <script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>

   <!--  <script type="text/javascript" src="js/src/1.js"></script>-->


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

        <li class="active"><a href="lhwylp.html">KPI日报</a></li>
 
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->

</nav>



<div class="container-fluid">
<div class="row" >
<div class="col-sm-12" >

<div class="panel panel-default">
  <div class="panel-heading">KPI日报
</div>
  <div class="panel-body">
   
<table class="table">
      <thead>
        <tr >
          <th>#</th>
          <th class="info"><h3>First Name</h></th>
          <th>Last Name</th>
          <th>Username</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <td>3</td>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </table>
   
</div>
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
