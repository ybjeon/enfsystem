<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<head>
<title>EarthCam Headquarters</title>
<meta name="description" content="Experience the rise of our new headquarters through EarthCam's construction camera technology."/>
<meta name="keywords" content=" construction camera, construction cameras, construction webcams, construction cam, construction cams, construction web cam, construction web cams, megapixel cam, megapixel camera, HD camera, HD cam, high def cam, high def webcam, time-lapse"/>
<meta name = "viewport" content = "width = 100%, height = 100%, initial-scale = 1.0, user-scalable = yes">
	<link rel="stylesheet" href="css/reset.css"> <!-- CSS reset -->
	<link rel="stylesheet" href="css/style.css"> <!-- Resource style -->
	<link rel="stylesheet" href="css/animate.css"> <!-- Resource style -->
	<link rel="stylesheet" href="css/lightbox.css"> <!-- Resource style -->
	<script src="js/modernizr.js"></script> <!-- Modernizr -->

</head>
<body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
 
  ga('create', 'UA-274246-15', 'auto');
  ga('send', 'pageview');
 
</script>
<header class="cd-header">
	<div id="cd-logo"><a ><img src="img/logo_sm.png" alt="LogoSmall"></a></div>

	<nav class="cd-primary-nav">
		<ul>
			<li><a class='active' href="/">Home</a></li>
			<li><a  href="webcams.php">Webcams</a></li>
			<li><a  href="gallery.php">Gallery</a></li>
			<li><a  href="about.php">About</a></li>
			<li><a  href="team.php">Team</a></li>
			<li><a  href="contact.php">Contact</a></li>
		</ul>
	</nav>
