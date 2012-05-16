/*
 Author: Robert Hashemian
 <a href="http://www.hashemian.com/">http://www.hashemian.com/</a>

 You can use this code in any manner so long as the author's
 name, Web address and this disclaimer is kept intact.
 */

function calcage(secs, num1, num2) {
    s = ((Math.floor(secs/num1))%num2).toString();
    if (LeadingZero && s.length < 2)
        s = "0" + s;
    return "<b>" + s + "</b>";
}

function CountBack(secs, elementId) {
//    if (secs < 0) {
//        document.getElementById("cntdwn").innerHTML = FinishMessage;
//        return;
//    }
    DisplayStr = DisplayFormat.replace(/%%D%%/g, calcage(secs,86400,100000));
    DisplayStr = DisplayStr.replace(/%%H%%/g, calcage(secs,3600,24));
    DisplayStr = DisplayStr.replace(/%%M%%/g, calcage(secs,60,60));
    DisplayStr = DisplayStr.replace(/%%S%%/g, calcage(secs,1,60));

    document.getElementById(elementId).innerHTML = DisplayStr;
    if (CountActive)
        setTimeout("CountBack(" + (secs+CountStepper) + ", \"" + elementId + "\")", SetTimeOutPeriod);

}

function putspan(backcolor, forecolor) {
    document.write("<span id='cntdwn' style='background-color:" + backcolor +
        ";'></span>");
}

if (typeof(BackColor)=="undefined")
    BackColor = "white";
if (typeof(ForeColor)=="undefined")
    ForeColor= "black";
TargetDateKiss = "12/25/2010 5:00";
TargetdateMerry = "2/14/2012 14:00";
if (typeof(DisplayFormat)=="undefined")
    DisplayFormat = "%%D%% Days, %%H%% Hours, %%M%% Minutes, %%S%% Seconds.";
if (typeof(CountActive)=="undefined")
    CountActive = true;
if (typeof(FinishMessage)=="undefined")
    FinishMessage = "";
if (typeof(CountStepper)!="number")
    CountStepper = -1;
if (typeof(LeadingZero)=="undefined")
    LeadingZero = true;
CountStepper = Math.ceil(CountStepper);
if (CountStepper == 0)
    CountActive = false;
var SetTimeOutPeriod = (Math.abs(CountStepper)-1)*1000 + 990;
//putspan(BackColor, ForeColor);
var dthenKiss = new Date(TargetDateKiss);
var dthenMerry = new Date(TargetdateMerry);
var dnow = new Date();
ddiffKiss = new Date(dnow - dthenKiss);
ddiffMerry = new Date(dnow - dthenMerry);
gsecsKiss = Math.floor(ddiffKiss.valueOf()/1000);
gsecsMerry = Math.floor(ddiffMerry.valueOf()/1000);
CountBack(gsecsKiss, "kiss");
CountBack(gsecsMerry, "merry");
