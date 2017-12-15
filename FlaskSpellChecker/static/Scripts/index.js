

function GetResult(){
    var str = $("#InputText").val();
    if(str.length>0){
    dataSend = {"InputText" : $("#InputText").val()}
    console.log(dataSend)
    $.ajax({
        type: "POST",
        url: "/uploader",
        data: JSON.stringify(dataSend, null, '\t'),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            console.log(data)
            if(data.gramr === "wrong grammer"){
                $("#resultString").text("සෙව්ම වැරදියි");
            }
            if(data.gramr === "correct grammer") {
                $("#resultString").text("සෙව්ම නිවැරදි");
            }
            if(data.tense === "test"){
                $("#resultTense").text("කාලය වැරදියි");
            }
            if(data.tense === "present"){
                $("#resultTense").text("වර්තමාන කාල");
             }
             if(data.tense === "past"){
                $("#resultTense").text("අතීත කාල");
             }
             if(data.singular_plural === "test"){
                $("#numberVal").text("වාචී බව වැරදියි");
             }
             if(data.singular_plural === "plural"){
                $("#numberVal").text("බහු වචී");
             }
             if(data.singular_plural === "singular"){
                $("#numberVal").text("එක වචී");
             }
        },
        complete: function (xhr, textStatus) {
            console.log("AJAX Request complete -> ", xhr, " -> ", textStatus);
        },
        error: function () {
            $("#resultString").text("ඔබගේ සෙවුම සිදු කරන්න");
            $("#resultTense").text("කාලය මෙහි දැක්වෙනු ඇත");
            $("#numberVal").text("වාචය මෙහි දැක්වෙනු ඇත");
            $("#myModal").modal();
            console.log("Error occur");
        }
    });

    }else{
        $("#resultString").text("ඔබගේ සෙවුම සිදු කරන්න");
        $("#resultTense").text("කාලය මෙහි දැක්වෙනු ඇත");
        $("#numberVal").text("වාචය මෙහි දැක්වෙනු ඇත");
        $("#myModal02").modal();
    }
};
