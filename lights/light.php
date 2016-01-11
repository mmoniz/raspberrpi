<html>
<head>
</head>
<title>Light Switch</title>
<body>

<div>

<?php

$status = "sudo python status.py";
$response = shell_exec($command);
echo ($response);

$ctl = $_POST['ctl'];
$command = "sudo python lights.py $ctl";
//echo($command);
$result = shell_exec($command);

echo ($result);

if ($result == 1) { ?>

	<img src="" alt="lights on" />

<?php } else { ?>

	<img src="" alt="lights off" />

<?php } ?>

</div>
<p class="head">Light Switch</p>
<form action="" method="POST" name="form">
<p class="title"> Control the lights from here: </p>
<p class="form">
<input type="submit" id="on" value="ON">
<input type="hidden" name="ctl" value="1">
</form></p>
<form action="" method="POST" name="form">
<p class="lol">
<input type="submit" id="off" value="OFF">
<input type="hidden" name="ctl" value="0">
</form>
</p>

</body>

</html>
