$(function(){

    $('#load_files').on('click', () => {
        $.ajax({
            type: 'GET',
            url: "loadfiles",
            success: function (response) {
                console.log(response);
                $("#load_files").css("display","none");
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    });

    $('#search').on('keyup', function(){
        let text = $(this).val();
        if(/^user [0-9]/.test(text)){
            $.ajax({
                type: 'GET',
                url: "userSearch",
                data: {
                    "user_id": text.replace('user ', '')
                },
                success: function (response) {
                    let players = JSON.parse(response['players']);
                    let body = '';
                    if(players.length > 0){
                        fillTable(players);
                    }
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }else if(/^tags /.test(text)){
            $.ajax({
                type: 'GET',
                url: "tagsSearch",
                data: {
                    "tags": JSON.stringify(text.replace('tags ', '').replace(/[\']/g, '').split(' '))
                },
                success: function (response) {
                    let players = JSON.parse(response['players']);
                    let body = '';
                    if(players.length > 0){
                        fillTable(players);
                    }
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }else if(/^top[0-9]+ /.test(text)){
            let num = parseInt(text.split(' ')[0].replace('top', ''));
            let pos = (text.split(' ')[1]).replace(/[\']/g, '');
            $.ajax({
                type: 'GET',
                url: "topSearch",
                data: {
                    "top": num,
                    'posicao': pos
                },
                success: function (response) {
                    let players = JSON.parse(response['players']);
                    let body = '';
                    if(players.length > 0){
                        fillTable(players);
                    }
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }else if(/^player /.test(text)){
            $.ajax({
                type: 'GET',
                url: "playerSearch",
                data: {
                    "prefixo": text.replace('player ', '')
                },
                success: function (response) {
                    let players = JSON.parse(response['players']);
                    let body = '';
                    if(players.length > 0){
                        fillTable(players);
                    }
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            });
        }
    });
});

function fillTable(players){
    let body = '';
    let head = Object.keys(players[0]);
    let headers = '';

    head.forEach(function(e){
        headers += `<th>${e}</th>`;
    });

    $(".response_field").html(`
        <table>
            <thead>
                <tr>
                    ${headers}
                </tr> 
            </thead>
            <tbody></tbody>
        </table>
    `);

    players.forEach(function (e){
        let keys = Object.keys(e);
        body += '<tr>';
        keys.forEach((key, index) => {
            body += `<td>${e[key]}</td>`;
        });
        body += '</tr>';
    });
    $('.response_field >* tbody').html(body);
}