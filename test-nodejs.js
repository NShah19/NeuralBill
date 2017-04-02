var OAuth2 = require('OAuth').OAuth2;
var https = require('https');

var oauth2 = new OAuth2('8n2xIVxdWhW661SSRkYMX5PWJ', 'Av9WibDlGyR5yGPvxzX7voxcXs2McHkDCFvZcqjP6nYvsYDcEa', 'https://api.twitter.com/', null, 'oauth2/token', null);
oauth2.getOAuthAccessToken('', {
    'grant_type': 'client_credentials'
}, function (e, access_token) {
    console.log(access_token); //string that we can use to authenticate request

    var options = {
        hostname: 'api.twitter.com',
        path: '/1.1/statuses/user_timeline.json?screen_name=realDonaldTrump&count=1&trim_user=true&exclude_replies=true&include_rts=false',
        headers: {
            Authorization: 'Bearer ' + access_token
        }
    };


    https.get(options, function(result){
        result.setEncoding('utf8');
        result.on('data', function(data){
            console.log(data); //the response!

        var fs = require('fs');
        fs.appendFile("test.txt", data, function(err) {
            if(err) {
                return console.log(err);
            }
        });
        });

    });
});