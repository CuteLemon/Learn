var jayson = require('jayson')

var client = jayson.client.http({
    port: 9898,
    hostname: 'localhost'
});

// Test RPC method
function add(a, b, callback) {
    client.request('add', [a, b], function(err, error, response) {
        if (err) throw err;
        console.log(response);
        // callback(response);
    });
}

add(355,4)
