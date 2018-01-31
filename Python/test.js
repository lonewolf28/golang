/Here the command-line arguments that you've passed when invoking the PhantomJS executable 
//are obtained as an array. In this case I have passed phantom-js.exe as first argument, 
//the screenshot.js as the second argument.

//Note that The third argument is accessed as args[1] in the javascript file and the numbering continues.
var system = require('system');

// Web Address (URL) of the page to capture
var url = system.args[1];

// File name of the captured image
var file = system.args[2];

var reportPage = require('webpage').create();

// Browser size - height and width in pixels
// Change the viewport to 480x320 to emulate the iPhone
reportPage.viewportSize = {
    width: 1920,
    height: 1080
};

reportPage.paperSize = {
    format: 'A4',
    orientation: 'portrait',
    footer: {
        height: "1.0cm",
        contents: phantom.callback(function (pageNum, numPages) {
            return "<div style='font-size:13px;font-weight:normal;'>
                    <span style='text-align:left'>Confidential</span>
                    <span style='margin-left:44em'>" + pageNum + " of " + numPages + "</span></div>";
        })
    }
};

reportPage.settings.localToRemoteUrlAccessEnabled = true;
reportPage.settings.webSecurityEnabled = false;

// Set the User Agent String
// You can change it to iPad or Android for mobile screenshot
reportPage.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5";

var loginPage = require('webpage').create();

function getLoginUrl() {
    var loginUrl,
        domain = system.args[3],
        username = system.args[4],
        passCode = system.args[5],
        organization = system.args[6];

    //Form the login url. As a GET Request.
    loginUrl = domain + "?j_organization=" + organization + "&j_username=" 
               + username + "&j_password=" + passCode;

    return loginUrl;
}

function saveReport() {
    var logoutPage = require('webpage').create();
    reportPage.open(url, function (status) {
        if (status !== "success") {
            console.log("Fatal Error. Could not open web page : " + url);
            phantom.exit();
        } else {
            window.setTimeout(function () {
                reportPage.render(file);
                console.log("Download the screenshot : " + file);
                //Logout
                logoutPage.open("./j_spring_security_logout");
                phantom.exit();
            }, 3000);
        }
    });
}

//Now if login is successful, take the screenshot
loginPage.open(getLoginUrl(), function (loginStatus) {
    if (loginStatus !== "success") {
        console.log("Fatal Error. Couldn't login to get the report screenshot.");
    } else {
        // Render the screenshot image
        saveReport();
    }
});