</header>
	<section class="cd-hero">
		<ul class="cd-hero-slider">
			<li class="selected">
				<div class="cd-full-width">
					<h2 class="animated fadeIn"><img src="img/logo.png" alt="EarthCam Headquarters"></h2>
					<p class="tagline animated fadeIn">The leaders in providing webcam technology and services since 1996</p>
					<div style="width:100%;height:50%;"></div>
					<a href="#webcams" class="cd-btn" id="webcamSection">Welcome</a>
					
				</div> <!-- .cd-full-width -->
			</li>
		</ul> <!-- .cd-hero-slider -->
	</section> <!-- .cd-hero -->

	<p class="imageCaption">In the Fall of 2015, we broke ground on EarthCam's new 10-acre campus located in Northern New Jersey.</p>
	
	
	<div class="cd-main-content">
		<div style="width:100%;height:5px;"></div>

		<p style="margin-top:7px;margin-bottom:0px;font-weight:bold;">Proudly sharing progress of the world's largest facility dedicated to construction camera technology</p>
		<div style="height:3px;width:100%;background:#66b2ff;"></div>
		
		<p class="body-copy" style="margin-top:12px;margin-bottom:0px;font-style:italic;font-size:17px;text-align:left;">"The groundbreaking of our new headquarters is an exciting and significant moment in EarthCam's history. While the increased capabilities of our technology-driven campus will have immediate benefits to our clients, the expansive park-like landscape provides a creative environment and healthy work space for our dedicated team."</p>
		<p class="bc-signature">- Brian Cury, CEO and Founder</p>
		
		<br/> <!-------- Intro Ends ------------>
		<br/> <!-------- WebCam Start ------------>
		
		<p class="title" id="webcams" style="padding-top:17px;">Webcam Technology</p>
		
		<div id="player" style="width:100%;height:auto;margin:0px auto 5px;">
			<!--EARTHCAM EMBED CODE-->
			<script type="text/javascript"
			 src="http://www.earthcam.net/projects/earthcam/embed/playerrwd.js">
			</script>
			<!--/EARTHCAM EMBED CODE-->
		</div>

		<p class="body-copy" style="margin-top:3px;font-size:18px;line-height:21px;">Experience the rise of our new headquarters through EarthCam's construction camera technology.</p>
 
			<p class="body-copy" style="padding-left:13px;font-size:14px;line-height:17px;">1. <span style="font-weight:bold;"><a href="http://earthcam.net/products/gigapixelcamx10.php" target="_blank" style="color:#444;">GigapixelCam X10:</a></span> &nbsp;Our best outdoor robotic time-lapse system capable of producing panoramas with over 10 billion pixels.</p>
			
			<p class="body-copy" style="padding-left:13px;font-size:14px;line-height:17px;">2. <span style="font-weight:bold;"><a href="http://earthcam.net/products/streamcam4k.php" target="_blank" style="color:#444;">StreamCam 4K:</a></span> &nbsp;Our new ultra 4K live streaming video camera for project monitoring and time-lapse documentation.</p>
			
			<p class="body-copy" style="padding-left:13px;font-size:14px;line-height:17px;">3. <span style="font-weight:bold;"><a href="http://earthcam.net/products/24megapixelcam.php" target="_blank" style="color:#444;">MegapixelCam:</a></span> &nbsp;Our professional grade fixed position time-lapse system with live video previews.</p>
			
			<p class="body-copy" style="padding-left:13px;font-size:14px;line-height:17px;">4. <span style="font-weight:bold;"><a href="http://www.workzonecam.com/constructioncamera/" target="_blank" style="color:#444;">Work Zone Cam:</a></span> &nbsp;Our basic low-cost digital SLR time-lapse construction jobsite webcam.</p>
		
		<!--<p class="body-copy" style="margin-top:0px;font-size:14px;line-height:21px;">
			See the headquarters through the lens of our newest, greatest and most basic webcam technology solutions. With our new StreamCam 4K, enjoy a live streaming look at progress with ultra-high resolution video. Experience the rise of our new facility from an unparalleled perspective with our GigapixelCam X10 and see updating HD images from our Work Zone Cam system.
		</p>-->
		
		<br/> <!-------- Webcam Ends ------------>
		<br/> <!-------- Gallery Start ------------>
		
		<p class="title" id="gallery">Media Gallery</p>
		
		<div class="image-gallery" style="margin-bottom:15px;">
			<div class="imagebox-lg">
				<a href="https://www.earthcam.net/products/panoviewer.php?id=echq_pano_03_29_16" target="_blank">
					<img src="img/gallery/gpcx10pano032916.jpg" border="0"/></a>
			</div>
			<!--<p style="text-align:left;padding:0;margin:0;font-weight:bold;font-size:12px;">GigapixelCam X10 Panorama</p>-->
		</div>
		
		<div class="image-gallery">
			<div class="imagebox row1">
				<a class="img" href="img/gallery/large/IMG_028.jpg" data-lightbox="gallery">
					<img class="grow" src="img/gallery/thumbs/IMG_028.jpg" border="0"/></a>
			</div>
			<div class="imagebox">
				<a href="aerialfootage.php?footage=aerial-2" onClick="window.open(this.href,'video','width=1000, height=590, toolbar=no, menubar=no, location=no, scrollbars=no, resizable=no'); return false;">
				
				<!--<a class="img" href="img/gallery/large/IMG_029.jpg" data-lightbox="gallery">-->
					<img class="grow" src="img/gallery/thumbs/IMG_029.jpg" border="0"/></a>
			</div>
			<div class="imagebox row3">
				<a class="img" href="img/gallery/large/IMG_030.jpg" data-lightbox="gallery">
					<img class="grow" src="img/gallery/thumbs/IMG_030.jpg" border="0"/></a>
			</div>
		</div>
		
		<div class="image-gallery">
			<div class="imagebox row1">
				<a class="img" href="img/gallery/large/IMG_025.jpg" data-lightbox="gallery">
					<img class="grow" src="img/gallery/thumbs/IMG_025.jpg" border="0"/></a>
			</div>
			<div class="imagebox">
				<a class="img" href="img/gallery/large/IMG_026.jpg" data-lightbox="gallery">
					<img class="grow" src="img/gallery/thumbs/IMG_026.jpg" border="0"/></a>
			</div>
			<div class="imagebox row3">
				<a class="img" href="img/gallery/large/IMG_027.jpg" data-lightbox="gallery">
					<img class="grow" src="img/gallery/thumbs/IMG_027.jpg" border="0"/></a>
			</div>
		</div>
		
		
		<div  style="width:207px;margin:10px auto;">
			<a href="gallery.php" class="cd-btn" style="margin-bottom:30px;">View More Images</a>
		</div>
	</div> <!-- .cd-main-content -->
	
	
	

