
  
    

function getNums(state2) {
    int1 = 0;
    int2 = 0;
    int3 = 0;
    list = [0, 0, 0];
        $.ajax({
            url: '/background_process_testEdison',
            type: 'GET',
            data: {state: state2},
            dataType: 'json',
            success: function(data) {
                console.log(data)
              document.getElementById("Date").innerHTML = "Date/Time when retrieved: " + new Date().toLocaleTimeString();
                var table = document.getElementById("NBC");
                table.innerHTML = ""; 
                var row = table.insertRow(0);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                cell3.innerHTML = "Edison Votes";
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                cell1.innerHTML = "County";
                cell2.innerHTML = "Biden %"; 
                cell3.innerHTML = "Biden Votes";     
                cell4.innerHTML = "Trump %";   
                cell5.innerHTML = "Trump Votes"; 
                cell6.innerHTML = "PR";  
                i = 2;
                $.each(data, function(index, element) {
                    var row = table.insertRow(i);
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    var cell4 = row.insertCell(3);
                    var cell5 = row.insertCell(4);
                    var cell6 = row.insertCell(5);
                    cell1.innerHTML = element.countyName;
                    cell2.innerHTML = element.candidates[0].votePercentStr; 
                    cell3.innerHTML = element.candidates[0].voteNum; 
                    int1 += parseInt(element.candidates[0].voteNum);    
                    cell4.innerHTML = element.candidates[1].votePercentStr;   
                    cell5.innerHTML = element.candidates[1].voteNum; 
                    int1 += parseInt(element.candidates[1].voteNum);   
                    cell6.innerHTML = element.percentReporting;  
                    i++;
                }); 
                list[0] = int1;
                document.getElementById("EdisonTotal").innerHTML = "Edison total votes are: " + int1;
             // display the response of your php function
             
            }
            
        });
        $.ajax({
            url: '/background_process_testDDHQ',
            type: 'GET',
            data: {state: state2},
            dataType: 'json',
            success: function(data) {
                var table = document.getElementById("DDHQ");
                table.innerHTML = ""; 
                var row = table.insertRow(0);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                cell3.innerHTML = "DDHQ Votes";
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                cell1.innerHTML = "County";
                cell2.innerHTML = "Biden %"; 
                cell3.innerHTML = "Biden Votes";     
                cell4.innerHTML = "Trump %";   
                cell5.innerHTML = "Trump Votes"; 
                cell6.innerHTML = "PR";  
                cell7.innerHTML = "TP";        
                counties = data.data;
                if (counties[0].state == "New Hampshire"){
                counties2 = counties[0].vcuResults.counties;
                } else {
                counties2 = counties[0].countyResults.counties;
                }
                i = 2;
                $.each(counties2, function(index, element) {
                    var row = table.insertRow(i);
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    var cell4 = row.insertCell(3);
                    var cell5 = row.insertCell(4);
                    var cell6 = row.insertCell(5);
                    var cell7 = row.insertCell(6);
                    cell1.innerHTML = element.county;
                    cell2.innerHTML = ((parseInt(element.votes["11918"])/(parseInt(element.votes["11918"]) + parseInt(element.votes["5"]) + parseInt(element.votes["12080"])))  * 100).toFixed(2) + '%'; 
                    cell3.innerHTML = element.votes["11918"];     
                    int2 += parseInt(element.votes["11918"]);
                    cell4.innerHTML = ((parseInt(element.votes["5"])/(parseInt(element.votes["11918"]) + parseInt(element.votes["5"]) + parseInt(element.votes["12080"])))  * 100).toFixed(2) + '%';   
                    cell5.innerHTML = element.votes["5"]; 
                    int2 += parseInt(element.votes["5"]);
                    cell6.innerHTML = element.precincts.reporting;  
                    cell7.innerHTML = element.precincts.total; 
                    i++;
                }); 
                list[1] = int2;
                document.getElementById("DDHQTotal").innerHTML = "DDHQ total votes are: " + int2;
                // display the response of your php function
            }
        });
        
        $.ajax({
            url: '/background_process_testAP',
            type: 'GET',
            data: {state: state2},
            dataType: 'json',
            success: function(data) {
                var table = document.getElementById("AP");
                table.innerHTML = ""; 
                var row = table.insertRow(0);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                cell3.innerHTML = "AP Votes";
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                var row = table.insertRow(1);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                var cell6 = row.insertCell(5);
                var cell7 = row.insertCell(6);
                cell1.innerHTML = "County";
                cell2.innerHTML = "Biden %"; 
                cell3.innerHTML = "Biden Votes";     
                cell4.innerHTML = "Trump %";   
                cell5.innerHTML = "Trump Votes"; 
                cell6.innerHTML = "PR";  
                cell7.innerHTML = "TP";  
                counties = data.results;         
                i = 2;
                $.each(counties, function(index, element) {
                    var row = table.insertRow(i);
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    var cell4 = row.insertCell(3);
                    var cell5 = row.insertCell(4);
                    var cell6 = row.insertCell(5);
                    var cell7 = row.insertCell(6);
                    cell1.innerHTML = element.county.countyName;
                    cell2.innerHTML = ((element.candidates[1].votes / (element.candidates[0].votes + element.candidates[1].votes + element.candidates[2].votes)) * 100).toFixed(2) + '%'; 
                    cell3.innerHTML = element.candidates[1].votes;   
                    int3 +=  parseInt(element.candidates[1].votes);
                    cell4.innerHTML = ((element.candidates[0].votes / (element.candidates[0].votes + element.candidates[1].votes + element.candidates[2].votes)) * 100).toFixed(2) + '%';   
                    cell5.innerHTML = element.candidates[0].votes; 
                    int3 +=  parseInt(element.candidates[0].votes);
                    cell6.innerHTML = element.reporting;  
                    cell7.innerHTML = element.precincts; 
                    i++;
                })
                list[2] = int3; 
                document.getElementById("APTotal").innerHTML = "AP total votes are: " + int3;

             // display the response of your php function
            }
        });



}
