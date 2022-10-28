import json

json_file = open('people.json')
data = json.load(json_file)

header = """
<!DOCTYPE html>
<html dir="ltr" lang="en-US">
<head>

    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="author" content="SemiColonWeb" />
    <link rel="shortcut icon" type="image/png" href="images/favicon.png">

    <!-- Stylesheets
    ============================================= -->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,400i,700|Raleway:300,400,500,600,700|Crete+Round:400i" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" href="css/bootstrap.css" type="text/css" />
    <link rel="stylesheet" href="style.css" type="text/css" />
    <link rel="stylesheet" href="css/dark.css" type="text/css" />
    <link rel="stylesheet" href="css/font-icons.css" type="text/css" />
    <link rel="stylesheet" href="css/animate.css" type="text/css" />
    <link rel="stylesheet" href="css/magnific-popup.css" type="text/css" />

    <link rel="stylesheet" href="css/responsive.css" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Document Title
    ============================================= -->
    <title>Team | BOND Consulting</title>

</head>

<body class="stretched">

    <!-- Document Wrapper
    ============================================= -->
    <div id="wrapper" class="clearfix">

        <!-- Header
         ============================================= -->
        <header id="header" class="dark" data-sticky-class="not-dark">

            <div id="header-wrap">

                <div style="padding: 0 40px">

                    <div id="primary-menu-trigger"><i class="icon-reorder"></i></div>

                    <!-- Logo
                     ============================================= -->
                    <div id="logo">
                        <a href="index.html" class="standard-logo" data-dark-logo="images/BONDLogo.png"><img src="images/BONDLogo.png" alt="Canvas Logo"></a>
                        <a href="index.html" class="retina-logo" data-dark-logo="images/BONDLogo.png"><img src="images/BONDLogo.png" alt="Canvas Logo"></a>
                    </div><!-- #logo end -->

                    <!-- Primary Navigation
                     ============================================= -->
                    <nav id="primary-menu">
                        <nav id="primary-menu">
                            <ul>
                                <li><a href="index.html"><div>Home</div></a> </li>
                                <li><a href="Our-Impact.html"><div>Clients</div></a>
                                    <ul>
                                        <li><a href="Our-Impact.html"><div><i class="icon-city"></i>Our Impact</div></a></li>
                                        <li><a href="client.html"><div><i class="icon-chart-line"></i>Client Services</div></a></li>
                                    </ul>
                                </li>
                                <li><a href="team.html"><div>Our Team</div></a>
                                <ul>
                                        <li><a href="team.html"><div><i class="icon-group"></i>Our Members</div></a></li>
                                        <li><a href="BONDBlurbs.html"><div><i class="icon-book"></i>BOND Blurbs</div></a></li>
                                        <li><a href="BONDW2.html"><div><i class="icon-comments2"></i>BONDw</div></a></li>
                                    </ul>
                                </li>

                                <li><a href="Alumni.html"><div>Alumni</div></a> </li>
                                <li><a href="Prospective-Members.html"><div>Prospective Members</div></a>
                                    <ul>
                                        <li><a href="Prospective-Members.html"><div><i class="icon-chalkboard-teacher"></i>Prospective Members</div></a></li>
                                        <li><a href="President-Welcome.html"><div><i class="icon-user-friends"></i>President's Welcome</div></a></li>
                                    </ul>
                                </li>
                            </ul>
                        </nav><!-- #primary-menu end -->

                </div>

            </div>

        </header><!-- #header end -->

        <!-- Page Title
        ============================================= -->
        <section id="page-title">

            <div class="container clearfix">
                <h1>Our Team</h1>
                <span>All the people to BOND with...</span>
            </div>

        </section><!-- #page-title end -->

        <!-- Content ALL PHOTOS ARE CALLED name21.jpg ALL LOWERCASE
        ============================================= -->
        <section id="content">

            <div class="content-wrap" style="padding-bottom: 0px !important;">

                <div class="container clearfix">

                    <div class="clear"></div>
"""

footer = """
            </div>


        </section><!-- #content end -->

        <!-- Footer
         ============================================= -->
        <footer id="footer" class="dark">

            <div class="container">

            </div>

            <!-- Copyrights
             ============================================= -->
            <div id="copyrights">

                <div class="container clearfix">

                    <div class="col_half">
                        Copyrights &copy; 2019 All Rights Reserved by BOND Consulting Group<br>
                        <div class="copyright-links">Ross School of Business: 701 Tappan Ave, Ann Arbor, MI 48109</div>

                    </div>

                    <div class="col_half col_last tright">

                        <div class="copyrights-menu copyright-links fright clearfix">
                            <a href="index.html">Home</a>/<a href="client.html">Clients</a>/<a href="team.html">Our Team</a>/<a href="Alumni.html">Alumni</a>/<a href="Prospective-Members.html">Prospective Members</a>
                        </div>

                        <div class="clear"></div>

                        <i class="icon-envelope2"></i> bondexecutives@umich.edu
                        <div class="clear"></div>

                        <div class="fright clearfix">

                            <a href="https://instagram.com/bond_umich?igshid=17lrlt83e62xj" class="social-icon si-small si-borderless si-instagram">
                                <i class="icon-instagram"></i>
                                <i class="icon-instagram"></i>
                            </a>
                            <a href="https://www.linkedin.com/company/bondconsultinggroup" class="social-icon si-small si-borderless si-linkedin">
                                <i class="icon-linkedin"></i>
                                <i class="icon-linkedin"></i>
                            </a>
                            <a href="https://m.facebook.com/BONDConsultingUMICH/" class="social-icon si-small si-borderless si-facebook">
                                <i class="icon-facebook"></i>
                                <i class="icon-facebook"></i>
                            </a>
                        </div>
                    </div>

                </div>

            </div><!-- #copyrights end -->

        </footer><!-- #footer end -->

    </div><!-- #wrapper end -->

    <!-- Go To Top
    ============================================= -->
    <div id="gotoTop" class="icon-angle-up"></div>

    <!-- External JavaScripts
    ============================================= -->
    <script src="js/jquery.js"></script>
    <script src="js/plugins.js"></script>

    <!-- Footer Scripts
    ============================================= -->
    <script src="js/functions.js"></script>

</body>
</html>
<script type='text/javascript'>
window.__lo_site_id = 187730;

    (function() {
        var wa = document.createElement('script'); wa.type = 'text/javascript'; wa.async = true;
        wa.src = 'https://d10lpsik1i8c69.cloudfront.net/w.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(wa, s);
      })();
    </script>
"""

count = 0
tabs = "                        "
open_line = tabs+"<div class=\"row\" style=\"margin-top: 60px;\">"
close_line = tabs+"</div>"

print(header)
print(open_line)
for name in data:
    body = f"""
                            <div class="col-lg-3 col-md-6 bottommargin">
                                <div class="team">
                                    <div class="team-image">
                                        <img src="images/{data[name]["image"]}" alt="{name}">
                                            </div>
                                    <div class="team-desc">
                                        <div class="team-title"><h4>{name}</h4><span>{data[name]["role"]}</span></div><br>
                                        <a href="{data[name]["linkedin"]}" class="social-icon si-colored si-linkedin" title="LinkedIn">
                                            <i class="icon-linkedin"></i>
                                            <i class="icon-linkedin"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
    """
    if count != 0 and count % 4 == 0:
        print(close_line+'\n\n'+open_line)
    print(body)
    count += 1
print(close_line)
print(footer)