<div class="footer-wrapper">
	<div class="footer-content">
		<nav class="footer-nav">
			<ul class="footer-menu">
				<!--<span style="color:#aaa;font-size:11px;text-align:left;font-weight:normal;text-decoration:underline;">Explore Our Company Websites:</span>-->
				<li><a href="http://www.earthcam.net" target="_blank">EarthCam.net</a></li>
				<li><a href="http://www.earthcam.com" target="_blank">EarthCam.com</a></li>
				<li><a href="http://www.earthcamtv.com" target="_blank">EarthCamTV</a></li>
				<li><a href="http://www.constructioncamtv.com" target="_blank">ConstructionCamTV</a></li>
				<li><a href="http://www.earthcam.net/about/press.php?action=view&prid=564" target="_blank">Press Release</a></li>
				<!--<li><a  href="index.php">Home</a></li>
				<li><a  href="webcams.php">Webcams</a></li>
				<li><a  href="gallery.php">Gallery</a></li>
				<li><a  href="about.php">About</a></li>
				<li><a  href="team.php">Team</a></li>
				<li><a  href="contact.php">Contact</a></li>-->
			</ul>
			
			<ul class="footer-social">
				<span style="color:#aaa;font-size:11px;text-align:left;font-weight:normal;vertical-align:super;">Copyright 2015 EarthCam, Inc. All Rights Reserved.</span>
				<li><a class="facebook" href="http://www.facebook.com/earthcaminc" target="_blank"><img src="img/social/facebook.png" width="25" height="auto" border="0"/></a></li>
				<li><a class="twitter" href="http://www.twitter.com/earthcam" target="_blank"><img src="img/social/twitter.png" width="25" height="auto" border="0"/></a></li>
				<li><a class="instagram" href="https://instagram.com/earthcam/" target="_blank"><img src="img/social/instagram.png" width="25" height="auto" border="0"/></a></li>
				<!--<li><a class="linkedin" href="https://www.linkedin.com/company/earthcam-inc" target="_blank"><img src="img/social/linkedin.png" width="25" height="auto" border="0"/></a></li>-->
				<li><a class="youtube" href="https://www.youtube.com/user/earthcam" target="_blank"><img src="img/social/youtube.png" width="25" height="auto" border="0"/></a></li>
				<!--<li><a class="app" href="http://www.earthcam.com/mobile/" target="_blank"><img src="img/social/appstore.png" width="25" height="auto" border="0"/></a></li>
				<li><a class="rss" href="http://www.earthcam.com/rss.php" target="_blank"><img src="img/social/rss.png" width="25" height="auto" border="0"/></a></li>-->
				<li><a class="email" href="http://www.earthcam.com/newsletter/signup.php" target="_blank"><img src="img/social/email.png" width="25" height="auto" border="0"/></a></li>
			</ul>
		</nav> <!-- .footer-nav -->
		<a href="#" class="top"><img src="img/top.png" border="0" title="Back to Top"/></a>
</div> <!-- .footer-content -->
</div>
	
<script src="js/jquery-2.1.1.js"></script>
<script src="js/main.js"></script> <!-- Resource jQuery -->
<script type="text/javascript" src="js/lightbox.js"></script>
</body>
</html>